# 🧠 大模型相关研究 | 2026年05月13日

> 本类共 **223** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**101-150**（第 3/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-223](./part-05.md)

---

### 101. [A CAP-like Trilemma for Large Language Models: Correctness, Non-bias, and Utility under Semantic Underdetermination](https://arxiv.org/abs/2605.11672)

**<font color=#1a73e8>作者：</font>** Vinu Ellampallil Venugopal  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The CAP theorem states that a distributed system cannot simultaneously guarantee consistency, availability, and partition tolerance under network partition. Inspired by this result, this paper formulates a CAP-like conjecture for Large Language Models (LLMs). The proposed trilemma states that, under semantic underdetermination, an LLM cannot always simultaneously guarantee strong correctness, strict non-bias, and high utility. A prompt is semantically underdetermined when the given premises do not determine a unique answer. In such cases, a useful and decisive response requires the model to introduce a selection criterion, preference, prior, or value ordering. If this criterion is not supplied by the user or justified by the available premises, the response becomes biased in a broad selection-theoretic sense. Conversely, if the model avoids unsupported preferences, it may preserve correctness and non-bias but may reduce utility through refusal, hedging, or clarification. The paper formalizes this correctness--non-bias--utility trilemma, develops examples, and argues that certain LLM failures arise not merely from model limitations but from the structure of underdetermined decision requests.

---


### 102. [Explaining and Breaking the Safety-Helpfulness Ceiling via Preference Dimensional Expansion](https://arxiv.org/abs/2605.11679)

**<font color=#1a73e8>作者：</font>** ShiYing Huang, Liang Lin, Yuer Li 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In the realm of multi-objective alignment for large language models, balancing disparate human preferences often manifests as a zero-sum conflict. Specifically, the intrinsic tension between competing goals dictates that aggressively optimizing for one metric (e.g., helpfulness) frequently incurs a substantial penalty on another (e.g., harmlessness). While prior work mainly focuses on data selection, parameter merging, or algorithmic balancing during training, these approaches merely force compromises between divergent preferences along a fixed Pareto frontier, failing to fundamentally resolve the inherent trade-off. In this work, we approach this problem from a novel perspective of multi-dimensional rewards. By scaling up the model's rollouts and analyzing the outputs across different reward dimensions, we arrive at a critical conclusion: the conflict among multiple objectives stems from the fact that the prompt itself inherently restricts the achievable multi-dimensional rewards. Based on this core observation, we propose MORA: Multi-Objective Reward Assimilation. Specifically, MORA isolates single-reward prompts through pre-sampling and expands their reward diversity by rewriting the original questions to incorporate multi-dimensional intents. Extensive experiments demonstrate that: (1) in sequential alignment, MORA achieves single-preference improvements ranging from 5% to 12.4%, with exceptional gains in harmlessness, after multiple-preference alignment across helpful, harmless, and truthful dimensions. (2) In simultaneous alignment, MORA achieves an average overall reward improvement of 4.6%. Our codes are available at this https URL.

---


### 103. [Robust LLM Unlearning Against Relearning Attacks: The Minor Components in Representations Matter](https://arxiv.org/abs/2605.11685)

**<font color=#1a73e8>作者：</font>** Zeguan Xiao, Xuanzhe Xu, Yun Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) unlearning aims to remove specific data influences from pre-trained model without costly retraining, addressing privacy, copyright, and safety concerns. However, recent studies reveal a critical vulnerability: unlearned models rapidly recover "forgotten" knowledge through relearning attacks. This fragility raises serious security concerns, especially for open-weight models. In this work, we investigate the fundamental mechanism underlying this fragility from a representation geometry perspective. We discover that existing unlearning methods predominantly optimize along dominant components, leaving minor components largely unchanged. Critically, during relearning attacks, the modifications in these dominant components are easily reversed, enabling rapid knowledge recovery, whereas minor components exhibit stronger resistance to such reversal. We further provide a theoretical analysis that explains both observations from the spectral structure of representations. Building on this insight, we propose Minor Component Unlearning (MCU), a novel unlearning approach that explicitly targets minor components in representations. By concentrating unlearning effects in these inherently robust directions, our method achieves substantially improved resistance to relearning attacks. Extensive experiments on three datasets validate our approach, demonstrating significant improvements over state-of-the-art methods including sharpness-aware minimization.

---


### 104. [Measuring What Matters Beyond Text: Evaluating Multimodal Summaries by Quality, Alignment, and Diversity](https://arxiv.org/abs/2605.11693)

**<font color=#1a73e8>作者：</font>** Abid Ali, Diego Molla-Aliod, Usman Naseem  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) have facilitated Multimodal Summarization with Multimodal Output (MSMO), wherein systems generate concise textual summaries accompanied by salient visuals from multimodal sources. However, current MSMO evaluation remains fragmented: text quality, image-text alignment, and visual diversity are typically assessed in isolation using unimodal metrics, making it difficult to capture whether the modalities jointly support a faithful and useful summary. To address this gap, we introduce MM-Eval, a unified evaluation framework that integrates assessments of textual quality, cross-modal alignment, and visual diversity. MM-Eval comprises three components: (1) text quality, measured using OpenFActScore for factual consistency and G-Eval for coherence, fluency, and relevance; (2) image-text relevance, evaluated via an MLLM-as-a-judge approach; and (3) image-set diversity, quantified using Truncated CLIP Entropy. We calibrate MM-Eval through a learned aggregation model trained on the mLLM-EVAL news benchmark, aligning component contributions with human preferences. Our analysis reveals a text-dominant hierarchy in this setting, where factual consistency acts as a critical determinant of perceived overall quality, while visual relevance and diversity provide complementary signals. MM-Eval improves over heuristic aggregation baselines and provides an interpretable, reference-weak framework for comparative evaluation of multimodal summaries.

---


### 105. [MindMirror: A Local-First Multimodal State-Aware Support System for Digital Workers](https://arxiv.org/abs/2605.11700)

**<font color=#1a73e8>作者：</font>** Wenqi Luo, Changbo Wang, Yan Wang  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Digital workers often experience fatigue, anxiety, reduced attention, and task blockage during prolonged computer-based work. Existing productivity tools mainly focus on task completion, while general-purpose AI chatbots require users to formulate clear prompts before receiving useful help. This paper presents MindMirror, a local-first multimodal state-aware support system for digital workers. MindMirror integrates camera-based facial expression cues, text input, optional speech interaction, structured blockage reflection, local large language model (LLM)-based response generation, and daily/weekly review reports. The system forms a closed workflow of state checking, manual correction, structured articulation, suggestion generation, and state review. The current prototype follows a local-first design, while optional speech services may rely on third-party APIs when enabled. It is implemented with a Web frontend, Flask backend, an emotion recognition model, an Ollama-hosted Qwen model, this http URL visualization, and local JSON/LocalStorage records. We evaluate the emotion recognition module on an independent seven-class image-level facial expression benchmark containing 6,767 images. The fine-tuned Hugging Face model improves accuracy from 59.66% to 94.49% over a non-fine-tuned checkpoint baseline, an absolute gain of 34.83 percentage points. We further validate the prototype through endpoint-level reliability tests, voice-interaction latency tests, and a small formative user feedback study with six digital workers. Results suggest that users value the local-first design, manual correction mechanism, and structured reflection workflow. MindMirror is not intended for psychological diagnosis; instead, it serves as a lightweight, user-controllable tool for state reflection and supportive interaction.

---


### 106. [CAST: Collapse-Aware multi-Scale Topology Fusion for Multimodal Coreset Selection](https://arxiv.org/abs/2605.11705)

**<font color=#1a73e8>作者：</font>** Boran Zhao, Hetian Liu, Zhenxian Hu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The training of large multimodal models fundamentally relies on massive image-text datasets, which inevitably incur prohibitive computational overhead. Dataset selection offers a promising paradigm by identifying a highly informative coreset. However, existing approaches suffer from two critical limitations: (i) single-modality-dominated sampling methods, which ignore the fine-grained cross-modal information imbalance inherent in multimodal datasets and thus lead to semantic loss in the other modality; and (ii) coarse-grained sample-scoring-based sampling methods, where the selected coreset tends to be biased toward the scoring model, making it difficult to guarantee distributional equivalence between the coreset and the original dataset. Meanwhile, existing distribution matching and discrete sampling strategies often fail to jointly account for global semantic structure, local fine-grained details, and redundancy-aware coverage in dense regions. To this end, we propose CAST, a Collapse-Aware multi-Scale Topology fusion framework for multimodal coreset selection. We first construct image- and text-modality topologies, and derive a unified topology via local-collapse-aware refinement and cross-modal fusion. We then introduce a multi-scale distribution matching criterion in the diffusion wavelet domain, encouraging the coreset to approximate the original dataset at multiple scales. Finally, we introduce a local soft relational coverage mechanism that extends pure geometric coverage to relation-aware indirect coverage, penalizing redundant selections in dense clusters. Extensive experiments on Flickr30K and MS-COCO show that CAST outperforms existing dataset selection baselines, showcasing great superiority in cross-architecture generalization and energy efficiency over state-of-the-art multimodal synthesis methods.

