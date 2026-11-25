{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/lungabalintulo7-lang/python-small-projects/blob/main/shopping_cart_program.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "items_list = []\n",
        "price_list = []\n",
        "total = 0\n",
        "\n",
        "while True:\n",
        "  try:\n",
        "    items = input(\"Enter a item to buy (done to checkout): \")\n",
        "    if items.lower() == \"done\":\n",
        "      break\n",
        "    else:\n",
        "      price = float(input(\"Enter the cost for the item: R\"))\n",
        "      items_list.append(items)\n",
        "      price_list.append(price)\n",
        "      total += price\n",
        "  except ValueError:\n",
        "    print(\"Invalid input. Please retry.\")\n",
        "\n",
        "print(\"\\n===== Your Cart =====\")\n",
        "for i in range(len(items_list)):\n",
        "  print(f\"{items_list[i]}: R{price_list[i]:.2f}\")\n",
        "\n",
        "print(f\"\\nYour total is: R{total:.2f}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "jB2-T-bTQ4XR",
        "outputId": "e61ea579-2cbe-4ed1-968f-cb7e70bc3520"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter a item to buy (done to checkout): phone\n",
            "Enter the cost for the item: R3500\n",
            "Enter a item to buy (done to checkout): Mcdonalds\n",
            "Enter the cost for the item: R200\n",
            "Enter a item to buy (done to checkout): Clothes\n",
            "Enter the cost for the item: R3500\n",
            "Enter a item to buy (done to checkout): done\n",
            "\n",
            "===== Your Cart =====\n",
            "phone: R3500.00\n",
            "Mcdonalds: R200.00\n",
            "Clothes: R3500.00\n",
            "\n",
            "Your total is: R7200.00\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "fGW5xdVsYnql"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}