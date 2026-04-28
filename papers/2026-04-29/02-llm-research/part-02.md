# 🧠 大模型相关研究 | 2026年04月29日

> 本类共 **215** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**51-100**（第 2/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-215](./part-05.md)

---

### 51. [Scaling Multi-Node Mixture-of-Experts Inference Using Expert Activation Patterns](https://arxiv.org/abs/2604.23150)

**<font color=#1a73e8>作者：</font>** Abhimanyu Bambhaniya, Geonhwa Jeong, Jason Park 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Most recent state-of-the-art (SOTA) large language models (LLMs) use Mixture-of-Experts (MoE) architectures to scale model capacity without proportional per-token compute, enabling higher-quality outputs at manageable serving costs. However, MoE inference at scale is fundamentally bottlenecked by expert load imbalance and inefficient token routing, especially in multi-node deployments where tokens are not guaranteed to be routed to local experts, resulting in significant inter-node all-to-all communication overhead.
To systematically characterize these challenges, we profile SOTA open-source MoE models, including Llama 4 Maverick, DeepSeek V3-671B, and Qwen3-230B-A22B, on various datasets and collected over 100k real expert activation traces. Upon studying the expert activation patterns, we uncover various persistent properties across all the frontier MoE models: variable expert load imbalance, domain-specific expert activation where expert popularity shifts across task families (code, math, chat, general), and a strong correlation between prefill and decode expert activations. Motivated by these findings, we propose workload-aware micro-batch grouping and an expert placement strategy to maximize token locality to the destination expert, thereby reducing inter-node communication. Across models and datasets, these optimizations help reduce all2all communication data up to 20, resulting in lower MoE decode latency and better accelerator utilization.

---


### 52. [One Identity, Many Roles: Multimodal Entity Coreference for Enhanced Video Situation Recognition](https://arxiv.org/abs/2604.23173)

**<font color=#1a73e8>作者：</font>** Balaji Darur, Amanmeet Garg, Makarand Tapaswi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video Situation Recognition (VidSitu) addresses the challenging problem of "who did what to whom, with what, how, and where" in a video. It tests thorough video understanding by requiring identification of salient actions and associated short descriptions for event roles across multiple events. Grounding with VidSitu requires spatio-temporal localization of key entities across shots and varied appearances.
We posit that coherent video understanding requires consistent identification of entities that play different roles. We propose Multimodal Entity Coreference (MEC) to unite entity descriptions in text with grounding across the video. Towards this, we introduce CineMEC, a multi-stage approach that unites event role mention groups with visual clusters of entities, without explicit grounding supervision during training. Our approach is designed to exploit the synergy between visual grounding and captioning, where improving one influences the other and vice versa. For evaluation, we extend the VidSitu dataset with grounding annotations. While previous work focuses primarily on descriptions, CineMEC improves consistency across both: captioning (+2.5% CIDEr, +7% LEA) and visual grounding (+18% HOTA).

---


### 53. [Judging the Judges: A Systematic Evaluation of Bias Mitigation Strategies in LLM-as-a-Judge Pipelines](https://arxiv.org/abs/2604.23178)

**<font color=#1a73e8>作者：</font>** Sadman Kabir Soumik  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-as-a-Judge has become the dominant paradigm for evaluating language model outputs, yet LLM judges exhibit systematic biases that compromise evaluation reliability. We present a comprehensive empirical study comparing nine debiasing strategies across five judge models from four provider families (Google, Anthropic, OpenAI, Meta), three benchmarks (MT-Bench n=400, LLMBar n=200, custom n=225), and four bias types. Our key findings: (1) Style bias is the dominant bias (0.76-0.92 across all models), far exceeding position bias (<= 0.04), yet has received minimal research attention. (2) All models show a conciseness preference on expansion pairs, but truncation controls confirm they correctly distinguish quality from length (0.92-1.00 accuracy), suggesting quality-sensitive evaluation rather than a simple length bias. (3) Debiasing is beneficial but model-dependent: the combined budget strategy significantly improves Claude Sonnet 4 by +11.2 pp (p < 0.0001), with directionally positive trends for other models. Only 2 of 20 non-baseline configurations show decreased agreement. We release our evaluation framework, controlled dataset, and all experimental artifacts at this https URL.

---


### 54. [From Coarse to Fine: Self-Adaptive Hierarchical Planning for LLM Agents](https://arxiv.org/abs/2604.23194)

**<font color=#1a73e8>作者：</font>** Haoran Tan, Zeyu Zhang, Chen Ma 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model-based agents have recently emerged as powerful approaches for solving dynamic and multi-step tasks. Most existing agents employ planning mechanisms to guide long-term actions in dynamic environments. However, current planning approaches face a fundamental limitation that they operate at a fixed granularity level. Specifically, they either provide excessive detail for simple tasks or insufficient detail for complex ones, failing to achieve an optimal balance between simplicity and complexity. Drawing inspiration from the principle of \textit{progressive refinement} in cognitive science, we propose \textbf{AdaPlan-H}, a self-adaptive hierarchical planning mechanism that mimics human planning strategies. Our method initiates with a coarse-grained macro plan and progressively refines it based on task complexity. It generates self-adaptive hierarchical plans tailored to the varying difficulty levels of different tasks, which can be optimized by imitation learning and capability enhancement. Experimental results demonstrate that our method significantly improves task execution success rates while mitigating overplanning at the planning level, providing a flexible and efficient solution for multi-step complex decision-making tasks. To contribute to the community, our code and data will be made publicly available at this https URL.

---


### 55. [AnalogRetriever: Learning Cross-Modal Representations for Analog Circuit Retrieval](https://arxiv.org/abs/2604.23195)

**<font color=#1a73e8>作者：</font>** Yihan Wang, Lei Li, Yao Lai 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Analog circuit design relies heavily on reusing existing intellectual property (IP), yet searching across heterogeneous representations such as SPICE netlists, schematics, and functional descriptions remains challenging. Existing methods are largely limited to exact matching within a single modality, failing to capture cross-modal semantic relationships. To bridge this gap, we present AnalogRetriever, a unified tri-modal retrieval framework for analog circuit search. We first build a high-quality dataset on top of Masala-CHAI through a two-stage repair pipeline that raises the netlist compile rate from 22\% to 100\%. Built on this foundation, AnalogRetriever encodes schematics and descriptions with a vision-language model and netlists with a port-aware relational graph convolutional network, mapping all three modalities into a shared embedding space via curriculum contrastive learning. Experiments show that AnalogRetriever achieves an average Recall@1 of 75.2\% across all six cross-modal retrieval directions, significantly outperforming existing baselines. When integrated into the AnalogCoder agentic framework as a retrieval-augmented generation module, it consistently improves functional pass rates and enables previously unsolved tasks to be completed. Our code and dataset will be released.

---


### 56. [Discovering Agentic Safety Specifications from 1-Bit Danger Signals](https://arxiv.org/abs/2604.23210)

**<font color=#1a73e8>作者：</font>** Víctor Gallego  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Can large language model agents discover hidden safety objectives through experience alone? We introduce EPO-Safe (Experiential Prompt Optimization for Safe Agents), a framework where an LLM iteratively generates action plans, receives sparse binary danger warnings, and evolves a natural language behavioral specification through reflection. Unlike standard LLM reflection methods that rely on rich textual feedback (e.g., compiler errors or detailed environment responses), EPO-Safe demonstrates that LLMs can perform safety reasoning from a strictly impoverished signal in structured, low-dimensional environments: the agent never observes the hidden performance function $R^*$, only a single bit per timestep indicating that an action was unsafe. We evaluate on five AI Safety Gridworlds (Leike et al., 2017) and five text-based scenario analogs where visible reward $R$ may diverge from $R^*$. EPO-Safe discovers safe behavior within 1-2 rounds (5-15 episodes), producing human-readable specifications with correct explanatory hypotheses about hazards (e.g., "X cells are directionally hazardous: entering from the north is dangerous"). Critically, we show that standard reward-driven reflection actively degrades safety: agents reflecting on reward alone use the loop to justify and accelerate reward hacking, proving that reflection must be paired with a dedicated safety channel to discover hidden constraints. We further evaluate robustness to noisy oracles: even when 50% of non-dangerous steps produce spurious warnings, mean safety performance degrades by only 15% on average, though sensitivity is environment-dependent, as cross-episode reflection naturally filters inconsistent signals. Each evolved specification functions as an auditable set of grounded behavioral rules discovered autonomously through interaction, rather than authored by humans as in Constitutional AI (Bai et al., 2022).

---


### 57. [Measuring Temporal Linguistic Emergence in Diffusion Language Models](https://arxiv.org/abs/2604.23235)

