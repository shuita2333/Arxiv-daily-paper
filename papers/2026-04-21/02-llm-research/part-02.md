# 🧠 大模型相关研究 | 2026年04月21日

> 本类共 **114** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**51-100**（第 2/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-114](./part-03.md)

---

### 51. [TTL: Test-time Textual Learning for OOD Detection with Pretrained Vision-Language Models](https://arxiv.org/abs/2604.15756)

**<font color=#1a73e8>作者：</font>** Jinlun Ye, Jiang Liao, Runhe Lai 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) such as CLIP exhibit strong Out-of-distribution (OOD) detection capabilities by aligning visual and textual representations. Recent CLIP-based test-time adaptation methods further improve detection performance by incorporating external OOD labels. However, such labels are finite and fixed, while the real OOD semantic space is inherently open-ended. Consequently, fixed labels fail to represent the diverse and evolving OOD semantics encountered in test streams. To address this limitation, we introduce Test-time Textual Learning (TTL), a framework that dynamically learns OOD textual semantics from unlabeled test streams, without relying on external OOD labels. TTL updates learnable prompts using pseudo-labeled test samples to capture emerging OOD knowledge. To suppress noise introduced by pseudo-labels, we introduce an OOD knowledge purification strategy that selects reliable OOD samples for adaptation while suppressing noise. In addition, TTL maintains an OOD Textual Knowledge Bank that stores high-quality textual features, providing stable score calibration across batches. Extensive experiments on two standard benchmarks with nine OOD datasets demonstrate that TTL consistently achieves state-of-the-art performance, highlighting the value of textual adaptation for robust test-time OOD detection. Our code is available at this https URL.

---


### 52. [Skill-RAG: Failure-State-Aware Retrieval Augmentation via Hidden-State Probing and Skill Routing](https://arxiv.org/abs/2604.15771)

**<font color=#1a73e8>作者：</font>** Kai Wei, Raymond Li, Xi Zhu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-Augmented Generation (RAG) has emerged as a foundational paradigm for grounding large language models in external knowledge. While adaptive retrieval mechanisms have improved retrieval efficiency, existing approaches treat post-retrieval failure as a signal to retry rather than to diagnose -- leaving the structural causes of query-evidence misalignment unaddressed. We observe that a significant portion of persistent retrieval failures stem not from the absence of relevant evidence but from an alignment gap between the query and the evidence space. We propose Skill-RAG, a failure-aware RAG framework that couples a lightweight hidden-state prober with a prompt-based skill router. The prober gates retrieval at two pipeline stages; upon detecting a failure state, the skill router diagnoses the underlying cause and selects among four retrieval skills -- query rewriting, question decomposition, evidence focusing, and an exit skill for truly irreducible cases -- to correct misalignment before the next generation attempt. Experiments across multiple open-domain QA and complex reasoning benchmarks show that Skill-RAG substantially improves accuracy on hard cases persisting after multi-turn retrieval, with particularly strong gains on out-of-distribution datasets. Representation-space analyses further reveal that the proposed skills occupy structured, separable regions of the failure state space, supporting the view that query-evidence misalignment is a typed rather than monolithic phenomenon.

---


### 53. [MemEvoBench: Benchmarking Memory MisEvolution in LLM Agents](https://arxiv.org/abs/2604.15774)

**<font color=#1a73e8>作者：</font>** Weiwei Xie, Shaoxiong Guo, Fan Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Equipping Large Language Models (LLMs) with persistent memory enhances interaction continuity and personalization but introduces new safety risks. Specifically, contaminated or biased memory accumulation can trigger abnormal agent behaviors. Existing evaluation methods have not yet established a standardized framework for measuring memory misevolution. This phenomenon refers to the gradual behavioral drift resulting from repeated exposure to misleading information. To address this gap, we introduce MemEvoBench, the first benchmark evaluating long-horizon memory safety in LLM agents against adversarial memory injection, noisy tool outputs, and biased feedback. The framework consists of QA-style tasks across 7 domains and 36 risk types, complemented by workflow-style tasks adapted from 20 Agent-SafetyBench environments with noisy tool returns. Both settings employ mixed benign and misleading memory pools within multi-round interactions to simulate memory evolution. Experiments on representative models reveal substantial safety degradation under biased memory updates. Our analysis suggests that memory evolution is a significant contributor to these failures. Furthermore, static prompt-based defenses prove insufficient, underscoring the urgency of securing memory evolution in LLM agents.

---


### 54. [Pruning Unsafe Tickets: A Resource-Efficient Framework for Safer and More Robust LLMs](https://arxiv.org/abs/2604.15780)

**<font color=#1a73e8>作者：</font>** Wai Man Si, Mingjie Li, Michael Backes 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine learning models are increasingly deployed in real-world applications, but even aligned models such as Mistral and LLaVA still exhibit unsafe behaviors inherited from pre-training. Current alignment methods like SFT and RLHF primarily encourage models to generate preferred responses, but do not explicitly remove the unsafe subnetworks that trigger harmful outputs. In this work, we introduce a resource-efficient pruning framework that directly identifies and removes parameters associated with unsafe behaviors while preserving model utility. Our method employs a gradient-free attribution mechanism, requiring only modest GPU resources, and generalizes across architectures and quantized variants. Empirical evaluations on ML models show substantial reductions in unsafe generations and improved robustness against jailbreak attacks, with minimal utility loss. From the perspective of the Lottery Ticket Hypothesis, our results suggest that ML models contain "unsafe tickets" responsible for harmful behaviors, and pruning reveals "safety tickets" that maintain performance while aligning outputs. This provides a lightweight, post-hoc alignment strategy suitable for deployment in resource-constrained settings.

---


### 55. [ReVis: Towards Reusable Image-Based Visualizations with MLLMs](https://arxiv.org/abs/2604.15781)

**<font color=#1a73e8>作者：</font>** Xiaolin Wen, Changlin Li, Manusha Karunathilaka 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Many expressive visualizations are shared online only as bitmap images, making them difficult to redesign or adapt to new data. Reusing such image-based visualizations requires substantial expertise and is often time-consuming, even for experienced visualization practitioners. Existing work on reproducing visualizations often relies on structured SVG or specifications, supports limited visualization types, and offers limited flexibility for customization. To address these challenges, we present ReVis, a human-AI collaboration approach that enables flexible reuse of image-based visualizations. First, a generic Domain-Specific language (DSL) is proposed to model complex visualizations and support both visualization decomposition and reproduction. Then, ReVis employs an MLLM-based pipeline to parse an image-based visualization into the DSL, delineating its core visual structures and data-to-encoding mappings, and further reproduces the visualization from the DSL. Finally, ReVis includes an interactive interface to allow users to upload visualization images, inspect reproduced results, update the underlying data, and customize visual encodings. A gallery of 40 visualizations demonstrates the expressiveness of the DSL, and a quantitative study evaluates the reproduction quality of ReVis on these examples. Two usage scenarios and user interviews with 16 visualization practitioners demonstrate the effectiveness of ReVis.

---


### 56. [EVIL: Evolving Interpretable Algorithms for Zero-Shot Inference on Event Sequences and Time Series with LLMs](https://arxiv.org/abs/2604.15787)

**<font color=#1a73e8>作者：</font>** David Berghaus  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce EVIL (\textbf{EV}olving \textbf{I}nterpretable algorithms with \textbf{L}LMs), an approach that uses LLM-guided evolutionary search to discover simple, interpretable algorithms for dynamical systems inference. Rather than training neural networks on large datasets, EVIL evolves pure Python/NumPy programs that perform zero-shot, in-context inference across datasets. We apply EVIL to three distinct tasks: next-event prediction in temporal point processes, rate matrix estimation for Markov jump processes, and time series imputation. In each case, a single evolved algorithm generalizes across all evaluation datasets without per-dataset training (analogous to an amortized inference model). To the best of our knowledge, this is the first work to show that LLM-guided program evolution can discover a single compact inference function for these dynamical-systems problems. Across the three domains, the discovered algorithms are often competitive with, and even outperform, state-of-the-art deep learning models while being orders of magnitudes faster, and remaining fully interpretable.

