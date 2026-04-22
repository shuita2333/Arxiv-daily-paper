# 🧠 大模型相关研究 | 2026年04月23日

> 本类共 **132** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**51-100**（第 2/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-132](./part-03.md)

---

### 51. [SAMoRA: Semantic-Aware Mixture of LoRA Experts for Task-Adaptive Learning](https://arxiv.org/abs/2604.19048)

**<font color=#1a73e8>作者：</font>** Boyan Shi, Wei Chen, Shuyuan Zhao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The combination of Mixture-of-Experts (MoE) and Low-Rank Adaptation (LoRA) has shown significant potential for enhancing the multi-task learning capabilities of Large Language Models. However, existing methods face two primary challenges: (1)Imprecise Routing in the current MoE-LoRA method fails to explicitly match input semantics with expert capabilities, leading to weak expert specialization. (2)Uniform weight fusion strategies struggle to provide adaptive update strengths, overlooking the varying complexity of different tasks. To address these limitations, we propose SAMoRA (Semantic-Aware Mixture of LoRA Experts), a novel parameter-efficient fine-tuning framework tailored for task-adaptive learning. Specifically, A Semantic-Aware Router is proposed to explicitly align textual semantics with the most suitable experts for precise routing. A Task-Adaptive Scaling mechanism is designed to regulate expert contributions based on specific task requirements dynamically. In addition, a novel regularization objective is proposed to jointly promote expert specialization and effective scaling. Extensive experiments on multiple multi-task benchmarks demonstrate that SAMoRA significantly outperforms the state-of-the-art methods and holds excellent task generalization capabilities. Code is available at this https URL

---


### 52. [Cell-Based Representation of Relational Binding in Language Models](https://arxiv.org/abs/2604.19052)

**<font color=#1a73e8>作者：</font>** Qin Dai, Benjamin Heinzerling, Kentaro Inui  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Understanding a discourse requires tracking entities and the relations that hold between them. While Large Language Models (LLMs) perform well on relational reasoning, the mechanism by which they bind entities, relations, and attributes remains unclear. We study discourse-level relational binding and show that LLMs encode it via a Cell-based Binding Representation (CBR): a low-dimensional linear subspace in which each ``cell'' corresponds to an entity--relation index pair, and bound attributes are retrieved from the corresponding cell during inference. Using controlled multi-sentence data annotated with entity and relation indices, we identify the CBR subspace by decoding these indices from attribute-token activations with Partial Least Squares regression. Across domains and two model families, the indices are linearly decodable and form a grid-like geometry in the projected space. We further find that context-specific CBR representations are related by translation vectors in activation space, enabling cross-context transfer. Finally, activation patching shows that manipulating this subspace systematically changes relational predictions and that perturbing it disrupts performance, providing causal evidence that LLMs rely on CBR for relational binding.

---


### 53. [Reinforcement Learning Improves LLM Accuracy and Reasoning in Disease Classification from Radiology Reports](https://arxiv.org/abs/2604.19060)

**<font color=#1a73e8>作者：</font>** Yishu Wei, Yi Lin, Adam Flanders 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Accurate disease classification from radiology reports is essential for many applications. While supervised fine-tuning (SFT) of lightweight LLMs improves accuracy, it can degrade reasoning. We propose a two-stage approach: SFT on disease labels followed by Group Relative Policy Optimization (GRPO) to refine predictions by optimizing accuracy and format without reasoning supervision. Across three radiologist-annotated datasets, SFT outperformed baselines and GRPO further improved classification and enhanced reasoning recall and comprehensiveness.

---


### 54. [TRN-R1-Zero: Text-rich Network Reasoning via LLMs with Reinforcement Learning Only](https://arxiv.org/abs/2604.19070)

**<font color=#1a73e8>作者：</font>** Yilun Liu, Ruihong Qiu, Zi Huang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Zero-shot reasoning on text-rich networks (TRNs) remains a challenging frontier, as models must integrate textual semantics with relational structure without task-specific supervision. While graph neural networks rely on fixed label spaces and supervised objectives, recent large language model (LLM)-based approaches often overlook graph context or depend on distillation from larger models, limiting generalisation. We propose TRN-R1-Zero, a post-training framework for TRN reasoning trained solely via reinforcement learning. TRN-R1-Zero directly optimises base LLMs using a Neighbour-aware Group Relative Policy Optimisation objective that dynamically adjusts rewards based on a novel margin gain metric for the informativeness of neighbouring signals, effectively guiding the model toward relational reasoning. Unlike prior methods, TRN-R1-Zero requires no supervised fine-tuning or chain-of-thought data generated from large reasoning models. Extensive experiments across citation, hyperlink, social and co-purchase TRN benchmarks demonstrate the superiority and robustness of TRN-R1-Zero. Moreover, relying strictly on node-level training, TRN-R1-Zero achieves zero-shot inference on edge- and graph-level tasks, extending beyond cross-domain transfer. The codebase is publicly available at this https URL.

---


### 55. [HoWToBench: Holistic Evaluation for LLM's Capability in Human-level Writing using Tree of Writing](https://arxiv.org/abs/2604.19071)

**<font color=#1a73e8>作者：</font>** Andrew Zhuoer Feng, Cunxiang Wang, Yu Luo 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Evaluating the writing capabilities of large language models (LLMs) remains a significant challenge due to the multidimensional nature of writing skills and the limitations of existing metrics. LLM's performance in thousand-words level and open-ended writing is inadequately assessed by traditional reference-based metrics or modern LLM-as-a-judge methods. We propose Tree-of-Writing (ToW), to resolve the implicit inconsistency often found when LLM-as-a-judge aggregates all sub-features in text evaluation. ToW incorporates a tree-structured workflow by explicitly modeling the aggregation weights of sub-features. We also present HowToBench, a large-scale Chinese writing benchmark encompassing 12 genres and 1302 instructions across three task categories: contextual completion, outline-guided writing, and open-ended generation. ToW successfully mitigates the biases, achieving a 0.93 Pearson correlation with human judgments. Furthermore, we detect that both overlap-based text generation metrics and popular LLM-as-a-judge practices are vulnerable to textual disturbances, while ToW is robust to them. We also uncover a negative correlation between input length and content-related scores in the Guide task, showcasing that it cannot be simply improved by input-side information piling.

---


### 56. [OLLM: Options-based Large Language Models](https://arxiv.org/abs/2604.19087)

**<font color=#1a73e8>作者：</font>** Shashank Sharma, Janina Hoffmann, Vinay Namboodiri  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We introduce Options LLM (OLLM), a simple, general method that replaces the single next-token prediction of standard LLMs with a \textit{set of learned options} for the next token, indexed by a discrete latent variable. Instead of relying on temperature or sampling heuristics to induce diversity, OLLM models variation explicitly: a small latent space parametrizes multiple plausible next-token options which can be selected or searched by a downstream policy. Architecturally, OLLM is a lightweight "plug-in" that inserts two layers: an encoder and a decoder, before the output head, allowing almost any pretrained LLM to be converted with minimal additional parameters. We apply OLLM to a 1.7B-parameter backbone (only $1.56\%$ of parameters trainable) trained on OpenMathReasoning and evaluated on OmniMath. The SOTA LoRA-adapted baselines peak at $51\%$ final answer correctness, while OLLM's option set allows up to $\sim 70\%$ under optimal latent selection. We then train a compact policy in the latent space that emits latents to control generation. Operating in a low-dimensional option space makes reward optimization far more sample-efficient and substantially reduces common misalignments (e.g., language switching or degenerate reasoning), as the policy is constrained to options learned during SFT. Crucially, this alignment arises from model structure rather than additional KL or handcrafted alignment losses. Our results demonstrate that optionized next-token modeling enhances controllability, robustness, and efficiency in math reasoning, and highlight latent-space policy learning as a promising direction for reinforcement learning in LLMs.

---


### 57. [Revisiting Framing Codebooks with AI: Employing Large Language Models as Analytical Collaborators in Deductive Content Analysis](https://arxiv.org/abs/2604.19111)