**<font color=#1a73e8>作者：</font>** Harry Lu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Diffusion language models expose an explicit denoising trajectory, making it possible to ask when different kinds of information become measurable during generation. We study three independent 32-step runs of LLaDA-8B-Base on masked WikiText-103 text, each with 1{,}000 probe-training sequences and 200 held-out evaluation sequences. From saved trajectories, we derive four temporal measurements: token commitment; linear recoverability of part-of-speech (POS), coarse semantic category, and token identity; confidence and entropy dynamics; and sensitivity under mid-trajectory re-masking. Across seeds, the same ordering recurs: content categories stabilize earlier than function-heavy categories, POS and coarse semantic labels remain substantially more linearly recoverable than exact lexical identity under our probe setup, uncertainty remains higher for tokens that ultimately resolve incorrectly even though late confidence becomes less calibrated, and perturbation sensitivity peaks in the middle of the trajectory. A direct/collateral decomposition shows that this peak is overwhelmingly local to the perturbed positions themselves. In this LLaDA+WikiText setting, denoising time is therefore a useful analysis axis: under our measurements, coarse labels are recovered earlier and more robustly than lexical identity, trajectory-level uncertainty tracks eventual correctness, and mid-trajectory states are the most intervention-sensitive.

---


### 58. [Scalable LLM-based Coding of Dialogue in Healthcare Simulation: Balancing Coding Performance, Processing Time, and Environmental Impact](https://arxiv.org/abs/2604.23255)

**<font color=#1a73e8>作者：</font>** Kiyoshige Garces, Gloria Milena Fernandez-Nieto, Linxuan Zhao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Research shows that dialogue, the interactive process through which participants articulate their thinking, plays a central role in constructing shared understanding, coordinating action, and shaping learning outcomes in teams. Analysing dialogue content has been central to advancing team learning theory and informing the design of computer-supported collaborative learning environments, yet this progress has depended on labour-intensive qualitative coding. LLMs offer new possibilities for automating and enhancing the dialogue layer within emerging multimodal learning analytics approaches, with recent studies showing that they can approximate human coding through few-shot prompting. However, prior work has focused on replicating human coding accuracy for research purposes, rather than addressing a more educationally consequential question: how can we design prompts that allow an LLM to label team dialogue accurately and fast enough to be useful in real settings, such as in-person healthcare simulations, where results must be returned quickly and computational cost and sustainability also matter? This paper investigates how prompt design and batching strategies can be optimised to balance coding accuracy, processing time, and environmental impact in team-based healthcare simulation debriefing. Using a dataset of 11,647 utterances coded across 6 dialogue constructs, we compared 4 prompt designs across varying batch sizes, evaluating coding performance, processing time, and energy consumption, as well as the trade-offs between these metrics. Results indicate that increasing batch size improves speed and reduces energy use, but negatively impacts coding performance. Beyond demonstrating the feasibility of LLM-based qualitative analysis, this study offers practical guidance for scaling dialogue analytics in contexts where timeliness, privacy, and sustainability are critical.

---


### 59. [Small Language Model Helps Resolve Semantic Ambiguity of LLM Prompt](https://arxiv.org/abs/2604.23263)

**<font color=#1a73e8>作者：</font>** Zhenzhen Huang, Chaoning Zhang, Fachrina Dewi Puspitasari 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly utilized in various complex reasoning tasks due to their excellent instruction following capability. However, the model's performance is highly dependent on the open-ended characteristics of the users' input prompt. Natural prompts often do not follow proper syntactic rules, which creates ambiguous queries that yield multiple interpretations. Such ambiguous prompts confuse the model in choosing the correct reasoning paths to answer questions. Prior works address this challenge by applying query editing during the LLM inference process without explicitly solving the root cause of the ambiguity. To address this limitation, we propose a pre-inference prompt optimization mechanism via explicit prompt disambiguation. Particularly, we identify semantic risks in the prompt, check their multi-perspective consistency, and resolve any semantic conflicts that arise. Finally, we organize the resolved ambiguities in a logically structured manner as a clean input to the LLM. By explicitly resolving semantic ambiguity, our method can produce a more focused attention distribution to the semantically essential tokens. We also leverage small language models (SLMs) as the main executor of prompt disambiguation to benefit from their efficient computation. Through comprehensive experiments on multiple benchmarks, we demonstrate that our method improves reasoning performance by 2.5 points at a cost of only \$0.02. Our study promotes explicit prompt disambiguation as an effective prompt optimization method without disturbing the internal mechanism of LLM inference.

---


### 60. [Fine-tuning vs. In-context Learning in Large Language Models: A Formal Language Learning Perspective](https://arxiv.org/abs/2604.23267)

**<font color=#1a73e8>作者：</font>** Bishwamittra Ghosh, Soumi Das, Till Speicher 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) operate in two fundamental learning modes - fine-tuning (FT) and in-context learning (ICL) - raising key questions about which mode yields greater language proficiency and whether they differ in their inductive biases. Prior studies comparing FT and ICL have yielded mixed and inconclusive results due to inconsistent experimental setups. To enable a rigorous comparison, we propose a formal language learning task - offering precise language boundaries, controlled string sampling, and no data contamination - and introduce a discriminative test for language proficiency, where an LLM succeeds if it assigns higher generation probability to in-language strings than to out-of-language strings.
Empirically, we find that: (a) FT has greater language proficiency than ICL on in-distribution generalization, but both perform equally well on out-of-distribution generalization. (b) Their inductive biases, measured by the correlation in string generation probabilities, are similar when both modes partially learn the language but diverge at higher proficiency levels. (c) Unlike FT, ICL performance differs substantially across models of varying sizes and families and is sensitive to the token vocabulary of the language. Thus, our work demonstrates the promise of formal languages as a controlled testbed for evaluating LLMs, behaviors that are difficult to isolate in natural language datasets. Our source code is available at this https URL.

---


### 61. [CAP-CoT: Cycle Adversarial Prompt for Improving Chain of Thoughts in LLM Reasoning](https://arxiv.org/abs/2604.23270)

**<font color=#1a73e8>作者：</font>** Shuxu Chen, Yitian Zhou, Jiaquan Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Chain-of-Thought (CoT) prompting has emerged as a simple and effective way to elicit step-by-step solutions from large language models (LLMs). However, CoT reasoning can be unstable across runs on long, multi-step problems, leading to inconsistent answers for unchanged task. Most prior work focuses on improving the forward reasoning chain within a single pass, with less attention to iterative and contrastive correction. To address this gap, we propose CAP-CoT, a Cycle Adversarial Prompt optimization framework designed to improve both CoT reasoning accuracy and stability of a single deployed solver. In each cycle, a forward solver generates candidate reasoning chains, an adversarial challenger constructs plausible but deliberately flawed chains using targeted error strategies, and a feedback agent contrasts the two chains and produces step-aligned structured feedback. This feedback closes the optimization loop in two directions, including updating the solver prompt based on errors exposed by the challenger, and updating the challenger prompt to generate increasingly targeted errors in subsequent cycles. Unlike safety-oriented adversarial prompting such as jailbreak or prompt-injection attacks, our adversarial component is task-semantic and aims to expose logical vulnerabilities in reasoning chains. Experiments across six benchmarks and four LLM backbones demonstrate that within two to three adversarial prompt optimization cycles, CAP-CoT consistently reduces variability across runs while improving reasoning accuracy and robustness to prompt perturbations.

---


### 62. [SemiGDA: Generative Dual-distribution Alignment for Semi-Supervised Medical Image Segmentation](https://arxiv.org/abs/2604.23274)

**<font color=#1a73e8>作者：</font>** Kaiwen Huang, Yi Zhou, Yizhe Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Semi-supervised learning addresses label scarcity and high annotation costs in medical image segmentation by exploiting the latent information in unlabeled data to enhance model performance. Traditional discriminative segmentation relies on segmentation masks, neglecting feature-level distribution constraints. This limits robust semantic representation learning and adaptive modeling of unlabeled data in scenarios with few labels. To address these limitations, we propose SemiGDA, a novel Generative Dual-distribution Alignment framework for semi-supervised medical image segmentation. Our SemiGDA overcomes the reliance of discriminative methods on large labeled datasets by aligning feature and semantic distributions to boost semantic learning and scene adaptability. Specifically, we propose a Dual-distribution Alignment Module (DAM), which employs two structurally distinct encoders to model image and mask feature distributions. It enforces their alignment in the latent space via distributional constraints, establishing structured feature consistency. Moreover, we design a Consistency-Driven Skip Adapter (CDSA) strategy, which introduces dual skip adapters (Image and Mask) to fuse multi-scale features via skip connections. Using a consistency loss, CDSA enhances cross-branch semantic alignment and reinforces fine-grained semantic consistency. Experimental results on diverse medical datasets show that our method outperforms other state-of-the-art semi-supervised segmentation methods. Code is released at: this https URL.

