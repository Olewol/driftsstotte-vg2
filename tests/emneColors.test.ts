import { describe, it, expect } from 'vitest';
import { getEmneColor, EMNE_LIST } from '../src/lib/emneColors';

describe('emneColors', () => {
  it('returns color token for nettverk', () =>
    expect(getEmneColor('nettverk')).toEqual({ color: '#4f8cff', bg: 'rgba(79,140,255,.13)' }));
  it('returns color token for it-drift', () =>
    expect(getEmneColor('it-drift')).toEqual({ color: '#ec4899', bg: 'rgba(236,72,153,.13)' }));
  it('returns fallback for unknown emne', () =>
    expect(getEmneColor('ukjent').color).toBe('#4f8cff'));
  it('EMNE_LIST contains all 6 emner', () =>
    expect(EMNE_LIST).toHaveLength(6));
});
