############################################################################
# Copyright (C) 2014 Pegatron Corp.
#
# NAME        : main.py
#
# DESCRIPTION : Check the files of assetdata in Aio master server and move it to 173 server.
# INPUT:   None
# 
#
# CHANGE ACTIVITY:
#  Aug 21 2014 Vincent - Initial release
#  Aug 26 2014 Vincent - Support seperate files copy, won't delete folder
############################################################################
import os, sys, shutil
import os.path
import time, datetime
import filecmp

def copytree(src, dst, symlinks=False):  
    names = os.listdir(src)  
    if not os.path.isdir(dst):  
        os.makedirs(dst)  
          
    errors = []  
    for name in names:  
        srcname = os.path.join(src, name)  
        dstname = os.path.join(dst, name)  
        try:  
            if symlinks and os.path.islink(srcname):  
                linkto = os.readlink(srcname)  
                os.symlink(linkto, dstname)  
            elif os.path.isdir(srcname):  
                copytree(srcname, dstname, symlinks)  
            else:  
                if os.path.isdir(dstname):  
                    os.rmdir(dstname)  
                elif os.path.isfile(dstname):  
                    os.remove(dstname)  
                shutil.copy2(srcname, dstname)  
            # XXX What about devices, sockets etc.?  
        except (IOError, os.error) as why:  
            errors.append((srcname, dstname, str(why)))  
        # catch the Error from the recursive copytree so that we can  
        # continue with other files  
        except OSError as err:  
            errors.extend(err.args[0])  
    try:  
        shutil.copystat(src, dst)  
    except WindowsError:  
        # can't copy file access times on Windows  
        pass  
    except OSError as why:  
        errors.extend((src, dst, str(why)))  
    if errors:  
        raise Error(errors)  

def filecmp(f1, f2):
    """Compare two files.

    Arguments:

    f1 -- First file name

    f2 -- Second file name

    Return value:

    True if the files are the same, False otherwise.

    This function uses information of os.stat() for comparisons,if files of the same
    size created at the same time are reported as the same without looking at content.

    """

    if os.path.isfile(f1) and os.path.isfile(f2):
        s1 = _sig(os.stat(f1))
        s2 = _sig(os.stat(f2))
        
        if s1 == s2:
            return True
            
    return False
    
def _sig(st):
    return (st.st_size,
            st.st_mtime)

def timer(n):
    while True:
        print "Task starting on %s" % time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        logCollect()
        print "\n\n######End########\n"
        time.sleep(n)
        print "\n\n######Start########\n"

