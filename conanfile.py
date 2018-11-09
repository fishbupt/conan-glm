#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, CMake, tools


class GlmConan(ConanFile):
    name = "glm"
    version = "0.9.9.3"
    license = "MIT"
    author = "fishbupt fishbupt@gmail.com"
    url = "https://github.com/g-truc/glm"
    description = "mathematics library for graphics software based on the OpenGL Shading Language (GLSL) specifications"
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    no_copy_source = True
    extracted_dir = "glm-" + version

    def source(self):
        source_url = "https://github.com/g-truc/glm"
        tools.get("{0}/archive/{1}.tar.gz".format(source_url, self.version))

    def build(self):
        cmake = CMake(self)
        cmake.definitions["GLM_TEST_ENABLE"] = "OFF"
        cmake.configure(source_folder=self.extracted_dir)
        cmake.build()
        cmake.install()

    def package_id(self):
        self.info.header_only()


