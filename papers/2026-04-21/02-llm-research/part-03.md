# 🧠 大模型相关研究 | 2026年04月21日

> 本类共 **114** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**101-114**（第 3/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-114**

---

### 101. [Optimizing Korean-Centric LLMs via Token Pruning](https://arxiv.org/abs/2604.16235)

**<font color=#1a73e8>作者：</font>** Hoyeol Kim, Hyeonwoo Kim  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper presents a systematic benchmark of state-of-the-art multilingual large language models (LLMs) adapted via token pruning - a compression technique that eliminates tokens and embedding parameters corresponding to languages irrelevant to the target application. Focusing on Korean-centric natural language processing (NLP) tasks, we evaluate architectures including Qwen3, Gemma-3, Llama-3, and Aya across three vocabulary configurations: Original, English-Korean (EnKo), and English-Korean-Chinese (EnKoZh). Performance is assessed using established benchmarks for general aptitude, cultural literacy, instruction following, and machine translation. Our findings indicate that token pruning significantly improves generation stability by eliminating language confusion, and in the case of machine translation, frequently enhances performance on Korean-specific tasks. While instruction-following capabilities display architecture-dependent variance linked to latent cross-lingual representations, the significant reduction in vocabulary size validates token pruning as a highly effective optimization strategy for memory-constrained, domain-specific deployments, despite modest gains in inference latency.

---


### 102. [BAGEL: Benchmarking Animal Knowledge Expertise in Language Models](https://arxiv.org/abs/2604.16241)

**<font color=#1a73e8>作者：</font>** Jiacheng Shen, Masato Hagiwara, Milad Alizadeh 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models have shown strong performance on broad-domain knowledge and reasoning benchmarks, but it remains unclear how well language models handle specialized animal-related knowledge under a unified closed-book evaluation protocol. We introduce BAGEL, a benchmark for evaluating animal knowledge expertise in language models. BAGEL is constructed from diverse scientific and reference sources, including bioRxiv, Global Biotic Interactions, Xeno-canto, and Wikipedia, using a combination of curated examples and automatically generated closed-book question-answer pairs. The benchmark covers multiple aspects of animal knowledge, including taxonomy, morphology, habitat, behavior, vocalization, geographic distribution, and species interactions. By focusing on closed-book evaluation, BAGEL measures animal-related knowledge of models without external retrieval at inference time. BAGEL further supports fine-grained analysis across source domains, taxonomic groups, and knowledge categories, enabling a more precise characterization of model strengths and systematic failure modes. Our benchmark provides a new testbed for studying domain-specific knowledge generalization in language models and for improving their reliability in biodiversity-related applications.

---


### 103. [Joint-Centric Dual Contrastive Alignment with Structure-Preserving and Information-Balanced Regularization](https://arxiv.org/abs/2604.16247)

**<font color=#1a73e8>作者：</font>** Habibeh Naderi, Behrouz Haji Soleimani, Stan Matwin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose HILBERT (HIerarchical Long-sequence Balanced Embedding with Reciprocal contrastive Training), a cross-attentive multimodal framework for learning document-level audio-text representations from long, segmented sequences in low-resource data settings. HILBERT leverages frozen pre-trained speech and language encoders to extract segment-level features, which are aggregated via cross-modal attention and self-attentive pooling to form modality-specific document representations and a joint cross-attentive embedding. To align modalities while preserving modality-specific structure under severe audio-text dimensional imbalance, we introduce a reciprocal dual contrastive objective that simultaneously aligns audio-to-joint and text-to-joint representations, rather than directly contrasting audio and text alone. Two auxiliary regularizers further stabilize long-sequence fusion: a Centered Kernel Alignment (CKA) loss that preserves structural consistency between each modality and the joint embedding, and a mutual information balancing loss that prevents dominance of a single modality by equalizing information flow from audio and text into the joint space. For downstream prediction, HILBERT employs a Mixture-of-Experts (MoE) classifier over concatenated audio, text, and joint representations to accommodate heterogeneous label regimes. Extensive evaluation across multiple audio-text backbone combinations demonstrates that HILBERT learns semantically meaningful long-sequence representations and achieves superior performance on highly imbalanced multi-class settings.