---


### 107. [GRAFT: Graph-Tokenized LLMs for Tool Planning](https://arxiv.org/abs/2605.11706)

**<font color=#1a73e8>作者：</font>** Xinyi Gao, Xinyu Ren, Junliang Yu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used to complete complex tasks by selecting and coordinating external tools across multiple steps. This requires aligning tool choices with subtask intent while satisfying directional execution dependencies among tools. To do this, existing methods model these dependencies as tool graphs and incorporate the graphs with LLMs through retrieval, serialization, or prompt-level injection. However, these external graph-use strategies all follow a matching paradigm, which often fails to align tool choices with the underlying subtask structure, producing semantically plausible plans that violate graph constraints. This issue is further exacerbated by error accumulation, where an early incorrect tool selection shifts the plan into an invalid graph state and causes subsequent predictions to drift away from the valid execution path. To address these challenges, we propose GRAFT, a graph-tokenized language model framework for dependency-aware tool planning. GRAFT internalizes the tool graph by mapping each tool node to a dedicated special token and learning directed tool dependencies within the representation space. It further introduces on-policy tool context distillation, training the model on its own sampled trajectories while distilling stepwise planning signals. Experiments show that GRAFT achieves state-of-the-art performance in exact sequence matching and dependency legality, supporting more reliable LLM tool planning in complex workflows.

---


### 108. [Toward Stable Value Alignment: Introducing Independent Modules for Consistent Value Guidance](https://arxiv.org/abs/2605.11712)

**<font color=#1a73e8>作者：</font>** Wenhao Chen, Sirui Sun, Shengyuan Bai 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Aligning large language models (LLMs) with human values typically relies on post-training or inference-time steering that directly manipulates the backbone's parameters or representation space. However, a critical gap exists: the model's residual stream is highly dynamic, in which values exist as fragile, low-dimensional properties, inherently incompatible with the stability required for consistent value expression. In this paper, we propose the Stable Value Guidance Transformer (SVGT), which addresses this gap through an independent value module incorporating two key designs: (1) independent value modeling, maintaining normative representations in a dedicated value space isolated from the backbone, and (2) explicit behavioral guidance, transducing these stable signals into learnable latent Bridge Tokens. These tokens serve as dynamic value anchors to explicitly steer the generative trajectory, ensuring robust adherence across diverse contexts without disrupting the backbone's internal representations. Experiments across multiple backbones and safety benchmarks show that SVGT generally reduces harmful scores by over 70% while maintaining generation fluency, demonstrating the efficacy of architecturally grounded value modeling. Our code is available at this https URL.

---


### 109. [SafeSteer: A Decoding-level Defense Mechanism for Multimodal Large Language Models](https://arxiv.org/abs/2605.11716)

**<font color=#1a73e8>作者：</font>** Xinyi Zeng, Xue Yang, Jingyuan Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) are gaining increasing attention. Due to the heterogeneity of their input features, they face significant challenges in terms of jailbreak defenses. Current defense methods rely on costly fine-tuning or inefficient post-hoc interventions, limiting their ability to address novel attacks and involving performance trade-offs. To address the above issues, we explore the inherent safety capabilities within MLLMs and quantify their intrinsic ability to discern harmfulness at decoding stage. We observe that 1) MLLMs can distinguish the harmful and harmless inputs during decoding process, 2) Image-based attacks are more stealthy. Based on these insights, we introduce SafeSteer, a decoding-level defense mechanism for MLLMs. Specifically, it includes a Decoding-Probe, a lightweight probe for detecting and correcting harmful output during decoding, which iteratively steers the decoding process toward safety. Furthermore, a modal semantic alignment vector is integrated to transfer the strong textual safety alignment to the vision modality. Experiments on multiple MLLMs demonstrate that SafeSterr can improve MLLMs' safety by up to 33.40\% without fine-tuning. Notably, it can maintain the effectiveness of MLLMs, ensuring a balance between their helpfulness and harmlessness.

---


### 110. [Block-R1: Rethinking the Role of Block Size in Multi-domain Reinforcement Learning for Diffusion Large Language Models](https://arxiv.org/abs/2605.11726)

**<font color=#1a73e8>作者：</font>** Yan Jiang, Ruihong Qiu, Zi Huang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recently, reinforcement learning (RL) has been widely applied during post-training for diffusion large language models (dLLMs) to enhance reasoning with block-wise semi-autoregressive generation. Block size has therefore become a vital factor in dLLMs, since it determines the parallel decoding granularity and affects the rollout trajectories during RL optimisation, e.g., GRPO. Instead of investigating the effect of block size during inference on individual domains, this paper studies block size from a domain conflict perspective for dLLM RL post-training in multi-domain scenarios. The main contributions are: (1) a formulation of domain block size conflict in multi-domain RL for dLLMs, which will largely affect the post-training effectiveness for rollout-based RL methods; (2) a novel dataset, Block-R1-41K is constructed with a best-improved training block size for each sample, which also induces a Block Size Conflict Score to quantitatively measure the domain conflict; (3) a new benchmark, Block-R1, for flexible RL post-training for dLLMs in both single and cross domain; and (4) a simple yet powerful cross-domain post-training method with sample-level best-improved training block sizes. Extensive experiments on 13 distinct datasets, 7 latest RL algorithms, and various different dLLM backbones are covered in Block-R1. The benchmark is open-sourced at this https URL, with the dataset released at this https URL.

---


### 111. [Allegory of the Cave: Measurement-Grounded Vision-Language Learning](https://arxiv.org/abs/2605.11727)

**<font color=#1a73e8>作者：</font>** Kepeng Xu, Li Xu, Gang He 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Vision-language models typically reason over post-ISP RGB images, although RGB rendering can clip, suppress, or quantize sensor evidence before inference. We study whether grounding improves when the visual interface is moved closer to the underlying camera measurement. We formulate measurement-grounded vision-language learning and instantiate it as PRISM-VL, which combines RAW-derived Meas.-XYZ inputs, camera-conditioned grounding, and Exposure-Bracketed Supervision Aggregation for transferring supervision from RGB proxies to measurement-domain observations. Using a quality-controlled 150K instruction-tuning set and a held-out benchmark targeting low-light, HDR, visibility-sensitive, and hallucination-sensitive cases, PRISM-VL-8B reaches 0.6120 BLEU, 0.4571 ROUGE-L, and 82.66\% LLM-Judge accuracy, improving over the RGB Qwen3-VL-8B baseline by +0.1074 BLEU, +0.1071 ROUGE-L, and +4.46 percentage points. These results suggest that part of VLM grounding error arises from information lost during RGB rendering, and that preserving measurement-domain evidence can improve multimodal reasoning.

---


### 112. [Persona-Conditioned Adversarial Prompting: Multi-Identity Red-Teaming for Adversarial Discovery and Mitigation](https://arxiv.org/abs/2605.11730)

**<font color=#1a73e8>作者：</font>** Cristian Morasso, Anisa Halimi, Muhammad Zaid Hameed 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Automated red-teaming for LLMs often discovers narrow attack slices, missing diverse real-world threats, and yielding insufficient data for safety fine-tuning. We introduce Persona-Conditioned Adversarial Prompting (PCAP), which conditions adversarial search on diverse attacker personas (e.g., doctors, students, malicious actors) and strategy sets to explore realistic attack scenarios. By running parallel persona-conditioned searches, PCAP discovers transferable jailbreaks across different contexts and generates rich defense datasets with automatic metadata tracking. On GPT-OSS 120B, PCAP increases attack success from 57\% to 97\% while producing 2-6$\times$ more diverse prompts covering varied real-world scenarios. Critically, fine-tuning lightweight adapters on PCAP-generated data significantly improves model robustness (recall: 0.36 $\rightarrow$ 0.99, F1: 0.53 $\rightarrow$ 0.96) with minimal false positives, demonstrating a practical closed-loop approach from vulnerability discovery to automated alignment.

---


### 113. [U-STS-LLM A Unified Spatio-Temporal Steered Large Language Model for Traffic Prediction and Imputation](https://arxiv.org/abs/2605.11735)

