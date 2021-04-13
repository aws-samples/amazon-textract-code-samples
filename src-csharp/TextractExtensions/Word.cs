/*
class Word:
    def __init__(self, block, blockMap):
        self._block = block
        self._confidence = block['Confidence']
        self._geometry = Geometry(block['Geometry'])
        self._id = block['Id']
        self._text = ""
        if(block['Text']):
            self._text = block['Text']

    def __str__(self):
        return self._text

    @property
    def confidence(self):
        return self._confidence

    @property
    def geometry(self):
        return self._geometry

    @property
    def id(self):
        return self._id

    @property
    def text(self):
        return self._text

    @property
    def block(self):
        return self._block
 */

using System.Collections.Generic;
using Amazon.Textract.Model;

namespace Amazon.Textract.Model {
	public class Word {
		public Word(Block block, Dictionary<string, Block> blocks) {
			this.Block = block ?? new Block();
			this.Blocks = blocks ?? new Dictionary<string, Block>();
			this.Confidence = block == null ? 0 : block.Confidence;
			this.Geometry = block == null ? new Geometry() : block.Geometry;
            this.Id = block == null ? string.Empty : block.Id;
			this.Text = block == null ? string.Empty : block.Text;
		}

		public Block Block { get; set; }
		public Dictionary<string, Block> Blocks { get; set; }
		public float Confidence { get; set; }
		public Geometry Geometry { get; set; }
		public string Id { get; set; }
		public string Text { get; set; }

		public override string ToString() {
			return Text;
		}
	}
}