# Install script for directory: /home/borg/Downloads/rccsserver/rcssserver-17.0.1/rcss/clang

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/usr/local")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "Release")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xLibrariesx" OR NOT CMAKE_INSTALL_COMPONENT)
  foreach(file
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/librcssclangparser.so.2.1.0"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/librcssclangparser.so.2"
      )
    if(EXISTS "${file}" AND
       NOT IS_SYMLINK "${file}")
      file(RPATH_CHECK
           FILE "${file}"
           RPATH "")
    endif()
  endforeach()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY PERMISSIONS OWNER_READ OWNER_WRITE OWNER_EXECUTE GROUP_READ GROUP_EXECUTE WORLD_READ WORLD_EXECUTE FILES
    "/home/borg/Downloads/rccsserver/rcssserver-17.0.1/build/rcss/clang/librcssclangparser.so.2.1.0"
    "/home/borg/Downloads/rccsserver/rcssserver-17.0.1/build/rcss/clang/librcssclangparser.so.2"
    )
  foreach(file
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/librcssclangparser.so.2.1.0"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/librcssclangparser.so.2"
      )
    if(EXISTS "${file}" AND
       NOT IS_SYMLINK "${file}")
      if(CMAKE_INSTALL_DO_STRIP)
        execute_process(COMMAND "/usr/bin/strip" "${file}")
      endif()
    endif()
  endforeach()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xLibrariesx" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/librcssclangparser.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/librcssclangparser.so")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/librcssclangparser.so"
         RPATH "")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY PERMISSIONS OWNER_READ OWNER_WRITE OWNER_EXECUTE GROUP_READ GROUP_EXECUTE WORLD_READ WORLD_EXECUTE FILES "/home/borg/Downloads/rccsserver/rcssserver-17.0.1/build/rcss/clang/librcssclangparser.so")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/librcssclangparser.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/librcssclangparser.so")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/librcssclangparser.so")
    endif()
  endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/rcss/clang" TYPE FILE FILES
    "/home/borg/Downloads/rccsserver/rcssserver-17.0.1/rcss/clang/clangparser.h"
    "/home/borg/Downloads/rccsserver/rcssserver-17.0.1/rcss/clang/coach_lang_tok.h"
    "/home/borg/Downloads/rccsserver/rcssserver-17.0.1/rcss/clang/clangbuilder.h"
    "/home/borg/Downloads/rccsserver/rcssserver-17.0.1/rcss/clang/clangmsgbuilder.h"
    "/home/borg/Downloads/rccsserver/rcssserver-17.0.1/rcss/clang/clangmsg.h"
    "/home/borg/Downloads/rccsserver/rcssserver-17.0.1/rcss/clang/clangmetamsg.h"
    "/home/borg/Downloads/rccsserver/rcssserver-17.0.1/rcss/clang/clangfreeformmsg.h"
    "/home/borg/Downloads/rccsserver/rcssserver-17.0.1/rcss/clang/clangunsuppmsg.h"
    "/home/borg/Downloads/rccsserver/rcssserver-17.0.1/rcss/clang/clangrulemsg.h"
    "/home/borg/Downloads/rccsserver/rcssserver-17.0.1/rcss/clang/clangdelmsg.h"
    "/home/borg/Downloads/rccsserver/rcssserver-17.0.1/rcss/clang/clanginfomsg.h"
    "/home/borg/Downloads/rccsserver/rcssserver-17.0.1/rcss/clang/clangadvicemsg.h"
    "/home/borg/Downloads/rccsserver/rcssserver-17.0.1/rcss/clang/clangdefmsg.h"
    "/home/borg/Downloads/rccsserver/rcssserver-17.0.1/rcss/clang/clangaction.h"
    "/home/borg/Downloads/rccsserver/rcssserver-17.0.1/rcss/clang/clangutil.h"
    "/home/borg/Downloads/rccsserver/rcssserver-17.0.1/rcss/clang/coach_lang_comp.h"
    "/home/borg/Downloads/rccsserver/rcssserver-17.0.1/build/rcss/clang/coach_lang_parser.hpp"
    "/home/borg/Downloads/rccsserver/rcssserver-17.0.1/rcss/clang/arithop.h"
    "/home/borg/Downloads/rccsserver/rcssserver-17.0.1/rcss/clang/compop.h"
    "/home/borg/Downloads/rccsserver/rcssserver-17.0.1/rcss/clang/cond.h"
    "/home/borg/Downloads/rccsserver/rcssserver-17.0.1/rcss/clang/region.h"
    "/home/borg/Downloads/rccsserver/rcssserver-17.0.1/rcss/clang/rule.h"
    )
endif()