---


### 57. [A Systematic Study of Training-Free Methods for Trustworthy Large Language Models](https://arxiv.org/abs/2604.15789)

**<font color=#1a73e8>作者：</font>** Wai Man Si, Mingjie Li, Michael Backes 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As Large Language Models (LLMs) receive increasing attention and are being deployed across various domains, their potential risks, including generating harmful or biased content, producing unsupported claims, and exhibiting vulnerabilities to adversarial attacks, have drawn significant attention. To enable quick and low-cost adaptation, training-free methods have recently emerged as cost-effective alternatives to post-training alignment techniques. Despite their promising results, these methods are evaluated inconsistently across the literature, cover limited dimensions of trustworthiness, and can introduce undesirable side effects, such as utility degradation and increased brittleness. To fully assess the impacts of these training-free methods, we take a step back and systematically re-evaluate the effectiveness of existing training-free methods against various trustworthy settings and their influence on utility, robustness, and computational overhead. We also categorize these methods into three levels (input, internal, and output) based on where they intervene in the model's information flow during inference. Using this taxonomy, we conduct a comprehensive analysis of various representative and effective methods from each level across different LLM families and sizes. Our analysis highlights several trade-offs and unresolved challenges in current approaches. We summarize key findings and limitations in the existing literature, and propose practical recommendations for balancing trustworthiness, utility, and robustness in LLMs without the need for additional training.

---


### 58. [Self-Distillation as a Performance Recovery Mechanism for LLMs: Counteracting Compression and Catastrophic Forgetting](https://arxiv.org/abs/2604.15794)

**<font color=#1a73e8>作者：</font>** Chi Liu, Xin Chen, Xu Zhou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have achieved remarkable success, underpinning diverse AI applications. However, they often suffer from performance degradation due to factors such as catastrophic forgetting during Supervised Fine-Tuning (SFT), quantization, and pruning. In this work, we introduce a performance recovery framework based on Self-Distillation Fine-Tuning (SDFT) that effectively restores model capabilities. Complementing this practical contribution, we provide a rigorous theoretical explanation for the underlying recovery mechanism. We posit that an LLM's generative capability fundamentally relies on the high-dimensional manifold constructed by its hidden layers. To investigate this, we employ Centered Kernel Alignment (CKA) to quantify the alignment between student and teacher activation trajectories, leveraging its invariance to orthogonal transformations and scaling. Our experiments demonstrate a strong correlation between performance recovery and manifold alignment, substantiating the claim that self-distillation effectively aligns the student's high-dimensional manifold with the optimal structure represented by the teacher. This study bridges the gap between practical recovery frameworks and geometric representation theory, offering new insights into the internal mechanisms of self-distillation.

---


### 59. [CHOP: Chunkwise Context-Preserving Framework for RAG on Multi Documents](https://arxiv.org/abs/2604.15802)

**<font color=#1a73e8>作者：</font>** Hyunseok Park, Jihyeon Kim, Jongeun Kim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-Augmented Generation (RAG) systems lose retrieval accuracy when similar documents coexist in the vector database, causing unnecessary information, hallucinations, and factual errors. To alleviate this issue, we propose CHOP, a framework that iteratively evaluates chunk relevance with Large Language Models (LLMs) and progressively reconstructs documents by determining their association with specific topics or query types. CHOP integrates two key components: the CNM-Extractor, which generates compact per-chunk signatures capturing categories, key nouns, and model names, and the Continuity Decision Module, which preserves contextual coherence by deciding whether consecutive chunks belong to the same document flow. By prefixing each chunk with context-aware metadata, CHOP reduces semantic conflicts among similar documents and enhances retriever discrimination. Experiments on benchmark datasets show that CHOP alleviates retrieval confusion and provides a scalable approach for building high-quality knowledge bases, achieving a Top-1 Hit Rate of 90.77% and notable gains in ranking quality metrics.

---


### 60. [Qwen3.5-Omni Technical Report](https://arxiv.org/abs/2604.15804)

**<font color=#1a73e8>作者：</font>** Qwen Team  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In this work, we present Qwen3.5-Omni, the latest advancement in the Qwen-Omni model family. Representing a significant evolution over its predecessor, Qwen3.5-Omni scales to hundreds of billions of parameters and supports a 256k context length. By leveraging a massive dataset comprising heterogeneous text-vision pairs and over 100 million hours of audio-visual content, the model demonstrates robust omni-modality capabilities. Qwen3.5-Omni-plus achieves SOTA results across 215 audio and audio-visual understanding, reasoning, and interaction subtasks and benchmarks, surpassing Gemini-3.1 Pro in key audio tasks and matching it in comprehensive audio-visual understanding. Architecturally, Qwen3.5-Omni employs a Hybrid Attention Mixture-of-Experts (MoE) framework for both Thinker and Talker, enabling efficient long-sequence inference. The model facilitates sophisticated interaction, supporting over 10 hours of audio understanding and 400 seconds of 720P video (at 1 FPS). To address the inherent instability and unnaturalness in streaming speech synthesis, often caused by encoding efficiency discrepancies between text and speech tokenizers, we introduce ARIA. ARIA dynamically aligns text and speech units, significantly enhancing the stability and prosody of conversational speech with minimal latency impact. Furthermore, Qwen3.5-Omni expands linguistic boundaries, supporting multilingual understanding and speech generation across 10 languages with human-like emotional nuance. Finally, Qwen3.5-Omni exhibits superior audio-visual grounding capabilities, generating script-level structured captions with precise temporal synchronization and automated scene segmentation. Remarkably, we observed the emergence of a new capability in omnimodal models: directly performing coding based on audio-visual instructions, which we call Audio-Visual Vibe Coding.

---


### 61. [Beyond a Single Frame: Multi-Frame Spatially Grounded Reasoning Across Volumetric MRI](https://arxiv.org/abs/2604.15808)

**<font color=#1a73e8>作者：</font>** Lama Moukheiber, Caleb M. Yeung, Haotian Xue 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Spatial reasoning and visual grounding are core capabilities for vision-language models (VLMs), yet most medical VLMs produce predictions without transparent reasoning or spatial evidence. Existing benchmarks also evaluate VLMs on isolated 2D images, overlooking the volumetric nature of clinical imaging, where findings can span multiple frames or appear on only a few slices. We introduce Spatially Grounded MRI Visual Question Answering (SGMRI-VQA), a 41,307-pair benchmark for multi-frame, spatially grounded reasoning on volumetric MRI. Built from expert radiologist annotations in the fastMRI+ dataset across brain and knee studies, each QA pair includes a clinician-aligned chain-of-thought trace with frame-indexed bounding box coordinates. Tasks are organized hierarchically across detection, localization, counting/classification, and captioning, requiring models to jointly reason about what is present, where it is, and across which frames it extends. We benchmark 10 VLMs and show that supervised fine-tuning of Qwen3-VL-8B with bounding box supervision consistently improves grounding performance over strong zero-shot baselines, indicating that targeted spatial supervision is an effective path toward grounded clinical reasoning.

---


### 62. [Aligning What Vision-Language Models See and Perceive with Adaptive Information Flow](https://arxiv.org/abs/2604.15809)

**<font color=#1a73e8>作者：</font>** Chengxin Liu, Wonseok Choi, Chenshuang Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) have demonstrated strong capability in a wide range of tasks such as visual recognition, document parsing, and visual grounding. Nevertheless, recent work shows that while VLMs often manage to capture the correct image region corresponding to the question, they do not necessarily produce the correct answers. In this work, we demonstrate that this misalignment could be attributed to suboptimal information flow within VLMs, where text tokens distribute too much attention to irrelevant visual tokens, leading to incorrect answers. Based on the observation, we show that modulating the information flow during inference can improve the perception capability of VLMs. The idea is that text tokens should only be associated with important visual tokens during decoding, eliminating the interference of irrelevant regions. To achieve this, we propose a token dynamics-based method to determine the importance of visual tokens, where visual tokens that exhibit distinct activation patterns during different decoding stages are viewed as important. We apply our approach to representative open-source VLMs and evaluate on various datasets, including visual question answering, visual grounding and counting, optical character recognition, and object hallucination. The results show that our approach significantly improves the performance of baselines. Project page: this https URL.