**<font color=#1a73e8>作者：</font>** Yichen Zhang, Jun Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The efficient operation of modern cellular networks hinges on the accurate analysis of spatio-temporal traffic data. Mastering these patterns is essential for core network functions, chiefly forecasting future load to pre-empt congestion and imputing missing values caused by sensor failures or transmission errors to ensure data continuity. While deeply connected, forecasting and imputation have historically evolved as separate sub-fields. The dominant paradigm, Spatio-Temporal Graph Neural Networks (STGNNs), while effective, are often specialized, computationally intensive, and exhibit limited generalization. Concurrently, adapting large pre-trained language models (LLMs) offers a powerful alternative for sequence modeling, yet existing approaches provide weak structural guidance, leading to unstable convergence and a narrow focus on forecasting. To bridge these gaps, we propose U-STS-LLM, a unified framework built on a spatio-temporally steered LLM. Our core innovation is a Dynamic Spatio-Temporal Attention Bias Generator that synthesizes a persistent functional graph with transient nodal states to explicitly steer the LLM's attention. Coupled with a partially frozen backbone tuned via Low-Rank Adaptation (LoRA) and a Gated Adaptive Fusion mechanism, the model achieves stable, parameter-efficient adaptation. Trained under a unified multi-task objective, U-STS-LLM learns a holistic data representation. Extensive experiments on real-world cellular datasets demonstrate that U-STS-LLM establishes new state-of-the-art performance in both long-horizon forecasting and high-missing-rate imputation, while maintaining remarkable training efficiency and stability, offering a novel blueprint for harnessing foundation models in structured, non-linguistic domains.

---


### 114. [OptArgus: A Multi-Agent System to Detect Hallucinations in LLM-based Optimization Modeling](https://arxiv.org/abs/2605.11738)

**<font color=#1a73e8>作者：</font>** Zhong Li, Zihan Guo, Xiaohan Lu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used to translate natural-language optimization problems into mathematical formulations and solver code, but matching the reference objective value is not a reliable test of correctness: an artifact may agree numerically while still changing the underlying optimization semantics. We formulate this issue as \emph{optimization-modeling hallucination detection}, namely structural consistency auditing over the problem description, symbolic model, and solver implementation. We develop, to our knowledge, the first fine-grained hallucination taxonomy specifically for optimization modeling, spanning objective, variable, constraint, and implementation failures. We use this taxonomy to design OptArgus, a multi-agent detector with conductor routing, specialist auditors, and evidence consolidation. To evaluate this setting, we introduce a three-part benchmark suite with $484$ clean artifacts, $1266$ controlled injected artifacts, and $6292$ natural LLM-generated artifacts. Against a matched single-agent baseline, OptArgus produces fewer false alarms on clean artifacts, more accurate top-ranked localization on controlled single-error cases, and stronger detection on natural model outputs. Together, these contributions turn optimization-modeling hallucination detection into a concrete empirical problem and suggest that modular, taxonomy-grounded auditing is a practical route to more reliable optimization modeling.

---


### 115. [Learning to Foresee: Unveiling the Unlocking Efficiency of On-Policy Distillation](https://arxiv.org/abs/2605.11739)

**<font color=#1a73e8>作者：</font>** Yuchen Cai, Ding Cao, Liang Lin 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) has emerged as an efficient post-training paradigm for large language models. However, existing studies largely attribute this advantage to denser and more stable supervision, while the parameter-level mechanisms underlying OPD's efficiency remain poorly understood. In this work, we argue that OPD's efficiency stems from a form of ``foresight'': it establishes a stable update trajectory toward the final model early in training. This foresight manifests in two aspects. First, at the \textbf{Module-Allocation Level}, OPD identifies regions with low marginal utility and concentrates updates on modules that are more critical to reasoning. Second, at the \textbf{Update-Direction Level}, OPD exhibits stronger low-rank concentration, with its dominant subspaces aligning closely with the final update subspace early in training. Building on these findings, we propose \textbf{EffOPD}, a plug-and-play acceleration method that speeds up OPD by adaptively selecting an extrapolation step size and moving along the current update direction. EffOPD requires no additional trainable modules or complex hyperparameter tuning, and achieves an average training acceleration of $3\times$ while maintaining comparable final performance. Overall, our findings provide a parameter-dynamics perspective for understanding the efficiency of OPD and offer practical insights for designing more efficient post-training methods for large language models.

---


### 116. [Training-Inference Consistent Segmented Execution for Long-Context LLMs](https://arxiv.org/abs/2605.11744)

**<font color=#1a73e8>作者：</font>** Xianpeng Shang, Jiang Li, Zehua Duo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Transformer-based large language models face severe scalability challenges in long-context generation due to the computational and memory costs of full-context attention. Under practical computation and memory constraints, many inference-efficient long-context methods improve efficiency by adopting bounded-context or segment-level execution only during inference, while continuing to train models under full-context attention, resulting in a mismatch between training and inference execution and state-transition semantics. Based on this insight, we propose a training-inference consistent segment-level generation framework, in which training and inference follow the same segment-level forward execution semantics. During training, consistency with inference is enforced by restricting gradient propagation to KV states carried over from the immediately preceding segment, while permitting head-specific access to past KV states during the forward pass without involving them in gradient propagation. Across long-context benchmarks, our approach achieves performance comparable to full-context attention, while achieving competitive latency-memory trade-offs against strong inference-efficient baselines, and substantially improving scalability at very long context lengths (e.g., approximately 6x lower peak prefill memory at 128K compared to full-context attention with FlashAttention).

---


### 117. [When Reasoning Traces Become Performative: Step-Level Evidence that Chain-of-Thought Is an Imperfect Oversight Channel](https://arxiv.org/abs/2605.11746)

**<font color=#1a73e8>作者：</font>** Wenkai Li, Fan Yang, Ananya Hazarika 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Chain-of-thought (CoT) traces are increasingly used both to improve language model capability and to audit model behavior, implicitly assuming that the visible trace remains synchronized with the computation that determines the answer. We test this assumption with a step-level Detect-Classify-Compare framework built around an answer-commitment proxy that is cross-validated with Patchscopes, tuned-lens probes, and causal direction ablation. Across nine models and seven reasoning benchmarks, latent commitment and explicit answer arrival align on only 61.9% of steps on average. The dominant mismatch pattern is confabulated continuation: 58.0% of detected mismatch events occur after the answer-commitment proxy has already stabilized while the trace continues producing deliberative-looking text, and a vacuousness analysis shows that the committed answer does not change during these steps. In architecture-matched Qwen2.5/DeepSeek-R1-Distill comparisons, the reasoning pipeline changes failure composition more than aggregate alignment, most clearly at 32B where confabulated steps decrease as contradictory states increase. Lower step-level alignment is also associated with larger CoT utility, suggesting that the settings that benefit most from CoT are often the least temporally faithful. Paired truncation and a complementary donor-corruption test further indicate that much post-commitment text is not load-bearing for the final answer. These findings suggest that CoT can remain useful while still being an unreliable report of when the answer was formed.

---


### 118. [Towards Visually Grounded Multimodal Summarization via Cross-Modal Transformer and Gated Attention](https://arxiv.org/abs/2605.11753)

**<font color=#1a73e8>作者：</font>** Abid Ali, Diego Molla-Aliod, Usman Naseem  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal summarization requires models to jointly understand textual and visual inputs to generate concise, semantically coherent summaries. Existing methods often inject shallow visual features into deep language models, leading to representational mismatches and weak cross-modal grounding. We propose a unified framework that jointly performs text summarization and representative image selection. Our system, SPeCTrA-Sum (Sampler Perceiver with Cross-modal Transformer and gated Attention for Summarization), introduces two key innovations. First, a Deep Visual Processor (DVP) aligns the visual encoder with the language model at corresponding depths, enabling hierarchical, layer-wise fusion that preserves semantic consistency. Second, a lightweight Visual Relevance Predictor (VRP) selects salient and diverse images by distilling soft labels from a Determinantal Point Processes (DPP) teacher. SPeCTrA-Sum is trained using a multi-objective loss that combines autoregressive summarization, cross-modal alignment, and DPP-based distillation. Experiments show that our system produces more accurate, visually grounded summaries and selects more representative images, demonstrating the benefits of depth-aware fusion and principled image selection for multimodal summarization.

---


### 119. [From Token to Token Pair: Efficient Prompt Compression for Large Language Models in Clinical Prediction](https://arxiv.org/abs/2605.11774)

**<font color=#1a73e8>作者：</font>** Mingcheng Zhu, Zhiyao Luo, Yu Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> By processing electronic health records (EHRs) as natural language sequences, large language models (LLMs) have shown potential in clinical prediction tasks such as mortality prediction and phenotyping. However, longitudinal or highly frequent EHRs often yield excessively long token sequences that result in high computational costs and even reduced performance. Existing solutions either add modules for compression or remove less important tokens, which introduce additional inference latency or risk losing clinical information. To achieve lossless compression of token sequences without additional cost or loss of performance, we propose Medical Token-Pair Encoding (MedTPE), a layered method that extends standard tokenisation for EHR sequences. MedTPE merges frequently co-occurring medical token pairs into composite tokens, providing lossless compression while preserving the computational complexity through a dependency-aware replacement strategy. Only the embeddings of the newly introduced tokens of merely 0.5-1.0% of the LLM's parameters are fine-tuned via self-supervised learning. Experiments on real-world datasets for two clinical scenarios demonstrate that MedTPE reduces input token length by up to 31% and inference latency by 34-63%, while maintaining or even improving both predictive performance and output format compliance across multiple LLMs and four clinical prediction tasks. Furthermore, MedTPE demonstrates robustness across different input context lengths and generalisability to scientific and financial domains and different languages.

---


