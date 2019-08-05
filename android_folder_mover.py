import shutil as sh
import os
def android_folder_mover(path='/home/stormlightx/Desktop',destination='/home/stormlightx/Dropbox/backup'):
    contents = os.listdir(path)
    folders = [os.path.join(path,item) for item in contents if os.path.isdir(os.path.join(path,item))]
    androids = [item for item in folders if 'build.gradle' in os.listdir(item)]

    # REMOVING BUILD AND GRADLE FOLDERS
    print('removing folders')
    for project in androids:
        if os.path.exists(project) and os.path.exists(os.path.join(project,'gradle')):
            try:sh.rmtree(os.path.join(project,'gradle'))
            except Exception as e:pass
        if os.path.exists(project) and os.path.exists(os.path.join(project,'app','build')):
            try:sh.rmtree(os.path.join(project,'app','build'))
            except Exception as e:pass
    print("removed folders")
    
    # MOVING THEM TO A SINGLE FOLDER
    print(f'moving projects to {destination}')
    for project in androids:
        if os.path.exists(project):
            if not os.path.exists(destination):
                os.mkdir(destination)
            try:
                sh.copytree(project,os.path.join(destination,os.path.basename(project)))
                sh.rmtree(project)
            except Exception as e:pass
    return "task completed"