---


### 63. [SSFT: A Lightweight Spectral-Spatial Fusion Transformer for Generic Hyperspectral Classification](https://arxiv.org/abs/2604.15828)

**<font color=#1a73e8>作者：</font>** Alexander Musiat, Nikolas Ebert, Oliver Wasenmüller  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Hyperspectral imaging enables fine-grained recognition of materials by capturing rich spectral signatures, but learning robust classifiers is challenging due to high dimensionality, spectral redundancy, limited labeled data, and strong domain shifts. Beyond earth observation, labeled HSI data is often scarce and imbalanced, motivating compact models for generic hyperspectral classification across diverse acquisition regimes. We propose the lightweight Spectral-Spatial Fusion Transformer (SSFT), which factorizes representation learning into spectral and spatial pathways and integrates them via cross-attention to capture complementary wavelength-dependent and structural information. We evaluate our SSFT on the challenging HSI-Benchmark, a heterogeneous multi-dataset benchmark covering earth observation, fruit condition assessment, and fine-grained material recognition. SSFT achieves state-of-the-art overall performance, ranking first while using less than 2% of the parameters of the previous leading method. We further evaluate transfer to the substantially larger SpectralEarth benchmark under the official protocol, where SSFT remains competitive despite its compact size. Ablation studies show that both spectral and spatial pathways are crucial, with spatial modeling contributing most, and that SSFT remains robust without data augmentation.

---


### 64. [Discover and Prove: An Open-source Agentic Framework for Hard Mode Automated Theorem Proving in Lean 4](https://arxiv.org/abs/2604.15839)

**<font color=#1a73e8>作者：</font>** Chengwu Liu, Yichun Yin, Ye Yuan 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Most ATP benchmarks embed the final answer within the formal statement -- a convention we call "Easy Mode" -- a design that simplifies the task relative to what human competitors face and may lead to optimistic estimates of model capability. We call the stricter, more realistic setting "Hard Mode": the system must independently discover the answer before constructing a formal proof. To enable Hard Mode research, we make two contributions. First, we release MiniF2F-Hard and FIMO-Hard, expert-reannotated Hard Mode variants of two widely-used ATP benchmarks. Second, we introduce Discover And Prove (DAP), an agentic framework that uses LLM natural-language reasoning with explicit self-reflection to discover answers, then rewrites Hard Mode statements into Easy Mode ones for existing ATP provers. DAP sets the state of the art: on CombiBench it raises solved problems from 7 (previous SOTA, Pass@16) to 10; on PutnamBench it is the first system to formally prove 36 theorems in Hard Mode -- while simultaneously revealing that state-of-the-art LLMs exceed 80% answer accuracy on the same problems where formal provers manage under 10%, exposing a substantial gap that Hard Mode benchmarks are uniquely suited to measure.

---


### 65. [CoEvolve: Training LLM Agents via Agent-Data Mutual Evolution](https://arxiv.org/abs/2604.15840)

**<font color=#1a73e8>作者：</font>** Shidong Yang, Ziyu Ma, Tongwen Huang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning for LLM agents is typically conducted on a static data distribution, which fails to adapt to the agent's evolving behavior and leads to poor coverage of complex environment interactions. To address these challenges, we propose CoEvolve, an agent-data mutual evolution framework that enables LLM agents to improve through closed-loop, interaction-driven training. Specifically, CoEvolve extracts feedback signals such as forgetting and uncertainty from rollout trajectories to identify failure-prone interaction patterns, and utilizes them to guide LLM-based task synthesis. The synthesized tasks are validated through environment interaction and utilized to update the data distribution, enabling joint adaptation of the agent and its data. Extensive experiments on AppWorld and BFCL across Qwen2.5-7B, Qwen3-4B, and Qwen3-30B-A3B demonstrate consistent and significant improvements over strong base models, yielding absolute gains of 19.43%, 15.58%, and 18.14%, respectively.

---


### 66. [Exploring the Capability Boundaries of LLMs in Mastering of Chinese Chouxiang Language](https://arxiv.org/abs/2604.15841)

**<font color=#1a73e8>作者：</font>** Dianqing Lin, Tian Lan, Jiali Zhu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While large language models (LLMs) have achieved remarkable success in general language tasks, their performance on Chouxiang Language, a representative subcultural language in the Chinese internet context, remains largely unexplored. In this paper, we introduce Mouse, a specialized benchmark designed to evaluate the capabilities of LLMs on NLP tasks involving Chouxiang Language across six tasks. Experimental results show that, current state-of-the-art (SOTA) LLMs exhibit clear limitations on multiple tasks, while performing well on tasks that involve contextual semantic understanding. In addition, we further discuss the reasons behind the generally low performance of SOTA LLMs on Chouxiang Language, examine whether the LLM-as-a-judge approach adopted for translation tasks aligns with human judgments and values, and analyze the key factors that influence Chouxiang translation. Our study aims to promote further research in the NLP community on multicultural integration and the dynamics of evolving internet languages. Our code and data are publicly available.

---


### 67. [Disentangling Mathematical Reasoning in LLMs: A Methodological Investigation of Internal Mechanisms](https://arxiv.org/abs/2604.15842)

**<font color=#1a73e8>作者：</font>** Tanja Baeumel, Josef van Genabith, Simon Ostermann  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have demonstrated impressive capabilities, yet their internal mechanisms for handling reasoning-intensive tasks remain underexplored. To advance the understanding of model-internal processing mechanisms, we present an investigation of how LLMs perform arithmetic operations by examining internal mechanisms during task execution. Using early decoding, we trace how next-token predictions are constructed across layers. Our experiments reveal that while the models recognize arithmetic tasks early, correct result generation occurs only in the final layers. Notably, models proficient in arithmetic exhibit a clear division of labor between attention and MLP modules, where attention propagates input information and MLP modules aggregate it. This division is absent in less proficient models. Furthermore, successful models appear to process more challenging arithmetic tasks functionally, suggesting reasoning capabilities beyond factual recall.

---


### 68. [CiPO: Counterfactual Unlearning for Large Reasoning Models through Iterative Preference Optimization](https://arxiv.org/abs/2604.15847)

**<font color=#1a73e8>作者：</font>** Junyi Li, Yongqiang Chen, Ningning Ding  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Machine unlearning has gained increasing attention in recent years, as a promising technique to selectively remove unwanted privacy or copyrighted information from Large Language Models that are trained on a massive scale of human data. However, the emergence of Large Reasoning Models (LRMs), which emphasize long chain-of-thought (CoT) reasoning to address complex questions, presents a dilemma to unlearning: existing methods either struggle to completely eliminate undesired knowledge from the CoT traces or degrade the reasoning performances due to the interference with the reasoning process. To this end, we introduce Counterfactual Unlearning through iterative Preference Optimization (CiPO), a novel framework that redefines unlearning as the targeted intervention of the CoT reasoning in LRMs. More specifically, given a desired unlearning target answer, CiPO instructs LRMs to generate a logically valid counterfactual reasoning trace for preference tuning. As the LRM adjusts to the counterfactual trace, CiPO iteratively updates the preference learning data to increase the discrepancy from the original model. This iterative loop ensures both desirable unlearning and smooth optimization, effectively mitigating the dilemma. Experiments on challenging benchmarks demonstrate that CiPO excels at unlearning, completely removing knowledge from both the intermediate CoT steps and the final answer, while preserving the reasoning abilities of LRMs.

---