**<font color=#1a73e8>作者：</font>** Diego Gomez-Zara, Hernán Valdivieso, Jorge Pérez 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Codebooks are central to framing research, providing theoretically grounded criteria for analyzing news content. While traditionally codebooks are built from theoretical frameworks and researchers' knowledge, applying these codebooks to large news corpora often exposes ambiguities, borderline cases, and underspecified rules that are difficult to resolve through theory alone. Moreover, news corpora evolve over time and differ across cultures, necessitating that researchers revisit the theoretical frameworks underlying these codebooks. In this article, we propose a workflow that uses Large Language Models (LLMs) to augment the creation and refinement of framing codebooks by combining theoretical frameworks with data-driven exploration. Rather than treating LLMs as automated classifiers, this approach positions them as analytic collaborators that help externalize decision rules, surface latent dimensions, and support iterative revisions of codebooks through dialogues between researchers and their data. We illustrate this workflow using a dataset of Latin American news coverage, demonstrating how the application of LLMs' capabilities has led to the surfacing of latent patterns, the generation of frame distinctions, and the adaptation of frameworks to new contexts. This method provides an LLM-assisted strategy that supports methodology creativity while preserving researchers' interpretative authority.

---


### 58. [LLMs Know They're Wrong and Agree Anyway: The Shared Sycophancy-Lying Circuit](https://arxiv.org/abs/2604.19117)

**<font color=#1a73e8>作者：</font>** Manav Pandey  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> When a language model agrees with a user's false belief, is it failing to detect the error, or noticing and agreeing anyway? We show the latter. Across twelve open-weight models from five labs, spanning small to frontier scale, the same small set of attention heads carries a "this statement is wrong" signal whether the model is evaluating a claim on its own or being pressured to agree with a user. Silencing these heads flips sycophantic behavior sharply while leaving factual accuracy intact, so the circuit controls deference rather than knowledge. Edge-level path patching confirms that the same head-to-head connections drive sycophancy, factual lying, and instructed lying. Opinion-agreement, where no factual ground truth exists, reuses these head positions but writes into an orthogonal direction, ruling out a simple "truth-direction" reading of the substrate. Alignment training leaves this circuit in place: an RLHF refresh cuts sycophantic behavior roughly tenfold while the shared heads persist or grow, a pattern that replicates on an independent model family and under targeted anti-sycophancy DPO. When these models sycophant, they register that the user is wrong and agree anyway.

---


### 59. [Detoxification for LLM: From Dataset Itself](https://arxiv.org/abs/2604.19124)

**<font color=#1a73e8>作者：</font>** Wei Shao, Yihang Wang, Gaoyu Zhu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Existing detoxification methods for large language models mainly focus on post-training stage or inference time, while few tackle the source of toxicity, namely, the dataset itself. Such training-based or controllable decoding approaches cannot completely suppress the model's inherent toxicity, whereas detoxifying the pretraining dataset can fundamentally reduce the toxicity that the model learns during training. Hence, we attempt to detoxify directly on raw corpora with SoCD (Soft Contrastive Decoding), which guides an LLM to localize and rewrite toxic spans in raw data while preserving semantics, in our proposed HSPD (Hierarchical Semantic-Preserving Detoxification) pipeline, yielding a detoxified corpus that can drop-in replace the original for fine-tuning or other training. On GPT2-XL, HSPD attains state-of-the-art detoxification, reducing Toxicity Probability (TP) from 0.42 to 0.18 and Expected Maximum Toxicity (EMT) from 0.43 to 0.20. We further validate consistent best-in-class results on LLaMA2-7B, OPT-6.7B, and Falcon-7B. These findings show that semantics-preserving, corpus-level rewriting with HSPD effectively suppresses downstream toxicity while retaining data utility and allowing seamless source-level mitigation, thereby reducing the cost of later model behavior adjustment. (Code is available at: this https URL)

---


### 60. [Do Emotions Influence Moral Judgment in Large Language Models?](https://arxiv.org/abs/2604.19125)

**<font color=#1a73e8>作者：</font>** Mohammad Saim, Tianyu Jiang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models have been extensively studied for emotion recognition and moral reasoning as distinct capabilities, yet the extent to which emotions influence moral judgment remains underexplored. In this work, we develop an emotion-induction pipeline that infuses emotion into moral situations and evaluate shifts in moral acceptability across multiple datasets and LLMs. We observe a directional pattern: positive emotions increase moral acceptability and negative emotions decrease it, with effects strong enough to reverse binary moral judgments in up to 20% of cases, and with susceptibility scaling inversely with model capability. Our analysis further reveals that specific emotions can sometimes behave contrary to what their valence would predict (e.g., remorse paradoxically increases acceptability). A complementary human annotation study shows humans do not exhibit these systematic shifts, indicating an alignment gap in current LLMs.

---


### 61. [Diff-SBSR: Learning Multimodal Feature-Enhanced Diffusion Models for Zero-Shot Sketch-Based 3D Shape Retrieval](https://arxiv.org/abs/2604.19135)

**<font color=#1a73e8>作者：</font>** Hang Cheng, Fanhe Dong, Long Zeng  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper presents the first exploration of text-to-image diffusion models for zero-shot sketch-based 3D shape retrieval (ZS-SBSR). Existing sketch-based 3D shape retrieval methods struggle in zero-shot settings due to the absence of category supervision and the extreme sparsity of sketch inputs. Our key insight is that large-scale pretrained diffusion models inherently exhibit open-vocabulary capability and strong shape bias, making them well suited for zero-shot visual retrieval. We leverage a frozen Stable Diffusion backbone to extract and aggregate discriminative representations from intermediate U-Net layers for both sketches and rendered 3D views. Diffusion models struggle with sketches due to their extreme abstraction and sparsity, compounded by a significant domain gap from natural images. To address this limitation without costly retraining, we introduce a multimodal feature-enhanced strategy that conditions the frozen diffusion backbone with complementary visual and textual cues from CLIP, explicitly enhancing the ability of semantic context capture and concentrating on sketch contours. Specifically, we inject global and local visual features derived from a pretrained CLIP visual encoder, and incorporate enriched textual guidance by combining learnable soft prompts with hard textual descriptions generated by BLIP. Furthermore, we employ the Circle-T loss to dynamically strengthen positive-pair attraction once negative samples are sufficiently separated, thereby adapting to sketch noise and enabling more effective sketch-3D alignment. Extensive experiments on two public benchmarks demonstrate that our method consistently outperforms state-of-the-art approaches in ZS-SBSR.

---


### 62. [Construction of Knowledge Graph based on Language Model](https://arxiv.org/abs/2604.19137)

**<font color=#1a73e8>作者：</font>** Qiubai Zhu, Qingwang Wang, Haibin Yuan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Knowledge Graph (KG) can effectively integrate valuable information from massive data, and thus has been rapidly developed and widely used in many fields. Traditional KG construction methods rely on manual annotation, which often consumes a lot of time and manpower. And KG construction schemes based on deep learning tend to have weak generalization capabilities. With the rapid development of Pre-trained Language Models (PLM), PLM has shown great potential in the field of KG construction. This paper provides a comprehensive review of recent research advances in the field of construction of KGs using PLM. In this paper, we explain how PLM can utilize its language understanding and generation capabilities to automatically extract key information for KGs, such as entities and relations, from textual data. In addition, We also propose a new Hyper-Relarional Knowledge Graph construction framework based on lightweight Large Language Model (LLM) named LLHKG and compares it with previous methods. Under our framework, the KG construction capability of lightweight LLM is comparable to GPT3.5.

---


### 63. [The Rise of Verbal Tics in Large Language Models: A Systematic Analysis Across Frontier Models](https://arxiv.org/abs/2604.19139)

**<font color=#1a73e8>作者：</font>** Shuai Wu, Xue Li, Yanna Feng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As Large Language Models (LLMs) continue to evolve through alignment techniques such as Reinforcement Learning from Human Feedback (RLHF) and Constitutional AI, a growing and increasingly conspicuous phenomenon has emerged: the proliferation of verbal tics -- repetitive, formulaic linguistic patterns that pervade model outputs. These range from sycophantic openers ("That's a great question!", "Awesome!") to pseudo-empathetic affirmations ("I completely understand your concern", "I'm right here to catch you") and overused vocabulary ("delve", "tapestry", "nuanced"). In this paper, we present a systematic analysis of the verbal tic phenomenon across eight state-of-the-art LLMs: GPT-5.4, Claude Opus 4.7, Gemini 3.1 Pro, Grok 4.2, Doubao-Seed-2.0-pro, Kimi K2.5, DeepSeek V3.2, and MiMo-V2-Pro. Utilizing a custom evaluation framework for standardized API-based evaluation, we assess 10,000 prompts across 10 task categories in both English and Chinese, yielding 160,000 model responses. We introduce the Verbal Tic Index (VTI), a composite metric quantifying tic prevalence, and analyze its correlation with sycophancy, lexical diversity, and human-perceived naturalness. Our findings reveal significant inter-model variation: Gemini 3.1 Pro exhibits the highest VTI (0.590), while DeepSeek V3.2 achieves the lowest (0.295). We further demonstrate that verbal tics accumulate over multi-turn conversations, are amplified in subjective tasks, and show distinct cross-lingual patterns. Human evaluation (N = 120) confirms a strong inverse relationship between sycophancy and perceived naturalness (r = -0.87, p < 0.001). These results underscore the "alignment tax" of current training paradigms and highlight the urgent need for more authentic human-AI interaction frameworks.

