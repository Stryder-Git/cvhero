.. code:: ipython3

    import sys
    sys.path.append("../") 
    import cvhero as cv


.. parsed-literal::

    DONWLOADED


This is another demonstration
-----------------------------

.. code:: ipython3

    import pandas as pd

This is a major header
======================

.. code:: ipython3

    series = pd.Series([1, "two", 3.0])

.. code:: ipython3

    series




.. parsed-literal::

    0      1
    1    two
    2    3.0
    dtype: object



This is a minor header
^^^^^^^^^^^^^^^^^^^^^^

::

   with:
      * not one
      * but three
      * bulletpoints
       

.. code:: ipython3

    pd.concat([series, series], axis= 1)




.. raw:: html

    <div>
    <style scoped>
        .dataframe tbody tr th:only-of-type {
            vertical-align: middle;
        }
    
        .dataframe tbody tr th {
            vertical-align: top;
        }
    
        .dataframe thead th {
            text-align: right;
        }
    </style>
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>0</th>
          <th>1</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>1</td>
          <td>1</td>
        </tr>
        <tr>
          <th>1</th>
          <td>two</td>
          <td>two</td>
        </tr>
        <tr>
          <th>2</th>
          <td>3.0</td>
          <td>3.0</td>
        </tr>
      </tbody>
    </table>
    </div>



Thanks for watching