---


### 104. [Where Do Vision-Language Models Fail? World Scale Analysis for Image Geolocalization](https://arxiv.org/abs/2604.16248)

**<font color=#1a73e8>作者：</font>** Siddhant Bharadwaj, Ashish Vashist, Fahimul Aleem 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image geolocalization has traditionally been addressed through retrieval-based place recognition or geometry-based visual localization pipelines. Recent advances in Vision-Language Models (VLMs) have demonstrated strong zero-shot reasoning capabilities across multimodal tasks, yet their performance in geographic inference remains underexplored. In this work, we present a systematic evaluation of multiple state-of-the-art VLMs for country-level image geolocalization using ground-view imagery only. Instead of relying on image matching, GPS metadata, or task-specific training, we evaluate prompt-based country prediction in a zero-shot setting. The selected models are tested on three geographically diverse datasets to assess their robustness and generalization ability. Our results reveal substantial variation across models, highlighting the potential of semantic reasoning for coarse geolocalization and the limitations of current VLMs in capturing fine-grained geographic cues. This study provides the first focused comparison of modern VLMs for country-level geolocalization and establishes a foundation for future research at the intersection of multimodal reasoning and geographic understanding.

---


### 105. [Do Vision-Language Models Truly Perform Vision Reasoning? A Rigorous Study of the Modality Gap](https://arxiv.org/abs/2604.16256)

**<font color=#1a73e8>作者：</font>** Yige Xu, Yongjie Wang, Zizhuo Wu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reasoning in vision-language models (VLMs) has recently attracted significant attention due to its broad applicability across diverse downstream tasks. However, it remains unclear whether the superior performance of VLMs stems from genuine vision-grounded reasoning or relies predominantly on the reasoning capabilities of their textual backbones. To systematically measure this, we introduce CrossMath, a novel multimodal reasoning benchmark designed for controlled cross-modal comparisons. Specifically, we construct each problem in text-only, image-only, and image+text formats guaranteeing identical task-relevant information, verified by human annotators. This rigorous alignment effectively isolates modality-specific reasoning differences while eliminating confounding factors such as information mismatch. Extensive evaluation of state-of-the-art VLMs reveals a consistent phenomenon: a substantial performance gap between textual and visual reasoning. Notably, VLMs excel with text-only inputs, whereas incorporating visual data (image+text) frequently degrades performance compared to the text-only baseline. These findings indicate that current VLMs conduct reasoning primarily in the textual space, with limited genuine reliance on visual evidence. To mitigate this limitation, we curate a CrossMath training set for VLM fine-tuning. Empirical evaluations demonstrate that fine-tuning on this training set significantly boosts reasoning performance across all individual and joint modalities, while yielding robust gains on two general visual reasoning tasks. Source code is available at this https URL.

---


### 106. [Characterising LLM-Generated Competency Questions: a Cross-Domain Empirical Study using Open and Closed Models](https://arxiv.org/abs/2604.16258)

**<font color=#1a73e8>作者：</font>** Reham Alharbi, Valentina Tamma, Terry R. Payne 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Competency Questions (CQs) are a cornerstone of requirement elicitation in ontology engineering. CQs represent requirements as a set of natural language questions that an ontology should satisfy; they are traditionally modelled by ontology engineers together with domain experts as part of a human-centred, manual elicitation process. The use of Generative AI automates CQ creation at scale, therefore democratising the process of generation, widening stakeholder engagement, and ultimately broadening access to ontology engineering. However, given the large and heterogeneous landscape of LLMs, varying in dimensions such as parameter scale, task and domain specialisation, and accessibility, it is crucial to characterise and understand the intrinsic, observable properties of the CQs they produce (e.g., readability, structural complexity) through a systematic, cross-domain analysis. This paper introduces a set of quantitative measures for the systematic comparison of CQs across multiple dimensions. Using CQs generated from well defined use cases and scenarios, we identify their salient properties, including readability, relevance with respect to the input text and structural complexity of the generated questions. We conduct our experiments over a set of use cases and requirements using a range of LLMs, including both open (KimiK2-1T, LLama3.1-8B, LLama3.2-3B) and closed models (Gemini 2.5 Pro, GPT 4.1). Our analysis demonstrates that LLM performance reflects distinct generation profiles shaped by the use case.