### 69. [DPrivBench: Benchmarking LLMs' Reasoning for Differential Privacy](https://arxiv.org/abs/2604.15851)

**<font color=#1a73e8>作者：</font>** Erchi Wang, Pengrun Huang, Eli Chien 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Differential privacy (DP) has a wide range of applications for protecting data privacy, but designing and verifying DP algorithms requires expert-level reasoning, creating a high barrier for non-expert practitioners. Prior works either rely on specialized verification languages that demand substantial domain expertise or remain semi-automated and require human-in-the-loop guidance. In this work, we investigate whether large language models (LLMs) can automate DP reasoning. We introduce DPrivBench, a benchmark in which each instance asks whether a function or algorithm satisfies a stated DP guarantee under specified assumptions. The benchmark is carefully designed to cover a broad range of DP topics, span diverse difficulty levels, and resist shortcut reasoning through trivial pattern matching. Experiments show that while the strongest models handle textbook mechanisms well, all models struggle with advanced algorithms, revealing substantial gaps in current DP reasoning capabilities. Through further analytic study and failure-mode analysis, we identify several promising directions for improving automated DP reasoning. Our benchmark provides a solid foundation for developing and evaluating such methods, and complements existing benchmarks for mathematical reasoning.

---


### 70. [QuantSightBench: Evaluating LLM Quantitative Forecasting with Prediction Intervals](https://arxiv.org/abs/2604.15859)

**<font color=#1a73e8>作者：</font>** Jeremy Qin, Maksym Andriushchenko  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Forecasting has become a natural benchmark for reasoning under uncertainty. Yet existing evaluations of large language models remain limited to judgmental tasks in simple formats, such as binary or multiple-choice questions. In practice, however, forecasting spans a far broader scope. Across domains such as economics, public health, and social demographics, decisions hinge on numerical estimates over continuous quantities, a capability that current benchmarks do not capture. Evaluating such estimates requires a format that makes uncertainty explicit and testable. We propose prediction intervals as a natural and rigorous interface for this purpose. They demand scale awareness, internal consistency across confidence levels, and calibration over a continuum of outcomes, making them a more suitable evaluation format than point estimates for numerical forecasting. To assess this capability, we introduce a new benchmark QuantSightBench, and evaluate frontier models under multiple settings, assessing both empirical coverage and interval sharpness. Our results show that none of the 11 evaluated frontier and open-weight models achieves the 90\% coverage target, with the top performers Gemini 3.1 Pro (79.1\%), Grok 4 (76.4\%), and GPT-5.4 (75.3\%) all falling at least 10 percentage points short. Calibration degrades sharply at extreme magnitudes, revealing systematic overconfidence across all evaluated models.

---


### 71. [DiZiNER: Disagreement-guided Instruction Refinement via Pilot Annotation Simulation for Zero-shot Named Entity Recognition](https://arxiv.org/abs/2604.15866)

**<font color=#1a73e8>作者：</font>** Siun Kim, Hyung-Jin Yoon  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have advanced information extraction (IE) by enabling zero-shot and few-shot named entity recognition (NER), yet their generative outputs still show persistent and systematic errors. Despite progress through instruction fine-tuning, zero-shot NER still lags far behind supervised systems. These recurring errors mirror inconsistencies observed in early-stage human annotation processes that resolve disagreements through pilot annotation. Motivated by this analogy, we introduce DiZiNER (Disagreement-guided Instruction Refinement via Pilot Annotation Simulation for Zero-shot Named Entity Recognition), a framework that simulates the pilot annotation process, employing LLMs to act as both annotators and supervisors. Multiple heterogeneous LLMs annotate shared texts, and a supervisor model analyzes inter-model disagreements to refine task instructions. Across 18 benchmarks, DiZiNER achieves zero-shot SOTA results on 14 datasets, improving prior bests by +8.0 F1 and reducing the zero-shot to supervised gap by over +11 points. It also consistently outperforms its supervisor, GPT-5 mini, indicating that improvements stem from disagreement-guided instruction refinement rather than model capacity. Pairwise agreement between models shows a strong correlation with NER performance, further supporting this finding.

---


### 72. [UniEditBench: A Unified and Cost-Effective Benchmark for Image and Video Editing via Distilled MLLMs](https://arxiv.org/abs/2604.15871)

**<font color=#1a73e8>作者：</font>** Lifan Jiang, Tianrun Wu, Yuhang Pei 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The evaluation of visual editing models remains fragmented across methods and modalities. Existing benchmarks are often tailored to specific paradigms, making fair cross-paradigm comparisons difficult, while video editing lacks reliable evaluation benchmarks. Furthermore, common automatic metrics often misalign with human preference, yet directly deploying large multimodal models (MLLMs) as evaluators incurs prohibitive computational and financial costs. We present UniEditBench, a unified benchmark for image and video editing that supports reconstruction-based and instruction-driven methods under a shared protocol. UniEditBench includes a structured taxonomy of nine image operations (Add, Remove, Replace, Change, Stroke-based, Extract, Adjust, Count, Reorder) and eight video operations, with coverage of challenging compositional tasks such as counting and spatial reordering. To enable scalable evaluation, we distill a high-capacity MLLM judge (Qwen3-VL-235B-A22B Instruct) into lightweight 4B/8B evaluators that provide multi-dimensional scoring over structural fidelity, text alignment, background consistency, naturalness, and temporal-spatial consistency (for videos). Experiments show that the distilled evaluators maintain strong agreement with human judgments and substantially reduce deployment cost relative to the teacher model. UniEditBench provides a practical and reproducible protocol for benchmarking modern visual editing methods. Our benchmark and the associated reward models are publicly available at this https URL.

---


### 73. [How Hypocritical Is Your LLM judge? Listener-Speaker Asymmetries in the Pragmatic Competence of Large Language Models](https://arxiv.org/abs/2604.15873)

**<font color=#1a73e8>作者：</font>** Judith Sieker, Sina Zarrieß  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly studied as repositories of linguistic knowledge. In this line of work, models are commonly evaluated both as generators of language and as judges of linguistic output, yet these two roles are rarely examined in direct relation to one another. As a result, it remains unclear whether success in one role aligns with success in the other. In this paper, we address this question for pragmatic competence by comparing LLMs' performance as pragmatic listeners, judging the appropriateness of linguistic outputs, and as pragmatic speakers, generating pragmatically appropriate language. We evaluate multiple open-weight and proprietary LLMs across three pragmatic settings. We find a robust asymmetry between pragmatic evaluation and pragmatic generation: many models perform substantially better as listeners than as speakers. Our results suggest that pragmatic judging and pragmatic generation are only weakly aligned in current LLMs, calling for more integrated evaluation practices.

---


### 74. [Experience Compression Spectrum: Unifying Memory, Skills, and Rules in LLM Agents](https://arxiv.org/abs/2604.15877)

**<font color=#1a73e8>作者：</font>** Xing Zhang, Guanghui Wang, Yanwei Cui 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As LLM agents scale to long-horizon, multi-session deployments, efficiently managing accumulated experience becomes a critical bottleneck. Agent memory systems and agent skill discovery both address this challenge -- extracting reusable knowledge from interaction traces -- yet a citation analysis of 1,136 references across 22 primary papers reveals a cross-community citation rate below 1%. We propose the \emph{Experience Compression Spectrum}, a unifying framework that positions memory, skills, and rules as points along a single axis of increasing compression (5--20$\times$ for episodic memory, 50--500$\times$ for procedural skills, 1,000$\times$+ for declarative rules), directly reducing context consumption, retrieval latency, and compute overhead. Mapping 20+ systems onto this spectrum reveals that every system operates at a fixed, predetermined compression level -- none supports adaptive cross-level compression, a gap we term the \emph{missing diagonal}. We further show that specialization alone is insufficient -- both communities independently solve shared sub-problems without exchanging solutions -- that evaluation methods are tightly coupled to compression levels, that transferability increases with compression at the cost of specificity, and that knowledge lifecycle management remains largely neglected. We articulate open problems and design principles for scalable, full-spectrum agent learning systems.

