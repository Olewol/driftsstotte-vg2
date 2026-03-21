import { describe, it, expect } from 'vitest';
import { slugify } from '../src/lib/slugify';

describe('slugify', () => {
  it('lowercases', () => expect(slugify('TCP')).toBe('tcp'));
  it('replaces spaces with hyphens', () => expect(slugify('tcp ip modellen')).toBe('tcp-ip-modellen'));
  it('replaces æ with ae', () => expect(slugify('nættverk')).toBe('naettverk'));
  it('replaces ø with oe', () => expect(slugify('størrelse')).toBe('stoerrelse'));
  it('replaces å with aa', () => expect(slugify('årsplan')).toBe('aarsplan'));
  it('strips special characters', () => expect(slugify('hello! world?')).toBe('hello-world'));
  it('collapses multiple hyphens', () => expect(slugify('a  --  b')).toBe('a-b'));
  it('trims leading and trailing hyphens', () => expect(slugify('--hello--')).toBe('hello'));
  it('handles full Norwegian note name', () =>
    expect(slugify('TCP/IP-modellen')).toBe('tcp-ip-modellen'));
});