---


### 107. [SwanNLP at SemEval-2026 Task 5: An LLM-based Framework for Plausibility Scoring in Narrative Word Sense Disambiguation](https://arxiv.org/abs/2604.16262)

**<font color=#1a73e8>作者：</font>** Deshan Sumanathilaka, Nicholas Micallef, Julian Hough 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent advances in language models have substantially improved Natural Language Understanding (NLU). Although widely used benchmarks suggest that Large Language Models (LLMs) can effectively disambiguate, their practical applicability in real-world narrative contexts remains underexplored. SemEval-2026 Task 5 addresses this gap by introducing a task that predicts the human-perceived plausibility of a word sense within a short story. In this work, we propose an LLM-based framework for plausibility scoring of homonymous word senses in narrative texts using a structured reasoning mechanism. We examine the impact of fine-tuning low-parameter LLMs with diverse reasoning strategies, alongside dynamic few-shot prompting for large-parameter models, on accurate sense identification and plausibility estimation. Our results show that commercial large-parameter LLMs with dynamic few-shot prompting closely replicate human-like plausibility judgments. Furthermore, model ensembling slightly improves performance, better simulating the agreement patterns of five human annotators compared to single-model predictions

---


### 108. [Information Router for Mitigating Modality Dominance in Vision-Language Models](https://arxiv.org/abs/2604.16264)

**<font color=#1a73e8>作者：</font>** Seulgi Kim, Mohit Prabhushankar, Ghassan AlRegib  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision Language models (VLMs) have demonstrated strong performance across a wide range of benchmarks, yet they often suffer from modality dominance, where predictions rely disproportionately on a single modality. Prior approaches primarily address this issue by steering model's attention allocation, implicitly assuming that all modalities provide sufficient information. However, attention only determines where the model focuses, and cannot enrich information that is missing or ambiguous. In the real world, input modalities often differ in information density and their signal-to-noise ratios. In such cases, simply adjusting model's attention does not resolve the underlying lack of information. In this paper, we propose \textsc{MoIR}: \textit{Multi-modal Information Router}, an information-level fusion method that explicitly reduces information disparity prior to fusion. \textsc{MoIR} identifies less informative tokens and routes complementary information from a stronger modality, constructing information-dense token representations before they are processed by a large language model. By modifying information availability, \textsc{MoIR} enables reliable shifts in modality dominance, even when one modality is degraded. We evaluate \textsc{MoIR} on three widely used multi-modal benchmarks across multiple model backbones. Experimental results show that \textsc{MoIR} consistently demonstrates more balanced modality contribution, and improves robustness and downstream performance, particularly even under modality degradation. These findings demonstrate that explicitly modifying cross-modal information is an effective and complementary strategy for mitigating modality dominance in multi-modal reasoning models.

---


### 109. [From Benchmarking to Reasoning: A Dual-Aspect, Large-Scale Evaluation of LLMs on Vietnamese Legal Text](https://arxiv.org/abs/2604.16270)

