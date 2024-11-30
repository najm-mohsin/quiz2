import os
import pygame

def load_assets_from_folder(folder_path):
    assets = {}
    for filename in os.listdir(folder_path):
        if filename.endswith('.png'):
            key = os.path.splitext(filename)[0]
            asset_path = os.path.join(folder_path, filename)
            assets[key] = pygame.image.load(asset_path)
    return assets

# Example usage in a Pygame application:
pygame.init()
screen = pygame.display.set_mode((800, 600))

# Load all assets from a folder
assets = load_assets_from_folder('assets')

# Use an asset
player_image = assets.get('player')  # Assuming a 'player.png' exists
screen.blit(player_image, (100, 100))
pygame.display.flip()