### 120. [Entropy Polarity in Reinforcement Fine-Tuning: Direction, Asymmetry, and Control](https://arxiv.org/abs/2605.11775)

**<font color=#1a73e8>作者：</font>** Jiazheng Zhang, Ziche Fu, Junrui Shen 等 20 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Policy entropy has emerged as a fundamental measure for understanding and controlling exploration in reinforcement learning with verifiable rewards (RLVR) for LLMs. However, existing entropy-aware methods mainly regulate entropy through global objectives, while the token-level mechanism by which sampled policy updates reshape policy entropy remains underexplored. In this work, we develop a theoretical framework of entropy mechanics in RLVR. Our analysis yields a first-order approximation of the entropy change, giving rise to entropy polarity, a signed token-level quantity that predicts how much a sampled update expands or contracts entropy. This analysis further reveals a structural asymmetry: reinforcing frequent high-probability tokens triggers contraction tendencies, whereas expansive tendencies typically require lower-probability samples or stronger distributional correction. Empirically, we show that entropy polarity reliably predicts entropy changes, and that positive and negative polarity branches play complementary roles in preserving exploration while strengthening exploitation. Building on these insights, we propose Polarity-Aware Policy Optimization (PAPO), which preserves both polarity branches and implements entropy control through advantage reweighting. With the empirical entropy trajectory as an online phase signal, PAPO adaptively reallocates optimization pressure between entropy-expanding and entropy-contracting updates. Experiments on mathematical reasoning and agentic benchmarks show that PAPO consistently outperforms competitive baselines, while delivering superior training efficiency and substantial reward improvements.

---


### 121. [Urban Risk-Aware Navigation via VQA-Based Event Maps for People with Low Vision](https://arxiv.org/abs/2605.11782)

**<font color=#1a73e8>作者：</font>** Antoni Valls, Jordi Sanchez-Riera  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual impairment affects hundreds of millions of people worldwide, severely limiting their ability to navigate urban environments safely and independently. While wearable assistive devices offer a promising platform for real-time hazard detection, existing approaches rely on task-specific vision pipelines that lack flexibility and generalizability. In this work, we propose an event map framework based on visual question answering that leverages Vision-Language Models (VLMs) for pedestrian scene description and hazard identification across diverse real-world environments, using a three-level hierarchical query structure to enable fine-grained scene understanding without task-specific retraining. Model responses are aggregated into a weighted risk scoring system that maps street segments into four discrete safety categories, producing navigable risk-aware event maps for route planning. To support evaluation and future research, we introduce a geographically diverse dataset spanning 20 cities across six continents, comprising over 800 annotated images and 18,000 answered questions. We benchmark four VQA architectures -ViLT, LLaVA, InstructBLIP, and Qwen-VL- and find that generative Multimodal Large Language Models (MLLMs) substantially outperform classification-based approaches, with Qwen-VL achieving the best overall balance of precision and recall. These results demonstrate the viability of MLLMs as a flexible and generalizable foundation for assistive navigation systems for visually impaired people.

---


### 122. [Beyond Inefficiency: Systemic Costs of Incivility in Multi-Agent Monte Carlo Simulations](https://arxiv.org/abs/2605.11789)

**<font color=#1a73e8>作者：</font>** Alison Moldovan-Mauer, Benedikt Mangold  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Unconstructive debate and uncivil communication carry well-documented costs for productivity and cohesion, yet isolating their effect on operational efficiency has proven difficult. Human subject research in this domain is constrained by ethical oversight, limited reproducibility, and the inherent unpredictability of naturalistic settings. We address this gap by leveraging Large Language Model (LLM) based Multi-Agent Systems as a controlled sociological sandbox, enabling systematic manipulation of communicative behavior at scale. Using a Monte Carlo simulation framework, we generate thousands of structured 1-on-1 adversarial debates across varying toxicity conditions, measuring convergence time, defined as the number of rounds required to reach a conclusion, as a proxy for interactional efficiency. Building on a prior study, we replicate and extend its findings across two additional LLM agents of varying parameter size, allowing us to assess whether the effects of toxic behavior on debate dynamics generalize across model scale. The convergence latency of 25% reported in the previous study was confirmed. It was found that this latency is significantly bigger for models with fewer parameters. We further identify a significant first-mover advantage, whereby the agent initiating the discussion wins significantly above chance regardless of toxicity condition.

---


### 123. [ROMER: Expert Replacement and Router Calibration for Robust MoE LLMs on Analog Compute-in-Memory Systems](https://arxiv.org/abs/2605.11800)

**<font color=#1a73e8>作者：</font>** Wenyong Zhou, Yuannuo Feng, Yizhe Chen 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) with mixture-of-experts (MoE) architectures achieve remarkable scalability by sparsely activating a subset of experts per token, yet their frequent expert switching creates memory bandwidth bottlenecks that compute-in-memory (CIM) architectures are well-suited to mitigate. However, analog CIM systems suffer from inherent hardware imperfections that perturb stored weights, and its negative impact on MoE-based LLMs in noisy CIM environments remains unexplored. In this work, we present the first systematic investigation of MoE-based LLMs under noise model calibrated with real chip measurements, revealing that hardware noise critically disrupts expert load balance and renders clean-trained routing decisions consistently suboptimal. Based on these findings, we propose ROMER, a post-training calibration framework that (1) replaces underactivated experts with high-frequency ones to restore load balance, and (2) recalibrates router logits via percentile-based normalization to stabilize routing under noise. Extensive experiments across multiple benchmarks demonstrate that ROMER achieves up to 58.6\%, 58.8\%, and 59.8\% reduction in perplexity under real-chip noise conditions for DeepSeek-MoE, Qwen-MoE, and OLMoE, respectively, establishing its effectiveness and generalizability across diverse MoE architectures.

---


### 124. [OTT-Vid: Optimal Transport Temporal Token Compression for Video Large Language Models](https://arxiv.org/abs/2605.11803)

**<font color=#1a73e8>作者：</font>** Minseok Kang, Minhyeok Lee, Jungho Lee 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> As Video Large Language Models (Video-LLMs) scale to longer and more complex videos, their inference cost grows rapidly due to the large volume of visual tokens accumulated across frames. Training-free token compression has emerged as a practical solution to this bottleneck. However, existing temporal compression methods rely primarily on cross-frame token similarity or segmentation heuristics, overlooking each token's semantic role within its frame and failing to adapt compression strength to the compressibility of each frame pair. In this work, we propose OTT-Vid, a transport-derived allocation framework for temporal token compression. Our approach consists of two stages: spatial pruning identifies representative content within each frame, and optimal transport (OT) is then solved between neighboring frames to estimate temporal compressibility. We formulate this OT with non-uniform token mass, which protects semantically important tokens from aggressive compression, and a locality-aware cost that captures both feature and spatial disparities. The resulting transport plan jointly balances token importance and matching cost, while its total cost defines the transport difficulty of each frame pair, which we use to allocate compression budgets dynamically. Experiments on six benchmarks spanning video question answering and temporal grounding show that OTT-Vid preserves 95.8% of VQA and 73.9% of VTG performance while retaining only 10% of tokens, consistently outperforming existing state-of-the-art training-free compression methods.

---


### 125. [Why Users Go There: World Knowledge-Augmented Generative Next POI Recommendation](https://arxiv.org/abs/2605.11807)

**<font color=#1a73e8>作者：</font>** Qiuyu Ding, Heng-Da Xu, Wei Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Generative point-of-interest (POI) recommendation models based on large language models (LLMs) have shown promising results by formulating next POI prediction as a sequence generation task. However, the knowledge encoded in these models remains fixed after training, making them unable to perceive evolving real-world conditions that shape user mobility decisions, such as local events and cultural trends. To bridge this gap, we propose AWARE (Agent-based World knowledge Augmented REcommendation), which employs an LLM agent to generate location- and time-aware contextual narratives that capture regional cultural characteristics, seasonal trends, and ongoing events relevant to each user. Rather than introducing generic or noisy information, AWARE further anchors these narratives in each user's behavioral context, grounding external world knowledge in personalized spatial-temporal patterns. Extensive experiments on three real-world datasets demonstrate that AWARE consistently outperforms competitive baselines, achieving up to 12.4% relative improvement.

---


### 126. [Mitigating Action-Relation Hallucinations in LVLMs via Relation-aware Visual Enhancement](https://arxiv.org/abs/2605.11808)

**<font color=#1a73e8>作者：</font>** Zhenxin Qin, Qiang Li, Qingzhuo Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large Vision-Language Models (LVLMs) have achieved remarkable performance on diverse vision-language tasks. However, LVLMs still suffer from hallucinations, generating text that contradicts the visual input. Existing research has primarily focused on mitigating object hallucinations, but often overlooks more complex relation hallucinations, particularly action relations involving interactions between objects. In this study, we empirically observe that the primary cause of action-relation hallucinations in LVLMs is the insufficient attention allocated to visual information. Thus, we propose a framework to locate action-relevant image regions and enhance the LVLM's attention to those regions. Specifically, we define the Action-Relation Sensitivity (ARS) score to identify attention heads that are most sensitive to action-relation changes, thereby localizing action-relevant image regions that contain key visual cues. Then, we propose the Relation-aware Visual Enhancement (RVE) method to enhance the LVLM's attention to these action-relevant image regions. Extensive experiments demonstrate that, compared to existing baselines, our method achieves superior performance in mitigating action-relation hallucinations with negligible additional inference cost. Furthermore, it effectively generalizes to spatial-relation hallucinations and object hallucinations.

