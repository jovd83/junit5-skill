param(
    [string]$Root = "."
)

$ErrorActionPreference = "Stop"

function Test-PathSafe {
    param([string]$Path)
    return [System.IO.File]::Exists($Path)
}

function Find-FirstMatch {
    param(
        [string[]]$Files,
        [string[]]$Patterns
    )

    foreach ($file in $Files) {
        if (-not (Test-PathSafe -Path $file)) {
            continue
        }

        $content = Get-Content -Raw -Path $file
        foreach ($pattern in $Patterns) {
            if ($content -match $pattern) {
                return $true
            }
        }
    }

    return $false
}

$resolvedRoot = Resolve-Path $Root
$pom = Join-Path $resolvedRoot "pom.xml"
$gradle = Join-Path $resolvedRoot "build.gradle"
$gradleKts = Join-Path $resolvedRoot "build.gradle.kts"
$junitProps = Join-Path $resolvedRoot "src\test\resources\junit-platform.properties"

$isMaven = Test-PathSafe $pom
$isGradle = (Test-PathSafe $gradle) -or (Test-PathSafe $gradleKts)
$buildFiles = @($pom, $gradle, $gradleKts)

$hasJupiter = Find-FirstMatch -Files $buildFiles -Patterns @("junit-jupiter", "org\.junit\.jupiter")
$hasVintage = Find-FirstMatch -Files $buildFiles -Patterns @("junit-vintage", "org\.junit\.vintage")
$hasJUnit4 = Find-FirstMatch -Files $buildFiles -Patterns @("<artifactId>junit</artifactId>", "testImplementation\s+['""]junit:junit", "testCompile\s+['""]junit:junit")
$usesJUnitPlatform = Find-FirstMatch -Files @($gradle, $gradleKts) -Patterns @("useJUnitPlatform\s*\(")
$hasSurefire = Find-FirstMatch -Files @($pom) -Patterns @("maven-surefire-plugin")
$hasFailsafe = Find-FirstMatch -Files @($pom) -Patterns @("maven-failsafe-plugin")
$hasSpring = Find-FirstMatch -Files $buildFiles -Patterns @("spring-boot-starter-test", "org\.springframework\.boot")
$hasQuarkus = Find-FirstMatch -Files $buildFiles -Patterns @("quarkus-junit5", "io\.quarkus")
$hasMicronaut = Find-FirstMatch -Files $buildFiles -Patterns @("micronaut-test", "io\.micronaut")
$hasMockito = Find-FirstMatch -Files $buildFiles -Patterns @("mockito")
$hasTestcontainers = Find-FirstMatch -Files $buildFiles -Patterns @("testcontainers")

$testJava = Join-Path $resolvedRoot "src\test\java"
$testKotlin = Join-Path $resolvedRoot "src\test\kotlin"

$testFolders = @()
if (Test-Path $testJava) { $testFolders += "src/test/java" }
if (Test-Path $testKotlin) { $testFolders += "src/test/kotlin" }

Write-Output ("root={0}" -f $resolvedRoot)
Write-Output ("build.maven={0}" -f $isMaven.ToString().ToLowerInvariant())
Write-Output ("build.gradle={0}" -f $isGradle.ToString().ToLowerInvariant())
Write-Output ("junit.jupiter={0}" -f $hasJupiter.ToString().ToLowerInvariant())
Write-Output ("junit.vintage={0}" -f $hasVintage.ToString().ToLowerInvariant())
Write-Output ("junit4.present={0}" -f $hasJUnit4.ToString().ToLowerInvariant())
Write-Output ("gradle.useJUnitPlatform={0}" -f $usesJUnitPlatform.ToString().ToLowerInvariant())
Write-Output ("maven.surefire={0}" -f $hasSurefire.ToString().ToLowerInvariant())
Write-Output ("maven.failsafe={0}" -f $hasFailsafe.ToString().ToLowerInvariant())
Write-Output ("junit.platform.properties={0}" -f (Test-Path $junitProps).ToString().ToLowerInvariant())
Write-Output ("framework.spring={0}" -f $hasSpring.ToString().ToLowerInvariant())
Write-Output ("framework.quarkus={0}" -f $hasQuarkus.ToString().ToLowerInvariant())
Write-Output ("framework.micronaut={0}" -f $hasMicronaut.ToString().ToLowerInvariant())
Write-Output ("tool.mockito={0}" -f $hasMockito.ToString().ToLowerInvariant())
Write-Output ("tool.testcontainers={0}" -f $hasTestcontainers.ToString().ToLowerInvariant())
Write-Output ("test.folders={0}" -f ($testFolders -join ","))
