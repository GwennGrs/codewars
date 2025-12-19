import marimo

__generated_with = "0.18.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    # Import all my function to test everything
    from codewars.sum_multiple_3_5 import sum_multiples_3_5
    from codewars.dna_to_rna import dna_to_rna
    from codewars.first_non_repeating import first_non_repeating_letter
    from codewars.hamming_distance import hamming
    from codewars.mse import mean_square_error
    from codewars.order_str import order
    from codewars.order_weight import order_weight
    from codewars.sum_arrays import sum_array
    from codewars.tribonacci import tribonacci
    from codewars.zero_to_end import move_zeros
    return (
        dna_to_rna,
        first_non_repeating_letter,
        hamming,
        mean_square_error,
        mo,
        move_zeros,
        order,
        order_weight,
        sum_array,
        sum_multiples_3_5,
        tribonacci,
    )


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## sum_multiples_3_5
    """)
    return


@app.cell
def _(mo):
    slider = mo.ui.slider(start=0, stop=100, label="Value of n")
    mo.md(f"Choose a value :\n{slider}")
    return (slider,)


@app.cell
def _(slider, sum_multiples_3_5):
    sum_multiples_3_5(slider.value)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## tribonnacci
    """)
    return


@app.cell
def _(mo):
    n_input = mo.ui.number(start=1, stop=1000, label="n")
    mo.md(f"Insert number of iteration :\n{n_input}")
    return (n_input,)


@app.cell
def _(mo):
    array = mo.ui.dropdown(
        options={
            "[0, 0, 1]": [0, 0, 1],
            "[1, 1, 1]": [1, 1, 1],
            "[1, 2, 3]": [1, 2, 3],
        },
        label="signature",
    )
    mo.md(f"Choose which starting array you want :\n{array}")
    return (array,)


@app.cell
def _(array, n_input, tribonacci):
    tribonacci(array, n_input.value)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## first_non_repeating_letter
    """)
    return


@app.cell
def _(mo):
    text = mo.ui.text(placeholder="Word or short sentence", label="s")
    mo.md(f"Insert your string :\n{text}")
    return (text,)


@app.cell
def _(first_non_repeating_letter, text):
    first_non_repeating_letter(text.value)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## dna_to_rna
    """)
    return


@app.cell
def _(mo):
    dna = mo.ui.text(placeholder="Ex: CAGT", label="dna")
    mo.md(f"Insert your string :\n{dna}")
    return (dna,)


@app.cell
def _(dna, dna_to_rna):
    dna_to_rna(dna.value)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## hamming
    """)
    return


@app.cell
def _(mo):
    s1 = mo.ui.text(placeholder="Ex: Boat", label="word1")
    s2 = mo.ui.text(placeholder="Ex: Goat", label="word2")
    return s1, s2


@app.cell
def _(mo, s1):
    mo.md(f"Insert your string :\n{s1}")
    return


@app.cell
def _(mo, s2):
    mo.md(f"Insert your string :\n{s2}")
    return


@app.cell
def _(hamming, s1, s2):
    hamming(s1.value, s2.value)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## mse
    """)
    return


@app.cell
def _(mean_square_error):
    mean_square_error([1, 8, 7, 4], [1, 8, 7, 12])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## order
    """)
    return


@app.cell
def _(order):
    order("gon2na up4 Ne1ver 3you")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## sum_array
    """)
    return


@app.cell
def _(mo):
    list = mo.ui.text(placeholder="1, 8, 4", label="list")
    mo.md(f"Insert your number (separate by a coma) :\n{list}")
    return (list,)


@app.cell
def _(list):
    l = [int(x.strip()) for x in list.value.split(",") if x.strip()]
    return (l,)


@app.cell
def _(l, sum_array):
    sum_array(l)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## move_zeros
    """)
    return


@app.cell
def _(mo):
    bin_list = mo.ui.text(placeholder="0,1,0,1,0,0,1,0", label="list")
    mo.md(f"Insert your number (separate by a coma) :\n{bin_list}")
    return (bin_list,)


@app.cell
def _(bin_list):
    bin_l = [int(x.strip()) for x in bin_list.value.split(",") if x.strip()]
    return (bin_l,)


@app.cell
def _(bin_l, move_zeros):
    move_zeros(bin_l)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## order_weight
    """)
    return


@app.cell
def _(order_weight):
    order_weight("154 175 1 1224")
    return


if __name__ == "__main__":
    app.run()