---


### 127. [Automated Reformulation of Robust Optimization via Memory-Augmented Large Language Models](https://arxiv.org/abs/2605.11813)

**<font color=#1a73e8>作者：</font>** Jinbiao Chen, Shuang Jin, Guoyun Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Robust optimization (RO) provides a principled framework for decision-making under uncertainty, but its practical use is often limited by the need to manually reformulate uncertain optimization models into tractable deterministic counterparts. Recent large language models (LLMs) have been shown promising for automating optimization formulation, yet RO reformulation remains challenging because it requires precise multi-step reasoning and mathematically consistent transformations. To facilitate systematic evaluation of LLM-based reformulation, for which no dedicated benchmark currently exists, we develop AutoRO-Bench, a benchmark featuring an automated data generation pipeline for the core RO reformulation task and a curated dataset for the RO application task. To address the reformulation challenge, we propose Automated Reformulation with Experience Memory (AutoREM), a tuning-free memory-augmented framework that autonomously builds a structured textual experience memory by reflecting on past failed trajectories through a tailored offline adaptation procedure. AutoREM requires neither domain-specific expert knowledge nor parameter updates, and the resulting memory readily transfers across different base LLMs. Experimental results show that AutoREM consistently improves the accuracy and efficiency of RO reformulation across in-distribution datasets, out-of-distribution datasets, and diverse base LLMs.

---


### 128. [Probabilistic Calibration Is a Trainable Capability in Language Models](https://arxiv.org/abs/2605.11845)

**<font color=#1a73e8>作者：</font>** Davide Baldelli, Sruthi Kuriakose, Maryam Hashemzadeh 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language models are increasingly used in settings where outputs must satisfy user-specified randomness constraints, yet their generation probabilities are often poorly calibrated to those targets. We study whether this capability can be improved directly through fine-tuning. Concretely, we fine-tune language models on synthetic prompts that require sampling from mathematical distributions, and compare two Calibration Fine-Tuning variants: a soft-target method that converts the desired output distribution into trie-derived next-token targets, and a hard-target method that trains on sampled completions from the same target distribution. Across 12 models spanning four families, both methods substantially improve structured-sampling fidelity on held-out distribution families and unseen parameter settings, showing that probabilistic calibration is a trainable capability. Under our selected training configurations, the two methods exhibit different empirical profiles: hard-target fine-tuning is often strongest on structured numeric sampling, while soft-target fine-tuning performs better on broader stochastic generation benchmarks, including open-ended random generation, multiple-choice answer-position balancing, and NoveltyBench. The gains sometimes reduce downstream capability, especially arithmetic reasoning, with costs varying by model. Overall, our results show that probabilistic calibration can be improved through fine-tuning, with our hard-target configuration favoring exact numeric fidelity and our soft-target configuration favoring broader stochastic transfer. Code is available at this https URL.

---


### 129. [GEAR: Granularity-Adaptive Advantage Reweighting for LLM Agents via Self-Distillation](https://arxiv.org/abs/2605.11853)

**<font color=#1a73e8>作者：</font>** Sijia Li, Yuchen Huang, Zifan Liu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning has become a widely used post-training approach for LLM agents, where training commonly relies on outcome-level rewards that provide only coarse supervision. While finer-grained credit assignment is promising for effective policy updates, obtaining reliable local credit and assigning it to the right parts of the long-horizon trajectory remains an open challenge. In this paper, we propose Granularity-adaptivE Advantage Reweighting (GEAR), an adaptive-granularity credit assignment framework that reshapes the trajectory-level GRPO advantage using token- and segment-level signals derived from self-distillation. GEAR compares an on-policy student with a ground-truth-conditioned teacher to obtain a reference-guided divergence signal for identifying adaptive segment boundaries and modulating local advantage weights. This divergence often spikes at the onset of a semantic deviation, while later tokens in the same autoregressive continuation may return to low divergence. GEAR therefore treats such spikes as anchors for adaptive credit regions: where the student remains aligned with the teacher, token-level resolution is preserved; where it departs, GEAR groups the corresponding continuation into an adaptive segment and uses the divergence at the departure point to modulate the segment' s advantage. Experiments across eight mathematical reasoning and agentic tool-use benchmarks with Qwen3 4B and 8B models show that GEAR consistently outperforms standard GRPO, self-distillation-only baselines, and token- or turn-level credit-assignment methods. The gains are especially strong on benchmarks with lower GRPO baseline accuracy, reaching up to around 20\% over GRPO, suggesting that the proposed adaptive reweighting scheme is especially useful in more challenging long-horizon settings.

---


### 130. [Self-Distilled Trajectory-Aware Boltzmann Modeling: Bridging the Training-Inference Discrepancy in Diffusion Language Models](https://arxiv.org/abs/2605.11854)

**<font color=#1a73e8>作者：</font>** Kecheng Chen, Ziru Liu, Xijia Tao 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Diffusion Language Models (DLMs) have recently emerged as a promising alternative to autoregressive language models, offering stronger global awareness and highly parallel generation. However, post-training DLMs with standard Negative Evidence Lower Bound (NELBO)-based supervised fine-tuning remains inefficient: training reconstructs randomly masked tokens in a single step, whereas inference follows a confidence-guided, multi-step easy-to-hard denoising trajectory. Recent trajectory-based self-distillation methods exploit such inference trajectories mainly for sampling-step compression and acceleration, often improving decoding efficiency without substantially enhancing the model's underlying capability, and may even degrade performance under full diffusion decoding. In this work, we ask whether self-distilled trajectories can be used not merely for faster inference, but for genuine knowledge acquisition. Although these trajectories lie on the pretrained DLM's own distributional manifold and thus offer a potentially lower optimization barrier, we find that naively fine-tuning on them with standard NELBO objectives yields only marginal gains. To address this limitation, we propose \textbf{T}rajectory-\textbf{A}ligned optimization via \textbf{Bo}ltzmann \textbf{M}odeling (\textbf{TABOM}), a self-distilled trajectory-based post-training framework that aligns training with the easy-to-hard structure of inference. TABOM models the inference unmasking preference as a Boltzmann distribution over predictive entropies and derives a tractable pairwise ranking objective to align the model's certainty ordering with the observed decoding trajectory. Empirically, TABOM achieves substantial gains in new domains, expands the effective knowledge boundary of DLMs, and significantly mitigates catastrophic forgetting compared with standard SFT.

---


### 131. [UniVLR: Unifying Text and Vision in Visual Latent Reasoning for Multimodal LLMs](https://arxiv.org/abs/2605.11856)

**<font color=#1a73e8>作者：</font>** Houcheng Jiang, Jiajun Fu, Junfeng Fang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models are increasingly expected to perform thinking with images, yet existing visual latent reasoning methods still rely on explicit textual chain-of-thought interleaved with visual latent tokens. This interleaved design limits efficiency and keeps reasoning fragmented across separate text and vision channels. We propose UniVLR, a unified visual latent reasoning framework that treats textual reasoning and auxiliary visual evidence as a shared visual workspace. Instead of preserving text CoT as an independent inference-time path, UniVLR renders reasoning traces together with auxiliary images and learns to compress this unified representation into compact visual latent tokens. At inference time, the model reasons only through visual latents and directly decodes the final answer, avoiding both external tool calls and verbose text reasoning. Experiments on real-world perception and visual reasoning tasks show that UniVLR outperforms prior visual latent reasoning methods while using substantially fewer generated reasoning tokens, suggesting a more unified and efficient paradigm for visual thinking in MLLMs.

---


### 132. [Beyond Parameter Aggregation: Semantic Consensus for Federated Fine-Tuning of LLMs](https://arxiv.org/abs/2605.11857)

**<font color=#1a73e8>作者：</font>** Amr Abourayya, Jens Kleesiek, Michael Kamp  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated fine-tuning of large language models is commonly formulated as a parameter aggregation problem. However, even parameter-efficient methods require transmitting large collections of trainable weights, assume aligned architectures, and rely on white-box access to model parameters. As model sizes continue to grow and deployments become increasingly heterogeneous, these assumptions become progressively misaligned with practical constraints. We consider an alternative formulation in which collaboration is mediated through model behavior rather than parameters. Clients fine-tune local models on private data and exchange generated outputs on a shared, public prompt set. The server maps these outputs into a semantic representation space, forms a per-prompt semantic consensus, and returns pseudo-labels for further local fine-tuning. This formulation fundamentally changes the communication scaling of federated LLM fine-tuning. The amount of information exchanged depends only on the public prompt budget and the size of the communicated behaviors, independent of model size. As a consequence, the protocol naturally accommodates heterogeneous architectures and applies directly to open-ended text generation. We present a theoretical analysis and empirical results demonstrating that this approach can match strong federated fine-tuning baselines while substantially reducing communication by orders of magnitude (e.g., analytically by a factor of $1006$ for Llama3.1-405B), as well as reductions in runtime and energy consumption. These results suggest that, for generative foundation models, behavior-level consensus provides a more appropriate abstraction for federated adaptation than parameter aggregation.

