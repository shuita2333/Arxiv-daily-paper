# 🧠 大模型相关研究 | 2026年07月22日

> 本类共 **204** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**201-204**（第 5/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-204**

---

### 201. [HOMIE: Human-object Centric Video Personalization via Multimodal Intelligent Enchancement](https://arxiv.org/abs/2607.18217)

**<font color=#1a73e8>作者：</font>** Yiyang Cai, Nan Chen, Rongchang Xie 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Human-object centric video personalization (HOCVP) is a core task within subject-driven video generation. However, existing methods suffer from two key limitations. First, most approaches focusing on inter-subject personalization still struggle to strike a balance between high subject fidelity and accurate interaction patterns between humans and diverse objects, especially when objects represent abstract concepts such as logos. Second, while intra-subject references (e.g., OCR maps, multi-view inputs) are expected to enhance subject fidelity, most existing works lack mechanisms to understand such latent correspondence. To address both challenges, we propose HOMIE, an HOCVP framework that tackles both inter- and intra-subject input settings in a unified manner. Compared to previous approaches, HOMIE proposes a better MLLM integration strategy to extract knowledge of reference-level relationships without compromising the controllability of text encoders or incurring costly re-alignment. Specifically, we introduce global multimodal guidance within self-attention to better align MLLM-derived semantic features with VAE tokens. Furthermore, we propose modality-reference embedding to differentiate tokens from MLLM features and VAE tokens and associate intra-subject reference image tokens. Extensive experiments validate that our method achieves state-of-the-art performance across various HOCVP tasks. Project Page: this https URL

---


### 202. [GigaPath-Flash and GigaTIME-Flash: Efficient Pathology Foundation Models for Whole-Slide and Tumor Microenvironment Analysis](https://arxiv.org/abs/2607.18218)

**<font color=#1a73e8>作者：</font>** Naoto Usuyama, Jeya Maria Jose Valanarasu, Sicong Yao 等 27 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Foundation models have emerged as a driving force in computational pathology, with the potential to transform cancer diagnosis, prognosis, and treatment selection by learning transferable representations from large-scale histopathology data. A growing landscape of pathology foundation models now spans diverse data sources, architectures, and downstream applications. However, most pretrained models operate only at the image-tile level, use restrictive licenses, and remain computationally expensive, limiting large-scale slide-level clinical and research use.
Here, we introduce GigaPath-Flash and GigaTIME-Flash, efficient models for whole-slide pathology AI and spatial proteomics prediction. GigaPath-Flash combines a 22M-parameter ViT-S tile encoder with a 21M-parameter LongNet slide encoder, both pretrained on large-scale real-world histopathology data. Its compact tile encoder is distilled from the billion-parameter GigaPath (ViT-g) teacher and shared by both models. GigaPath-Flash retains 97% of GigaPath's average slide-level performance with 50x less compute. GigaTIME-Flash extends this backbone to predict the tumor immune microenvironment directly from routine H&E images. It surpasses the original CNN-based GigaTIME in prediction quality while running 6x faster and using 8x less GPU memory.
Together with GigaPath and GigaTIME, these models form an open-weight, Apache-2.0-licensed family pretrained on large-scale real-world clinical data. By releasing all models and weights, we provide accessible building blocks for computational pathology, immuno-oncology, and precision health.

---


### 203. [Simple Domain Generalization for Strong Pixel-Level Image Tampering Detection in Modern VLMs](https://arxiv.org/abs/2607.18230)

**<font color=#1a73e8>作者：</font>** Yi Tang, Xinyi Shang, Jiacheng Cui 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modern vision-language models (VLMs) have significantly improved image generation and editing capabilities, making pixel-level image tampering detection increasingly important yet challenging under cross-model and out-of-distribution shifts. This work studies domain generalization for pixel-level image tampering detection in modern VLMs like ChatGPT, Gemini, Qwen-Image, etc., aiming to learn tampering localization models that remain robust across diverse VLM-generated manipulation distributions. We propose a simple yet effective domain-generalized training framework built on two practical strategies. First, we introduce a balanced minibatch sampling scheme that strategically samples tampered and real images in each minibatch, preventing biased optimization toward either manipulated artifacts or clean-image priors and avoiding training collapse, ensuring that each optimization step receives proper sampled gradient signals. Second, we adopt a simple late-injection strategy, where the detector is first trained on large-scale base data until stable convergence, and then exposed to a small amount of newly selected supporting data from emerging VLM distributions, improving adaptability without overfitting to limited new domains. Together, these components provide a simple yet strong recipe for improving pixel-level tampering localization and OOD robustness across modern VLMs. Despite the conceptual simplicity, our framework outperforms the prior state-of-the-art PIXAR by a large margin of 26.1% and 26.8% relative improvement in average gIoU and cIoU, respectively, across OOD VLMs of GPT-Images-2.0, Gemini-3.1, FLUX.2, and Seedream 4.5. Our code is available at this https URL

---


### 204. [It's Not What You Say, It's How You Say It: Evaluating LLM Responses to Expressions of Belief](https://arxiv.org/abs/2607.18232)

**<font color=#1a73e8>作者：</font>** Kevin Du, Clara Kümpel, Michelle Wastl 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Users frequently express their beliefs to large language models (LLMs). In some situations, the LLM should accept these contextual beliefs as true. In others, they should stick to their prior knowledge. Notably, users' expressions of belief (EoBs) can take linguistically diverse forms - using presuppositions, evidential and certainty markers, or varied tones - each of which may have a different persuasiveness over the LLMs. We introduce a typology to systematically evaluate how different EoBs affect whether models follow context versus prior knowledge. The typology is grounded in four linguistically motivated dimensions: form, evidentiality, epistemic stance, and tone, spanning 17 fine-grained types. By pairing these EoBs with world knowledge facts, we generate controlled EoB-query pairs that isolate the effect of linguistic variation. Using this benchmark, we evaluate 16 LLMs that differ in architecture (Llama3, Qwen3, Gemma3), scale (1B-30B parameters), and training stages (base vs instruct). We identify meaningful variations in response behavior across these axes, e.g., that bigger models and instruction models tend to be less context-following than smaller models and base models. We further identify specific EoBs that statistically significantly persuade LMs more consistently than others. Our work reveals systematic patterns in how linguistic framing affects LLM context integration, with implications for prompt engineering and model robustness.

---


> [!TIP]
> 当前位于：**201-204**（第 5/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-204**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
