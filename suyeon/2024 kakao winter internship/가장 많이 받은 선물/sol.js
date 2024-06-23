function solution(friends, gifts) {
    const giftDoc = {};
    const giverCount = {};
    const takerCount = {};

    for (let i = 0; i < gifts.length; i++) {
        const str = gifts[i];
        const [giver, taker] = str.split(' ');
        if (giverCount[giver]) {
            giverCount[giver]++;
        } else {
            giverCount[giver] = 1;
        }

        if (takerCount[taker]) {
            takerCount[taker]++;
        } else {
            takerCount[taker] = 1;
        }

        const reverseStr = `${taker} ${giver}`;
        if (!giftDoc[reverseStr]) {
            if (giftDoc[str]) {
                giftDoc[str]++;
            } else {
                giftDoc[str] = 1;
            }
        } else {
            giftDoc[reverseStr]--;
        }
    }
    // console.log('giftDoc', giftDoc);
    const scores = {};

    for (let i = 0; i < friends.length - 1; i++) {
        for (let j = i + 1; j < friends.length; ++j) {
            const a = friends[i];
            const b = friends[j];

            if (a == b) {
                continue;
            }

            const atob = giftDoc[`${a} ${b}`] ?? 0;
            const btoa = giftDoc[`${b} ${a}`] ?? 0;

            if (atob > btoa) {
                if (scores[a]) {
                    scores[a]++;
                } else {
                    scores[a] = 1;
                }
            } else if (atob < btoa) {
                if (scores[b]) {
                    scores[b]++;
                } else {
                    scores[b] = 1;
                }
            } else {
                const aScore = (giverCount[a] ?? 0) - (takerCount[a] ?? 0);
                const bScore = (giverCount[b] ?? 0) - (takerCount[b] ?? 0);

                if (aScore > bScore) {
                    if (scores[a]) {
                        scores[a]++;
                    } else {
                        scores[a] = 1;
                    }
                } else if (aScore < bScore) {
                    if (scores[b]) {
                        scores[b]++;
                    } else {
                        scores[b] = 1;
                    }
                }
            }
        }
    }

    const values = [...Object.values(scores)];
    return values.length ? Math.max(...[...Object.values(scores)]) : 0;
}