---


### 133. [LOFT: Low-Rank Orthogonal Fine-Tuning via Task-Aware Support Selection](https://arxiv.org/abs/2605.11872)

**<font color=#1a73e8>作者：</font>** Lanxin Zhao, Bamdev Mishra, Pratik Jawanpuria 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Orthogonal parameter-efficient fine-tuning (PEFT) adapts pretrained weights through structure-preserving multiplicative transformations, but existing methods often conflate two distinct design choices: the subspace in which adaptation occurs and the transformation applied within that subspace. This paper introduces LOFT, a low-rank orthogonal fine-tuning framework that explicitly separates these two components. By viewing orthogonal adaptation as a multiplicative subspace rotation, LOFT provides a unified formulation that recovers representative orthogonal PEFT methods, including coordinate-, butterfly-, Householder-, and principal-subspace-based variants. More importantly, this perspective exposes support selection as a central design axis rather than a byproduct of a particular parameterization. We develop a first-order analysis showing that useful adaptation supports should be informed by the downstream training signal, motivating practical task-aware support selection strategies. Across language understanding, visual transfer, mathematical reasoning, and multilingual out-of-distribution adaptation, LOFT recovers principal-subspace orthogonal adaptation while gradient-informed supports improve the efficiency-performance trade-off under matched parameter, memory, and compute budgets. These results suggest that principled support selection is an important direction for improving orthogonal PEFT.

---


### 134. [On-Policy Self-Evolution via Failure Trajectories for Agentic Safety Alignment](https://arxiv.org/abs/2605.11882)

**<font color=#1a73e8>作者：</font>** Bo Yin, Qi Li, Xinchao Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Tool-using LLM agents fail through trajectories rather than only final responses, as they may execute unsafe tool calls, follow injected instructions, comply with harmful requests, or over-refuse benign tasks despite producing a seemingly safe answer. Existing safety-alignment signals are largely response-level or off-policy, and often incur a safety-utility trade-off: improving agent safety comes at the cost of degraded task performance. Such sparse and single-objective rewards severely limit real-world usability. To bridge this gap, we propose FATE, an on-policy self-evolving framework that transforms verifier-scored failures into repair supervision without expert demonstrations. For each failure, the same policy proposes repair candidates, which are then re-scored by verifiers and filtered across security, utility, over-refusal control, and trajectory validity. This dense trajectory-level information is then used as a supervision signal for agent self-evolution. During this process, we further introduce Pareto-Front Policy Optimization (PFPO), combining supervised warmup with Pareto-aware policy optimization to preserve safety-utility trade-offs. Experiments on AgentDojo, AgentHarm, and ATBench show that FATE improves safety across different models and scales while preserving useful behavior. Compared with strong baselines, FATE reduces attack success rate by 33.5%, harmful compliance by 82.6%, and improves external trajectory-safety diagnosis by 6.5%. These results suggest that failed trajectories can provide structured repair supervision for safer self-evolving agents.

---


### 135. [Qwen-Scope: Turning Sparse Features into Development Tools for Large Language Models](https://arxiv.org/abs/2605.11887)

**<font color=#1a73e8>作者：</font>** Boyi Deng, Xu Wang, Yaoning Wang 等 18 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models have achieved remarkable capabilities across diverse tasks, yet their internal decision-making processes remain largely opaque, limiting our ability to inspect, control, and systematically improve them. This opacity motivates a growing body of research in mechanistic interpretability, with sparse autoencoders (SAEs) emerging as one of the most promising tools for decomposing model activations into sparse, interpretable feature representations. We introduce Qwen-Scope, an open-source suite of SAEs built on the Qwen model family, comprising 14 groups of SAEs across 7 model variants from the Qwen3 and Qwen3.5 series, covering both dense and mixture-of-expert architectures. Built on top of these SAEs, we show that SAEs can go beyond post-hoc analysis to serve as practical interfaces for model development along four directions: (i) inference-time steering, where SAE feature directions control language, concepts, and preferences without modifying model weights; (ii) evaluation analysis, where activated SAE features provide a representation-level proxy for benchmark redundancy and capability coverage; (iii) data-centric workflows, where SAE features support multilingual toxicity classification and safety-oriented data synthesis; and (iv) post-training optimization, where SAE-derived signals are incorporated into supervised fine-tuning and reinforcement learning objectives to mitigate undesirable behaviors such as code-switching and repetition. Together, these results demonstrate that SAEs can serve not only as post-hoc analysis tools, but also as reusable representation-level interfaces for diagnosing, controlling, evaluating, and improving large language models. By open-sourcing Qwen-Scope, we aim to support mechanistic research and accelerate practical workflows that connect model internals to downstream behavior.

---


### 136. [Rethinking Supervision Granularity: Segment-Level Learning for LLM-Based Theorem Proving](https://arxiv.org/abs/2605.11905)

**<font color=#1a73e8>作者：</font>** Shuo Xu, Jiakun Zhang, Junyu Lai 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Automated theorem proving with large language models in Lean 4 is commonly approached through either step-level tactic prediction with tree search or whole-proof generation. These two paradigms represent opposite granularities for constructing supervised training data: the former provides dense local signals but may fragment coherent proof processes, while the latter preserves global structure but requires complex end-to-end generation. In this paper, we revisit supervision granularity as a training set construction problem over proof trajectories and propose segment-level supervision, a training data construction strategy that extracts locally coherent proof segments for training policy models. We further reuse the same strategy at inference time to trigger short rollouts for existing step-level models. When trained with segment-level supervision on STP, LeanWorkbook, and NuminaMath-LEAN, the resulting policy models achieve proof success rates of 64.84%, 60.90%, and 66.31% on miniF2F, respectively, consistently outperforming both step-level and whole-proof baselines. Goal-aware rollout further improves existing step-level provers while reducing inference costs. It increases the proof success rate of BFS-Prover-V2-7B from 68.77% to 70.74% and that of InternLM2.5-StepProver from 59.59% to 60.33%, showing that appropriate supervision granularity better aligns model learning with proof structure and search. Code and models are available at this https URL.

---


### 137. [Procedural-skill SFT across capacity tiers: A W-Shaped pre-SFT Trajectory and Regime-Asymmetric Mechanism on 0.8B-4B Qwen3.5 Models](https://arxiv.org/abs/2605.11907)

**<font color=#1a73e8>作者：</font>** Igor Strozzi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We measure procedural-skill SFT contribution across three Qwen3.5 dense scales (0.8B, 2B, 4B) on a 200-task / 40-skill holdout, with Claude Haiku 4.5 as a frontier reference. The corpus is 353 rows of (task + procedural-skill block, Opus chain-of-thought, judge-pass) demonstrations.
\textbf{Main finding.} Under matched-path LLM-only scoring, the SFT-attributable procedural-$\Delta$ lift is roughly uniform across sizes: $+0.070$ / $+0.040$ / $+0.075$ at 0.8B / 2B / 4B. Variation in post-SFT $\Delta$ ($-0.005$, $+0.100$, $+0.065$) is dominated by a W-shaped pre-SFT base trajectory ($-0.075$, $+0.060$, $-0.010$, Haiku-4-5 at $+0.030$): the 5-step procedure hurts 0.8B and 4B, helps 2B, and helps frontier Haiku modestly. SFT works hardest in absolute terms where the base struggles with the procedure -- a regime-asymmetric pattern with a falsifiable prediction at 8B/14B.
\textbf{Methodology.} (i) A bench format-compliance artifact: 83.5\% of the holdout uses a deterministic \texttt{ANSWER}-line extractor that under-counts free-form conclusions; an LLM-only re-judge reveals it was systematically biased against \CU. (ii) A negative-iteration sequence at 0.8B: five recipe variants cluster post-SFT \CU{} pass-rate within a 2\,pp band, constraining the absolute-pass-rate ceiling to base capacity rather than recipe.
\textbf{Cross-family validation.} GPT-5.4 via OpenRouter on all 7 configurations (2800 paired episodes) agrees on the direction of every per-student finding: Cohen's $\kappa \geq 0.754$, agreement $\geq 93.25\%$.
Earlier ``format-only at 0.8B'' and ``shrinking SFT at 4B'' framings were path-mismatch artifacts; this paper supersedes both (Appendix~\ref{sec:appendix-path}). Single-seed; threats in §\ref{sec:threats}.

---


### 138. [STAGE: Tackling Semantic Drift in Multimodal Federated Graph Learning](https://arxiv.org/abs/2605.11919)