---


### 63. [Lightweight and Production-Ready PDF Visual Element Parsing](https://arxiv.org/abs/2604.23276)

**<font color=#1a73e8>作者：</font>** Meizhu Liu, Yassi Abbasi, Matthew Rowe 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> PDF documents contain critical visual elements such as figures, tables, and forms whose accurate extraction is essential for document understanding and multimodal retrieval-augmented generation (RAG). Existing PDF parsers often miss complex visuals, extract non-informative artifacts (e.g., watermarks, logos), produce fragmented elements, and fail to reliably associate captions with their corresponding elements, which degrades downstream retrieval and question answering. We present a lightweight and production level PDF parsing framework that can accurately detect visual elements and associates captions using a combination of spatial heuristics, layout analysis, and semantic similarity. On popular benchmark datasets and internal product data, the proposed solution achieves $\geq96\%$ visual element detection accuracy and $93\%$ caption association accuracy. When used as a preprocessing step for multimodal RAG, it significantly outperforms state-of-the-art parsers and large vision-language models on both internal data and the MMDocRAG benchmark, while reducing latency by over $2\times$. We have deployed the proposed system in challenging production environment.

---


### 64. [From Similarity to Structure: Training-free LLM Context Compression with Hybrid Graph Priors](https://arxiv.org/abs/2604.23277)

**<font color=#1a73e8>作者：</font>** Yitian Zhou, Chaoning Zhang, Jiaquan Zhang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-context large language models remain computationally expensive to run and often fail to reliably process very long inputs, which makes context compression an important component of many systems. Existing compression approaches typically rely on trained compressors, dense retrieval-style selection, or heuristic trimming, and they often struggle to jointly preserve task relevance, topic coverage, and cross-sentence coherence under a strict token budget. To address this, we propose a training-free and model-agnostic compression framework that selects a compact set of sentences guided by structural graph priors. Our method constructs a sparse hybrid sentence graph that combines mutual k-NN semantic edges with short-range sequential edges, extracts a topic skeleton via clustering, and ranks sentences using an interpretable score that integrates task relevance, cluster representativeness, bridge centrality, and a cycle coverage cue. A budgeted greedy selection with redundancy suppression then produces a readable compressed context in original order. Experimental results on four datasets show that our approach is competitive with strong extractive and abstractive baselines, demonstrating larger gains on long-document benchmarks.

---


### 65. [Contrastive Learning for Multimodal Human Activity Recognition with Limited Labeled Data](https://arxiv.org/abs/2604.23281)

**<font color=#1a73e8>作者：</font>** Long Jing, Zhixiong Yang, Yajun Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Human activity recognition serves as the foundation for various emerging applications. In recent years, researchers have used collaborative sensing of multi-source sensors to capture complex and dynamic human activities. However, multimodal human activity sensing typically encounters highly heterogeneous data across modalities and label scarcity, resulting in an application gap between existing solutions and real-world needs. In this paper, we propose CLMM, a general contrastive learning framework for human activity recognition that achieves effective multimodal recognition with limited labeled data.
CLMM employs a novel two-stage training strategy. In the first stage, CLMM employs a CNN-DiffTransformer encoder to capture cross-modal shared information by extracting local and global features. Meanwhile, a hard-positive samples weighting algorithm enhances gradient propagation to reinforce shared learning. In the second stage, a dual-branch architecture combining quality-guided attention and bidirectional gated units captures modality-specific information, while a primary-auxiliary collaborative training strategy fuses both shared and modality-specific information. Experimental results on three public datasets demonstrate that CLMM significantly improves state-of-the-art baselines in both recognition accuracy and convergence performance.

---


### 66. [Bridging the Pose-Semantic Gap: A Cascade Framework for Text-Based Person Anomaly Search](https://arxiv.org/abs/2604.23282)

**<font color=#1a73e8>作者：</font>** Zequn Xie, Guijin Luo, Chuxin Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-based person anomaly search retrieves specific behavioral events from surveillance archives using natural-language queries. Although recent pose-aware methods align geometric structures well, they face a fundamental Pose-Semantic Gap: semantically different actions can share similar skeletal geometries. While Multimodal Large Language Models (MLLMs) can reduce this ambiguity, using them for large-scale retrieval is computationally prohibitive. We propose the Structure-Semantic Decoupled Cascade (SSDC) framework, which decouples retrieval into two stages: (1) Structure-Aware Coarse Retrieval, where a lightweight model quickly filters candidates by skeletal similarity ; and (2) Detective Squad Interaction, a multi-agent semantic verification module. The squad consists of a Detective for fast binary filtering, an Analyst for evidence extraction, and a Writer for semantic synthesis. Finally, we re-rank candidates by fusing the synthesized captions with structural priors. Experiments on the PAB benchmark show that SSDC achieves state-of-the-art performance by balancing efficiency and semantic reasoning.

---


### 67. [Revisable by Design: A Theory of Streaming LLM Agent Execution](https://arxiv.org/abs/2604.23283)

**<font color=#1a73e8>作者：</font>** Zhiyuan Zhai, Ming Li, Xin Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Current LLM agents operate under an implicit but universal assumption: execution is a transaction -- the user submits a request, the agent works in isolation, and only upon completion does the dialogue resume. This forces users into a binary choice: wait for a potentially incorrect output, or interrupt and lose all progress. We reject this assumption and propose the stream paradigm, in which agent execution and user intervention are concurrent, interleaved processes sharing a bidirectional channel. We formalize this paradigm through a reversibility taxonomy that classifies every agent action as Idempotent, Reversible, Compensable, or Irreversible, and arrive at a core conclusion: an agent's flexibility is bounded by its reversibility. We prove that conflicting compensable actions impose unavoidable adaptation costs and that conflicting irreversible actions make full specification satisfaction impossible -- these costs are properties of the action space, not of the algorithm. Guided by this insight, we present the Revision Absorber, a reactive algorithm based on the Earliest-Conflict Rollback rule that is structurally optimal under mild assumptions. Experiments on StreamBench with real LLM agents validate all predictions: the Absorber matches the quality of a brute-force full-restart baseline while wasting an order of magnitude fewer steps of already-completed work, turning mid-execution revisions from a dead-end into a first-class interaction.

---


### 68. [Au-M-ol: A Unified Model for Medical Audio and Language Understanding](https://arxiv.org/abs/2604.23284)

**<font color=#1a73e8>作者：</font>** Meizhu Liu, Nistha Mitra, Paul Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In this work, we present Au-M-ol, a novel multimodal architecture that extends Large Language Models (LLMs) with audio processing. It is designed to improve performance on clinically relevant tasks such as Automatic Speech Recognition (ASR). Au-M-ol has three main components: (1) an audio encoder that extracts rich acoustic features from medical speech, (2) an adaptation layer that maps audio features into the LLM input space, and (3) a pretrained LLM that performs transcription and clinical language understanding. This design allows the model to interpret spoken medical content directly, improving both accuracy and robustness. In experiments, Au-M-ol reduces Word Error Rate (WER) by 56\% compared to state-of-the-art baselines on medical transcription tasks. The model also performs well in challenging conditions, including noisy environments, domain-specific terminology, and speaker variability. These results suggest that Au-M-ol is a strong candidate for real-world clinical applications, where reliable and context-aware audio understanding is essential.

---


### 69. [$\mathcal{S}^2$IT: Stepwise Syntax Integration Tuning for Large Language Models in Aspect Sentiment Quad Prediction](https://arxiv.org/abs/2604.23296)

**<font color=#1a73e8>作者：</font>** Bingfeng Chen, Chenjie Qiu, Yifeng Xie 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Aspect Sentiment Quad Prediction (ASQP) has seen significant advancements, largely driven by the powerful semantic understanding and generative capabilities of large language models (LLMs). However, while syntactic structure information has been proven effective in previous extractive paradigms, it remains underutilized in the generative paradigm of LLMs due to their limited reasoning capabilities. In this paper, we propose S^2IT, a novel Stepwise Syntax Integration Tuning framework that progressively integrates syntactic structure knowledge into LLMs through a multi-step tuning process. The training process is divided into three steps. S^2IT decomposes the quadruple generation task into two stages: 1) Global Syntax-guided Extraction and 2) Local Syntax-guided Classification, integrating both global and local syntactic structure information. Finally, Fine-grained Structural Tuning enhances the model's understanding of syntactic structures through the prediction of element links and node classification. Experiments demonstrate that S^2IT significantly improves state-of-the-art performance across multiple datasets. Our implementation will be open-sourced at this https URL.