**<font color=#1a73e8>作者：</font>** Van-Truong Le  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The complexity of Vietnam's legal texts presents a significant barrier to public access to justice. While Large Language Models offer a promising solution for legal text simplification, evaluating their true capabilities requires a multifaceted approach that goes beyond surface-level metrics. This paper introduces a comprehensive dual-aspect evaluation framework to address this need. First, we establish a performance benchmark for four state-of-the-art large language models (GPT-4o, Claude 3 Opus, Gemini 1.5 Pro, and Grok-1) across three key dimensions: Accuracy, Readability, and Consistency. Second, to understand the "why" behind these performance scores, we conduct a large-scale error analysis on a curated dataset of 60 complex Vietnamese legal articles, using a novel, expert-validated error typology. Our results reveal a crucial trade-off: models like Grok-1 excel in Readability and Consistency but compromise on fine-grained legal Accuracy, while models like Claude 3 Opus achieve high Accuracy scores that mask a significant number of subtle but critical reasoning errors. The error analysis pinpoints \textit{Incorrect Example} and \textit{Misinterpretation} as the most prevalent failures, confirming that the primary challenge for current LLMs is not summarization but controlled, accurate legal reasoning. By integrating a quantitative benchmark with a qualitative deep dive, our work provides a holistic and actionable assessment of LLMs for legal applications.

---


### 110. [No Universal Courtesy: A Cross-Linguistic, Multi-Model Study of Politeness Effects on LLMs Using the PLUM Corpus](https://arxiv.org/abs/2604.16275)

**<font color=#1a73e8>作者：</font>** Hitesh Mehta, Arjit Saxena, Garima Chhikara 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper explores the response of Large Language Models (LLMs) to user prompts with different degrees of politeness and impoliteness. The Politeness Theory by Brown and Levinson and the Impoliteness Framework by Culpeper form the basis of experiments conducted across three languages (English, Hindi, Spanish), five models (Gemini-Pro, GPT-4o Mini, Claude 3.7 Sonnet, DeepSeek-Chat, and Llama 3), and three interaction histories between users (raw, polite, and impolite). Our sample consists of 22,500 pairs of prompts and responses of various types, evaluated across five levels of politeness using an eight-factor assessment framework: coherence, clarity, depth, responsiveness, context retention, toxicity, conciseness, and readability. The findings show that model performance is highly influenced by tone, dialogue history, and language. While polite prompts enhance the average response quality by up to ~11% and impolite tones worsen it, these effects are neither consistent nor universal across languages and models. English is best served by courteous or direct tones, Hindi by deferential and indirect tones, and Spanish by assertive tones. Among the models, Llama is the most tone-sensitive (11.5% range), whereas GPT is more robust to adversarial tone. These results indicate that politeness is a quantifiable computational variable that affects LLM behaviour, though its impact is language- and model-dependent rather than universal. To support reproducibility and future work, we additionally release PLUM (Politeness Levels in Utterances, Multilingual), a publicly available corpus of 1,500 human-validated prompts across three languages and five politeness categories, and provide a formal supplementary analysis of six falsifiable hypotheses derived from politeness theory, empirically assessed against the dataset.

---


### 111. [Learning to Reason with Insight for Informal Theorem Proving](https://arxiv.org/abs/2604.16278)

**<font color=#1a73e8>作者：</font>** Yunhe Li, Hao Shi, Bowen Deng 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Although most of the automated theorem-proving approaches depend on formal proof systems, informal theorem proving can align better with large language models' (LLMs) strength in natural language processing. In this work, we identify a primary bottleneck in informal theorem proving as a lack of insight, namely the difficulty of recognizing the core techniques required to solve complex problems. To address this, we propose a novel framework designed to cultivate this essential reasoning skill and enable LLMs to perform insightful reasoning. We propose $\mathtt{DeepInsightTheorem}$, a hierarchical dataset that structures informal proofs by explicitly extracting core techniques and proof sketches alongside the final proof. To fully exploit this dataset, we design a Progressive Multi-Stage SFT strategy that mimics the human learning process, guiding the model from basic proof writing to insightful thinking. Our experiments on challenging mathematical benchmarks demonstrate that this insight-aware generation strategy significantly outperforms baselines. These results demonstrate that teaching models to identify and apply core techniques can substantially improve their mathematical reasoning.

---


### 112. [Evaluating the Progression of Large Language Model Capabilities for Small-Molecule Drug Design](https://arxiv.org/abs/2604.16279)