**<font color=#1a73e8>作者：</font>** Zekai Chen, Xun Wu, Xunkai Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated graph learning (FGL) enables collaborative training on graph data across multiple clients. As graph data increasingly contain multimodal node attributes such as text and images, multimodal federated graph learning (MM-FGL) has become an important yet substantially harder setting. The key challenge is that clients from different modality domains may not share a common semantic space: even for the same concept, their local encoders can produce inconsistent representations before collaboration begins. This makes direct parameter coordination unreliable and further causes two downstream problems: forcing heterogeneous client representations into a naively shared semantic space may create false semantic agreement, and graph message passing may amplify residual inconsistency across neighborhoods. To address this issue, we propose \textbf{STAGE}, a protocol-first framework for MM-FGL. Instead of relying on direct parameter averaging, STAGE builds a shared semantic space that first translates heterogeneous multimodal features into comparable representations and then regulates how these representations propagate over local graph structures. In this way, STAGE not only improves cross-client semantic calibration, but also reduces the risk of inconsistency amplification during graph learning. Extensive experiments on 8 multimodal-attributed graphs across 5 graph-centric and modality-centric tasks show that STAGE consistently achieves state-of-the-art performance while reducing per-round communication payload.

---


### 139. [Learn to Think: Improving Multimodal Reasoning through Vision-Aware Self-Improvement Training](https://arxiv.org/abs/2605.11931)

**<font color=#1a73e8>作者：</font>** Qihuang Zhong, Liang Ding, Wenjie Xuan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Post-training with explicit reasoning traces is common to improve the reasoning capabilities of Multimodal Large Language Models (MLLMs). However, acquiring high-quality reasoning traces is often costly and time-consuming. Hence, the self-improvement paradigm has emerged, enabling MLLMs to self-generate reasoning traces for training without external supervision. Despite its effectiveness, we reveal two shortcomings in the self-improvement training of MLLMs: 1) data imbalance, where simple samples are over-trained, but the challenging yet crucial samples are under-trained; 2) language prior bias, where MLLMs overly rely on linguistic priors while neglecting the visual cues. To this end, we propose VISTA, a vision-aware self-improvement training framework for enhancing the multimodal reasoning of MLLMs. Specifically, VISTA first introduces a prefix resampling strategy to reuse the partial correct reasoning traces for efficient data collection, and then designs a vision-aware attention score to quantify the model's focus on visual information. Extensive experiments show that VISTA can be applied to various post-training scenarios, i.e., supervised fine-tuning and preference learning, and effectively enhances the multimodal reasoning performance across various MLLMs and tasks, e.g., bringing up to +13.66% average performance gains for Qwen2.5-VL-3B-Instruct.

---


### 140. [From Noise to Diversity: Random Embedding Injection in LLM Reasoning](https://arxiv.org/abs/2605.11936)

**<font color=#1a73e8>作者：</font>** Heejun Kim, Seungpil Lee, Jewon Yeom 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent soft prompt research has tried to improve reasoning by inserting trained vectors into LLM inputs, yet whether the gain comes from the learned content or from the act of injection itself has not been carefully separated. We study Random Soft Prompts (RSPs), which drop the training step entirely and append a freshly drawn sequence of random embedding vectors to the input. Each RSP vector is sampled from an isotropic Gaussian fitted to the entrywise mean and variance of the pretrained embedding table; the sequence carries no learned content, and yet reaches accuracy comparable to optimized soft prompts on math reasoning benchmarks in several settings. The mechanism unfolds in two stages: because attention has to absorb a never-seen-before random position, the distribution over the first few generated tokens flattens and reasoning trajectories branch, and as generation continues this influence dilutes naturally so the response commits to a single completion. We show that during inference RSPs lift early-stage token diversity and, combined with temperature sampling, widen Pass@N, the probability that at least one out of N attempts is correct. Beyond inference, we carry the same effect into DAPO training and demonstrate practical gains. Our contributions are: (i) RSP isolates the simplest form of soft prompt -- training-free, freshly resampled -- providing a unified lens for the structural effect of injection that variants otherwise differing in training and form all share; (ii) a theoretical and empirical validation of the underlying mechanism; and (iii) an extension from inference to training.

---


### 141. [Cluster-Aware Neural Collapse Prompt Tuning for Long-Tailed Generalization of Vision-Language Models](https://arxiv.org/abs/2605.11939)

**<font color=#1a73e8>作者：</font>** Boyang Guo, Liang Li, Lin Peng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Prompt learning has emerged as an efficient alternative to fine-tuning pre-trained vision-language models (VLMs). Despite its promise, current methods still struggle to maintain tail-class discriminability when adapting to class-imbalanced datasets. In this work, we propose cluster-aware neural collapse prompt tuning (CPT), which enhances the discriminability of tail classes in prompt-tuned VLMs without sacrificing their overall generalization. First, we design a cluster-invariant space by mining semantic assignments from the pre-trained VLM and mapping them to prompt-tuned features. This computes cluster-level boundaries and restricts the constraints to local neighborhoods, which reduces interference with the global semantic structure of the pre-trained VLM. Second, we introduce neural-collapse-driven discriminability optimization with three losses: textual Equiangular Tight Frame (ETF) separation loss, class-wise convergence loss, and rotation stabilization loss. These losses work together to shape intra-cluster geometry for better inter-class separation and intra-class alignment. Extensive experiments on 11 diverse datasets demonstrate that CPT outperforms SOTA methods, with stronger performance on long-tail classes and good generalization to unseen classes.

---


### 142. [Counterfactual Trace Auditing of LLM Agent Skills](https://arxiv.org/abs/2605.11946)

**<font color=#1a73e8>作者：</font>** Xiaolin Zhou, Jinbo Liu, Li Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Model agents are increasingly augmented with agent skills. Current evaluation methods for skills remain limited. Most deployed benchmarks report only pass rate before and after a skill is attached, treating the skill as a black box change to agent behavior. We introduce Counterfactual Trace Auditing (CTA), a framework for measuring how a skill changes agent behavior. CTA pairs each with skill agent trace with a without skill counterpart on the same task, segments both traces into goal directed phases, aligns the phases, and emits structured Skill Influence Pattern (SIP) annotations. These annotations describe the behavioral effect of a skill rather than only its task outcome. We instantiate CTA on SWE-Skills-Bench with Claude across 49 software engineering tasks. The resulting audit reveals a clear evaluation gap. Pass rate changes by only +0.3 percentage points on average, suggesting little aggregate effect. Yet CTA identifies 522 SIP instances across the same paired traces, showing that the skills substantially reshape agent behavior even when pass rate is nearly unchanged. The audit also separates several recurring effects that pass rate cannot detect, including literal template copying, off task artifact creation, excess planning, and task recovery. Three findings emerge. First, high baseline tasks contain most of the observed skill effects, although their pass rate is already saturated and therefore cannot reflect those effects. Second, tasks with moderate baseline performance show the most recoverable gain, but often at substantially higher token cost. Third, the dominant SIP type can be identified by baseline bucket: surface anchoring is most common on ceiling tasks and edge-case prompting is most common on mid-range and floor tasks. These regularities turn informal failure mode observations into reproducible behavioral measurements.

---


### 143. [Assessing and Mitigating Miscalibration in LLM-Based Social Science Measurement](https://arxiv.org/abs/2605.11954)

**<font color=#1a73e8>作者：</font>** Jinyuan Wang, Ningyuan Deng, Yi Yang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used in social science as scalable measurement tools for converting unstructured text into variables that can enter standard empirical designs. Measurement validity demands more than high average accuracy, which requires well calibrated confidence that faithfully reflects the empirical probability of each measurement being correct. This paper studies the model miscalibration in LLM-based social science measurement. We begin with a case study on FOMC and show that confidence based filtering can change downstream regression estimates when LLM confidence is miscalibrated. We then audit calibration across 14 social science constructs covering both proprietary models, including GPT-5-mini, DeepSeek-V3.2, and open source models. Across tasks and model families, reported confidence is poorly aligned with tolerance-based correctness. As a simple mitigation, we propose a soft label distillation pipeline for calibrating Bert with LLM. The method converts an LLM score and its verbalized confidence into a soft target distribution, then trains a smaller discriminative classifier on encoder models for these targets. Averaged across datasets, this approach reduces ECE by 43.2\% and Brier by 34.0\%. These results suggest that LLM-based social science pipelines should treat calibration as part of measurement validity, rather than as an optional post-processing concern.

---


### 144. [Multimodal Abstractive Summarization of Instructional Videos with Vision-Language Models](https://arxiv.org/abs/2605.11959)