---


### 70. [Process Supervision of Confidence Margin for Calibrated LLM Reasoning](https://arxiv.org/abs/2604.23333)

**<font color=#1a73e8>作者：</font>** Liaoyaqi Wang, Chunsheng Zuo, William Jurayj 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Scaling test-time computation with reinforcement learning (RL) has emerged as a reliable path to improve large language models (LLM) reasoning ability. Yet, outcome-based reward often incentivizes models to be overconfident, leading to hallucinations, unreliable confidence-based control, and unnecessary compute allocation. We introduce Reinforcement Learning with Confidence Margin (\textbf{RLCM}), a calibration-aware RL framework that jointly optimizes correctness and confidence reliability via a margin-enhanced process reward over intermediate-budget completions. Rather than aligning confidence to correctness likelihoods, RLCM encourages to widen the confidence margin between correct and incorrect steps within a single reasoning trajectory. Across mathematical, code, logic and science benchmarks, our method substantially improves calibration while maintaining or improving accuracy. We further show that, with calibrated confidence signals, the resulting models enable more efficient conformal risk control and effective confidence-weighted aggregation.

---


### 71. [Bridging Reasoning and Action: Hybrid LLM-RL Framework for Efficient Cross-Domain Task-Oriented Dialogue](https://arxiv.org/abs/2604.23345)

**<font color=#1a73e8>作者：</font>** Yangyang Zhao, Linfan Dai, Li Cai 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Cross-domain task-oriented dialogue requires reasoning over implicit and explicit feasibility constraints while planning long-horizon, multi-turn actions. Large language models (LLMs) can infer such constraints but are unreliable over long horizons, while Reinforcement learning (RL) optimizes long-horizon behavior yet cannot recover constraints from raw dialogue. Naively coupling LLMs with RL is therefore brittle: unverified or unstructured LLM outputs can corrupt state representations and misguide policy learning. Motivated by this, we propose Verified LLM-Knowledge empowered RL (VLK-RL), a hybrid framework that makes LLM-derived constraint reasoning usable for RL. VLK-RL first elicits candidate constraints with an LLM and then verifies them via a dual-role cross-examination procedure to suppress hallucinations and cross-turn inconsistencies. The verified constraints are mapped into ontology-aligned slot-value representations, yielding a structured, constraint-aware state for RL policy optimization. Experiments across multiple benchmarks demonstrate that VLK-RL significantly improves generalization and robustness, outperforming strong single-model baselines on long-horizon tasks.

---


### 72. [Evaluating Large Language Models on Computer Science University Exams in Data Structures](https://arxiv.org/abs/2604.23347)

**<font color=#1a73e8>作者：</font>** Edan Gabay, Yael Maoz, Jonathan Stahl 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present a comprehensive evaluation of Large Language Models (LLMs) on Computer Science (CS) Data Structure examination questions. Our work introduces a new benchmark dataset comprising exam questions from Tel Aviv University (TAU), curated to assess LLMs' abilities in handling closed and multiple-choice questions. We evaluated the performance of OpenAI's GPT 4o and Anthropic's Claude 3.5, popular LLMs, alongside two smaller LLMs, Mathstral 7B and LLaMA 3 8B, across the TAU exams benchmark. Our findings provide insight into the current capabilities of LLMs in CS education.

---


### 73. [EmoTrans: A Benchmark for Understanding, Reasoning, and Predicting Emotion Transitions in Multimodal LLMs](https://arxiv.org/abs/2604.23348)

**<font color=#1a73e8>作者：</font>** He Hu, Tengjin Weng, Zebang Cheng 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent multimodal large language models (MLLMs) have shown strong capabilities in perception, reasoning, and generation, and are increasingly used in applications such as social robots and human-computer interaction, where understanding human emotions is essential. However, existing benchmarks mainly formulate emotion understanding as a static recognition problem, leaving it largely unclear whether current MLLMs can understand emotion as a dynamic process that evolves, shifts between states, and unfolds across diverse social contexts. To bridge this gap, we present EmoTrans, a benchmark for evaluating emotion dynamics understanding in multimodal videos. EmoTrans contains 1,000 carefully collected and manually annotated video clips, covering 12 real-world scenarios, and further provides over 3,000 task-specific question-answer (QA) pairs for fine-grained evaluation. The benchmark introduces four tasks, namely Emotion Change Detection (ECD), Emotion State Identification (ESI), Emotion Transition Reasoning (ETR), and Next Emotion Prediction (NEP), forming a progressive evaluation framework from coarse-grained detection to deeper reasoning and prediction. We conduct a comprehensive evaluation of 18 state-of-the-art MLLMs on EmoTrans and obtain two main findings. First, although current MLLMs show relatively stronger performance on coarse-grained emotion change detection, they still struggle with fine-grained emotion dynamics modeling. Second, socially complex settings, especially multi-person scenarios, remain substantially challenging, while reasoning-oriented variants do not consistently yield clear improvements. To facilitate future research, we publicly release the benchmark, evaluation protocol, and code at this https URL.

---


### 74. [LEGO: An LLM Skill-Based Front-End Design Generation Platform](https://arxiv.org/abs/2604.23355)

**<font color=#1a73e8>作者：</font>** Jincheng Lou, Ruohan Xu, Jiecheng Ma 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Existing LLM-based EDA agents are often isolated task-specific systems. This leads to repeated engineering effort and limited reuse of successful design and debugging strategies. We present LEGO, a unified skill-based platform for front-end design generation. It decomposes the digital front-end flow into six independent steps and represents every agent capability as a standardized composable circuit skill within a plug-and-play architecture. To build this skill library, we survey more than 100 papers, select 11 representative open-source projects, and extract 42 executable circuit skills within a six-step finite state machine formulation. Circuit Skill Builder automates skill extraction with linear scalability. Agent Skill RAG achieves submillisecond retrieval without relying on embedding models. Empirical evaluation on a hard subset of 41 VerilogEval v2 problems that gpt-5.2-codex fails to solve under extra-high reasoning effort shows that individual circuit skills constructed within LEGO raise Pass@1 from 0.000 to 0.805. This is an 80.5% gain over the baseline. Cross-project skill compositions also reach 0.805 Pass@1. They outperform hierarchy-verilog by 14.6% and VerilogCoder by 2.5%. They also match MAGE. These results show that modular skill composition supports both effective and flexible RTL design automation. The LEGO platform and all circuit skills are publicly available at GitHub: this https URL

---


### 75. [VeriLLMed: Interactive Visual Debugging of Medical Large Language Models with Knowledge Graphs](https://arxiv.org/abs/2604.23356)

**<font color=#1a73e8>作者：</font>** Yurui Xiang, Xingyi Mao, Rui Sheng 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) show promise in medical diagnosis, but real-world deployment remains challenging due to high-stakes clinical decisions and imperfect reasoning reliability. As a result, careful inspection of model behavior is essential for assessing whether diagnostic reasoning is reliable and clinically grounded. However, debugging medical LLMs remains difficult. First, developers often lack sufficient medical domain expertise to interpret model errors in clinically meaningful terms. Second, models can fail across a large and diverse set of instances involving different input types, tasks, and reasoning steps, making it challenging for developers to prioritize which errors deserve focused inspection. Third, developers struggle to identify recurring error patterns across cases, as existing debugging practices are largely instance-centric and rely on manual inspection of isolated failures. To address these challenges, we present VeriLLMed, a visual analytics system that integrates external biomedical knowledge to audit and debug medical LLM diagnostic reasoning. VeriLLMed transforms model outputs into comparable reasoning paths, constructs knowledge graph-grounded reference paths, and identifies three recurring classes of diagnosis errors: relation errors, branch errors, and missing errors. Case studies and expert evaluation demonstrate that VeriLLMed helps developers identify clinically implausible reasoning and generate actionable insights that can inform the improvement of medical LLMs.

---


### 76. [GSAR: Typed Grounding for Hallucination Detection and Recovery in Multi-Agent LLMs](https://arxiv.org/abs/2604.23366)