---


### 75. [PolarMAE: Efficient Fetal Ultrasound Pre-training via Semantic Screening and Polar-Guided Masking](https://arxiv.org/abs/2604.15893)

**<font color=#1a73e8>作者：</font>** Meng Lv, Yapeng Li, Hang Su 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Intelligent fetal ultrasound (US) interpretation is crucial for prenatal diagnosis, but high annotation costs and operator-induced variance make unsupervised pre-training a highly promising paradigm. However, existing pre-training methods largely ignore US-specific characteristics -- severe data redundancy, fan-shaped locality, and polar coordinate beamforming -- limiting their effectiveness in downstream tasks. To address this, we propose PolarMAE, a novel and efficient pre-training framework tailored for US images. Specifically, to mitigate continuous scanning redundancy, we introduce a Progressive Visual-Semantic Screening (PVSS) that adaptively extracts high-value samples, significantly boosting pre-training efficiency. Furthermore, we design an Acoustic-Bounded Region Constraint (ABRC) to accommodate US locality, forcing the model to focus strictly on valid acoustic regions rather than invalid dark backgrounds. Finally, leveraging the beamforming prior and local details, we propose a Polar-Texture Collaborative Masking (PTCM), enabling the model to capture underlying radial imaging patterns and critical tissue structures. Extensive experiments across diverse datasets and downstream interpretation tasks demonstrate that our method achieves state-of-the-art performance with strong pre-training scalability and efficiency.

---


### 76. [Making Image Editing Easier via Adaptive Task Reformulation with Agentic Executions](https://arxiv.org/abs/2604.15917)

**<font color=#1a73e8>作者：</font>** Bo Zhao, Kairui Guo, Runnan Du 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Instruction guided image editing has advanced substantially with recent generative models, yet it still fails to produce reliable results across many seemingly simple cases. We observe that a large portion of these failures stem not from insufficient model capacity, but from poorly formulated editing tasks, such as those involving small targets, implicit spatial relations, or under-specified instructions. In this work, we frame image editing failures as a task formulation problem and propose an adaptive task reformulation framework that improves editing performance without modifying the underlying model. Our key idea is to transform the original image-instruction pair into a sequence of operations that are dynamically determined and executed by a MLLM agent through analysis, routing, reformulation, and feedback-driven refinement. Experiments on multiple benchmarks, including ImgEdit, PICA, and RePlan, across diverse editing backbones such as Qwen Image Edit and Nano Banana, show consistent improvements, with especially large gains on challenging cases. These results suggest that task reformulation is a critical but underexplored factor, and that substantial gains can be achieved by better matching editing tasks to the effective operating regime of existing models.

---


### 77. [RAGognizer: Hallucination-Aware Fine-Tuning via Detection Head Integration](https://arxiv.org/abs/2604.15945)

**<font color=#1a73e8>作者：</font>** Fabian Ridder, Laurin Lessel, Malte Schilling  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-Augmented Generation (RAG) is widely used to augment the input to Large Language Models (LLMs) with external information, such as recent or domain-specific knowledge. Nonetheless, current models still produce closed-domain hallucinations and generate content that is unsupported by the retrieved context. Current detection approaches typically treat hallucination as a post-hoc problem, relying on black-box consistency checks or probes over frozen internal representations. In this work, we demonstrate that hallucination detection based on internal state representation can also serve as a direct training signal. We introduce RAGognize, a dataset of naturally occurring closed-domain hallucinations with token-level annotations, and RAGognizer, a hallucination-aware fine-tuning approach that integrates a lightweight detection head into an LLM, allowing for the joint optimization of language modeling and hallucination detection. This joint objective forces the model to improve the separability of its internal states regarding hallucinations while simultaneously learning to generate well-formed and meaningful responses. Across multiple benchmarks, RAGognizer achieves state-of-the-art token-level hallucination detection while substantially reducing hallucination rates during generation, without degrading language quality or relevance.

---


### 78. [Integrating Graphs, Large Language Models, and Agents: Reasoning and Retrieval](https://arxiv.org/abs/2604.15951)

**<font color=#1a73e8>作者：</font>** Hamed Jelodar, Samita Bai, Mohammad Meymani 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Generative AI, particularly Large Language Models, increasingly integrates graph-based representations to enhance reasoning, retrieval, and structured decision-making. Despite rapid advances, there remains limited clarity regarding when, why, where, and what types of graph-LLM integrations are most appropriate across applications. This survey provides a concise, structured overview of the design choices underlying the integration of graphs with LLMs. We categorize existing methods based on their purpose (reasoning, retrieval, generation, recommendation), graph modality (knowledge graphs, scene graphs, interaction graphs, causal graphs, dependency graphs), and integration strategies (prompting, augmentation, training, or agent-based use). By mapping representative works across domains such as cybersecurity, healthcare, materials science, finance, robotics, and multimodal environments, we highlight the strengths, limitations, and best-fit scenarios for each technique. This survey aims to offer researchers a practical guide for selecting the most suitable graph-LLM approach depending on task requirements, data characteristics, and reasoning complexity.

---


### 79. [ReactBench: A Benchmark for Topological Reasoning in MLLMs on Chemical Reaction Diagrams](https://arxiv.org/abs/2604.15994)

**<font color=#1a73e8>作者：</font>** Qiang Xu, Shengyuan Bai, Yu Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) excel at recognizing individual visual elements and reasoning over simple linear diagrams. However, when faced with complex topological structures involving branching paths, converging flows, and cyclic dependencies, their reasoning capabilities degrade sharply, even on tasks as basic as counting endpoints. Existing benchmarks fail to probe this gap, focusing on semantic comprehension rather than structural reasoning. We introduce ReactBench, a benchmark that reveals fundamental limitations in structural reasoning through chemical reaction diagrams. These real-world scientific diagrams offer an ideal testbed because they naturally span diverse structures from linear chains to cyclic graphs, while requiring both precise local recognition and coherent global reasoning. Our benchmark comprises 1,618 expert-annotated QA pairs across four hierarchical task dimensions. Extensive evaluation across 17 MLLMs reveals a significant performance gap exceeding 30% between anchor-based tasks and holistic structural reasoning tasks. Controlled ablations confirm this bottleneck lies in reasoning, not perception. These findings expose a fundamental deficit in structural understanding and establish directions for advancing visual reasoning.

---


### 80. [AgentV-RL: Scaling Reward Modeling with Agentic Verifier](https://arxiv.org/abs/2604.16004)

**<font color=#1a73e8>作者：</font>** Jiazheng Zhang, Ziche Fu, Zhiheng Xi 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Verifiers have been demonstrated to enhance LLM reasoning via test-time scaling (TTS). Yet, they face significant challenges in complex domains. Error propagation from incorrect intermediate reasoning can lead to false positives for seemingly plausible solutions, while lacking external grounding makes verifiers unreliable on computation or knowledge-intensive tasks. To address these challenges, we propose Agentic Verifier, a framework that transforms reward modeling into a multi-turn, tool-augmented deliberative process. We introduce complementary forward and backward agents: one traces solutions from premises to conclusions, while the other re-checks conclusions against their underlying premises. This bidirectional process enables a comprehensive, reliable, and interpretable assessment of solutions. To facilitate practical deployment, we propose AgentV-RL. Through proactive exploration and reinforcement learning, the verifier autonomously interleaves tool-use with internal reasoning. Extensive experiments show that Agentic Verifier yields consistent performance gains under both parallel and sequential TTS. Notably, our 4B variant surpasses state-of-the-art ORMs by 25.2%, positioning it as a promising paradigm for agentic reward modeling.

---


### 81. [SocialGrid: A Benchmark for Planning and Social Reasoning in Embodied Multi-Agent Systems](https://arxiv.org/abs/2604.16022)