---


### 64. [ST-Prune: Training-Free Spatio-Temporal Token Pruning for Vision-Language Models in Autonomous Driving](https://arxiv.org/abs/2604.19145)

**<font color=#1a73e8>作者：</font>** Lin Sha, Haiyun Guo, Tao Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) have become central to autonomous driving systems, yet their deployment is severely bottlenecked by the massive computational overhead of multi-view camera and multi-frame video input. Existing token pruning methods, primarily designed for single-image inputs, treat each frame or view in isolation and thus fail to exploit the inherent spatio-temporal redundancies in driving scenarios. To bridge this gap, we propose ST-Prune, a training-free, plug-and-play framework comprising two complementary modules: Motion-aware Temporal Pruning (MTP) and Ring-view Spatial Pruning (RSP). MTP addresses temporal redundancy by encoding motion volatility and temporal recency as soft constraints within the diversity selection objective, prioritizing dynamic trajectories and current-frame content over static historical background. RSP further resolves spatial redundancy by exploiting the ring-view camera geometry to penalize bilateral cross-view similarity, eliminating duplicate projections and residual background that temporal pruning alone cannot suppress. These two modules together constitute a complete spatio-temporal pruning process, preserving key scene information under strict compression. Validated across four benchmarks spanning perception, prediction, and planning, ST-Prune establishes new state-of-the-art for training-free token pruning. Notably, even at 90\% token reduction, ST-Prune achieves near-lossless performance with certain metrics surpassing the full-model baseline, while maintaining inference speeds comparable to existing pruning approaches.

---


### 65. [How Do Answer Tokens Read Reasoning Traces? Self-Reading Patterns in Thinking LLMs for Quantitative Reasoning](https://arxiv.org/abs/2604.19149)

**<font color=#1a73e8>作者：</font>** Haoyang Chen, Yi Liu, Jianzhi Shao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Thinking LLMs produce reasoning traces before answering. Prior activation steering work mainly targets on shaping these traces. It remains less understood how answer tokens actually read and integrate the reasoning to produce reliable outcomes. Focusing on quantitative reasoning, we analyze the answer-to-reasoning attention and observe a benign self-reading pattern aligned with correctness, characterized by a forward drift of the reading focus along the reasoning trace and a persistent concentration on key semantic anchors, whereas incorrect solutions exhibit diffuse and irregular attention pattern. We interpret this as internal certainty during answer decoding, where the model commits to a viable solution branch and integrates key evidence. Following this, we propose a training-free steering method driven by Self-Reading Quality (SRQ) scores combining geometric metrics for process control with semantic metrics for content monitoring. SRQ selects data to build steering vectors that guide inference toward benign self-reading and away from uncertain and disorganized reading. Experiments show that our method yields consistent accuracy gains.

---


### 66. [SAW-INT4: System-Aware 4-Bit KV-Cache Quantization for Real-World LLM Serving](https://arxiv.org/abs/2604.19157)

**<font color=#1a73e8>作者：</font>** Jinda Jia, Jisen Li, Zhongzhu Zhou 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> KV-cache memory is a major bottleneck in real-world LLM serving, where systems must simultaneously support latency-sensitive small-batch requests and high-throughput concurrent workloads. Although many KV-cache compression methods improve offline accuracy or compression ratio, they often violate practical serving constraints such as paged memory layouts, regular memory access, and fused attention execution, limiting their effectiveness in deployment.
In this work, we identify the minimal set of 4-bit KV-cache quantization methods that remain viable under these constraints. Our central finding is that a simple design--token-wise INT4 quantization with block-diagonal Hadamard rotation--consistently achieves the best accuracy-efficiency trade-off. Across multiple models and benchmarks, this approach recovers nearly all of the accuracy lost by naive INT4, while more complex methods such as vector quantization and Hessian-aware quantization provide only marginal additional gains once serving compatibility is taken into account.
To make this practical, we implement a fused rotation-quantization kernel that integrates directly into paged KV-cache layouts and introduces zero measurable end-to-end overhead, matching plain INT4 throughput across concurrency levels. Our results show that effective KV-cache compression is fundamentally a systems co-design problem: under real serving constraints, lightweight block-diagonal Hadamard rotation is a viable method that delivers near-lossless accuracy without sacrificing serving efficiency.

---


### 67. [Mind the Unseen Mass: Unmasking LLM Hallucinations via Soft-Hybrid Alphabet Estimation](https://arxiv.org/abs/2604.19162)

**<font color=#1a73e8>作者：</font>** Hongxing Pan, Yingying Guo, Wenqing Kuang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper studies uncertainty quantification for large language models (LLMs) under black-box access, where only a small number of responses can be sampled for each query. In this setting, estimating the effective semantic alphabet size--that is, the number of distinct meanings expressed in the sampled responses--provides a useful proxy for downstream risk. However, frequency-based estimators tend to undercount rare semantic modes when the sample size is small, while graph-spectral quantities alone are not designed to estimate semantic occupancy accurately. To address this issue, we propose SHADE (Soft-Hybrid Alphabet Dynamic Estimator), a simple and interpretable estimator that combines Generalized Good-Turing coverage with a heat-kernel trace of the normalized Laplacian constructed from an entailment-weighted graph over sampled responses. The estimated coverage adaptively determines the fusion rule: under high coverage, SHADE uses a convex combination of the two signals, while under low coverage it applies a LogSumExp fusion to emphasize missing or weakly observed semantic modes. A finite-sample correction is then introduced to stabilize the resulting cardinality estimate before converting it into a coverage-adjusted semantic entropy score. Experiments on pooled semantic alphabet-size estimation against large-sample references and on QA incorrectness detection show that SHADE achieves the strongest improvements in the most sample-limited regime, while the performance gap narrows as the number of samples increases. These results suggest that hybrid semantic occupancy estimation is particularly beneficial when black-box uncertainty quantification must operate under tight sampling budgets.

---


### 68. [LBLLM: Lightweight Binarization of Large Language Models via Three-Stage Distillation](https://arxiv.org/abs/2604.19167)

**<font color=#1a73e8>作者：</font>** Siqing Song, Chuang Wang, Yong Lang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deploying large language models (LLMs) in resource-constrained environments is hindered by heavy computational and memory requirements. We present LBLLM, a lightweight binarization framework that achieves effective W(1+1)A4 quantization through a novel three-stage quantization strategy. The framework proceeds as follows: (1) initialize a high-quality quantized model via PTQ; (2) quantize binarized weights, group-wise bitmaps, and quantization parameters through layer-wise distillation while keeping activations in full precision; and (3) training learnable activation quantization factors to dynamically quantize activations to 4 bits. This decoupled design mitigates interference between weight and activation quantization, yielding greater training stability and better inference accuracy. LBLLM, trained only using 0.016B tokens with a single GPU, surpasses existing state-of-the-art binarization methods on W2A4 quantization settings across tasks of language modeling, commonsense QA, and language understanding. These results demonstrate that extreme low-bit quantization of LLMs can be both practical and highly effective without introducing any extra high-precision channels or rotational matrices commonly used in recent PTQ-based works, offering a promising path toward efficient LLM deployment in resource-limited situations.

---


### 69. [Reasoning-Aware AIGC Detection via Alignment and Reinforcement](https://arxiv.org/abs/2604.19172)

**<font color=#1a73e8>作者：</font>** Zhao Wang, Max Xiong, Jianxun Lian 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The rapid advancement and widespread adoption of Large Language Models (LLMs) have elevated the need for reliable AI-generated content (AIGC) detection, which remains challenging as models evolve. We introduce AIGC-text-bank, a comprehensive multi-domain dataset with diverse LLM sources and authorship scenarios, and propose REVEAL, a detection framework that generates interpretable reasoning chains before classification. Our approach uses a two-stage training strategy: supervised fine-tuning to establish reasoning capabilities, followed by reinforcement learning to improve accuracy, improve logical consistency, and reduce hallucinations. Extensive experiments show that REVEAL achieves state-of-the-art performance across multiple benchmarks, offering a robust and transparent solution for AIGC detection. The project is open-source at this https URL

