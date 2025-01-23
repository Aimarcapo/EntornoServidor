<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Character extends Model
{
    protected $fillable = ['actor',    'name',    'description',    'house_id'];
    /** @use HasFactory<\Database\Factories\CharacterFactory> */
    use HasFactory;
}
