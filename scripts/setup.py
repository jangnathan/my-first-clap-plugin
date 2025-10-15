import subprocess
import shutil
import os
import sys

script_directory = os.path.dirname(os.path.realpath(__file__))
workspace = os.path.dirname(script_directory)
dependencies_dir = os.path.join(workspace, "dependencies")
project_include_dir = os.path.join(workspace, "include")

# install_header_only_lib function
# include_path - where to look for the include in the repository
def install_header_only_lib(git_url, include_path, output_dir):
    if os.path.isdir(os.path.join(project_include_dir, output_dir)):
        print(f"{output_dir} already installed. delete include/clap if you want to reinstall or install a new version");
        return


    result = subprocess.run(
        ["git", "clone", "--depth", "1", git_url, "temp_repo"],
        cwd = workspace,
        check=True,
        capture_output=True,
        text=True
    )

    # move files later on
    repo = os.path.join(workspace, "temp_repo")

    shutil.move(os.path.join(repo, "include", include_path),
                os.path.join(project_include_dir, output_dir))
    shutil.rmtree(repo);


# look for specific files (usually just a few)
def install_header_only_lib_files(git_url, include_paths, output_dir):
    if os.path.isdir(os.path.join(project_include_dir, output_dir)):
        print(f"{output_dir} already installed. delete include/clap if you want to reinstall or install a new version");
        return

    os.mkdir(os.path.join(project_include_dir, output_dir))

    result = subprocess.run(
        ["git", "clone", "--depth", "1", git_url, "temp_repo"],
        cwd = workspace,
        check=True,
        capture_output=True,
        text=True
    )

    # move files later on
    repo = os.path.join(workspace, "temp_repo")

    for include_path in include_paths:
        shutil.move(os.path.join(repo, include_path),
                    os.path.join(project_include_dir, output_dir, include_path))

    shutil.rmtree(repo);


def install_dependencies(git_url, dependency_name):
    if os.path.isdir(os.path.join(dependencies_dir, dependency_name)):
        print(f"{dependency_name} already installed. delete include/clap if you want to reinstall or install a new version");
        return


    result = subprocess.run(
        ["git", "clone", "--depth", "1", git_url, os.path.join(dependencies_dir, dependency_name)],
        cwd = workspace,
        check=True,
        capture_output=True,
        text=True
    )


# finally install things
install_header_only_lib("https://github.com/free-audio/clap.git",
                        os.path.join("clap"),
                        "clap")

install_header_only_lib("https://github.com/free-audio/clap-helpers.git",
                        os.path.join("clap", "helpers"), 
                        os.path.join("clap", "helpers"))

install_header_only_lib_files("https://github.com/cameron314/readerwriterqueue.git",
                              {"atomicops.h", "readerwriterqueue.h"},
                              "readerwriterqueue")

install_dependencies("https://github.com/free-audio/clap-imgui-support.git", "clap-imgui-support")
install_dependencies("https://github.com/ocornut/imgui.git", "imgui")