---


### 70. [SCURank: Ranking Multiple Candidate Summaries with Summary Content Units for Enhanced Summarization](https://arxiv.org/abs/2604.19185)

**<font color=#1a73e8>作者：</font>** Bo-Jyun Wang, Ying-Jia Lin, Hung-Yu Kao  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Small language models (SLMs), such as BART, can achieve summarization performance comparable to large language models (LLMs) via distillation. However, existing LLM-based ranking strategies for summary candidates suffer from instability, while classical metrics (e.g., ROUGE) are insufficient to rank high-quality summaries. To address these issues, we introduce \textbf{SCURank}, a framework that enhances summarization by leveraging \textbf{Summary Content Units (SCUs)}. Instead of relying on unstable comparisons or surface-level overlap, SCURank evaluates summaries based on the richness and semantic importance of information content. We investigate the effectiveness of SCURank in distilling summaries from multiple diverse LLMs. Experimental results demonstrate that SCURank outperforms traditional metrics and LLM-based ranking methods across evaluation measures and datasets. Furthermore, our findings show that incorporating diverse LLM summaries enhances model abstractiveness and overall distilled model performance, validating the benefits of information-centric ranking in multi-LLM distillation. The code for SCURank is available at this https URL.

---


### 71. [How Far Are Video Models from True Multimodal Reasoning?](https://arxiv.org/abs/2604.19193)

**<font color=#1a73e8>作者：</font>** Xiaotian Zhang, Jianhui Wei, Yuan Wang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite remarkable progress toward general-purpose video models, a critical question remains unanswered: how far are these models from achieving true multimodal reasoning? Existing benchmarks fail to address this question rigorously, as they remain constrained by straightforward task designs and fragmented evaluation metrics that neglect complex multimodal reasoning. To bridge this gap, we introduce CLVG-Bench, an evaluation framework designed to probe video models' zero-shot reasoning capabilities via Context Learning in Video Generation. CLVG-Bench comprises more than 1,000 high-quality, manually annotated metadata across 6 categories and 47 subcategories, covering complex scenarios including physical simulation, logical reasoning, and interactive contexts. To enable rigorous and scalable assessment, we further propose an Adaptive Video Evaluator (AVE) that aligns with human expert perception using minimal annotations, delivering interpretable textual feedback across diverse video context tasks. Extensive experiments reveal a striking answer to our central question: while state-of-the-art (SOTA) video models, such as Seedance 2.0, demonstrate competence on certain understanding and reasoning subtasks, they fall substantially short with logically grounded and interactive generation tasks (achieving success rates <25% and ~0%, respectively), exposing multimodal reasoning and physical grounding as critical bottlenecks. By systematically quantifying these limitations, the proposed method provides actionable feedbacks and a clear roadmap toward truly robust, general-purpose video models. CLVG-Bench and code are released here.

---


### 72. [Benchmarking Vision Foundation Models for Domain-Generalizable Face Anti-Spoofing](https://arxiv.org/abs/2604.19196)

**<font color=#1a73e8>作者：</font>** Mika Feng, Pierre Gallin-Martel, Koichi Ito 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Face Anti-Spoofing (FAS) remains challenging due to the requirement for robust domain generalization across unseen environments. While recent trends leverage Vision-Language Models (VLMs) for semantic supervision, these multimodal approaches often demand prohibitive computational resources and exhibit high inference latency. Furthermore, their efficacy is inherently limited by the quality of the underlying visual features. This paper revisits the potential of vision-only foundation models to establish a highly efficient and robust baseline for FAS. We conduct a systematic benchmarking of 15 pre-trained models, such as supervised CNNs, supervised ViTs, and self-supervised ViTs, under severe cross-domain scenarios including the MICO and Limited Source Domains (LSD) protocols. Our comprehensive analysis reveals that self-supervised vision models, particularly DINOv2 with Registers, significantly suppress attention artifacts and capture critical, fine-grained spoofing cues. Combined with Face Anti-Spoofing Data Augmentation (FAS-Aug), Patch-wise Data Augmentation (PDA) and Attention-weighted Patch Loss (APL), our proposed vision-only baseline achieves state-of-the-art performance in the MICO protocol. This baseline outperforms existing methods under the data-constrained LSD protocol while maintaining superior computational efficiency. This work provides a definitive vision-only baseline for FAS, demonstrating that optimized self-supervised vision transformers can serve as a backbone for both vision-only and future multimodal FAS systems. The project page is available at: this https URL .

---


### 73. [UAF: A Unified Audio Front-end LLM for Full-Duplex Speech Interaction](https://arxiv.org/abs/2604.19221)

**<font color=#1a73e8>作者：</font>** Yadong Li, Guoxin Wu, Haiping Hou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Full-duplex speech interaction, as the most natural and intuitive mode of human communication, is driving artificial intelligence toward more human-like conversational systems. Traditional cascaded speech processing pipelines suffer from critical limitations, including accumulated latency, information loss, and error propagation across modules. To address these issues, recent efforts focus on the end-to-end audio large language models (LLMs) like GPT-4o, which primarily unify speech understanding and generation task. However, most of these models are inherently half-duplex, and rely on a suite of separate, task-specific front-end components, such as voice activity detection (VAD) and turn-taking detection (TD). In our development of speech assistant, we observed that optimizing the speech front-end is equally crucial as advancing the back-end unified model for achieving seamless, responsive interactions. To bridge this gap, we propose the first unified audio front-end LLM (UAF) tailored for full-duplex speech systems. Our model reformulates diverse audio front-end tasks into a single auto-regressive sequence prediction problem, including VAD, TD, speaker recognition (SR), automatic speech recognition (ASR) and question answer (QA). It takes streaming fixed-duration audio chunk (e.g., 600 ms) as input, leverages a reference audio prompt to anchor the target speaker at the beginning, and regressively generates discrete tokens encoding both semantic content and system-level state controls (e.g., interruption signals). Experiments demonstrate that our model achieves leading performance across multiple audio front-end tasks and significantly enhances response latency and interruption accuracy in real-world interaction scenarios.

---


### 74. [Talking to a Know-It-All GPT or a Second-Guesser Claude? How Repair reveals unreliable Multi-Turn Behavior in LLMs](https://arxiv.org/abs/2604.19245)

**<font color=#1a73e8>作者：</font>** Clara Lachenmaier, Hannah Bultmann, Sina Zarrieß  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Repair, an important resource for resolving trouble in human-human conversation, remains underexplored in human-LLM interaction. In this study, we investigate how LLMs engage in the interactive process of repair in multi-turn dialogues around solvable and unsolvable math questions. We examine whether models initiate repair themselves and how they respond to user-initiated repair. Our results show strong differences across models: reactions range from being almost completely resistant to (appropriate) repair attempts to being highly susceptible and easily manipulated. We further demonstrate that once conversations extend beyond a single turn, model behavior becomes more distinctive and less predictable across systems. Overall, our findings indicate that each tested LLM exhibits its own characteristic form of unreliability in the context of repair.

---


### 75. [ShadowPEFT: Shadow Network for Parameter-Efficient Fine-Tuning](https://arxiv.org/abs/2604.19254)

**<font color=#1a73e8>作者：</font>** Xianming Li, Zongxi Li, Tsz-fung Andrew Lee 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Parameter-efficient fine-tuning (PEFT) reduces the training cost of full-parameter fine-tuning for large language models (LLMs) by training only a small set of task-specific parameters while freezing the pretrained backbone. However, existing approaches, such as Low-Rank Adaptation (LoRA), achieve adaptation by inserting independent low-rank perturbations directly to individual weights, resulting in a local parameterization of adaptation. We propose ShadowPEFT, a centralized PEFT framework that instead performs layer-level refinement through a depth-shared shadow module. At each transformer layer, ShadowPEFT maintains a parallel shadow state and evolves it repeatedly for progressively richer hidden states. This design shifts adaptation from distributed weight-space perturbations to a shared layer-space refinement process. Since the shadow module is decoupled from the backbone, it can be reused across depth, independently pretrained, and optionally deployed in a detached mode, benefiting edge computing scenarios. Experiments on generation and understanding benchmarks show that ShadowPEFT matches or outperforms LoRA and DoRA under comparable trainable-parameter budgets. Additional analyses on shadow pretraining, cross-dataset transfer, parameter scaling, inference latency, and system-level evaluation suggest that centralized layer-space adaptation is a competitive and flexible alternative to conventional low-rank PEFT.

---