**<font color=#1a73e8>作者：</font>** Hikaru Shindo, Hanzhao Lin, Lukas Helff 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As Large Language Models (LLMs) transition from text processors to autonomous agents, evaluating their social reasoning in embodied multi-agent settings becomes critical. We introduce SocialGrid, an embodied multi-agent environment inspired by Among Us that evaluates LLM agents on planning, task execution, and social reasoning. Our evaluations reveal that even the strongest open model (GPT-OSS-120B) achieves below 60% accuracy in task completion and planning, with agents getting stuck in repetitive behaviors or failing to navigate basic obstacles. Since poor navigation confounds evaluation of social intelligence, SocialGrid offers an optional Planning Oracle to isolate social reasoning from planning deficits. While planning assistance improves task completion, social reasoning remains a bottleneck: agents fail to detect deception at near-random chance regardless of scale, relying on shallow heuristics rather than accumulating behavioral evidence. SocialGrid provides automatic failure analysis and fine-grained metrics, enabling developers to diagnose and improve their agents. We also establish a competitive leaderboard using Elo ratings from adversarial league play.

---


### 82. [Where does output diversity collapse in post-training?](https://arxiv.org/abs/2604.16027)

**<font color=#1a73e8>作者：</font>** Constantinos Karouzos, Xingwei Tan, Nikolaos Aletras  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Post-trained language models produce less varied outputs than their base counterparts. This output diversity collapse undermines inference-time scaling methods that rely on varied samples, and risks homogenizing model outputs on creative and value-laden tasks. Prior work attributes collapse to specific post-training methods, without separating the role of training data composition from the method, or the generation format from the model weights. We trace output diversity through three parallel post-training lineages of Olmo 3, Think (chain-of-thought distillation), Instruct (broad multi-source data), and RL-Zero, across 15 tasks and four text diversity metrics. We find that the location of collapse co-varies with data composition: the Think lineage loses most semantic diversity at supervised fine-tuning, and the effect of DPO is larger in Instruct than in Think. Suppressing chain-of-thought reasoning at inference in Think models drops accuracy on hard tasks, yet leaves answer-level diversity unchanged, showing that the collapse is embedded in the model weights by training data, not imposed by the generation format. Decomposing diversity loss on six verifiable tasks into a quality-control component (removal of incorrect outputs) and a residual component (genuine narrowing among correct outputs) reveals that the split is task-dependent, and Think models retain more correct-answer diversity than Instruct despite collapsing more in aggregate. Our results indicate that diversity collapse is determined during training by data composition and cannot be addressed at inference time alone.

---


### 83. [Stochasticity in Tokenisation Improves Robustness](https://arxiv.org/abs/2604.16037)

**<font color=#1a73e8>作者：</font>** Sophie Steger, Rui Li, Sofiane Ennadir 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The widespread adoption of large language models (LLMs) has increased concerns about their robustness. Vulnerabilities in perturbations of tokenisation of the input indicate that models trained with a deterministic canonical tokenisation can be brittle to adversarial attacks. Recent studies suggest that stochastic tokenisation can deliver internal representations that are less sensitive to perturbations. In this paper, we analyse how stochastic tokenisations affect robustness to adversarial attacks and random perturbations. We systematically study this over a range of learning regimes (pre-training, supervised fine-tuning, and in-context learning), data sets, and model architectures. We show that pre-training and fine-tuning with uniformly sampled stochastic tokenisations improve robustness to random and adversarial perturbations. Evaluating on uniformly sampled non-canonical tokenisations reduces the accuracy of a canonically trained Llama-1b model by 29.8%. We find that training with stochastic tokenisation preserves accuracy without increasing inference cost.

---


### 84. [Towards Intrinsic Interpretability of Large Language Models:A Survey of Design Principles and Architectures](https://arxiv.org/abs/2604.16042)

**<font color=#1a73e8>作者：</font>** Yutong Gao, Qinglin Meng, Yuan Zhou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While Large Language Models (LLMs) have achieved strong performance across many NLP tasks, their opaque internal mechanisms hinder trustworthiness and safe deployment. Existing surveys in explainable AI largely focus on post-hoc explanation methods that interpret trained models through external approximations. In contrast, intrinsic interpretability, which builds transparency directly into model architectures and computations, has recently emerged as a promising alternative. This paper presents a systematic review of the recent advances in intrinsic interpretability for LLMs, categorizing existing approaches into five design paradigms: functional transparency, concept alignment, representational decomposability, explicit modularization, and latent sparsity induction. We further discuss open challenges and outline future research directions in this emerging field. The paper list is available at: this https URL.

---


### 85. [Mind's Eye: A Benchmark of Visual Abstraction, Transformation and Composition for Multimodal LLMs](https://arxiv.org/abs/2604.16054)

**<font color=#1a73e8>作者：</font>** Rohit Sinha, Aditya Kanade, Sai Srinivas Kancheti 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) have achieved impressive progress on vision language benchmarks, yet their capacity for visual cognitive and visuospatial reasoning remains less understood. We introduce "Mind's Eye", a multiple-choice benchmark of eight visuo-cognitive tasks inspired by classic human intelligence tests and organized under a novel "A-R-T" taxonomy: Abstraction, Relation, and Transformation. The tasks probe core processes of fluid intelligence such as pattern induction, analogical relation mapping, and mental transformation. We evaluate a diverse suite of closed-source and open-source MLLMs and compare their performance with human participants. Humans achieve 80% accuracy, while top performing MLLMs remain below 50%. Error analysis reveals failures in: (i) visual attention allocation, (ii) internal perceptual manipulation, and (iii) weak abstraction of underlying visual concepts. Our findings suggest that current MLLMs exhibit limited visuospatial reasoning capabilities, when compared with human participants, highlighting the need for more cognitively grounded evaluation frameworks.

---


### 86. [Chain-of-Thought Degrades Visual Spatial Reasoning Capabilities of Multimodal LLMs](https://arxiv.org/abs/2604.16060)

**<font color=#1a73e8>作者：</font>** Sai Srinivas Kancheti, Aditya Sanjiv Kanade, Vineeth N. Balasubramanian 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal Reasoning Models (MRMs) leveraging Chain-of-Thought (CoT) based thinking have revolutionized mathematical and logical problem-solving. However, we show that this paradigm struggles with generalized spatial intelligence. We perform a comprehensive evaluation of seventeen models across thirteen spatial benchmarks and identify a critical gap: CoT prompting consistently degrades performance in visual spatial reasoning. Furthermore, through a novel No-Image++ ablation, we demonstrate that MRMs and CoT prompted MLMs suffer from severe shortcut learning, and hallucinate visual details from textual priors even when the image is absent. These findings challenge the efficacy of text-only CoT for spatial tasks and underscore the need for vision-centric reasoning paradigms.

---


### 87. [AEGIS: Anchor-Enforced Gradient Isolation for Knowledge-Preserving Vision-Language-Action Fine-Tuning](https://arxiv.org/abs/2604.16067)

**<font color=#1a73e8>作者：</font>** Guransh Singh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Adapting pre-trained vision-language models (VLMs) for robotic control requires injecting high-magnitude continuous gradients from a flow-matching action expert into a backbone trained exclusively with cross-entropy. This cross-modal gradient asymmetry - the spectral dimensionality mismatch between low-rank MSE regression gradients and the high-dimensional semantic manifold sculpted by CE pre-training, causes rapid, severe erosion of the VLM's visual-question-answering (VQA) capability. Industry-standard defences either sever the gradient pathway entirely via stop gradient, discarding the rich continuous supervision, or restrict parameter capacity through low-rank adapters (LoRA) that constrain the rank of updates but not their direction, and thus still overwrite the pre-trained manifold. We introduce AEGIS (Anchor-Enforced Gradient Isolation System): a buffer-free, layer-wise orthogonal gradient projection framework that enables direct continuous MSE learning while preserving the pre-trained VQA manifold - without any co-training data or replay buffer. AEGIS pre-computes a static Gaussian reference anchor from masked VQA forward passes across all transformer layers, then at each training step constructs a Wasserstein-2 transport penalty that generates an anchor restoration gradient. A sequential dual-backward decomposes the task and anchor gradients; for each transformer layer, AEGIS applies a single Gram-Schmidt orthogonal projection that bends the task gradient away from the destructive direction while preserving its constructive content. The projection sheds less than 1% of gradient energy on average, yet eliminates the cumulative activation drift that drives severe forgetting.

