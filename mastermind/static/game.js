/* game.js */

document.addEventListener('DOMContentLoaded', function() {
    const counterElement = document.getElementById('counter');
    if (counterElement) {
        const counterValue = parseInt(counterElement.textContent);
        const myrValues = {
            1: '0 MYR',
            2: '50 MYR',
            3: '100 MYR',
            4: '200 MYR',
            5: '300 MYR',
            6: '500 MYR',
            7: '1,000 MYR',
            8: '2,000 MYR',
            9: '4,000 MYR',
            10: '8,000 MYR',
            11: '16,000 MYR',
            12: '32,000 MYR',
            13: '64,000 MYR',
            14: '125,000 MYR',
            15: '500,000 MYR',
            16: '1,000,000 MYR',
            17: '2,000,000 MYR',
            18: '4,000,000 MYR',
            19: '8,000,000 MYR',
            20: '16,000,000 MYR',
            21: '32,000,000 MYR',
            22: '64,000,000 MYR',
            23: '125,000,000 MYR',
            24: '250,000,000 MYR',
            25: '500,000,000 MYR',
            26: '1,000,000,000 MYR',
            27: '2,000,000,000 MYR',
            28: '4,000,000,000 MYR',
            29: '8,000,000,000 MYR',
            30: '16,000,000,000 MYR',
            31: '32,000,000,000 MYR',
            32: '64,000,000,000 MYR',
            33: '125,000,000,000 MYR',
            34: '250,000,000,000 MYR',
            35: '500,000,000,000 MYR',
            36: '1,000,000,000,000 MYR',
            37: '2,000,000,000,000 MYR',
            38: '4,000,000,000,000 MYR',
            39: '8,000,000,000,000 MYR',
            40: '16,000,000,000,000 MYR'
        };

        if (myrValues.hasOwnProperty(counterValue)) {
            counterElement.textContent = myrValues[counterValue];
        }
    }

});
