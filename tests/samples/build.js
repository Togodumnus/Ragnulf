(function () {

    /**
     * Générateur de jeux de test pour Ragnulf
     *
     * Génère un fichier JSON contenant 60 cubes et l'application de tous les
     * mouvements sur chacun.
     * Le jeu de test va servir pour les tests unitaires de Ragnulf.
     *
     * @example
     *
        {
            <cube original 1> : {
                'U' : <résulat de U sur 1>,
                'Ui' : <résulat de Ui sur 1>,
                ...
            },
            ...
        }
     *
     * @example
     *
        node build.js //sortie dans sample.js
        node build.js -o monBeauFichier_RoiDeNoël.js
     *
     */

    'use strict';

    var fs   = require('fs'),
        path = require('path'),
        Cube = require('./cubejs/lib/cube.js');

    var argv = process.argv;

    var DEFAULT_FILE = 'sample.json';

    var CONVERT_COLORS = {
        'U' : 'Y',
        'L' : 'O',
        'F' : 'B',
        'R' : 'R',
        'B' : 'G',
        'D' : 'W'
    };

    /**
     * translateRotation
     *
     * @param   {String}    r   Une rotation (notation Ragnulf, ie. Ri)
     *
     * @return  {String}        Une rotation (notation cube.js, ie. R')
     */
    var translateRotation = function (r) {
        return r.slice(-1) === 'i' ? r[0].concat("'") : r;
    };

    /**
     * fixCubeString
     *
     * Le développeur de cube.js a implémenté une fonction Cube::asString()
     * qui renvoie l'état du cube sous forme de chaîne
     * Mais la chaîne ne respecte pas nos notations. On fixe ça ici.
     *
     * Notations de Cubejs:
     *
                     +------------+
                     | U1  U2  U3 |
                     |            |
                     | U4  U5  U6 |
                     |            |
                     | U7  U8  U9 |
        +------------+------------+------------+------------+
        | L1  L2  L3 | F1  F2  F3 | R1  R2  F3 | B1  B2  B3 |
        |            |            |            |            |
        | L4  L5  L6 | F4  F5  F6 | R4  R5  R6 | B4  B5  B6 |
        |            |            |            |            |
        | L7  L8  L9 | F7  F8  F9 | R7  R8  R9 | B7  B8  B9 |
        +------------+------------+------------+------------+
                     | D1  D2  D3 |
                     |            |
                     | D4  D5  D6 |
                     |            |
                     | D7  D8  D9 |
                     +------------+
     *
     * Sous forme de chaîne, le cube est représenté par un ordre super chelou :
     *
            UUUUUUUUUR...F...D...L...B...
     *
     * @see https://github.com/akheron/cubejs#cubefromstringstr
     *
     * @param   {String}    str     Une chaîne renvoyée par Cube::asString()
     * @return  {String}            Le fix
     */
    var fixCubeString = function (str) {

        var result = str.substr(0, 9) //on commence par la face UP
        var lignes = ["", "", ""];    //les futures 3 lignes LFRB

        //construction des 3 lignes du milieu (alternance R, F, L, B)
        var faces = [4, 2, 1, 5]; //les faces dans l'ordre LFRB
        for (var x=0; x < 4; x++) {
            var i = faces[x];     //n° de la face

            var xoffset = i * 9;         //nombre de faces à passer
            for (var j=0; j < 3; j++) {  //pour les 3 lignes
                var yoffset = j * 3;     //nombre de ligne à descendre
                lignes[j] += str.substr( //on prend 3 caractères
                    xoffset + yoffset,
                    3
                );
            }
        }

        //on ajoute les 3 lignes
        result = result.concat(lignes[0], lignes[1], lignes[2]);
        //on ajoute Down
        result = result.concat(str.substr(27, 9))

        return result; //done
    };

    /**
     * convertColors
     *
     * Cubejs n'utilise pas les couleurs mais l'identifiant des faces
     * (U, L, F, ...) pour nommer ses facettes
     * On remplace par les couleurs (Y, O, B, ...)
     *
     * @param   {String}    str     Un état de cube
     *
     * @return  {String}            Même état, mais avec les couleurs
     */
    var convertColors = function (str) {
        return str.split('').map(function (c) {
            return CONVERT_COLORS[c];
        }).join('');
    };

    /**
     * buildRandom
     *
     * Génère un rubik's cube et applique dessus tous les mouvements.
     * Retourne le cube random et les résultats de tous les mouvements.
     *
     * @param   {Function}  callback
     */
    var buildRandom = function (callback) {

        var moves = { //les 18 mouvements
            "U"  : null,
            "Ui" : null,
            "U2" : null,
            "L"  : null,
            "Li" : null,
            "L2" : null,
            "F"  : null,
            "Fi" : null,
            "F2" : null,
            "R"  : null,
            "Ri" : null,
            "R2" : null,
            "B"  : null,
            "Bi" : null,
            "B2" : null,
            "D"  : null,
            "Di" : null,
            "D2" : null,
        };

        //cube random
        var c = new Cube();
        c.randomize();

        //on applique le mouvement et on fix l'output
        Object.keys(moves).forEach(function (m) {
            var cube = c.move(translateRotation(m)).asString();
            moves[m] = convertColors(fixCubeString(cube));
        });

        callback(convertColors(fixCubeString(c.asString())), moves);
    };

    /**
     * buildSamples
     *
     * @param   {int}       n           nombre de samples à générer
     * @param   {Function}  callback
     */
    var buildSamples = function (n, callback) {
        var samples = {};
        for (var i=0; i < n; i++) {
            buildRandom(function (origin, moves) {
                samples[origin] = moves;
            });
        }

        callback(samples)
    };

    //on demande 60 rubik's cube aléatoires (18 mouvements chacun)
    buildSamples(60, function(result) {
        //on save le résultat dans sample.json
        var content = JSON.stringify(result);

        //le nom du fichier
        var file = argv.length > 2 && argv[2] == '-o' ? argv[3] : DEFAULT_FILE;

        fs.writeFile(path.join(__dirname, file), content, function (err) {
            if (err) {
                return console.error(err);
            }
            console.log("Jeu sample sauvé dans", file);
        });
    });

}());