---


### 88. [Prototype-Grounded Concept Models for Verifiable Concept Alignment](https://arxiv.org/abs/2604.16076)

**<font color=#1a73e8>作者：</font>** Stefano Colamonaco, David Debot, Pietro Barbiero 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Concept Bottleneck Models (CBMs) aim to improve interpretability in Deep Learning by structuring predictions through human-understandable concepts, but they provide no way to verify whether learned concepts align with the human's intended meaning, hurting interpretability. We introduce Prototype-Grounded Concept Models (PGCMs), which ground concepts in learned visual prototypes: image parts that serve as explicit evidence for the concepts. This grounding enables direct inspection of concept semantics and supports targeted human intervention at the prototype level to correct misalignments. Empirically, PGCMs match the predictive performance of state-of-the-art CBMs while substantially improving transparency, interpretability, and intervenability.

---


### 89. [DINOv3 Beats Specialized Detectors: A Simple Foundation Model Baseline for Image Forensics](https://arxiv.org/abs/2604.16083)

**<font color=#1a73e8>作者：</font>** Jieming Yu, Qiuxiao Feng, Zhuohan Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> With the rapid advancement of deep generative models, realistic fake images have become increasingly accessible, yet existing localization methods rely on complex designs and still struggle to generalize across manipulation types and imaging conditions. We present a simple but strong baseline based on DINOv3 with LoRA adaptation and a lightweight convolutional decoder. Under the CAT-Net protocol, our best model improves average pixel-level F1 by 17.0 points over the previous state of the art on four standard benchmarks using only 9.1\,M trainable parameters on top of a frozen ViT-L backbone, and even our smallest variant surpasses all prior specialized methods. LoRA consistently outperforms full fine-tuning across all backbone scales. Under the data-scarce MVSS-Net protocol, LoRA reaches an average F1 of 0.774 versus 0.530 for the strongest prior method, while full fine-tuning becomes highly unstable, suggesting that pre-trained representations encode forensic information that is better preserved than overwritten. The baseline also exhibits strong robustness to Gaussian noise, JPEG re-compression, and Gaussian blur. We hope this work can serve as a reliable baseline for the research community and a practical starting point for future image-forensic applications. Code is available at this https URL.

---


### 90. [From Articles to Canopies: Knowledge-Driven Pseudo-Labelling for Tree Species Classification using LLM Experts](https://arxiv.org/abs/2604.16115)

**<font color=#1a73e8>作者：</font>** Michał Romaszewski, Dominik Kopeć, Michał Cholewa 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Hyperspectral tree species classification is challenging due to limited and imbalanced class labels, spectral mixing (overlapping light signatures from multiple species), and ecological heterogeneity (variability among ecological systems). Addressing these challenges requires methods that integrate biological and structural characteristics of vegetation, such as canopy architecture and interspecific interactions, rather than relying solely on spectral signatures. This paper presents a biologically informed, semi-supervised deep learning method that integrates multi-sensor Earth observation data, specifically hyperspectral imaging (HSI) and airborne laser scanning (ALS), with expert, ecological knowledge. The approach relies on biologically inspired pseudo-labelling over a precomputed canopy graph, yielding accurate classification at low training cost. In addition, ecological priors on species cohabitation are automatically derived from reliable sources using large language models (LLMs) and encoded as a cohabitation matrix with likelihoods of species occurring together. These priors are incorporated into the pseudo-labelling strategy, effectively introducing expert knowledge into the model. Experiments on a real-world forest dataset demonstrate 5.6% improvement over the best reference method. Expert evaluation of cohabitation priors reveals high accuracy with differences no larger than 15%.

---


### 91. [Tabular foundation models for in-context prediction of molecular properties](https://arxiv.org/abs/2604.16123)

**<font color=#1a73e8>作者：</font>** Karim K. Ben Hicham, Jan G. Rittig, Martin Grohe 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate molecular property prediction is central to drug discovery, catalysis, and process design, yet real-world applications are often limited by small datasets. Molecular foundation models provide a promising direction by learning transferable molecular representations; however, they typically involve task-specific fine-tuning, require machine learning expertise, and often fail to outperform classical baselines. Tabular foundation models (TFMs) offer a fundamentally different paradigm: they perform predictions through in-context learning, enabling inference without task-specific training. Here, we evaluate TFMs in the low- to medium-data regime across both standardized pharmaceutical benchmarks and chemical engineering datasets. We evaluate both frozen molecular foundation model representations, as well as classical descriptors and fingerprints. Across the benchmarks, the approach shows excellent predictive performance while reducing computational cost, compared to fine-tuning, with these advantages also transferring to practical engineering data settings. In particular, combining TFMs with CheMeleon embeddings yields up to 100\% win rates on 30 MoleculeACE tasks, while compact RDKit2d and Mordred descriptors provide strong descriptor-based alternatives. Molecular representation emerges as a key determinant in TFM performance, with molecular foundation model embeddings and 2D descriptor sets both providing substantial gains over classic molecular fingerprints on many tasks. These results suggest that in-context learning with TFMs provides a highly accurate and cost-efficient alternative for property prediction in practical applications.

---


### 92. [Can LLMs Understand the Impact of Trauma? Costs and Benefits of LLMs Coding the Interviews of Firearm Violence Survivors](https://arxiv.org/abs/2604.16132)

**<font color=#1a73e8>作者：</font>** Jessica H. Zhu, Shayla Stringfield, Vahe Zaprosyan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Firearm violence is a pressing public health issue, yet research into survivors' lived experiences remains underfunded and difficult to scale. Qualitative research, including in-depth interviews, is a valuable tool for understanding the personal and societal consequences of community firearm violence and designing effective interventions. However, manually analyzing these narratives through thematic analysis and inductive coding is time-consuming and labor-intensive. Recent advancements in large language models (LLMs) have opened the door to automating this process, though concerns remain about whether these models can accurately and ethically capture the experiences of vulnerable populations. In this study, we assess the use of open-source LLMs to inductively code interviews with 21 Black men who have survived community firearm violence. Our results demonstrate that while some configurations of LLMs can identify important codes, overall relevance remains low and is highly sensitive to data processing. Furthermore, LLM guardrails lead to substantial narrative erasure. These findings highlight both the potential and limitations of LLM-assisted qualitative coding and underscore the ethical challenges of applying AI in research involving marginalized communities.

---


### 93. [Sentiment Analysis of German Sign Language Fairy Tales](https://arxiv.org/abs/2604.16138)

**<font color=#1a73e8>作者：</font>** Fabrizio Nunnari, Siddhant Jain, Patrick Gebhard  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present a dataset and a model for sentiment analysis of German sign language (DGS) fairy tales. First, we perform sentiment analysis for three levels of valence (negative, neutral, positive) on German fairy tales text segments using four large language models (LLMs) and majority voting, reaching an inter-annotator agreement of 0.781 Krippendorff's alpha. Second, we extract face and body motion features from each corresponding DGS video segment using MediaPipe. Finally, we train an explainable model (based on XGBoost) to predict negative, neutral or positive sentiment from video features. Results show an average balanced accuracy of 0.631. A thorough analysis of the most important features reveal that, in addition to eyebrows and mouth motion on the face, also the motion of hips, elbows, and shoulders considerably contribute in the discrimination of the conveyed sentiment, indicating an equal importance of face and body for sentiment communication in sign language.

---


### 94. [On the Rejection Criterion for Proxy-based Test-time Alignment](https://arxiv.org/abs/2604.16146)

