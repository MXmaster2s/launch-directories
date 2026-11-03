// Draws the Launch Directories icon: an Apple SF Symbol in white on a blue rounded tile.
//
//     swiftc -o /tmp/make_icons scripts/make_icons.swift && /tmp/make_icons site/src
//
// To change the symbol, change `symbolName` and run it again, then rebuild the site and
// the social image (README.md, "Landing page"). Needs macOS; SF Symbols come with it.

import AppKit

let symbolName = "paperplane.fill"
let sizes: [(file: String, px: Int)] = [
    ("icon-32.png", 32), ("icon-48.png", 48), ("icon-180.png", 180),
    ("icon-208.png", 208), ("icon-512.png", 512),
]

func render(px: Int) -> NSBitmapImageRep {
    let size = CGFloat(px)
    let rep = NSBitmapImageRep(
        bitmapDataPlanes: nil, pixelsWide: px, pixelsHigh: px, bitsPerSample: 8,
        samplesPerPixel: 4, hasAlpha: true, isPlanar: false, colorSpaceName: .deviceRGB,
        bytesPerRow: 0, bitsPerPixel: 0)!
    NSGraphicsContext.saveGraphicsState()
    NSGraphicsContext.current = NSGraphicsContext(bitmapImageRep: rep)

    let tile = NSRect(x: 0, y: 0, width: size, height: size)
    let path = NSBezierPath(roundedRect: tile, xRadius: size * 0.2237, yRadius: size * 0.2237)
    NSGradient(
        starting: NSColor(red: 0.357, green: 0.576, blue: 1.0, alpha: 1),
        ending: NSColor(red: 0.114, green: 0.31, blue: 0.8, alpha: 1)
    )!.draw(in: path, angle: -60)

    // Small sizes get a bigger symbol so it stays readable.
    let fraction: CGFloat = px <= 48 ? 0.62 : 0.5
    let config = NSImage.SymbolConfiguration(pointSize: size * fraction, weight: .semibold)
    guard let symbol = NSImage(systemSymbolName: symbolName, accessibilityDescription: nil)?
        .withSymbolConfiguration(config)
    else { fatalError("No SF Symbol called \(symbolName) on this Mac") }

    let white = NSImage(size: symbol.size, flipped: false) { rect in
        symbol.draw(in: rect)
        NSColor.white.set()
        rect.fill(using: .sourceAtop)
        return true
    }
    let target = NSSize(width: symbol.size.width, height: symbol.size.height)
    let origin = NSPoint(x: (size - target.width) / 2, y: (size - target.height) / 2)
    white.draw(in: NSRect(origin: origin, size: target))

    NSGraphicsContext.restoreGraphicsState()
    return rep
}

let out = CommandLine.arguments.count > 1 ? CommandLine.arguments[1] : "."
for (file, px) in sizes {
    let png = render(px: px).representation(using: .png, properties: [:])!
    try png.write(to: URL(fileURLWithPath: out).appendingPathComponent(file))
    print("wrote \(file)")
}