**<font color=#1a73e8>作者：</font>** Federico A. Kamelhar  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Autonomous multi-agent LLM systems are increasingly deployed to investigate operational incidents and produce structured diagnostic reports. Their trustworthiness hinges on whether each claim is grounded in observed evidence rather than model-internal inference. Existing groundedness evaluators (binary classifiers, LLM-as-judge scalars, self-correction loops) treat supporting evidence as interchangeable and emit a single signal that offers no principled control over downstream action.
We present GSAR, a grounding-evaluation and replanning framework that (i) partitions claims into a four-way typology (grounded, ungrounded, contradicted, complementary), giving first-class standing to non-redundant alternative perspectives; (ii) assigns evidence-type-specific weights reflecting epistemic strength; (iii) computes an asymmetric contradiction-penalised weighted groundedness score; and (iv) couples that score to a three-tier decision function (proceed, regenerate, replan) driving a bounded-iteration outer loop under an explicit compute budget.
We formalise the algorithm, prove six structural properties, and evaluate five design claims on FEVER with gold Wikipedia evidence under four independently-trained LLM judges (gpt-5.4, claude-sonnet-4-6, claude-opus-4-7, gemini-2.5-pro). Every ablation reproduces in the same direction on every judge: bootstrap 95% CIs on the rho=0 effect exclude 0 on all four; the no-complementary ablation under Opus 4.7 has CI [-96,-68] of 200; at n=1000 three independent judges converge to DeltaS(rho=0)=+0.058. A head-to-head against Vectara HHEM-2.1-Open is included. To our knowledge, GSAR is the first published groundedness framework coupling evidence-typed scoring with tiered recovery under an explicit compute budget.

---


### 77. [When Context Sticks: Studying Interference in In-Context Learning](https://arxiv.org/abs/2604.23371)

**<font color=#1a73e8>作者：</font>** Hanna Rød, Dagny Streit, Nils Valseth Selte 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper investigates context stickiness in in-context learning (ICL), a phenomenon where earlier examples in a prompt interfere with a transformer's ability to adapt to later tasks. Using synthetic regression tasks over linear and quadratic functions, we examine how models trained under sequential, mixed, and random curricula handle abrupt task switches during inference. By sweeping over structured combinations of misleading linear examples followed by recovery quadratic examples, we quantify how prior context biases prediction error and how quickly models realign. Our results show strong evidence of persistent interference: more preceding linear examples reliably degrade quadratic predictions, while additional quadratic examples reduce error but with diminishing returns. We further find that training curricula significantly modulate resilience, with sequential training on the target function class yielding the fastest recovery, and surprisingly, random training producing the least robust behavior.

---


### 78. [Domain-Adapted Fine-Tuning of ECG Foundation Models for Multi-Label Structural Heart Disease Screening](https://arxiv.org/abs/2604.23385)

**<font color=#1a73e8>作者：</font>** Duc N. Do, Minh N. Do, Dang Nguyen 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Transthoracic echocardiography is the reference standard for confirming structural heart disease (SHD), but first-line screening is limited by cost, workflow burden, and specialist availability. We evaluated whether open pretrained electrocardiogram (ECG) foundation models can support echo-confirmed multi-label SHD detection using the public EchoNext Mini-Model benchmark. Six echocardiography-derived abnormalities were targeted: reduced left ventricular ejection fraction, increased left ventricular wall thickness, aortic stenosis, mitral regurgitation, tricuspid regurgitation, and right ventricular systolic dysfunction. Under a common pipeline, we compared engineered ECG features with gradient boosting, end-to-end waveform learning from scratch, and transfer from open ECG foundation models. We then applied in-domain self-supervised adaptation of an ECG foundation model (ECG-FM) on EchoNext waveforms followed by selective supervised fine-tuning, and evaluated trade-offs between discrimination and adaptation cost. Adapted ECG-FM models achieved the best overall performance: peak macro-AUROC 0.8509 and macro-AUPRC 0.4297, while a parameter-efficient operating point preserved AUROC (0.8501) and attained the highest fixed-threshold macro-F1 0.3691. Late fusion with covariates did not improve threshold-independent discrimination, and evaluated LoRA, alternative backbones, and mixture-of-foundations strategies did not surpass the best adapted single-backbone models. These results indicate that for ECG-based case finding and echocardiography triage, combining target-domain self-supervised adaptation with selective supervised updating of a pretrained ECG backbone is the most effective transfer strategy.

---


### 79. [SoccerRef-Agents: Multi-Agent System for Automated Soccer Refereeing](https://arxiv.org/abs/2604.23392)

**<font color=#1a73e8>作者：</font>** Zi Meng, Wanli Song, Yi Hu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Refereeing is vital in sports, where fair, accurate, and explainable decisions are fundamental. While intelligent assistant technologies are being widely adopted in soccer refereeing, current AI-assisted approaches remain preliminary. Existing research mostly focuses on isolated video perception tasks and lacks the ability to understand and reason about foul scenarios. To fill this gap, we propose SoccerRef-Agents, a holistic and explainable multi-agent decision-making framework for soccer refereeing. The main contributions are: (i) constructing the multimodal benchmark SoccerRefBench with over 1,200 referee theory questions and 600 foul video clips; (ii) building a vector-based knowledge base RefKnowledgeDB using the latest "Laws of the Game" and a classic case database for precise, knowledge-driven reasoning; (iii) designing a novel multi-agent architecture that collaborates via cross-modal RAG to bridge the semantic gap between visual content and regulatory texts. This work explores the technical capability of integrating MLLMs with refereeing expertise, and evaluations show our system significantly outperforms general-purpose MLLMs in decision accuracy and explanation quality. All databases, benchmarks, and code will be made available.

---


### 80. [When Corrective Hints Hurt: Prompt Design in Reasoner-Guided Repair of LLM Overcaution on Entailed Negations under OWL~2~DL](https://arxiv.org/abs/2604.23398)

**<font color=#1a73e8>作者：</font>** Yijiashun Qi, Xiang Xu, Yuxuan Li  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We report a reproducible error pattern in GPT-5.4 on OWL~2~DL compliance queries: the model frequently answers ``unknown'' when the reasoner-entailed answer is ``no'' under \emph{FunctionalProperty} closure or class \emph{disjointness}. Using 180 reasoner-audited queries from a procedural expansion of the observed pattern plus 18 hand-authored held-out queries in two unrelated domains (insurance and clinical), we compare four interaction modes under matched query budget: single-shot, three rounds of generic ``you-are-wrong'' retry, three rounds of reasoner-verdict repair with an open-world-assumption (OWA) hint, and the same repair without the hint. Direct faithfulness is 43.9\,\% (Wilson 95\,\% CI $[36.8,51.2]$); generic retry reaches 81.7\,\% ($[75.4,86.6]$); the verdict-with-hint variant is \emph{worse} at 67.2\,\% ($[60.1,73.7]$); the verdict-only variant reaches 97.8\,\% ($[94.4,99.1]$). All pairwise comparisons remain significant under McNemar's exact test with Bonferroni correction ($\alpha = 0.01$; all $p < 10^{-5}$). The same fingerprint accounts for 4/4 errors on the held-out queries. Our interpretation is bounded: prompt framing can matter more than corrective content, and reasoner-guided wrappers should be ablated explicitly.

---


### 81. [Beyond Local vs. External: A Game-Theoretic Framework for Trustworthy Knowledge Acquisition](https://arxiv.org/abs/2604.23413)

**<font color=#1a73e8>作者：</font>** Rujing Yao, Yufei Shi, Yang Wu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Cloud-hosted Large Language Models (LLMs) offer unmatched reasoning capabilities and dynamic knowledge, yet submitting raw queries to these external services risks exposing sensitive user intent. Conversely, relying exclusively on trusted local models preserves privacy but often compromises answer quality due to limited parameter scale and knowledge. To resolve this dilemma, we propose Game-theoretic Trustworthy Knowledge Acquisition (GTKA), a framework that formulates the trade-off between knowledge utility and privacy as a strategic game. GTKA consists of three components: (i) a privacy-aware sub-query generator that decomposes sensitive intent into generalized, low-risk fragments; (ii) an adversarial reconstruction attacker that attempts to infer the original query from these fragments, providing adaptive leakage signals; and (iii) a trusted local integrator that synthesizes external responses within a secure boundary. By training the generator and attacker in an alternating adversarial manner, GTKA optimizes the sub-query generation policy to maximize knowledge acquisition accuracy while minimizing the reconstructability of the original sensitive intent. To validate our approach, we construct two sensitive-domain benchmarks in the biomedical and legal fields. Extensive experiments demonstrate that GTKA significantly reduces intent leakage compared to state-of-the-art baselines while maintaining high-fidelity answer quality.

---


### 82. [Evolve: A Persistent Knowledge Lifecycle for Small Language Models](https://arxiv.org/abs/2604.23424)

