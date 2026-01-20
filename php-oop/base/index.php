<?php

function tampil()
{
    if (isset($_GET['a']) && isset($_GET['b'])) {
        $a = $_GET['a'];
        $b = $_GET['b'];
        echo "Hasil Penjumlahan: " . addition($a, $b);
    }
}
function addition($a, $b)
{
    return $a + $b;
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>WOKWOK JOKO SEMBUNG</title>
</head>
<body>
    <?php tampil(); ?>

    <form>
        <div>
            <label>Angka 1:</label>
            <input type="number" name="a">
        </div>

        <div>      
            <label>Angka 2:</label>
            <input type="number" name="b" >
        </div>
        <button type="submit">Kirim</button>
    </form>
</body>
</html>