def logCollect():
    # Populate local file path
    log_path = os.path.join(r"d:\LOGs_report\LOG")
    
    current_time = time.time()
    start = time.time()
    
    if os.path.isdir(log_path):
        # print "Log link passed!"
        t = time.localtime(current_time)
        date1 = time.strftime('%Y%m%d', t)
        time1 = time.strftime('%Y-%m-%d %H:%M:%S', t)
        month1 = time.strftime('%Y%m', t)
        
        #print date1, time1
        logname = 'LOG' + date1 + '.txt'
        logfile = os.path.join(log_path, logname)
        
        fout = open(logfile, 'a')
        
        fout.write('\n\n***********************************\n\n')
        fout.write('LOGs checking start on %s.\n' % time1)
    
    for i in range(2,54):
        dstpath = r'\\192.168.1.1\logs'
        srcpath = r'\\192.168.1.' + str(i) + '\logs\logs'
        print '[192.168.1.%s]' % str(i)
        if os.path.isdir(srcpath) and os.path.isdir(dstpath):
            fout.write('\n[192.168.1.%d] started.\n' % i)
            
            # ARMS
            fout.write('==ARMS report started.\n')
            arms_srcpath = srcpath + os.sep + 'ARMS'
            arms_dstpath = dstpath + os.sep + 'ARMS'
            if os.path.isdir(arms_srcpath) and os.path.isdir(arms_dstpath):
                for file in os.listdir(arms_srcpath):
                    try:
                        shutil.copy2(arms_srcpath + os.sep + file, arms_dstpath + os.sep + file)
                        os.remove(arms_srcpath + os.sep + file)
                        print ("%s moved to Master succeed." % file)
                        fout.write("%s moved to Master server succeed.\n" % file)
                    except Exception, e:
                        print e
            
            # AssetData
            fout.write('==Asset reprot started.\n')
            asset_srcpath = srcpath + os.sep + 'AssetData'
            asset_dstpath = dstpath + os.sep + 'AssetData'
            if os.path.isdir(asset_srcpath) and os.path.isdir(asset_dstpath):
                for file in os.listdir(asset_srcpath):
                    try:
                        shutil.copy2(asset_srcpath + os.sep + file, asset_dstpath + os.sep + file)
                        os.remove(asset_srcpath + os.sep + file)
                        print ("%s moved to Master succeed." % file)
                        fout.write("%s moved to Master server succeed.\n" % file)
                    except Exception, e:
                        print e
            
            # LOG
            fout.write('==LOG reprot started.\n')
            log_srcpath = srcpath + os.sep + 'LOG'
            log_dstpath = dstpath + os.sep + 'LOG'
            if os.path.isdir(log_srcpath) and os.path.isdir(log_dstpath):
                for file in os.listdir(log_srcpath):
                    try:
                        shutil.copy2(log_srcpath + os.sep + file, log_dstpath + os.sep + file)
                        os.remove(log_srcpath + os.sep + file)
                        print ("%s moved to Master succeed." % file)
                        fout.write("%s moved to Master server succeed.\n" % file)
                    except Exception, e:
                        print e
            
            # MTDL
            fout.write('==MTDL started.\n')
            mtdl_srcpath = srcpath + os.sep + 'MTDL'
            mtdl_dstpath = dstpath + os.sep + 'MTDL'
            if os.path.isdir(mtdl_srcpath) and os.path.isdir(mtdl_dstpath):
                for file in os.listdir(mtdl_srcpath):
                    try:
                        if os.path.isdir(mtdl_srcpath + os.sep + file):
                            copytree(mtdl_srcpath + os.sep + file, mtdl_dstpath + os.sep + file)
                            shutil.rmtree(mtdl_srcpath + os.sep + file)
                        else:
                            shutil.copy2(mtdl_srcpath + os.sep + file, mtdl_dstpath + os.sep + file)
                            os.remove(mtdl_srcpath + os.sep + file)
                        print ("%s moved to Master succeed." % file)
                        fout.write("%s moved to Master server succeed.\n" % file)
                    except Exception, e:
                        print e
            
            # ZIP
            fout.write('==ZIP started.\n')
            zip_srcpath = srcpath + os.sep + 'ZIP'
            zip_dstpath = dstpath + os.sep + 'ZIP'
            if os.path.isdir(zip_srcpath) and os.path.isdir(zip_dstpath):
                for file in os.listdir(zip_srcpath):
                    try:
                        copytree(zip_srcpath + os.sep + file, zip_dstpath + os.sep + file)
                        shutil.rmtree(zip_srcpath + os.sep + file)
                        print ("%s moved to Master succeed." % file)
                        fout.write("%s moved to Master server succeed.\n" % file)
                    except Exception, e:
                        print e
            
            # Others
            time.sleep(5)
            if os.path.isdir(srcpath + os.sep + 'fas'):
                try:
                    copytree(srcpath + os.sep + 'fas', dstpath + os.sep + 'fas')
                    shutil.rmtree(srcpath + os.sep + 'fas')
                except Exception, e:
                    print e   

            if os.path.isdir(srcpath + os.sep + 'batterylog'):
                try:             
                    copytree(srcpath + os.sep + 'batterylog', dstpath + os.sep + 'batterylog')
                    shutil.rmtree(srcpath + os.sep + 'batterylog')
                except Exception, e:
                    print e

            fout.write('\n[192.168.1.%d] finished.\n' % i)
        else:
            fout.write('\n[192.168.1.%d] passed.\n' % i)


    if fout != None:
        fout.write('LOG collection finished.\n\n')
        fout.close

    finish = time.time()
    print('\n***********************************\n')
    print "Collect log completed in %ds. " % (finish - start)
    print('\n***********************************\n')

if __name__ == "__main__": 
    timer(1800)
    