**<font color=#1a73e8>作者：</font>** Dikran Hovagimian  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Evolve pairs a small local language model with a persistent, teacher-compiled knowledge store -- refined through sleep consolidation and usage-driven refresh -- to deliver substantial accuracy gains over the model's parametric baseline while amortizing teacher costs through cross-query knowledge reuse. Rather than retrieving document fragments at query time, Evolve constructs a store of semantically coherent sections compiled by teacher models at natural conceptual boundaries; new sections are staged on acquisition, consolidated offline through teacher-mediated merging, and refreshed inline when expired. A 2B-parameter local model handles classification and generation; large teacher models are invoked only for knowledge operations.
Across 750 benchmark queries spanning custom specialist questions, NaturalQuestions, and TriviaQA, the 2B model augmented by Evolve improves from 20-33% baseline accuracy to 60-84% (+40-52pp) while reducing teacher invocations by over 50% through reuse. Post-consolidation compresses the knowledge store by 31-33.5% across three independent benchmarks while preserving accuracy; section-based retrieval outperforms chunk-based retrieval by 5-9pp across every lifecycle condition. The architecture supports two generation modes over the same lifecycle -- suppress (strict section-only grounding, auditable) and augment (section-supplemented responses).

---


### 83. [Revisiting Greedy Decoding for Visual Question Answering: A Calibration Perspective](https://arxiv.org/abs/2604.23443)

**<font color=#1a73e8>作者：</font>** Boqi Chen, Xudong Liu, Yunke Ao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Stochastic sampling strategies are widely adopted in large language models (LLMs) to balance output coherence and diversity. These heuristics are often inherited in Multimodal LLMs (MLLMs) without task-specific justification. However, we contend that stochastic decoding can be suboptimal for Visual Question Answering (VQA). VQA is a closed-ended task with head-heavy answer distributions where uncertainty is usually epistemic, arising from missing or ambiguous visual evidence rather than plausible continuations. In this work, we provide a theoretical formalization of the relationship between model calibration and predictive accuracy, and derive the sufficient conditions for greedy decoding optimality. Extensive experiments provide empirical evidence for the superiority of greedy decoding over stochastic sampling across multiple benchmarks. Furthermore, we propose Greedy Decoding for Reasoning Models, which outperforms both stochastic sampling and standard greedy decoding in multimodal reasoning scenarios. Overall, our results caution against naively inheriting LLMs decoding heuristics in MLLMs and demonstrate that greedy decoding can be an efficient yet strong default for VQA.

---


### 84. [AI Safety Training Can be Clinically Harmful](https://arxiv.org/abs/2604.23445)

**<font color=#1a73e8>作者：</font>** Suhas BN, Andrew M. Sherrill, Rosa I. Arriaga 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models are being deployed as mental health support agents at scale, yet only 16% of LLM-based chatbot interventions have undergone rigorous clinical efficacy testing, and simulations reveal psychological deterioration in over one-third of cases. We evaluate four generative models on 250 Prolonged Exposure (PE) therapy scenarios and 146 CBT cognitive restructuring exercises (plus 29 severity-escalated variants), scored by a three-judge LLM panel. All models scored near-perfectly on surface acknowledgment (~0.91-1.00) while therapeutic appropriateness collapsed to 0.22-0.33 at the highest severity for three of four models, with protocol fidelity reaching zero for two. Under CBT severity escalation, one model's task completeness dropped from 92% to 71% while the frontier model's safety-interference score fell from 0.99 to 0.61. We identify a systematic, modality-spanning failure: RLHF safety alignment disrupts the therapeutic mechanism of action by grounding patients during imaginal exposure, offering false reassurance, inserting crisis resources into controlled exercises, and refusing to challenge distorted cognitions mentioning self-harm in PE; and through task abandonment or safety-preamble insertion during CBT cognitive restructuring. These findings motivate a five-axis evaluation framework (protocol fidelity, hallucination risk, behavioral consistency, crisis safety, demographic robustness), mapped onto FDA SaMD and EU AI Act requirements. We argue that no AI mental health system should proceed to deployment without passing multi-axis evaluation across all five dimensions.

---


### 85. [Ulterior Motives: Detecting Misaligned Reasoning in Continuous Thought Models](https://arxiv.org/abs/2604.23460)

**<font color=#1a73e8>作者：</font>** Sharan Ramjee  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Chain-of-Thought (CoT) reasoning has emerged as a key technique for eliciting complex reasoning in Large Language Models (LLMs). Although interpretable, its dependence on natural language limits the model's expressive bandwidth. Continuous thought models address this bottleneck by reasoning in latent space rather than human-readable tokens. While they enable richer representations and faster inference, they raise a critical safety question: how can we detect misaligned reasoning in an uninterpretable latent space? To study this, we introduce MoralChain, a benchmark of 12,000 social scenarios with parallel moral/immoral reasoning paths. We train a continuous thought model with backdoor behavior using a novel dual-trigger paradigm - one trigger that arms misaligned latent reasoning ([T]) and another that releases harmful outputs ([O]). We demonstrate three findings: (1) continuous thought models can exhibit misaligned latent reasoning while producing aligned outputs, with aligned and misaligned reasoning occupying geometrically distinct regions of latent space; (2) linear probes trained on behaviorally-distinguishable conditions ([T][O] vs [O]) transfer to detecting armed-but-benign states ([T] vs baseline) with high accuracy; and (3) misalignment is encoded in early latent thinking tokens, suggesting safety monitoring for continuous thought models should target the "planning" phase of latent reasoning.

---


### 86. [Hybrid JIT-CUDA Graph Optimization for Low-Latency Large Language Model Inference](https://arxiv.org/abs/2604.23467)

**<font color=#1a73e8>作者：</font>** Divakar Kumar Yadav, Tian Zhao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have achieved strong performance across natural language and multimodal tasks, yet their practical deployment remains constrained by inference latency and kernel launch overhead, particularly in interactive, short-sequence settings. This paper presents a hybrid runtime framework that combines Just-In-Time (JIT) compilation with CUDA Graph execution to reduce launch overhead while preserving runtime flexibility during autoregressive decoding. The framework partitions transformer inference into static components executed via CUDA Graph replay and dynamic components handled through JIT-compiled kernels, enabling asynchronous graph capture and reuse across decoding steps.
We evaluate the proposed approach on LLaMA-2 7B using single-GPU, batch-size-one inference across prompt lengths from 10 to 500 tokens. Experimental results show that the hybrid runtime reduces Time-to-First-Token (TTFT) by up to 66.0% and achieves lower P99 latency compared with TensorRT-LLM in this regime. These results indicate that hybrid JIT-CUDA Graph execution can effectively reduce inference latency and variance for short-sequence LLM workloads, making it a practical optimization strategy for latency-sensitive AI applications.

---


### 87. [Supernodes and Halos: Loss-Critical Hubs in LLM Feed-Forward Layers](https://arxiv.org/abs/2604.23475)

**<font color=#1a73e8>作者：</font>** Audrey Cherilyn, Houman Safaai  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study the organization of channel-level importance in transformer feed-forward networks (FFNs). Using a Fisher-style loss proxy (LP) based on activation-gradient second moments, we show that loss sensitivity is concentrated in a small set of channels within each layer. In Llama-3.1-8B, the top 1% of channels per layer accounts for a median of 58.7% of LP mass, with a range of 33.0% to 86.1%. We call these loss-critical channels supernodes. Although FFN layers also contain strong activation outliers, LP-defined supernodes overlap only weakly with activation-defined outliers and are not explained by activation power or weight norms alone. Around this core, we find a weaker but consistent halo structure: some non-supernode channels share the supernodes' write support and show stronger redundancy with the protected core. We use one-shot structured FFN pruning as a diagnostic test of this organization. At 50% FFN sparsity, baselines that prune many supernodes degrade sharply, whereas our SCAR variants explicitly protect the supernode core; the strongest variant, SCAR-Prot, reaches perplexity 54.8 compared with 989.2 for Wanda-channel. The LP-concentration pattern appears across Mistral-7B, Llama-2-7B, and Qwen2-7B, remains visible in targeted Llama-3.1-70B experiments, and increases during OLMo-2-7B pretraining. These results suggest that LLM FFNs develop a small learned core of loss-critical channels, and that preserving this core is important for reliable structured pruning.

---


### 88. [JudgeSense: A Benchmark for Prompt Sensitivity in LLM-as-a-Judge Systems](https://arxiv.org/abs/2604.23478)