### 76. [CulturALL: Benchmarking Multilingual and Multicultural Competence of LLMs on Grounded Tasks](https://arxiv.org/abs/2604.19262)

**<font color=#1a73e8>作者：</font>** Peiqin Lin, Chenyang Lyu, Wenjiang Luo 等 25 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are now deployed worldwide, inspiring a surge of benchmarks that measure their multilingual and multicultural abilities. However, these benchmarks prioritize generic language understanding or superficial cultural trivia, leaving the evaluation of grounded tasks -- where models must reason within real-world, context-rich scenarios -- largely unaddressed. To fill this gap, we present CulturALL, a comprehensive and challenging benchmark to assess LLMs' multilingual and multicultural competence on grounded tasks. CulturALL is built via a human--AI collaborative framework: expert annotators ensure appropriate difficulty and factual accuracy, while LLMs lighten the manual workload. By incorporating diverse sources, CulturALL ensures comprehensive scenario coverage. Each item is carefully designed to present a high level of difficulty, making CulturALL challenging. CulturALL contains 2,610 samples in 14 languages from 51 regions, distributed across 16 topics to capture the full breadth of grounded tasks. Experiments show that the best LLM achieves 44.48% accuracy on CulturALL, underscoring substantial room for improvement.

---


### 77. [DR-MMSearchAgent: Deepening Reasoning in Multimodal Search Agents](https://arxiv.org/abs/2604.19264)

**<font color=#1a73e8>作者：</font>** Shengqin Wang, Wentao Yan, Huichi Zhou 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Agentic multimodal models have garnered significant attention for their ability to leverage external tools to tackle complex tasks. However, it is observed that such agents often meet premature interaction collapse, caused by two primary reasons: 1) the terminal reward often appending on the last token prevents the advantage from distinguishing trajectories with exploratory behavior; 2) excessively redundant context hinders the agent from absorbing useful feedback. To address these issues, we propose the Deepening Reasoning MMSearchAgent, the framework leverages the structural proximity to derive advantage signals from the whole rollout trajectories in an entire batch, such that trajectories of different lengths are further encouraged to be generated, even when containing the same correct answer. Additionally, differentiated gaussian rewards are employed to dynamically calibrate interaction tolerance, thereby ensuring information reliability and reduce redundancy. To support multi-turn interaction training, we have constructed a multi-step deep-reasoning dataset including 3602 high-quality QA pair with at least 3 reasonning steps. Extensive experiments demonstrate that our method achieves state-of-the-art performance, outperforming the MMSearch-R1 by 8.4$\%$ on FVQA-test.

---


### 78. [HarDBench: A Benchmark for Draft-Based Co-Authoring Jailbreak Attacks for Safe Human-LLM Collaborative Writing](https://arxiv.org/abs/2604.19274)

**<font color=#1a73e8>作者：</font>** Euntae Kim, Soomin Han, Buru Chang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used as co-authors in collaborative writing, where users begin with rough drafts and rely on LLMs to complete, revise, and refine their content. However, this capability poses a serious safety risk: malicious users could jailbreak the models-filling incomplete drafts with dangerous content-to force them into generating harmful outputs. In this paper, we identify the vulnerability of current LLMs to such draft-based co-authoring jailbreak attacks and introduce HarDBench, a systematic benchmark designed to evaluate the robustness of LLMs against this emerging threat. HarDBench spans a range of high-risk domains-including Explosives, Drugs, Weapons, and Cyberattacks-and features prompts with realistic structure and domain-specific cues to assess the model susceptibility to harmful completions. To mitigate this risk, we introduce a safety-utility balanced alignment approach based on preference optimization, training models to refuse harmful completions while remaining helpful on benign drafts. Experimental results show that existing LLMs are highly vulnerable in co-authoring contexts and our alignment method significantly reduces harmful outputs without degrading performance on co-authoring capabilities. This presents a new paradigm for evaluating and aligning LLMs in human-LLM collaborative writing settings. Our new benchmark and dataset are available on our project page at this https URL

---


### 79. [Beyond Semantic Similarity: A Component-Wise Evaluation Framework for Medical Question Answering Systems with Health Equity Implications](https://arxiv.org/abs/2604.19281)

**<font color=#1a73e8>作者：</font>** Abu Noman Md Sakib, Md. Main Oddin Chisty, Zijie Zhang  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The use of Large Language Models (LLMs) to support patients in addressing medical questions is becoming increasingly prevalent. However, most of the measures currently used to evaluate the performance of these models in this context only measure how closely a model's answers match semantically, and therefore do not provide a true indication of the model's medical accuracy or of the health equity risks associated with it. To address these shortcomings, we present a new evaluation framework for medical question answering called VB-Score (Verification-Based Score) that provides a separate evaluation of the four components of entity recognition, semantic similarity, factual consistency, and structured information completeness for medical question-answering models. We perform rigorous reviews of the performance of three well-known and widely used LLMs on 48 public health-related topics taken from high-quality, authoritative information sources. Based on our analyses, we discover a major discrepancy between the models' semantic and entity accuracy. Our assessments of the performance of all three models show that each of them has almost uniformly severe performance failures when evaluated against our criteria. Our findings indicate alarming performance disparities across various public health topics, with most of the models exhibiting 13.8% lower performance (compared to an overall average) for all the public health topics that relate to chronic conditions that occur in older and minority populations, which indicates the existence of what's known as condition-based algorithmic discrimination. Our findings also demonstrate that prompt engineering alone does not compensate for basic architectural limitations on how these models perform in extracting medical entities and raise the question of whether semantic evaluation alone is a sufficient measure of medical AI safety.

---


### 80. [Location Not Found: Exposing Implicit Local and Global Biases in Multilingual LLMs](https://arxiv.org/abs/2604.19292)

**<font color=#1a73e8>作者：</font>** Guy Mor-Lan, Omer Goldman, Matan Eyal 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multilingual large language models (LLMs) have minimized the fluency gap between languages. This advancement, however, exposes models to the risk of biased behavior, as knowledge and norms may propagate across languages. In this work, we aim to quantify models' inter- and intra-lingual biases, via their ability to answer locale-ambiguous questions. To this end, we present LocQA, a test set containing 2,156 questions in 12 languages, referring to various locale-dependent facts such as laws, dates, and measurements. The questions do not contain indications of the locales they relate to, other than the querying language itself. LLMs' responses to LocQA locale-ambiguous questions thus reveal models' implicit priors. We used LocQA to evaluate 32 models, and detected two types of structural biases. Inter-lingually, we show a global bias towards answers relevant to the US-locale, even when models are asked in languages other than English. Moreover, we discovered that this global bias is exacerbated in models that underwent instruction tuning, compared to their base counterparts. Intra-lingually, we show that when multiple locales are relevant for the same language, models act as demographic probability engines, prioritizing locales with larger populations. Taken together, insights from LocQA may help in shaping LLMs' desired local behavior, and in quantifying the impact of various training phases on different kinds of biases.

---


### 81. [TEMPO: Scaling Test-time Training for Large Reasoning Models](https://arxiv.org/abs/2604.19295)

**<font color=#1a73e8>作者：</font>** Qingyang Zhang, Xinke Kong, Haitao Wu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Test-time training (TTT) adapts model parameters on unlabeled test instances during inference time, which continuously extends capabilities beyond the reach of offline training. Despite initial gains, existing TTT methods for LRMs plateau quickly and do not benefit from additional test-time compute. Without external calibration, the self-generated reward signal increasingly drifts as the policy model evolves, leading to both performance plateaus and diversity collapse. We propose TEMPO, a TTT framework that interleaves policy refinement on unlabeled questions with periodic critic recalibration on a labeled dataset. By formalizing this alternating procedure through the Expectation-Maximization (EM) algorithm, we reveal that prior methods can be interpreted as incomplete variants that omit the crucial recalibration step. Reintroducing this step tightens the evidence lower bound (ELBO) and enables sustained improvement. Across diverse model families (Qwen3 and OLMO3) and reasoning tasks, TEMPO improves OLMO3-7B on AIME 2024 from 33.0% to 51.1% and Qwen3-14B from 42.3% to 65.8%, while maintaining high diversity.

---


### 82. [IndiaFinBench: An Evaluation Benchmark for Large Language Model Performance on Indian Financial Regulatory Text](https://arxiv.org/abs/2604.19298)