**<font color=#1a73e8>作者：</font>** Shriram Chennakesavalu, Kirill Shmilovich, Hayley Weir 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have the potential to accelerate small molecule drug design due to their ability to reason about information from diverse sources and formats. However, their practical utility remains unclear due to the lack of benchmarks that reflect real-world scenarios. In this work, we introduce a suite of chemically-grounded tasks spanning molecular property prediction, molecular representation transformations, and molecular design. Importantly, we formulate these tasks as reinforcement learning (RL) environments, enabling a unified approach for evaluation and post-training. Across three model families, we find that frontier models are increasingly proficient at chemical tasks, but that there is significant room for improvement, especially in experimental settings with low data. Critically, we show that RL-based post-training can substantially improve performance. A smaller model post-trained on our environments becomes competitive with state-of-the-art frontier models, despite a significantly weaker base model. This suggests a practical route toward employing LLMs in drug discovery; by combining carefully-designed evaluation tasks with targeted post-training, we can both elucidate and close critical capability gaps.

---


### 113. [Using Large Language Models and Knowledge Graphs to Improve the Interpretability of Machine Learning Models in Manufacturing](https://arxiv.org/abs/2604.16280)

**<font color=#1a73e8>作者：</font>** Thomas Bayer, Alexander Lohr, Sarah Weiß 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Explaining Machine Learning (ML) results in a transparent and user-friendly manner remains a challenging task of Explainable Artificial Intelligence (XAI). In this paper, we present a method to enhance the interpretability of ML models by using a Knowledge Graph (KG). We store domain-specific data along with ML results and their corresponding explanations, establishing a structured connection between domain knowledge and ML insights. To make these insights accessible to users, we designed a selective retrieval method in which relevant triplets are extracted from the KG and processed by a Large Language Model (LLM) to generate user-friendly explanations of ML results. We evaluated our method in a manufacturing environment using the XAI Question Bank. Beyond standard questions, we introduce more complex, tailored questions that highlight the strengths of our approach. We evaluated 33 questions, analyzing responses using quantitative metrics such as accuracy and consistency, as well as qualitative ones such as clarity and usefulness. Our contribution is both theoretical and practical: from a theoretical perspective, we present a novel approach for effectively enabling LLMs to dynamically access a KG in order to improve the explainability of ML results. From a practical perspective, we provide empirical evidence showing that such explanations can be successfully applied in real-world manufacturing environments, supporting better decision-making in manufacturing processes.

---


### 114. [FineCog-Nav: Integrating Fine-grained Cognitive Modules for Zero-shot Multimodal UAV Navigation](https://arxiv.org/abs/2604.16298)

**<font color=#1a73e8>作者：</font>** Dian Shao, Zhengzheng Xu, Peiyang Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> UAV vision-language navigation (VLN) requires an agent to navigate complex 3D environments from an egocentric perspective while following ambiguous multi-step instructions over long horizons. Existing zero-shot methods remain limited, as they often rely on large base models, generic prompts, and loosely coordinated modules. In this work, we propose FineCog-Nav, a top-down framework inspired by human cognition that organizes navigation into fine-grained modules for language processing, perception, attention, memory, imagination, reasoning, and decision-making. Each module is driven by a moderate-sized foundation model with role-specific prompts and structured input-output protocols, enabling effective collaboration and improved interpretability. To support fine-grained evaluation, we construct AerialVLN-Fine, a curated benchmark of 300 trajectories derived from AerialVLN, with sentence-level instruction-trajectory alignment and refined instructions containing explicit visual endpoints and landmark references. Experiments show that FineCog-Nav consistently outperforms zero-shot baselines in instruction adherence, long-horizon planning, and generalization to unseen environments. These results suggest the effectiveness of fine-grained cognitive modularization for zero-shot aerial navigation. Project page: this https URL.

---


> [!TIP]
> 当前位于：**101-114**（第 3/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-114**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