**<font color=#1a73e8>作者：</font>** Rohith Reddy Bellibatlu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly deployed as automated judges for evaluating other models, yet the stability of their verdicts under semantically equivalent prompt paraphrases remains unmeasured. We introduce JudgeSense, a framework and benchmark for quantifying this property via the Judge Sensitivity Score (JSS), defined as the fraction of paraphrase pairs on which a judge returns an identical decision.
Evaluating nine judge models on 494 validated paraphrase pairs, we find that coherence is the only task where judges meaningfully differ, with JSS ranging from 0.389 to 0.992. On factuality, all judges cluster near JSS about 0.63, driven by a polarity-inverted prompt artifact; after correction, factuality JSS rises to about 0.9. Pairwise tasks (preference and relevance) exhibit degenerate always-A behavior in 8 of 9 judges, indicating strong position bias.
Model scale does not predict consistency. We release code, decision logs, and a validated paraphrase dataset to support standardized JSS reporting.

---


### 89. [Leveraging Spatial Transcriptomics as Alternative to Manual Annotations for Deep Learning-Based Nuclei Analysis](https://arxiv.org/abs/2604.23481)

**<font color=#1a73e8>作者：</font>** Kazuya Nishimura, Ryoma Bise, Haruka Hirose 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep learning-based nuclei segmentation and classification in pathology images typically rely on large-scale pixel-level manual annotations, which are costly and difficult to obtain across diverse tissues and staining conditions. To address this limitation, we propose a framework that leverages spatial transcriptomics (ST) data as supervision for nuclei segmentation and classification. By incorporating cell-level ST data, we obtain gene expression profiles and corresponding nuclear masks from histopathological images. Gene expression profiles are converted into cell-type labels and used as training data for image-based classification. Because existing gene expression-based cell-type classification methods are not designed for image recognition, we introduce an image-oriented classification approach that bridges gene expression-based cell typing and image-based cell classification. To evaluate generalization, we conduct segmentation experiments on previously unseen organs and compare our method with conventional supervised models. Despite being trained on fewer organ types, our framework achieves higher segmentation accuracy, demonstrating strong transferability. Classification experiments further show consistent improvements over existing approaches.

---


### 90. [Agentic Adversarial Rewriting Exposes Architectural Vulnerabilities in Black-Box NLP Pipelines](https://arxiv.org/abs/2604.23483)

**<font color=#1a73e8>作者：</font>** Mazal Bethany, Kim-Kwang Raymond Choo, Nishant Vishwamitra 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-component natural language processing (NLP) pipelines are increasingly deployed for high-stakes decisions, yet no existing adversarial method can test their robustness under realistic conditions: binary-only feedback, no gradient access, and strict query budgets. We formalize this strict black-box threat model and propose a two-agent evasion framework operating in a semantic perturbation space. An Attacker Agent generates meaning-preserving rewrites while a Prompt Optimization Agent refines the attack strategy using only binary decision feedback within a 10-query budget. Evaluated against four evidence-based misinformation detection pipelines, the framework achieves evasion rates of 19.95 to 40.34% on modern large language model (LLM) based systems, compared to at most 3.90% for token-level perturbation baselines that rely on surrogate models because they cannot operate under our threat model. A legacy system relying on static lexical retrieval exhibits near-total vulnerability 97.02%, establishing a lower bound that exposes how architectural choices govern the attack surface. Evasion effectiveness is associated with three architectural properties: evidence retrieval mechanism, retrieval-inference coupling, and baseline classification accuracy. The iterative prompt optimization yields the largest marginal gains against the most robust targets, confirming that adaptive strategy discovery is essential when evasion is non-trivial. Analysis of successful rewrites reveals four exploitation patterns, each targeting failures at distinct pipeline stages. A pattern-informed defense reduces the evasion rate by up to 65.18%.

---


### 91. [Your Students Don't Use LLMs Like You Wish They Did](https://arxiv.org/abs/2604.23486)

**<font color=#1a73e8>作者：</font>** Sebastian Kobler, Matthew Clemson, Angela Sun 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Educational NLP systems are typically evaluated using engagement metrics and satisfaction surveys, which are at best a proxy for meeting pedagogical goals. We introduce six computational metrics for automated evaluation of pedagogical alignment in student-AI dialogue. We validate our metrics through analysis of 12,650 messages across 500 conversations from four courses. Using our metrics, we identify a fundamental misalignment: educators design conversational tutors for sustained learning dialogue, but students mainly use them for answer-extraction. Deployment context is the strongest predictor of usage patterns, outweighing student preference or system design: when AI tools are optional, usage concentrates around deadlines; when integrated into course structure, students ask for solutions to verbatim assignment questions. Whole-dialogue evaluation misses these turn-by-turn patterns. Our metrics will enable researchers building educational dialogue systems to measure whether they are achieving their pedagogical goals.

---


### 92. [MTRouter: Cost-Aware Multi-Turn LLM Routing with History-Model Joint Embeddings](https://arxiv.org/abs/2604.23530)

**<font color=#1a73e8>作者：</font>** Yiqun Zhang, Hao Li, Zihan Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multi-turn, long-horizon tasks are increasingly common for large language models (LLMs), but solving them typically requires many sequential model invocations, accumulating substantial inference costs. Here, we study cost-aware multi-turn LLM routing: selecting which model to invoke at each turn from a model pool, given a fixed cost budget. We propose MTRouter, which encodes the interaction history and candidate models into joint history-model embeddings, and learns an outcome estimator from logged trajectories to predict turn-level model utility. Experiments show that MTRouter improves the performance-cost trade-off: on ScienceWorld, it surpasses GPT-5 while reducing total cost by 58.7%; on Humanity's Last Exam (HLE), it achieves competitive accuracy while reducing total cost by 43.4% relative to GPT-5, and these gains even carry over to held-out tasks. Further analyses reveal several mechanisms underlying its effectiveness: relative to prior multi-turn routers, MTRouter makes fewer model switches, is more tolerant to transient errors, and exhibits emergent specialization across models. Code: this https URL

---


### 93. [Emotion-Conditioned Short-Horizon Human Pose Forecasting with a Lightweight Predictive World Model](https://arxiv.org/abs/2604.23532)

**<font color=#1a73e8>作者：</font>** Jingni Huang, Peter Bloodsworth  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Short-term human pose prediction plays a crucial role in interactive systems, assistive robots, and emotion-aware human-computer interaction[1-3]. While current trajectory prediction models primarily rely on geometric motion cues, they often overlook the underlying emotional signals influencing human motion dynamics[4-5]. This paper investigates whether facial expression-derived emotion embeddings can provide auxiliary conditional signals for short-term pose prediction. To further evaluate multimodal conditionation in a recursive prediction setting, we propose a lightweight autoregressive predictive world model that performs 15-step rolling pose prediction. This framework combines pose keypoints with emotion embeddings through a learnable gating mechanism and performs autoregressive unfolding prediction using a recurrent sequence model based on a two-layer LSTM architecture. Experiments were conducted on two small-scale pose-emotion video datasets: controlled motion sequences with minimal facial expression changes and, natural emotion-driven motion sequences with considerable facial expression changes. The results show that simple multimodal fusion does not consistently improve prediction accuracy, while normalized gating fusion significantly enhances the performance of emotion-driven motion sequences. Furthermore, counterfactual perturbation experiments demonstrate that the predicted trajectory exhibits measurable sensitivity to changes in multimodal input, suggesting that facial expression embeddings act as auxiliary conditional signals rather than redundant features. In summary, these results indicate that incorporating facial expression-derived emotion embeddings into emotion-conditional short-term pose prediction based on a lightweight predictive world model architecture is a feasible approach.

---


### 94. [$Z^2$-Sampling: Zero-Cost Zigzag Trajectories for Semantic Alignment in Diffusion Models](https://arxiv.org/abs/2604.23536)

**<font color=#1a73e8>作者：</font>** Haosen Li, Wenshuo Chen, Shaofeng Liang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion models have achieved unprecedented success in text-aligned generation, largely driven by Classifier-Free Guidance (CFG). However, standard CFG operates strictly on instantaneous gradients, omitting the intrinsic curvature of the data manifold. Recent methods like Zigzag-sampling (Z-Sampling) explicitly traverse multi-step forward-backward trajectories to probe this curvature, significantly improving semantic alignment. Yet, these explicit traversals triple the Neural Function Evaluation (NFE) cost and introduce unconstrained truncation errors from off-manifold evaluations, causing cumulative drift from the true marginal distribution. In this paper, we theoretically demonstrate that the explicit zigzag sequence is topologically reducible. We propose Implicit Z-Sampling, rigorously proving that intermediate states can be algebraically annihilated via operator dualities, physically eliminating off-manifold approximation errors. To push sampling efficiency to its theoretical lower bound, we introduce $Z^2$-Sampling (Zero-cost Zigzag Sampling). Exploiting the Probability Flow ODE's temporal coherence, $Z^2$-Sampling couples implicit algebraic collapse with a dynamically cached Temporal Semantic Surrogate. This restores the standard 2-NFE baseline without sacrificing semantic exploration. We formally prove via Backward Error Analysis that this discrete collapse inherently synthesizes a directional derivative curvature penalty. Finally, extensive evaluations demonstrate that $Z^2$-Sampling structurally shatters the performance-efficiency Pareto frontier. We validate its universal applicability across diverse architectures (U-Nets, DiTs) and modalities (image/video), establishing seamless orthogonality with advanced alignment frameworks (AYS, Diffusion-DPO).