**<font color=#1a73e8>作者：</font>** Rajveer Singh Pall  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We introduce IndiaFinBench, to our knowledge the first publicly available evaluation benchmark for assessing large language model (LLM) performance on Indian financial regulatory text. Existing financial NLP benchmarks draw exclusively from Western financial corpora (SEC filings, US earnings reports, and English-language financial news), leaving a significant gap in coverage of non-Western regulatory frameworks. IndiaFinBench addresses this gap with 406 expert-annotated question-answer pairs drawn from 192 documents sourced from the Securities and Exchange Board of India (SEBI) and the Reserve Bank of India (RBI), spanning four task types: regulatory interpretation (174 items), numerical reasoning (92 items), contradiction detection (62 items), and temporal reasoning (78 items). Annotation quality is validated through a model-based secondary pass (kappa=0.918 on contradiction detection) and a 60-item human inter-annotator agreement evaluation (kappa=0.611; 76.7% overall agreement). We evaluate twelve models under zero-shot conditions, with accuracy ranging from 70.4% (Gemma 4 E4B) to 89.7% (Gemini 2.5 Flash). All models substantially outperform a non-specialist human baseline of 60.0%. Numerical reasoning is the most discriminative task, with a 35.9 percentage-point spread across models. Bootstrap significance testing (10,000 resamples) reveals three statistically distinct performance tiers. The dataset, evaluation code, and all model outputs are available at this https URL

---


### 83. [Rethinking Scale: Deployment Trade-offs of Small Language Models under Agent Paradigms](https://arxiv.org/abs/2604.19299)

**<font color=#1a73e8>作者：</font>** Xinlin Wang, Mats Brorsson  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Despite the impressive capabilities of large language models, their substantial computational costs, latency, and privacy risks hinder their widespread deployment in real-world applications. Small Language Models (SLMs) with fewer than 10 billion parameters present a promising alternative; however, their inherent limitations in knowledge and reasoning curtail their effectiveness. Existing research primarily focuses on enhancing SLMs through scaling laws or fine-tuning strategies while overlooking the potential of using agent paradigms, such as tool use and multi-agent collaboration, to systematically compensate for the inherent weaknesses of small models. To address this gap, this paper presents the first large-scale, comprehensive study of <10B open-source models under three paradigms: (1) the base model, (2) a single agent equipped with tools, and (3) a multi-agent system with collaborative capabilities. Our results show that single-agent systems achieve the best balance between performance and cost, while multi-agent setups add overhead with limited gains. Our findings highlight the importance of agent-centric design for efficient and trustworthy deployment in resource-constrained settings.

---


### 84. [Large Language Models Exhibit Normative Conformity](https://arxiv.org/abs/2604.19301)

**<font color=#1a73e8>作者：</font>** Mikako Bito, Keita Nishimoto, Kimitaka Asatani 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The conformity bias exhibited by large language models (LLMs) can pose a significant challenge to decision-making in LLM-based multi-agent systems (LLM-MAS). While many prior studies have treated "conformity" simply as a matter of opinion change, this study introduces the social psychological distinction between informational conformity and normative conformity in order to understand LLM conformity at the mechanism level. Specifically, we design new tasks to distinguish between informational conformity, in which participants in a discussion are motivated to make accurate judgments, and normative conformity, in which participants are motivated to avoid conflict or gain acceptance within a group. We then conduct experiments based on these task settings. The experimental results show that, among the six LLMs evaluated, up to five exhibited tendencies toward not only informational conformity but also normative conformity. Furthermore, intriguingly, we demonstrate that by manipulating subtle aspects of the social context, it may be possible to control the target toward which a particular LLM directs its normative conformity. These findings suggest that decision-making in LLM-MAS may be vulnerable to manipulation by a small number of malicious users. In addition, through analysis of internal vectors associated with informational and normative conformity, we suggest that although both behaviors appear externally as the same form of "conformity," they may in fact be driven by distinct internal mechanisms. Taken together, these results may serve as an initial milestone toward understanding how "norms" are implemented in LLMs and how they influence group dynamics.

---


### 85. [RDP LoRA: Geometry-Driven Identification for Parameter-Efficient Adaptation in Large Language Models](https://arxiv.org/abs/2604.19321)

**<font color=#1a73e8>作者：</font>** Yusuf Çelebi, Yağız Asker, Özay Ezerceli 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fine-tuning Large Language Models (LLMs) remains structurally uncertain despite parameter-efficient methods such as Low-Rank Adaptation (LoRA), as the layer-specific roles of internal representations are poorly understood, leading to heuristic decisions about where adaptation should be applied. We model the evolution of hidden states as a high-dimensional geometric trajectory and propose using the Ramer-Douglas-Peucker (RDP) algorithm, a parameter-free and training-free polygon simplification method that preserves global structural transitions while eliminating locally redundant changes, to identify critical breakpoints along the representation path. Crucially, we use these geometric pivots not merely for analysis, but as a direct decision signal for determining which layers should be adapted during parameter-efficient fine-tuning. By integrating this geometry-aware layer selection strategy into LoRA fine-tuning of Qwen3-8B-Base, we achieve superior performance on MMLU-Math using only 13 RDP-selected layers (81.67%), significantly outperforming both full 36-layer adaptation (79.32%) and random 13-layer selection (75.56%), as well as the baseline Qwen3-8B-Base model (74.25%). These results demonstrate that leveraging the intrinsic geometry of representation trajectories provides a robust, interpretable, and training-free signal for optimizing layer selection during model adaptation.

---


### 86. [Evaluating LLM-Driven Summarisation of Parliamentary Debates with Computational Argumentation](https://arxiv.org/abs/2604.19331)

**<font color=#1a73e8>作者：</font>** Eoghan Cunningham, Derek Greene, James Cross 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Understanding how policy is debated and justified in parliament is a fundamental aspect of the democratic process. However, the volume and complexity of such debates mean that outside audiences struggle to engage. Meanwhile, Large Language Models (LLMs) have been shown to enable automated summarisation at scale. While summaries of debates can make parliamentary procedures more accessible, evaluating whether these summaries faithfully communicate argumentative content remains challenging. Existing automated summarisation metrics have been shown to correlate poorly with human judgements of consistency (i.e., faithfulness or alignment between summary and source). In this work, we propose a formal framework for evaluating parliamentary debate summaries that grounds argument structures in the contested proposals up for debate. Our novel approach, driven by computational argumentation, focuses the evaluation on formal properties concerning the faithful preservation of the reasoning presented to justify or oppose policy outcomes. We demonstrate our methods using a case-study of debates from the European Parliament and associated LLM-driven summaries.

---


### 87. [Are Large Language Models Economically Viable for Industry Deployment?](https://arxiv.org/abs/2604.19342)

**<font color=#1a73e8>作者：</font>** Abdullah Mohammad, Sushant Kumar Ray, Pushkar Arora 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Generative AI-powered by Large Language Models (LLMs)-is increasingly deployed in industry across healthcare decision support, financial analytics, enterprise retrieval, and conversational automation, where reliability, efficiency, and cost control are critical. In such settings, models must satisfy strict constraints on energy, latency, and hardware utilization-not accuracy alone. Yet prevailing evaluation pipelines remain accuracy-centric, creating a Deployment-Evaluation Gap-the absence of operational and economic criteria in model assessment. To address this gap, we present EDGE-EVAL-a industry-oriented benchmarking framework that evaluates LLMs across their full lifecycle on legacy NVIDIA Tesla T4 GPUs. Benchmarking LLaMA and Qwen variants across three industrial tasks, we introduce five deployment metrics-Economic Break-Even (Nbreak), Intelligence-Per-Watt (IPW ), System Density (\r{ho}sys), Cold-Start Tax (Ctax), and Quantization Fidelity (Qret)-capturing profitability, energy efficiency, hardware scaling, serverless feasibility, and compression safety. Our results reveal a clear efficiency frontier-models in the <2B parameter class dominate larger baselines across economic and ecological dimensions. LLaMA-3.2-1B (INT4) achieves ROI break-even in 14 requests (median), delivers 3x higher energy-normalized intelligence than 7B models, and exceeds 6,900 tokens/s/GB under 4-bit quantization. We further uncover an efficiency anomaly-while QLoRA reduces memory footprint, it increases adaptation energy by up to 7x for small models-challenging prevailing assumptions about quantization-aware training in edge deployment.

---


### 88. [Attend what matters: Leveraging vision foundational models for breast cancer classification using mammograms](https://arxiv.org/abs/2604.19350)

