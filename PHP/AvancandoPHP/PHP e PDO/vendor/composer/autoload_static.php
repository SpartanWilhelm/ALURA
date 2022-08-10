<?php

// autoload_static.php @generated by Composer

namespace Composer\Autoload;

class ComposerStaticInitd5190bfc501d3691f59708a2d32bdc89
{
    public static $prefixLengthsPsr4 = array (
        'A' => 
        array (
            'Alura\\Pdo\\' => 10,
        ),
    );

    public static $prefixDirsPsr4 = array (
        'Alura\\Pdo\\' => 
        array (
            0 => __DIR__ . '/../..' . '/src',
        ),
    );

    public static $classMap = array (
        'Composer\\InstalledVersions' => __DIR__ . '/..' . '/composer/InstalledVersions.php',
    );

    public static function getInitializer(ClassLoader $loader)
    {
        return \Closure::bind(function () use ($loader) {
            $loader->prefixLengthsPsr4 = ComposerStaticInitd5190bfc501d3691f59708a2d32bdc89::$prefixLengthsPsr4;
            $loader->prefixDirsPsr4 = ComposerStaticInitd5190bfc501d3691f59708a2d32bdc89::$prefixDirsPsr4;
            $loader->classMap = ComposerStaticInitd5190bfc501d3691f59708a2d32bdc89::$classMap;

        }, null, ClassLoader::class);
    }
}