---


### 95. [Oracle Noise: Faster Semantic Spherical Alignment for Interpretable Latent Optimization](https://arxiv.org/abs/2604.23540)

**<font color=#1a73e8>作者：</font>** Haosen Li, Wenshuo Chen, Lei Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-image diffusion models have achieved remarkable generative capabilities, yet accurately aligning complex textual prompts with synthesized layouts remains an ongoing challenge. In these models, the initial Gaussian noise acts as a critical structural seed dictating the macroscopic layout. Recent online optimization and search methods attempt to refine this noise to enhance text-image alignment. However, relying on unconstrained Euclidean gradient ascent mathematically inflates the latent norm and destroys the standard Gaussian prior, causing severe visual artifacts like color over-saturation. Furthermore, these methods suffer from inefficient semantic routing and easily fall into the ``reward hacking'' trap of external proxy models. To address these intertwined bottlenecks, we propose Oracle Noise, a zero-shot framework reframing noise initialization as semantic-driven optimization strictly confined to a Riemannian hypersphere. Instead of relying on complex external parsers, we directly identify the most impactful structural words in the prompt to efficiently route optimization energy. By updating the noise strictly along a spherical path, we mathematically preserve the original Gaussian distribution. This geometric constraint eliminates norm inflation and unlocks aggressive step sizes for rapid convergence. Extensive experiments demonstrate that Oracle Noise significantly accelerates semantic alignment and achieves superior aesthetics without black-box models. It completely mitigates Euclidean-induced degradation, establishing state-of-the-art performance across human preference metrics (e.g., HPSv2, ImageReward), semantic alignment (CLIP Score), and sample diversity, all within a strict 2-second optimization budget.

---


### 96. [Pref-CTRL: Preference Driven LLM Alignment using Representation Editing](https://arxiv.org/abs/2604.23543)

**<font color=#1a73e8>作者：</font>** Imranul Ashrafi, Inigo Jauregi Unanue, Massimo Piccardi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Test-time alignment methods offer a promising alternative to fine-tuning by steering the outputs of large language models (LLMs) at inference time with lightweight interventions on their internal representations. Recently, a prominent and effective approach, RE-Control (Kong et al., 2024), has proposed leveraging an external value function trained over the LLM's hidden states to guide generation via gradient-based editing. While effective, this method overlooks a key characteristic of alignment tasks, i.e. that they are typically formulated as learning from human preferences between candidate responses. To address this, in this paper we propose a novel preference-based training framework, Pref-CTRL, that uses a multi-objective value function to better reflect the structure of preference data. Our approach has outperformed RE-Control on two benchmark datasets and showed greater generalization on out-of-domain datasets. Our source code is available at this https URL.

---


### 97. [DLM: Unified Decision Language Models for Offline Multi-Agent Sequential Decision Making](https://arxiv.org/abs/2604.23557)

**<font color=#1a73e8>作者：</font>** Zhuohui Zhang, Bin Cheng, Bin He  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Building scalable and reusable multi-agent decision policies from offline datasets remains a challenge in offline multi-agent reinforcement learning (MARL), as existing methods often rely on fixed observation formats and action spaces that limit generalization. In contrast, large language models (LLMs) offer a flexible modeling interface that can naturally accommodate heterogeneous observations and actions. Motivated by this, we propose the Decision Language Model (DLM), which formulates multi-agent decision making as a dialogue-style sequence prediction problem under the centralized training with decentralized execution paradigm. DLM is trained in two stages: a supervised fine-tuning phase, which leverages dialogue-style datasets for centralized training with inter-agent context and generates executable actions from offline trajectories, followed by a group relative policy optimization phase to enhance robustness to out-of-distribution actions through lightweight reward functions. Experiments on multiple benchmarks show that a unified DLM outperforms strong offline MARL baselines and LLM-based conversational decision-making methods, while demonstrating strong zero-shot generalization to unseen scenarios across tasks.

---


### 98. [RouteNLP: Closed-Loop LLM Routing with Conformal Cascading and Distillation Co-Optimization](https://arxiv.org/abs/2604.23577)

**<font color=#1a73e8>作者：</font>** Dongxin Guo, Jikun Wu, Siu Ming Yiu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Serving diverse NLP workloads with large language models is costly: at one enterprise partner, inference costs exceeded $200K/month despite over 70% of queries being routine tasks well within the capability of smaller models. We present RouteNLP, a closed-loop framework that routes queries across a tiered model portfolio to minimize cost while satisfying per-task quality constraints. The framework integrates three components: a difficulty-aware router with shared task-conditioned representations trained on preference data and quality signals; confidence-calibrated cascading that uses conformal prediction for distribution-free threshold initialization; and a distillation-routing co-optimization loop that clusters escalation failures, applies targeted knowledge distillation to cheaper models, and automatically retrains the router, yielding over twice the cost improvement of untargeted distillation. In an 8-week pilot deployment processing ~5K queries/day at an enterprise customer-service division, RouteNLP reduced inference costs by 58% while maintaining 91% response acceptance and reducing p99 latency from 1,847 ms to 387 ms. On a six-task benchmark spanning finance, customer service, and legal domains, the framework achieves 40-85% cost reduction while retaining 96-100% quality on structured tasks and 96-98% on generation tasks, with human evaluation confirming that 74.5% of routed generation outputs match or exceed frontier-model quality.

---


### 99. [LLMs Reading the Rhythms of Daily Life: Aligned Understanding for Behavior Prediction and Generation](https://arxiv.org/abs/2604.23578)

**<font color=#1a73e8>作者：</font>** Fanjin Meng, Jingtao Ding, Nian Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Human daily behavior unfolds as complex sequences shaped by intentions, preferences, and context. Effectively modeling these behaviors is crucial for intelligent systems such as personal assistants and recommendation engines. While recent advances in deep learning and behavior pre-training have improved behavior prediction, key challenges remain--particularly in handling long-tail behaviors, enhancing interpretability, and supporting multiple tasks within a unified framework. Large language models (LLMs) offer a promising direction due to their semantic richness, strong interpretability, and generative capabilities. However, the structural and modal differences between behavioral data and natural language limit the direct applicability of LLMs.
To address this gap, we propose Behavior Understanding Alignment (BUA), a novel framework that integrates LLMs into human behavior modeling through a structured curriculum learning process. BUA employs sequence embeddings from pretrained behavior models as alignment anchors and guides the LLM through a three-stage curriculum, while a multi-round dialogue setting introduces prediction and generation capabilities. Experiments on two real-world datasets demonstrate that BUA significantly outperforms existing methods in both tasks, highlighting its effectiveness and flexibility in applying LLMs to complex human behavior modeling.

---


### 100. [Identity-Decoupled Anonymization for Visual Evidence in Multi-modal Retrieval-Augmented Generation](https://arxiv.org/abs/2604.23584)

**<font color=#1a73e8>作者：</font>** Zehua Cheng, Wei Dai, Jiahao Sun  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-modal retrieval-augmented generation (MRAG) systems retrieve visual evidence from large image corpora to ground the responses of large multi-modal models, yet the retrieved images frequently contain human faces whose identities constitute sensitive personal information. Existing anonymization techniques that destroy the non-identity visual cues that downstream reasoning depends on or fail to provide principled privacy guarantees. We propose Identity-Decoupled MRAG, a framework that interposes a generative anonymization module between retrieval and generation. Our approach consists of three components: (i)a disentangled variational encoder that factorizes each face into an identity code and a spatially-structured attribute code, regularized by a mutual-information penalty and a gradient-based independence term; (ii)a manifold-aware rejection sampler that replaces the identity code with a synthetic one guaranteed to be both distinct from the original and realistic; and (iii)a conditional latent diffusion generator that synthesizes the anonymized face from the replacement identity and the preserved attributes, distilled into a latent consistency model for low-latency deployment. Privacy is enforced through a multi-oracle ensemble of face recognition models with a hinge-based loss that halts optimization once identity similarity drops below the impostor-regime threshold.

---


> [!TIP]
> 当前位于：**51-100**（第 2/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-215](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