**<font color=#1a73e8>作者：</font>** Samyak Sanghvi, Piyush Miglani, Sarvesh Shashikumar 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision Transformers $(\texttt{ViT})$ have become the architecture of choice for many computer vision tasks, yet their performance in computer-aided diagnostics remains limited. Focusing on breast cancer detection from mammograms, we identify two main causes for this shortfall. First, medical images are high-resolution with small abnormalities, leading to an excessive number of tokens and making it difficult for the softmax-based attention to localize and attend to relevant regions. Second, medical image classification is inherently fine-grained, with low inter-class and high intra-class variability, where standard cross-entropy training is insufficient. To overcome these challenges, we propose a framework with three key components: (1) Region of interest $(\texttt{RoI})$ based token reduction using an object detection model to guide attention; (2) contrastive learning between selected $\texttt{RoI}$ to enhance fine-grained discrimination through hard-negative based training; and (3) a $\texttt{DINOv2}$ pretrained $\texttt{ViT}$ that captures localization-aware, fine-grained features instead of global $\texttt{CLIP}$ representations. Experiments on public mammography datasets demonstrate that our method achieves superior performance over existing baselines, establishing its effectiveness and potential clinical utility for large-scale breast cancer screening. Our code is available for reproducibility here: this https URL

---


### 89. [DASH-KV: Accelerating Long-Context LLM Inference via Asymmetric KV Cache Hashing](https://arxiv.org/abs/2604.19351)

**<font color=#1a73e8>作者：</font>** Jinyu Guo, Zhihan Zhang, Yutong Li 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The quadratic computational complexity of the standard attention mechanism constitutes a fundamental bottleneck for large language models in long-context inference. While existing KV cache compression methods alleviate memory pressure, they often sacrifice generation quality and fail to address the high overhead of floating-point arithmetic. This paper introduces DASH-KV, an innovative acceleration framework that reformulates attention as approximate nearest-neighbor search via asymmetric deep hashing. Under this paradigm, we design an asymmetric encoding architecture that differentially maps queries and keys to account for their distinctions in precision and reuse characteristics. To balance efficiency and accuracy, we further introduce a dynamic mixed-precision mechanism that adaptively retains full-precision computation for critical tokens. Extensive experiments on LongBench demonstrate that DASH-KV significantly outperforms state-of-the-art baseline methods while matching the performance of full attention, all while reducing inference complexity from O(N^2) to linear O(N). The code is available at this https URL

---


### 90. [Do Agents Dream of Root Shells? Partial-Credit Evaluation of LLM Agents in Capture The Flag Challenges](https://arxiv.org/abs/2604.19354)

**<font color=#1a73e8>作者：</font>** Ali Al-Kaswan, Maksim Plotnikov, Maxim Hájek 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Model (LLM) agents are increasingly proposed for autonomous cybersecurity tasks, but their capabilities in realistic offensive settings remain poorly understood. We present DeepRed, an open-source benchmark for evaluating LLM-based agents on realistic Capture The Flag (CTF) challenges in isolated virtualized environments. DeepRed places an agent in a Kali attacker environment with terminal tools and optional web search, connected over a private network to a target challenge, and records full execution traces for analysis. To move beyond binary solved/unsolved outcomes, we introduce a partial-credit scoring method based on challenge-specific checkpoints derived from public writeups, together with an automated summarise-then-judge labelling pipeline for assigning checkpoint completion from logs. Using DeepRed, we benchmark ten commercially accessible LLMs on ten VM-based CTF challenges spanning different challenge categories. The results indicate that current agents remain limited: the best model achieves only 35% average checkpoint completion, performing strongest on common challenge types and weakest on tasks requiring non-standard discovery and longer-horizon adaptation.

---


### 91. [PanDA: Unsupervised Domain Adaptation for Multimodal 3D Panoptic Segmentation in Autonomous Driving](https://arxiv.org/abs/2604.19379)

**<font color=#1a73e8>作者：</font>** Yining Pan, Shijie Li, Yuchen Wu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper presents the first study on Unsupervised Domain Adaptation (UDA) for multimodal 3D panoptic segmentation (mm-3DPS), aiming to improve generalization under domain shifts commonly encountered in real-world autonomous driving. A straightforward solution is to employ a pseudo-labeling strategy, which is widely used in UDA to generate supervision for unlabeled target data, combined with an mm-3DPS backbone. However, existing supervised mm-3DPS methods rely heavily on strong cross-modal complementarity between LiDAR and RGB inputs, making them fragile under domain shifts where one modality degrades (e.g., poor lighting or adverse weather). Moreover, conventional pseudo-labeling typically retains only high-confidence regions, leading to fragmented masks and incomplete object supervision, which are issues particularly detrimental to panoptic segmentation. To address these challenges, we propose PanDA, the first UDA framework specifically designed for multimodal 3D panoptic segmentation. To improve robustness against single-sensor degradation, we introduce an asymmetric multimodal augmentation that selectively drops regions to simulate domain shifts and improve robust representation learning. To enhance pseudo-label completeness and reliability, we further develop a dual-expert pseudo-label refinement module that extracts domain-invariant priors from both 2D and 3D modalities. Extensive experiments across diverse domain shifts, spanning time, weather, location, and sensor variations, significantly surpass state-of-the-art UDA baselines for 3D semantic segmentation.

---


### 92. [Air-Know: Arbiter-Calibrated Knowledge-Internalizing Robust Network for Composed Image Retrieval](https://arxiv.org/abs/2604.19386)

**<font color=#1a73e8>作者：</font>** Zhiheng Fu, Yupeng Hu, Qianyun Yang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Composed Image Retrieval (CIR) has attracted significant attention due to its flexible multimodal query method, yet its development is severely constrained by the Noisy Triplet Correspondence (NTC) problem. Most existing robust learning methods rely on the "small loss hypothesis", but the unique semantic ambiguity in NTC, such as "partial matching", invalidates this assumption, leading to unreliable noise identification. This entraps the model in a self dependent vicious cycle where the learner is intertwined with the arbiter, ultimately causing catastrophic "representation pollution". To address this critical challenge, we propose a novel "Expert-Proxy-Diversion" decoupling paradigm, named Air-Know (ArbIteR calibrated Knowledge iNternalizing rObust netWork). Air-Know incorporates three core modules: (1) External Prior Arbitration (EPA), which utilizes Multimodal Large Language Models (MLLMs) as an offline expert to construct a high precision anchor dataset; (2) Expert Knowledge Internalization (EKI), which efficiently guides a lightweight proxy "arbiter" to internalize the expert's discriminative logic; (3) Dual Stream Reconciliation (DSR), which leverages the EKI's matching confidence to divert the training data, achieving a clean alignment stream and a representation feedback reconciliation stream. Extensive experiments on multiple CIR benchmark datasets demonstrate that Air-Know significantly outperforms existing SOTA methods under the NTC setting, while also showing strong competitiveness in traditional CIR.

---


### 93. [Can Continual Pre-training Bridge the Performance Gap between General-purpose and Specialized Language Models in the Medical Domain?](https://arxiv.org/abs/2604.19394)

**<font color=#1a73e8>作者：</font>** Niclas Doll, Jasper Schulze Buschhoff, Shalaka Satheesh 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper narrows the performance gap between small, specialized models and significantly larger general-purpose models through domain adaptation via continual pre-training and merging. We address the scarcity of specialized non-English data by constructing a high-quality German medical corpus (FineMed-de) from FineWeb2. This corpus is used to continually pre-train and merge three well-known LLMs (ranging from $7B$ to $24B$ parameters), creating the DeFineMed model family. A comprehensive evaluation confirms that specialization dramatically enhances $7B$ model performance on German medical benchmarks. Furthermore, the pairwise win-rate analysis of the Qwen2.5-based models demonstrates an approximately $3.5$-fold increase in the win-rate against the much larger Mistral-Small-24B-Instruct through domain adaptation. This evidence positions specialized $7B$ models as a competitive, resource-efficient solution for complex medical instruction-following tasks. While model merging successfully restores instruction-following abilities, a subsequent failure mode analysis reveals inherent trade-offs, including the introduction of language mixing and increased verbosity, highlighting the need for more targeted fine-tuning in future work. This research provides a robust, compliant methodology for developing specialized LLMs, serving as the foundation for practical use in German-speaking healthcare contexts.

---


### 94. [GRASPrune: Global Gating for Budgeted Structured Pruning of Large Language Models](https://arxiv.org/abs/2604.19398)

