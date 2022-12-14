const std = @import("std");
const Allocator = std.mem.Allocator;
const List = std.ArrayList;
const Map = std.AutoHashMap;
const StrMap = std.StringHashMap;
const BitSet = std.DynamicBitSet;
const Str = []const u8;

const util = @import("util.zig");
const gpa = util.gpa;

const data = @embedFile("../01.txt");

pub fn main() !void {
    var count: u32 = 0;
    var window: [3]i64 = .{ 0, 0, 0 };
    var part1: u32 = 0;
    var part2: u32 = 0;

    var lines = tokenize(u8, data, "\r\n");
    while (lines.next()) |line| {
        const num = parseInt(i64, line, 10) catch unreachable;

        if (count >= 1 and num > window[2]) {
            part1 += 1;
        }
        if (count >= 3 and num > window[0]) {
            part2 += 1;
        }

        window[0] = window[1];
        window[1] = window[2];
        window[2] = num;
        count += 1;
    }

    print("part1={}, part2={}\n", .{part1, part2});
}

// Useful stdlib functions
const tokenize = std.mem.tokenize;
const split = std.mem.split;
const indexOf = std.mem.indexOfScalar;
const indexOfAny = std.mem.indexOfAny;
const indexOfStr = std.mem.indexOfPosLinear;
const lastIndexOf = std.mem.lastIndexOfScalar;
const lastIndexOfAny = std.mem.lastIndexOfAny;
const lastIndexOfStr = std.mem.lastIndexOfLinear;
const trim = std.mem.trim;
const sliceMin = std.mem.min;
const sliceMax = std.mem.max;

const parseInt = std.fmt.parseInt;
const parseFloat = std.fmt.parseFloat;

const min = std.math.min;
const min3 = std.math.min3;
const max = std.math.max;
const max3 = std.math.max3;

const print = std.debug.print;
const assert = std.debug.assert;

const sort = std.sort.sort;
const asc = std.sort.asc;
const desc = std.sort.desc;
