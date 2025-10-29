{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPTKAhj8ilZeVGYIq4o+NI8",
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
        "<a href=\"https://colab.research.google.com/github/josegalindo23/data-science-portfolio/blob/main/Patient-Age-Analysis.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Patient Age Analysis Script"
      ],
      "metadata": {
        "id": "N8yQvhfdMYaW"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "age_px = [7,23,56,78,43,24,12,19,34,60]\n",
        "avg_age = sum(age_px)/len(age_px)\n",
        "age_older_50 = [e for e in age_px if e > 50]\n",
        "print(f\"the age older 50 are:\",age_older_50)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "w-XFedBYgPBy",
        "outputId": "07cc3a30-b1a8-4ef0-8f6a-644e97fecba9"
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "the age older 50 are: [56, 78, 60]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "pYRMdtQQgS8L"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}