**<font color=#1a73e8>作者：</font>** Maham Nazir, Muhammad Aqeel, Richong Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal video summarization requires visual features that align semantically with language generation. Traditional approaches rely on CNN features trained for object classification, which represent visual concepts as discrete categories not aligned with natural language. We propose ClipSum, a framework that leverages frozen CLIP vision-language features with explicit temporal modeling and dimension-adaptive fusion for instructional video summarization. CLIP's contrastive pre-training on 400M image-text pairs yields visual features semantically aligned with the linguistic concepts that text decoders generate, bridging the vision-language gap at the representation level. On YouCook2, ClipSum achieves 33.0% ROUGE-1 versus 30.5% for ResNet-152 with 4x lower dimensionality (512 vs. 2048), demonstrating that semantic alignment matters more than feature capacity. Frozen CLIP (33.0%) surpasses fine-tuned CLIP (32.3%), showing that preserving pre-trained alignment is more valuable than task-specific adaptation. this https URL

---


### 145. [Towards Order Fairness: Mitigating LLMs Order Sensitivity through Dual Group Advantage Optimization](https://arxiv.org/abs/2605.11974)

**<font color=#1a73e8>作者：</font>** Xu Chu, Guanyu Wang, Zhijie Tan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) suffer from order bias, where their performance is affected by the arrangement order of input elements. This unfairness limits the model's applications in scenarios such as in-context learning and Retrieval-Augmented Generation (RAG). Recent studies attempt to obtain optimal or suboptimal arrangements based on statistical results or using dataset-based search, but these methods increase inference overhead while leaving the model's inherent order bias unresolved. Other studies mitigate order sensitivity through supervised fine-tuning using augmented training sets with multiple order variants, but often at the cost of accuracy, trapping the model in consistent yet incorrect hallucinations. In this paper, we propose \textbf{D}ual \textbf{G}roup \textbf{A}dvantage \textbf{O}ptimization (\textbf{DGAO}), which aims to improve model accuracy and order stability simultaneously. DGAO calculates and balances intra-group relative accuracy advantage and inter-group relative stability advantage, rewarding the policy model for generating order-stable and correct outputs while penalizing order-sensitive or incorrect responses. This marks the first time reinforcement learning has been used to mitigate LLMs' order sensitivity. We also propose two new metrics, Consistency Rate and Overconfidence Rate, to reveal the pseudo-stability of previous methods and guide more comprehensive evaluation. Extensive experiments demonstrate that DGAO achieves superior order fairness while improving performance on RAG, mathematical reasoning, and classification tasks. Our code is available at: this https URL.

---


### 146. [On Predicting the Post-training Potential of Pre-trained LLMs](https://arxiv.org/abs/2605.11978)

**<font color=#1a73e8>作者：</font>** Xiaoyuan Li, Yubo Ma, Kexin Yang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The performance of Large Language Models (LLMs) on downstream tasks is fundamentally constrained by the capabilities acquired during pre-training. However, traditional benchmarks like MMLU often fail to reflect a base model's plasticity in complex open-ended scenarios, leading to inefficient model selection. We address this by introducing a new task of predicting post-training potential - forecasting a base model's performance before post-training. We propose RuDE (Rubric-based Discriminative Evaluation), a unified framework that bypasses the generation gap of base models by leveraging response discrimination. Guided by our systematic 4C Taxonomy, RuDE constructs controlled contrastive pairs across diverse domains by fine-grained rubric violations. Extensive experiments demonstrate a correlation greater than 90% with post-training performance. Crucially, validation via Reinforcement Learning (RL) confirms that RuDE effectively identifies high-potential smaller models that outperform larger counterparts, offering a compute-efficient mechanism for foundation model development.

---


### 147. [On the Limitations of Large Language Models for Conceptual Database Modeling](https://arxiv.org/abs/2605.11986)

**<font color=#1a73e8>作者：</font>** Arthur F. Siqueira, Carlos D. S. Nogueira, Eduarda Farias 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This article analyzes the use of Large Language Models (LLMs) as support for the conceptual modeling of relational databases through the automatic generation of Entity-Relationship (ER) diagrams from natural language requirements. The approach combines different language models with prompt engineering techniques to evaluate their ability to identify entities, relationships, and attributes in a conceptually consistent manner. The experimental evaluation involved three LLMs, each subjected to three prompting techniques (Zero-Shot, Chain of Thought, and Chain of Thought + Verifier), applied to the same requirements scenario with progressively increasing complexity. The generated diagrams were qualitatively analyzed through direct comparison with the textual requirements, considering the structural and semantic adherence of the modeled elements. The results indicate that, although LLMs show reasonable performance in less complex scenarios, their reliability decreases as the complexity of the requirements increases, with a rise in inconsistencies, ambiguities, and failures in representing constraints. These findings reinforce that, in their current state, LLMs are not sufficiently mature for reliable use in complex scenarios, and the cost of validation may offset the apparent productivity gains.

---


### 148. [BadSKP: Backdoor Attacks on Knowledge Graph-Enhanced LLMs with Soft Prompts](https://arxiv.org/abs/2605.11996)

**<font color=#1a73e8>作者：</font>** Xiaoting Lyu, Yufei Han, Hangwei Qian 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent knowledge graph (KG)-enhanced large language models (LLMs) move beyond purely textual knowledge augmentation by encoding retrieved subgraphs into continuous soft prompts via graph neural networks, introducing a graph-conditioned channel that operates alongside the standard text interface. However, existing backdoor attacks are largely designed for the textual channel, and their effectiveness against this dual-channel architecture remains unclear. We show that this architecture creates a robustness gap: text-channel backdoor attacks that readily compromise textual KG prompting systems become largely ineffective against soft-prompt-based counterparts. We interpret this gap through semantic anchoring, whereby graph-derived soft prompts bias the generation-driving hidden state toward query-consistent semantics and suppress surface-level malicious instructions. Because this anchoring effect is itself induced by the graph channel, an attacker who manipulates graph-level representations can in turn redirect it toward adversarial semantics. To demonstrate this risk, we propose BadSKP, a backdoor attack that targets the graph-to-prompt interface through a multi-stage optimization strategy: it constructs adversarial target embeddings, optimizes poisoned node embeddings to steer the induced soft prompt, and approximates the optimized representations with fluent adversarial node attributes. Experiments on two soft-prompt KG-enhanced LLMs across four datasets show that BadSKP achieves high attack success under both frozen and trojaned settings, while text-only attacks remain unreliable even under perplexity-based defenses.

---


### 149. [Learning Agentic Policy from Action Guidance](https://arxiv.org/abs/2605.12004)

**<font color=#1a73e8>作者：</font>** Yuxiang Ji, Zengbin Wang, Yong Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Agentic reinforcement learning (RL) for Large Language Models (LLMs) critically depends on the exploration capability of the base policy, as training signals emerge only within its in-capability region. For tasks where the base policy cannot reach reward states, additional training or external guidance is needed to recover effective learning signals. Rather than relying on costly iterative supervised fine tuning (SFT), we exploit the abundant action data generated in everyday human interactions. We propose \textsc{ActGuide-RL}, which injects action data as plan-style reference guidance, enabling the agentic policy to overcome reachability barriers to reward states. Guided and unguided rollouts are then jointly optimized via mixed-policy training, internalizing the exploration gains back into the unguided policy. Motivated by a theoretical and empirical analysis of the benefit-risk trade-off, we adopt a minimal intervention principle that invokes guidance only as an adaptive fallback, matching task difficulty while minimizing off-policy risk. On search-agent benchmarks, \textsc{ActGuide-RL} substantially improves over zero RL (+10.7 pp on GAIA and +19 pp on XBench with Qwen3-4B), and performs on par with the SFT+RL pipeline without any cold start. This suggests a new paradigm for agentic RL that reduces the reliance on heavy SFT data by using scalable action guidance instead.

---


### 150. [LegalCheck: Retrieval- and Context-Augmented Generation for Drafting Municipal Legal Advice Letters](https://arxiv.org/abs/2605.12012)

**<font color=#1a73e8>作者：</font>** Virgill van der Meer, Julien Rossi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Public-sector legal departments in the Netherlands face acute staff shortages, increased case volumes, and increased pressure to meet regulatory compliance. This paper presents LegalCheck, a novel system that addresses these challenges by automating the drafting of objection response letters through a combination of Retrieval-Augmented Generation (RAG) and Context-Augmented Generation (CAG). Using a large language model (LLM) alongside curated legal knowledge bases, LegalCheck performs retrieval of relevant laws and precedents, and uses controlled prompting to incorporate both external knowledge and case-specific details into a coherent draft. An expert-in-the-loop review ensures that each generated letter is legally sound and contextually appropriate. In a real-world deployment within the Municipality of Amsterdam, LegalCheck produced near-final advice letters in minutes rather than hours, while maintaining high legal consistency and factual accuracy. The output is based on actual regulations and prior cases, providing explainable outputs that captured the vast majority of required legal reasoning (often 80\% to 100\% of essential content). Legal professionals found that the system reduced their workload and ensured a consistent application of legal standards, without replacing human judgment. These results demonstrate substantial efficiency gains, improved legal consistency, and positive user acceptance. More broadly, this work illustrates how responsible AI can be deployed in the legal domain by augmenting LLMs with domain knowledge and governance mechanisms.

---


> [!TIP]
> 当前位于：**101-150**（第 3/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-223](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