**<font color=#1a73e8>作者：</font>** Ayoub Hammal, Pierre Zweigenbaum, Caio Corro  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent works proposed test-time alignment methods that rely on a small aligned model as a proxy that guides the generation of a larger base (unaligned) model. The implicit reward approach skews the large model distribution, whereas the nudging approach defers the generation of the next token to the small aligned model when the large base one is unconfident about its outcome. In this work, we first show that both approaches can be reduced to sampling from similar graphical models, where they differ only in the definition of a rejection criterion (or distribution). Moreover, we argue that the confidence criterion is ill-motivated due to linguistic phenomena like ambiguous phrasing. We propose a novel rejection criterion based on a conservative confidence bet. Experimentally, our novel approach outperforms previous work on several datasets.

---


### 95. [AtManRL: Towards Faithful Reasoning via Differentiable Attention Saliency](https://arxiv.org/abs/2604.16158)

**<font color=#1a73e8>作者：</font>** Max Henning Höth, Kristian Kersting, Björn Deiseroth 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) increasingly rely on chain-of-thought (CoT) reasoning to solve complex tasks. Yet ensuring that the reasoning trace both contributes to and faithfully reflects the processes underlying the model's final answer, rather than merely accompanying it, remains challenging. We introduce AtManRL, a method that leverages differentiable attention manipulation to learn more faithful reasoning through reinforcement learning. By training an additive attention mask that identifies tokens in the CoT crucial for producing correct answers, we derive a saliency reward signal that encourages the model to generate reasoning traces that genuinely influence its final predictions. We integrate this saliency reward with outcome-based rewards within the GRPO framework to jointly optimize for correctness and interpretability. Experiments on GSM8K and MMLU with Llama-3.2-3B-Instruct demonstrate that our approach can identify influential reasoning tokens and enable training more transparent reasoning models.

---


### 96. [neuralCAD-Edit: An Expert Benchmark for Multimodal-Instructed 3D CAD Model Editing](https://arxiv.org/abs/2604.16170)

**<font color=#1a73e8>作者：</font>** Toby Perrett, Matthew Bouchard, William McCarthy  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce neuralCAD-Edit, the first benchmark for editing 3D CAD models collected from expert CAD engineers. Instead of text conditioning as in prior works, we collect realistic CAD editing requests by capturing videos of professional designers, interacting directly with CAD models in CAD software, while talking, pointing and drawing. We recruited ten consenting designers to contribute to this contained study. We benchmark leading foundation models against human CAD experts carrying out edits, and find a large performance gap in both automatic metrics and human evaluations. Even the best foundation model (GPT 5.2) scores 53% lower (absolute) than CAD experts in human acceptance trials, demonstrating the challenge of neuralCAD-Edit. We hope neuralCAD-Edit will provide a solid foundation against which 3D CAD editing approaches and foundation models can be developed. Code/data: this https URL

---


### 97. [JumpLoRA: Sparse Adapters for Continual Learning in Large Language Models](https://arxiv.org/abs/2604.16171)

**<font color=#1a73e8>作者：</font>** Alexandra Dragomir, Ioana Pintilie, Antonio Barbalau 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Adapter-based methods have become a cost-effective approach to continual learning (CL) for Large Language Models (LLMs), by sequentially learning a low-rank update matrix for each task. To mitigate catastrophic forgetting, state-of-the-art approaches impose constraints on new adapters with respect to the previous ones, by targeting either subspace or coordinate-wise interference. In this paper, we propose JumpLoRA, a novel framework to adaptively induce sparsity in the Low-Rank Adaptation (LoRA) blocks through the use of JumpReLU gating. The method achieves dynamic parameter isolation, which helps prevent task interference. We demonstrate that our method is highly modular and compatible with LoRA-based CL approaches. Specifically, it significantly boosts the performance of IncLoRA and outperforms the leading state-of-the-art CL method, ELLA.

---


### 98. [Sketching the Readout of Large Language Models for Scalable Data Attribution and Valuation](https://arxiv.org/abs/2604.16197)

**<font color=#1a73e8>作者：</font>** Yide Ran, Jianwen Xie, Minghui Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Data attribution and valuation are critical for understanding data-model synergy for Large Language Models (LLMs), yet existing gradient-based methods suffer from scalability challenges on LLMs. Inspired by human cognition, where decision making relies on a focused readout of relevant memories rather than replaying all pathways, we introduce RISE (Readout Influence Sketching Estimator). Instead of computing and indexing gradients across the entire LLM, RISE focuses on influence hotspots at the output layer, where influence signals concentrate, and the gradient admits a decomposed outer-product form. This enables a dual-channel representation combining a lexical residual channel (RH) and a semantic projected-error channel (GH). Applying CountSketch projections to these channels achieves strong compression while maintaining accurate attribution. Across the OLMo (1B-32B) and Pythia (14M-6.9B) families, RISE reduces index storage by up to 112$\times$ compared to RapidIn and scales to 32B parameters LLM, where gradient-based baselines such as RapidIn and ZO-Inf become memory-infeasible. We evaluate RISE on two paradigms: (1) retrospective attribution, retrieving influential training examples for specific predictions, and (2) prospective valuation, scoring candidate data utility zero-shot. We validate RISE on three tasks: Howdy backdoor data detection, Finance-Medical domain separation, and Brain Rot high-quality data selection. In a closed-loop Brain Rot study, continued pretraining on RISE-selected data yields consistent downstream improvements. Overall, RISE provides a practical and scalable primitive for influence analysis and training-data selection in modern large language models.

---


### 99. [GAViD: A Large-Scale Multimodal Dataset for Context-Aware Group Affect Recognition from Videos](https://arxiv.org/abs/2604.16214)

**<font color=#1a73e8>作者：</font>** Deepak Kumar, Abhishek Pratap Singh, Puneet Kumar 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Understanding affective dynamics in real-world social systems is fundamental to modeling and analyzing human-human interactions in complex environments. Group affect emerges from intertwined human-human interactions, contextual influences, and behavioral cues, making its quantitative modeling a challenging computational social systems problem. However, computational modeling of group affect in in-the-wild scenarios remains challenging due to limited large-scale annotated datasets and the inherent complexity of multimodal social interactions shaped by contextual and behavioral variability. The lack of comprehensive datasets annotated with multimodal and contextual information further limits advances in the field. To address this, we introduce the Group Affect from ViDeos (GAViD) dataset, comprising 5091 video clips with multimodal data (video, audio and context), annotated with ternary valence and discrete emotion labels and enriched with VideoGPT-generated contextual metadata and human-annotated action cues. We also present Context-Aware Group Affect Recognition Network (CAGNet) for multimodal context-aware group affect recognition. CAGNet achieves 63.20\% test accuracy on GAViD, comparable to state-of-the-art performance. The dataset and code are available at this http URL.

---


### 100. [Beyond Surface Statistics: Robust Conformal Prediction for LLMs via Internal Representations](https://arxiv.org/abs/2604.16217)

**<font color=#1a73e8>作者：</font>** Yanli Wang, Peng Kuang, Xiaoyu Han 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly deployed in settings where reliability matters, yet output-level uncertainty signals such as token probabilities, entropy, and self-consistency can become brittle under calibration--deployment mismatch. Conformal prediction provides finite-sample validity under exchangeability, but its practical usefulness depends on the quality of the nonconformity score. We propose a conformal framework for LLM question answering that uses internal representations rather than output-facing statistics: specifically, we introduce Layer-Wise Information (LI) scores, which measure how conditioning on the input reshapes predictive entropy across model depth, and use them as nonconformity scores within a standard split conformal pipeline. Across closed-ended and open-domain QA benchmarks, with the clearest gains under cross-domain shift, our method achieves a better validity--efficiency trade-off than strong text-level baselines while maintaining competitive in-domain reliability at the same nominal risk level. These results suggest that internal representations can provide more informative conformal scores when surface-level uncertainty is unstable under distribution shift.

---


> [!TIP]
> 当前位于：**51-100**（第 2/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-114](./part-03.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
