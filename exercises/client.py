import rados
import sys

cluster = rados.Rados(conffile='/etc/ceph/ceph.conf')
print "\nlibrados version: " + str(cluster.version())
print "Will attempt to connect to: " + str(cluster.conf_get('mon initial members'))

cluster.connect()
print "\nCluster ID: " + cluster.get_fsid()

print "\n\nCluster Statistics"
print "=================="
cluster_stats = cluster.get_cluster_stats()

for key, value in cluster_stats.iteritems():
    print key, value

print "bucket" + sys.argv[1]
ioctx = cluster.open_ioctx(sys.argv[1])

print "object attr" + sys.argv[2] + ":" + sys.argv[3]
print ioctx.get_xattr(sys.argv[2], sys.argv[3])

print "\nClosing the connection."
ioctx.close()