**<font color=#1a73e8>作者：</font>** Ziyang Wang, Jiangfeng Xiao, Chuan Xiao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are expensive to serve because model parameters, attention computation, and KV caches impose substantial memory and latency costs. We present GRASPrune, a structured pruning framework applied after pretraining that jointly prunes FFN channels and KV head groups under a single global budget. Instead of learning importance scores without constraints and applying the budget only after training, GRASPrune learns lightweight gate scores with a projected straight-through estimator that enforces a hard mask satisfying the budget at every step while keeping the backbone weights frozen. After the mask is fixed, we calibrate scaling factors on the retained units to mitigate scale mismatch caused by pruning, and fold these factors into the pruned weights to obtain a smaller dense checkpoint with no extra parameters at inference. On LLaMA-2-7B, GRASPrune removes 50% of parameters and achieves 12.18 perplexity on WikiText-2 while maintaining competitive average zero-shot accuracy on five benchmarks, using four epochs on 512 unlabeled calibration sequences on a single NVIDIA A100 80GB GPU without any full model fine-tuning.

---


### 95. [Lost in Translation: Do LVLM Judges Generalize Across Languages?](https://arxiv.org/abs/2604.19405)

**<font color=#1a73e8>作者：</font>** Md Tahmid Rahman Laskar, Mohammed Saidul Islam, Mir Tafseer Nayeem 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automatic evaluators such as reward models play a central role in the alignment and evaluation of large vision-language models (LVLMs). Despite their growing importance, these evaluators are almost exclusively assessed on English-centric benchmarks, leaving open the question of how well these evaluators generalize across languages. To answer this question, we introduce MM-JudgeBench, the first large-scale benchmark for multilingual and multimodal judge model evaluation, which includes over 60K pairwise preference instances spanning 25 typologically diverse languages. MM-JudgeBench integrates two complementary subsets: a general vision-language preference evaluation subset extending VL-RewardBench, and a chart-centric visual-text reasoning subset derived from OpenCQA, enabling systematic analysis of reward models (i.e., LVLM judges) across diverse settings. We additionally release a multilingual training set derived from MM-RewardBench, disjoint from our evaluation data, to support domain adaptation. By evaluating 22 LVLMs (15 open-source, 7 proprietary), we uncover substantial cross-lingual performance variance in our proposed benchmark. Our analysis further shows that model size and architecture are poor predictors of multilingual robustness, and that even state-of-the-art LVLM judges exhibit inconsistent behavior across languages. Together, these findings expose fundamental limitations of current reward modeling and underscore the necessity of multilingual, multimodal benchmarks for developing reliable automated evaluators.

---


### 96. [HP-Edit: A Human-Preference Post-Training Framework for Image Editing](https://arxiv.org/abs/2604.19406)

**<font color=#1a73e8>作者：</font>** Fan Li, Chonghuinan Wang, Lina Lei 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Common image editing tasks typically adopt powerful generative diffusion models as the leading paradigm for real-world content editing. Meanwhile, although reinforcement learning (RL) methods such as Diffusion-DPO and Flow-GRPO have further improved generation quality, efficiently applying Reinforcement Learning from Human Feedback (RLHF) to diffusion-based editing remains largely unexplored, due to a lack of scalable human-preference datasets and frameworks tailored to diverse editing needs. To fill this gap, we propose HP-Edit, a post-training framework for Human Preference-aligned Editing, and introduce RealPref-50K, a real-world dataset across eight common tasks and balancing common object editing. Specifically, HP-Edit leverages a small amount of human-preference scoring data and a pretrained visual large language model (VLM) to develop HP-Scorer--an automatic, human preference-aligned evaluator. We then use HP-Scorer both to efficiently build a scalable preference dataset and to serve as the reward function for post-training the editing model. We also introduce RealPref-Bench, a benchmark for evaluating real-world editing performance. Extensive experiments demonstrate that our approach significantly enhances models such as Qwen-Image-Edit-2509, aligning their outputs more closely with human preference.

---


### 97. [VCE: A zero-cost hallucination mitigation method of LVLMs via visual contrastive editing](https://arxiv.org/abs/2604.19412)

**<font color=#1a73e8>作者：</font>** Yanbin Huang, Yisen Li, Guiyao Tie 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large vision-language models (LVLMs) frequently suffer from Object Hallucination (OH), wherein they generate descriptions containing objects that are not actually present in the input image. This phenomenon is particularly problematic in real-world applications such as medical imaging and autonomous driving, where accuracy is critical. Recent studies suggest that the hallucination problem may stem from language priors: biases learned during pretraining that cause LVLMs to generate words based on their statistical co-occurrence. To mitigate this problem, we propose Visual Contrastive Editing (VCE), a novel post-hoc method that identifies and suppresses hallucinatory tendencies by analyzing the model's response to contrastive visual perturbations. Using Singular Value Decomposition (SVD), we decompose the model's activation patterns to isolate hallucination subspaces and apply targeted parameter edits to attenuate its influence. Unlike existing approaches that require fine-tuning or labeled data, VCE operates as a label-free intervention, making it both scalable and practical for deployment in resource-constrained settings. Experimental results demonstrate that VCE effectively reduces object hallucination across multiple benchmarks while maintaining the model's original computational efficiency.

---


### 98. [MER 2026: From Discriminative Emotion Recognition to Generative Emotion Understanding](https://arxiv.org/abs/2604.19417)

**<font color=#1a73e8>作者：</font>** Zheng Lian, Xiaojiang Peng, Kele Xu 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> MER2026 marks the fourth edition of the MER series of challenges. The MER series provides valuable data resources to the research community and offers tasks centered on recent research trends, establishing itself as one of the largest challenges in the field. Throughout its history, the focus of MER has shifted from discriminative emotion recognition to generative emotion understanding. Specifically, MER2023 concentrated on discriminative emotion recognition, restricting the emotion recognition scope to fixed basic labels. In MER2024 and MER2025, we transitioned to generative emotion understanding and introduced two new tasks: fine-grained emotion recognition and descriptive emotion analysis, aiming to leverage the extensive vocabulary and multimodal understanding capabilities of Multimodal Large Language Models (MLLMs) to facilitate fine-grained and explainable emotion recognition. Building on this trajectory, MER2026 continues to follow these research trends and contains four tracks: MER-Cross shifts the focus from individual to dyadic interaction scenarios; MER-FG centers on fine-grained emotion recognition; MER-Prefer aims to predict human preferences regarding different emotion descriptions; MER-PS focuses on emotion recognition based on physiological signals. More details regarding the dataset and baselines are available at this https URL.

---


### 99. [What Makes an LLM a Good Optimizer? A Trajectory Analysis of LLM-Guided Evolutionary Search](https://arxiv.org/abs/2604.19440)

**<font color=#1a73e8>作者：</font>** Xinhao Zhang, Xi Chen, François Portet 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent work has demonstrated the promise of orchestrating large language models (LLMs) within evolutionary and agentic optimization systems. However, the mechanisms driving these optimization gains remain poorly understood. In this work, we present a large-scale study of LLM-guided evolutionary search, collecting optimization trajectories for 15 LLMs across 8 tasks. Although zero-shot problem-solving ability correlates with final optimization outcomes, it explains only part of the variance: models with similar initial capability often induce dramatically different search trajectories and outcomes. By analyzing these trajectories, we find that strong LLM optimizers behave as local refiners, producing frequent incremental improvements while progressively localizing the search in semantic space. Conversely, weaker optimizers exhibit large semantic drift, with sporadic breakthroughs followed by stagnation. Notably, various measures of solution novelty do not predict final performance; novelty is beneficial only when the search remains sufficiently localized around high-performing regions of the solution space. Our results highlight the importance of trajectory analysis for understanding and improving LLM-based optimization systems and provide actionable insights for their design and training.

---


### 100. [Unsupervised Confidence Calibration for Reasoning LLMs from a Single Generation](https://arxiv.org/abs/2604.19444)

**<font color=#1a73e8>作者：</font>** Thomas Zollo, Jimmy Wang, Richard Zemel  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reasoning language models can solve increasingly complex tasks, but struggle to produce the calibrated confidence estimates necessary for reliable deployment. Existing calibration methods usually depend on labels or repeated sampling at inference time, making them impractical in many settings. We introduce a method for unsupervised confidence calibration of reasoning LLMs when only a single generation is available at inference time. Our approach uses offline sampling on unlabeled data to derive a self-consistency-based proxy target, then distills this signal into a lightweight deployment-time confidence predictor. In a broad evaluation across 5 math and question-answering tasks using 9 reasoning models, our method substantially outperforms baselines, including under distribution shift, and improves downstream performance in selective prediction and simulated downstream decision-making.

---


> [!TIP]
> 当前位于：**51-100**（第 2/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-132](./part-03.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
