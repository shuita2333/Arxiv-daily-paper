# 🧠 大模型相关研究 | 2026年05月23日

> 本类共 **162** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**101-150**（第 3/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-162](./part-04.md)

---

### 101. [EvoIR-Agent: Self-Evolving Image Restoration Agentic System via Experience-Driven Learning](https://arxiv.org/abs/2605.22208)

**<font color=#1a73e8>作者：</font>** Kailin Zhuang, Jiawei Wu, Zhi Jin  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Model (MLLM)-driven image restoration agent demonstrates effectiveness in degradation coupling scenarios by flexibly selecting tools and determining removal orders. However, their zero-shot planning often fails without experience, necessitating severe trial-and-error overhead to achieve satisfactory outcomes. Currently, two paradigms are employed to address this issue, yet a dilemma persists: Training-based methods embed intrinsic experience into parameters, achieving high inference efficiency but lacking compatibility with new tools or degradation. In contrast, training-free methods utilize explicit experience storage for compatibility but still incur trial-and-error overhead due to naive experience. To resolve the dilemma, we propose EvoIR-Agent, which first systematically formulates the experience components of a training-free image restoration agent. Subsequently, a hierarchical experience pool is constructed, which enables coarse-to-fine guidance for diverse tools and removal orders. Furthermore, a self-evolving mechanism is introduced to update the pool from scratch using accumulated records, thereby greatly improving performance and efficiency. Extensive experiments reveal that EvoIR-Agent achieves a significant lead in the full reference metrics and yields a remarkable Pareto-optimal balance between performance and efficiency compared to the state-of-the-art methods.

---


### 102. [CLORE: Content-Level Optimization for Reasoning Efficiency](https://arxiv.org/abs/2605.22211)

**<font color=#1a73e8>作者：</font>** Yuyang Wu, Qiyao Xue, Guanxing Lu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning post-training has improved the reasoning ability of large language models, but often produces unnecessarily long, repetitive, or semantically opaque reasoning traces. Existing efficient reasoning methods mainly regulate response length through explicit budgets or length-aware rewards, leaving intermediate reasoning content weakly supervised. We propose CLORE, a content-level optimization framework that improves reasoning efficiency by editing correct on-policy rollouts. CLORE uses an external augmentation model to delete repetitive segments, illegible or task-irrelevant content, and superfluous reasoning after the solution is established, while preserving the final answer. The resulting augmented--original pairs are optimized with an auxiliary reference-free DPO objective alongside standard policy-gradient training. By restricting augmentation to correct trajectories and performing local deletion, CLORE keeps edited rollouts close to the policy distribution and mitigates off-policy mismatch. Experiments on DeepSeek-R1-Distill-Qwen-7B and Qwen2.5-Math-7B across five mathematical reasoning benchmarks show that CLORE improves the accuracy--efficiency trade-off and remains compatible with GRPO, DAPO, Training Efficient, and ThinkPrune. Content-level analyses further show that CLORE reduces repetitive reasoning, illegible content, and post-answer exploration, supporting content-level supervision as a complementary direction to length-level control.

---


### 103. [SGR-Bench: Benchmarking Search Agents on State-Gated Retrieval](https://arxiv.org/abs/2605.22219)

**<font color=#1a73e8>作者：</font>** Ningyuan Li, Haiyang Shen, Mugeng Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent advances in large language models and tool-using agents have expanded the range of benchmarked web tasks. Yet an important class of specialized retrieval tasks remains undercharacterized. On many specialized data-retrieval websites, answer-bearing evidence becomes accessible only after establishing the correct site-specific retrieval state through filters, views, hierarchies, or scopes. We term this capability state-gated retrieval (SGR). We introduce SGR-Bench, a benchmark for this setting containing 100 expert-curated tasks spanning six source families and 12 public data ecosystems. Each task requires discovering the appropriate website and configuring its site-specific retrieval state to produce a structured answer. SGR-Bench pairs constraint-guided and goal-oriented formulations of the same underlying problems, enabling controlled comparisons between explicit and implicit guidance for state-gated retrieval. We evaluate eight CLI-based agentic LLM systems and three commercial search-agent products. On SGR-Bench, the strongest system reaches only 66.18% item-level F1, while row-level F1 remains much lower. A manual audit of 156 analyzable failed CLI trajectories shows why: agents often reach a relevant web source, but establish the wrong site-specific retrieval state. Retrieval-scope drift (37.2%) and criterion mismatch (27.6%) dominate, whereas final answer composition accounts for only 10.3%. The dataset and single-case evaluation instructions are available at this https URL.

---


### 104. [ARC-STAR: Auditable Post-Hoc Correction for PDE Foundation Models](https://arxiv.org/abs/2605.22222)

**<font color=#1a73e8>作者：</font>** Chengze Li, Lingwei Wei, Li Sun 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Partial differential equation (PDE) foundation models are pretrained networks that forecast how physical fields like velocity and pressure evolve from a single reusable solver. On unfamiliar flows their predictions drift step by step, errors concentrate in a few regions, yet retraining destabilizes the network and uniform post-hoc correction overlooks this spatial concentration. To address this, we propose a frozen-solver post-hoc correction framework, Adaptive Risk-Calibrated Spatial Triage for Auditable Refinement (ARC-STAR). ARC-STAR organizes correction into three stages: a global corrector removes broad solver bias, a blockwise local refiner cleans the post-global residual, and, at deployment, a label-free score routes refinement to high-risk blocks under a compute budget. The framework is designed to be (i) frozen-host, preserving the pretrained solver without fine-tuning; (ii) auditable, with global and local stages trained and evaluated separately for measurable contributions; and (iii) budget-aware, using a blockwise interface that either refines the full field or routes limited compute to high-risk regions. Across five flow benchmarks spanning ten regime cells, ARC-STAR is the only method that cuts velocity rollout error by at least 36x over raw Poseidon on every cell. The global stage reduces raw host error by 91-99%, and the local stage further reduces the remaining post-global residual by up to 94.4%. Our code implementation is available at this https URL.

---


### 105. [Evaluating Large Language Models as Live Strategic Agents: Provider Performance, Hybrid Decomposition, and Operational Gaps in Timed Risk Play](https://arxiv.org/abs/2605.22238)

**<font color=#1a73e8>作者：</font>** H. C. Ekne  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Static benchmarks capture only part of how large language models behave in practice. Real systems place models inside repeated loops with time limits, formatting constraints, and failure modes. We study this setting in a timed multi-phase Risk environment with explicit victory targets and repeated planning and execution cycles. In a replicated 32-game cross-provider championship under frozen rules, gemini-3.1-pro-preview won 20 of 32 games against gpt-5.1, claude-opus-4-7, and kimi-k2.6, and the pooled winner distribution differs strongly from an equal-strength null (p approx 1.5 x 10^-5). We then separate planning from execution by standardizing execution on a cheaper Gemini Flash scaffold. Under this design, a pooled 32-game planner bakeoff is consistent with near-equality (p approx 0.821), which indicates that much of the earlier provider spread came from end-to-end system behavior rather than planning alone. To study mechanism, we analyze saved planning and execution traces from the provider championship. Gemini refers to the terminal objective far more often than the other models and increases that focus as victory approaches. Gemini also converts more turns into deep conquest chains, even though it is not the cleanest runtime. These results show that live-agent performance depends on objective tracking, execution conversion, cost, and runtime reliability, and they support evaluating LLMs as components in bounded workflows rather than as isolated benchmark respondents.

---


### 106. [Harder to Defend: Towards Chinese Toxicity Attacks via Implicit Enhancement and Obfuscation Rewriting](https://arxiv.org/abs/2605.22258)

**<font color=#1a73e8>作者：</font>** Jingyi Kang, Junyu Lu, Bo Xu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) require robust toxicity evaluation beyond explicit wording. This setting remains underexplored in Chinese, where toxicity may combine semantic indirectness with surface obfuscation. We introduce Chinese Implicit Toxicity Attack (CITA), a controlled red-team evaluation and defense-data generation framework, not a deployable evasion tool. CITA uses three stages: (i) Harmful Intent Learning, (ii) Implicit Toxicity Enhancement, and (iii) Obfuscation Variant Rewriting, to preserve harmful intent, increase implicitness, and add controlled surface variants. On CITA-generated evaluation samples, the seven tested detectors exhibit substantial missed-detection risks, reaching an average ASR of 69.48%; human evaluation further confirms preserved harmfulness and increased implicitness/evasiveness. As a downstream defense application, we fine-tune a Chinese Implicit Toxicity Defense model (CITD) with CITA-generated red-team data, showing that such data can improve robustness through additional training.

---


### 107. [Tailoring Teaching to Aptitude: Direction-Adaptive Self-Distillation for LLM Reasoning](https://arxiv.org/abs/2605.22263)

**<font color=#1a73e8>作者：</font>** Hongbin Zhang, Chaozheng Wang, Kehai Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy self-distillation (OPSD) is an emerging LLM post-training paradigm in which the model serves as its own teacher: conditioned on privileged information such as a reference trace or hint, the same policy provides dense token-level supervision on its own rollouts. However, recent studies show that OPSD degrades complex reasoning by suppressing predictive uncertainty, which supports exploration and hypothesis revision. Our token-level analysis shows that this failure arises from applying a uniform direction of teacher supervision across tokens with different uncertainty levels: conformity to the privileged self-teacher suppresses exploration at high entropy, while deviation from the teacher degrades step accuracy at low entropy. Accordingly, we propose \textbf{Direction-Adaptive Self-Distillation} (\textbf{DASD}), which reframes privileged self-distillation from uniform teacher imitation into entropy-routed directional supervision: high-entropy tokens are pushed away from the privileged teacher to preserve exploration, while low-entropy tokens are pulled toward the teacher to stabilize step-level execution. Across six mathematical reasoning benchmarks, DASD achieves the best macro Avg@16 over strong RLVR and self-distillation baselines. Pass@$k$, reasoning-health, and generalization analyses show that these average gains come from preserving exploration without sacrificing step-level execution.

---


### 108. [SciCore-Mol: Augmenting Large Language Models with Pluggable Molecular Cognition Modules](https://arxiv.org/abs/2605.22287)

**<font color=#1a73e8>作者：</font>** Yuxuan Chen, Changwei Lv, Yunduo Xiao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are central to the one-for-all intelligent paradigm, but they face a fundamental challenge when dealing with heterogeneous scientific data such as molecules: the inherent gap between discrete linguistic symbols and topological molecular or continuous reaction data leads to significant information loss and semantic noise in text-based reasoning. We propose SciCore-Mol, a modular framework that bridges this gap through three deeply integrated pluggable cognitive modules: a topology-aware perception module, a latent diffusion-based molecular generation module, and a reaction-aware reasoning module. Each module is coupled to the LLM backbone through learned representation interfaces, enabling richer information exchange than is possible with text-only tool feedback. Our experiments on diverse chemical tasks demonstrate that SciCore-Mol achieves strong comprehensive performance across molecular understanding, generation, reaction prediction, and general chemistry knowledge, with an 8B-parameter open-source system that is competitive with and in several dimensions surpasses proprietary large models. This work provides a systematic blueprint for equipping LLMs with scientific expertise through decoupled, pluggable, and flexibly orchestrated modules, with direct implications for drug design, chemical synthesis, and broader scientific discovery.

---


### 109. [One LR Doesn't Fit All: Heavy-Tail Guided Layerwise Learning Rates for LLMs](https://arxiv.org/abs/2605.22297)

**<font color=#1a73e8>作者：</font>** Di He, Songjun Tu, Keyu Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning rate configuration is a fundamental aspect of modern deep learning. The prevailing practice of applying a uniform learning rate across all layers overlooks the structural heterogeneity of Transformers, potentially limiting their effectiveness as the backbone of Large Language Models (LLMs). In this paper, we introduce Layerwise Learning Rate (LLR), an adaptive scheme that assigns distinct learning rates to individual Transformer layers. Our method is grounded in Heavy-Tailed Self-Regularization (HT-SR) theory, which characterizes the empirical spectral density (ESD) of weight correlation matrices to quantify heavy-tailedness. Layers with weaker heavy-tailedness are assigned larger learning rates to accelerate their training, while layers with stronger heavy-tailedness receive smaller learning rates. By tailoring learning rates in this manner, LLR promotes balanced training across layers, leading to faster convergence and improved generalization. Extensive experiments across architectures (from LLaMA to GPT-nano), optimizers (AdamW and Muon), and parameter scales (60M-1B) demonstrate that LLR achieves up to 1.5x training speedup and outperforms baselines, notably raising average zero-shot accuracy from 47.09% to 49.02%. A key advantage of LLR is its low tuning overhead: it transfers nearly optimal LR settings directly from the uniform baseline. Code is available at this https URL.

---


### 110. [Meta-Soft: Leveraging Composable Meta-Tokens for Context-Preserving KV Cache Compression](https://arxiv.org/abs/2605.22337)

**<font color=#1a73e8>作者：</font>** Wei Luo, Yi Huang, Songchen Ma 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The KV cache used in large language models has linearly growing time complexity, so LLMs face memory blow-up and reduced decoding efficiency when they process long this http URL KV Cache eviction has become an important research direction; however, existing methods based on fixed Soft Tokens (e.g., Judge Q) rely on a static parameter set as the query to evaluate the importance of KV pairs, so they cannot adapt dynamically to different input prompts, and they cannot precisely capture complex and changing task this http URL, evicted KV pairs are discarded permanently, so this causes irreversible information loss and context breaks. To address this problem, we propose Meta-Soft, a dynamic compression framework based on probe-driven context integration. Specifically, we build a meta-library with a learnable orthogonal basis matrix $\mathcal{L}$, and we use a selector network with Gumbel-Softmax to produce differentiable sparse combination weights, so we dynamically synthesize the most targeted $k$ Soft Tokens from the input prompt this http URL append these Soft Tokens to the end of the input sequence to probe key information. We also introduce an attention-flow based integration mechanism, which redistributes the semantic information of removed tokens into retained tokens, and this keeps the dropped context information this http URL on multiple datasets show that our method outperforms existing state-of-the-art eviction methods and provides a new solution for KV Cache compression.

---


### 111. [Bernini: Latent Semantic Planning for Video Diffusion](https://arxiv.org/abs/2605.22344)

**<font color=#1a73e8>作者：</font>** Bernini Team, Chenchen Liu, Junyi Chen 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) and diffusion models have each reached remarkable maturity: MLLMs excel at reasoning over heterogeneous multimodal inputs with strong semantic grounding, while diffusion models synthesize images and videos with photorealistic fidelity. We argue that these two families can be unified through a simple division of labor: MLLMs perform semantic planning, while diffusion models render pixels from high-level semantic guidance and low-level visual features. Building on this idea, we propose Bernini, a unified framework for video generation and editing. An MLLM-based planner predicts the target semantic representation directly in the ViT embedding space, and a DiT-based renderer synthesizes pixels conditioned on this plan, augmented by text features and, for editing, source VAE features for detail preservation. Because semantics serve as the interface, the planner and renderer can be trained separately and only lightly co-trained, preserving the pretrained strengths of both components while keeping training efficient. To better handle multiple visual inputs, we introduce Segment-Aware 3D Rotary Positional Embedding (SA-3D RoPE), and further incorporate chain-of-thought reasoning in the planner to better transfer understanding into generation. Bernini achieves state-of-the-art performance across a wide range of video generation and editing benchmarks, with the MLLM's pretrained understanding translating into strong generalization on challenging editing tasks.

---


### 112. [Modeling Pathology-Like Behavioral Patterns in Language Models Through Behavioral Fine-Tuning](https://arxiv.org/abs/2605.22356)

**<font color=#1a73e8>作者：</font>** Nicola Milano, Davide Marocco  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly used as computational tools for modeling human-like behavior. We introduce a behavioral induction framework that modifies model policies through fine-tuning on structured decision-making tasks: using synthetic datasets inspired by maladaptive behavioral patterns, including depression and paranoia, we train transformer-based language models to consistently select specific classes of actions across diverse contexts. We then test whether this behavioral optimization produces systematic changes in generative distributions.
Across two architectures, fine-tuned models show stable, context-general shifts in next-token probability distributions, including increased probability assigned to negative and threat-related interpretations in open-ended language tasks. These effects generalize beyond training contexts and are detectable in qualitative completions, psychometric-style evaluations, and quantitative distributional metrics such as Jensen-Shannon divergence.
Induced behavioral profiles also show partial specificity. Models optimized for different behavioral patterns exhibit dissociable response tendencies across evaluation probes, suggesting that structured behavioral training produces differentiated policy-level biases rather than generic distributional skew.
We interpret these findings as evidence that consistent behavioral optimization in LLMs can generate stable behavioral and distributional patterns consistent with altered latent priors, linking action selection and language generation. More broadly, the results support a view of LLMs as policy-based systems in which behavioral constraints shape emergent representational structure, highlighting their potential as controlled testbeds for studying the relationship between behavior, interpretation, and generative language in computational models of cognition.

---


### 113. [AgroTools: A Benchmark for Tool-Augmented Multimodal Agents in Agriculture](https://arxiv.org/abs/2605.22366)

**<font color=#1a73e8>作者：</font>** Zi Ye, Yibin Wen, Xiaoya Fan 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Agricultural decision-making increasingly requires multimodal systems that can transform visual observations into reliable, executable actions. However, existing agricultural multimodal benchmarks mainly evaluate final-answer correctness and provide limited support for assessing whether models can use external tools to complete precision-sensitive workflows. In this paper, we introduce AgroTools, a benchmark for evaluating tool-augmented multimodal agents in agriculture. AgroTools contains 539 question-answer instances paired with 1,097 heterogeneous agricultural images, spanning five task families and an executable environment of 14 agricultural tools. Each query is annotated with structured tool-use traces, enabling a dual-view evaluation of both process-level execution quality and outcome-level task success. We benchmark 9 open-source and 4 closed-source multimodal large language models on AgroTools. Results show that current models remain far from reliable in agricultural tool-use settings, with clear bottlenecks in tool planning, argument generation, execution recovery, and final-answer synthesis. We hope AgroTools will support future research on multimodal agents for high-precision agricultural applications. The benchmark and evaluation are available at this https URL.

---


### 114. [Target-Aligned Bellman Backup for Cross-domain Offline Reinforcement Learning](https://arxiv.org/abs/2605.22376)

**<font color=#1a73e8>作者：</font>** Wei Liu, Ting Long  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Cross-domain offline reinforcement learning (CDRL) aims to improve policy learning in a target domain by leveraging data collected from a source domain. Existing works typically assess the transferability of source-domain data by measuring its similarity to target-domain transitions, and implicitly perform transition-level selection. Transitions that are considered similar are assigned higher weights or rewards, while dissimilar ones are down-weighted. However, transition-level similarity does not necessarily imply consistency in long-term returns. Even visually or dynamically similar transitions may lead to significantly different outcomes in the target domain, which can mislead policy learning and degrade performance. To address this issue, we revisit the fundamental objective of policy learning. Since policy optimization ultimately relies on Bellman targets to evaluate the quality of decisions, we propose to assess the transferability of source-domain transitions based on their alignment with target-domain Bellman targets, rather than superficial transition similarity. Based on this insight, we propose a method termed Target-Aligned Bellman Backup (TABB), which selectively leverages source-domain data by measuring their contribution to accurate Bellman target estimation in the target domain. We evaluate TABB across a broad range of cross-domain offline RL settings with highly limited target-domain data. Experimental results show that TABB consistently achieves strong performance.

---


### 115. [Cross-Subject EEG Emotion Recognition Based on Temporal Asynchronous Alignment Contrastive Learning](https://arxiv.org/abs/2605.22379)

**<font color=#1a73e8>作者：</font>** Ying Xie, Yi Zheng, Zehui Xiao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> With the advancement of science and technology, the importance of emotion research has become increasingly evident. Electroencephalography (EEG)-based emotion recognition has emerged as an active research area in recent years, owing to its objectivity and high temporal resolution. However, most existing methods focus on optimizing encoder structures to enhance feature extraction capabilities, while paying relatively little attention to similarity calculation strategies, particularly overlooking the potential temporal misalignment of responses among different subjects. To address these shortcomings, this paper draws inspiration from the late interaction mechanism of ColBERT in natural language processing (NLP) and proposes a Temporal Asynchronous Alignment-based Contrastive Learning (TA2CL) framework. This method transforms the traditional global "hard alignment" similarity calculation approach into a fine-grained local matching mechanism, enabling the model to adaptively search for and align "locally highly correlated" segments between two EEG signals, thereby effectively mitigating the effects of inter-subject differences and temporal delays. Experimental results demonstrate that the proposed method achieves strong performance across multiple public datasets. Specifically, on the FACED dataset, it achieves an accuracy of 64.5% for the nine-class classification task and 79.5% for the binary classification task, while on the SEED and SEED-V datasets, it achieves accuracies of 86.4% and 70.1%, respectively, validating the method's effectiveness and generalization capability.

---


### 116. [Unified Data Selection for LLM Reasoning](https://arxiv.org/abs/2605.22389)

**<font color=#1a73e8>作者：</font>** Xiaoyuan Li, Yubo Ma, Chengpeng Li 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Effectively training Large Language Models (LLMs) for complex, long-CoT reasoning is often bottlenecked by the need for massive high-quality reasoning data. Existing methods are either computationally expensive or fail to reliably distinguish high- from low-quality reasoning samples. To address this, we propose High-Entropy Sum (HES), a training-free metric that quantifies reasoning quality by summing only the entropy of the top (e.g., 0.5\%) highest-entropy tokens in each reasoning sample. We validate HES across three mainstream training paradigms: Supervised Fine-tuning (SFT), Rejection Fine-tuning (RFT), and Reinforcement Learning (RL), with extensive results demonstrating its consistent effectiveness and significantly reduced computational overhead. In SFT, training on the top 20\% HES-ranked data matches full-dataset performance, while using the lowest-HES data degrades it. In RFT, our HES-based training approach significantly outperforms baseline methods. In RL, HES-selected successful trajectories enable the model to learn strong reasoning patterns, significantly surpassing other compared methods. Our findings establish HES as a robust, training-free metric that enables a unified, effective, and efficient method for developing advanced reasoning in LLMs.

---


### 117. [Cross-Species RSA Reveals Conserved Early Visual Alignment but Divergent Higher-Area Rankings Across Human fMRI and Macaque Electrophysiology](https://arxiv.org/abs/2605.22401)

**<font color=#1a73e8>作者：</font>** Nils Leutenegger  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Does the relationship between learning rules and brain alignment generalize across species? We extend our prior finding that untrained CNNs match backpropagation at human V1 by testing the same five learning rules against macaque electrophysiology. The rules are backpropagation (BP), feedback alignment (FA), predictive coding (PC), spike-timing-dependent plasticity (STDP), and an untrained random-weights baseline. The macaque data come from two datasets: MajajHong2015 (V4/IT, 3,200 stimulus presentations, 88/168 neurons) and FreemanZiemba2013 (V1/V2, 135 stimuli, 102/103 neurons). Using RSA with identical model weights from our human study, we find: (1) all models achieve higher alignment with macaque early visual cortex (rho = 0.15-0.30 at V1/V2) than with human fMRI (rho = 0.01-0.08), consistent with the higher signal-to-noise ratio of electrophysiology; (2) STDP and PC produce the highest macaque V1/V2 alignment (rho ~ 0.30 and 0.28), consistent with their leading position among trained rules in human V1; (3) at IT, learning rule rankings show no detectable correlation across species (Kendall's tau = 0.00, p = 1.00), though this null result is expected given that n = 5 provides power only at tau = +/-1.0, and is further confounded by stimulus set differences; (4) a pretrained ResNet-50 (ImageNet) achieves rho = 0.25 at macaque IT, substantially above all custom CNN conditions (rho = 0.07-0.14), suggesting IT alignment is limited by model capacity and training data rather than by the learning rule. Noise ceilings, multi-seed variability (5 seeds), and a stimulus-control analysis are reported. These results demonstrate that early visual alignment is robust across species, while higher-area alignment is modulated by model capacity and stimulus domain.

---


### 118. [Translating Signals to Languages for sEMG-Based Activity Recognition](https://arxiv.org/abs/2605.22403)

**<font color=#1a73e8>作者：</font>** Ming Wang, Haoxuan Qu, Qiuhong Ke 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Surface electromyography (sEMG) signal-based activity recognition has attracted increasing research attention in recent years. To develop accurate sEMG signal-based activity recognizers, numerous approaches have been proposed. Some studies focus on designing larger and more expressive model architectures to enhance the representational capacity of sEMG signals, while others aim to enrich model priors through large-scale pretraining, thereby improving recognition performance. Recently, large language models (LLMs) have shown remarkable generalization and reasoning capabilities in natural language processing, whose implicit knowledge, learned from extensive linguistic descriptions of actions, opens new possibilities for interpreting sEMG signals and inferring activity intentions. Motivated by this, we propose LLM-sEMG, a novel framework that leverages LLMs as sEMG activity recognizers. Within this framework, we design a language-oriented mapping mechanism that converts continuous sEMG sequences into sEMG language, integrating several strategies to further facilitate the signal-to-language mapping process. Extensive experiments demonstrate that the proposed framework achieves highly accurate sEMG signal-based activity recognition using large language models.

---


### 119. [From Recognition to Reasoning: Benchmarking and Enhancing MLLMs on Real-World Receipt Document Understanding](https://arxiv.org/abs/2605.22413)

**<font color=#1a73e8>作者：</font>** Yandi Wang, Libin Zhan, Ziwei Huang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Extracting structured information from visual documents (Visual Information Extraction, VIE) is a cornerstone of business automation. While recent Multimodal Large Language Models (MLLMs) have shown promising capabilities, existing benchmarks suffer from critical limitations in scale and realism, lack semantic granularity, and fail to cover diverse document types. To bridge this gap, we introduce ReceiptBench, a large-scale, human-annotated benchmark consisting of 10k diverse receipts, organizing information extraction into four hierarchical sub-tasks: (1) Basic Perception for raw text spotting, (2) Format Normalization for strictly following standardization instructions, (3) Semantic Reasoning for inferring implicit attributes from context, and (4) Structure Parsing for handling nested line items. Furthermore, we propose a two-stage training framework incorporating Metric-Aware Group Relative Policy Optimization (GRPO), which translates rigorous evaluation constraints into reinforcement learning signals to enhance structural consistency. Extensive experiments demonstrate that our method yields state-of-the-art performance, surpassing leading proprietary models on complex reasoning tasks. We release our datasets and code at this https URL.

---


### 120. [From Correlation to Cause: A Five-Stage Methodology for Feature Analysis in Transformer Language Models](https://arxiv.org/abs/2605.22462)

**<font color=#1a73e8>作者：</font>** Caleb Munigety  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We propose a five-stage methodology for causal feature analysis in transformer language models (probe design, feature extraction, causal validation, robustness testing, and deployment integration) and demonstrate it end-to-end on GPT-2 small performing the Indirect Object Identification (IOI) task. Activation patching recovers the canonical IOI circuit (layer-9 head 9 alone gives recovery +1.02). A sparse autoencoder recovers per-name selective features with effect sizes of 30 to 50 activation units. Causal validation finds these features specifically but only partially causal: ablating fifteen of them leaves the model accurate on 98% of prompts. Two NLA-inspired evaluations strengthen this picture: the fifteen selective features explain only 31% of activation variance versus the SAE's 99.7%, and selectivity ratio anticorrelates with causal force (r = -0.56). Robustness testing under three distribution shifts finds that the circuit transfers cleanly but feature ablation effects degrade substantially, exposing a gap between detection robustness and causal robustness. A cost-based deployment evaluation (assumed $50/FN, $0.42/FP, 2% error rate) finds an optimal monitor configuration yielding $8.96 per 1000 queries against a $1000 baseline, a 99.1% saving. Optimal composition strategy varies with cost ratio and base rate. The conjunction of stages produces findings no single stage would.

---


### 121. [BioFormer: Rethinking Cross-Subject Generalization via Spectral Structural Alignment in Biomedical Time-Series](https://arxiv.org/abs/2605.22468)

**<font color=#1a73e8>作者：</font>** Guikang Du, Haoran Li, Xinyu Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Cross-subject generalization in biomedical time-series refers to training on data from some subjects and testing on unseen this http URL key challenge is to suppress subject specific variability in BTS this http URL existing methods implicitly suppress the variability through model building or subject adversarial learning, but rarely model it this http URL introduce spectral drift as a new perspective to characterize subject specific this http URL, BTS signals under the same label often share consistent oscillatory structure, yet exhibit subject-dependent magnitude or phase shifts in specific frequency components, which we interpret as subject-specific variability. Building on this insight, we propose this http URL its core is a Frequency-Band Alignment Module(FBAM) that generates band-wise modulation factors from the spectral distribution and adaptively adjusts amplitude and phase to align spectral structure, thereby mitigating this http URL further pair FBAM with Sample Conditional Layer Normalization, which infers normalization parameters from intrinsic signal statistics rather than subject identity, stabilizing cross-subject this http URL experiments on six datasets demonstrate that BioFormer outperforms 12 baselines, yielding absolute F1-score improvements of 6%.

---


### 122. [Supervised Classification Heads as Semantic Prototypes: Unlocking Vision-Language Alignment via Weight Recycling](https://arxiv.org/abs/2605.22484)

**<font color=#1a73e8>作者：</font>** David Méndez, Roberto Confalonieri, Natalia Díaz Rodríguez  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) excel at tasks like zero-shot classification and cross-modal retrieval by mapping images and text to a shared space, but this requires expensive end-to-end training with massive paired datasets. Current post-hoc alignment methods reduce computational costs by connecting pretrained encoders through lightweight mappings, yet still demand substantial paired data. In this work, we investigate the potential of repurposing the classification heads of pretrained vision models as semantic prototypes. The recycling of these weights, typically discarded after pretraining, unlocks two distinct capabilities: it enables zero-shot alignment by using weights as semantic anchors, and serves as a robust data augmentation strategy by mixing these prototypes with real image-text pairs. We demonstrate that integrating our approach with several state-of-the-art post-hoc alignment techniques consistently boosts accuracy in cross-modal retrieval, zero- and few-shot classification tasks.

---


### 123. [Polite on the Surface, Wrong in Practice: A Curated Dataset for Fixing Honorific Failures in Multilingual Bangla Generation](https://arxiv.org/abs/2605.22487)

**<font color=#1a73e8>作者：</font>** Md. Asaduzzaman Shuvo, Mahedi Hasan, Md. Tashin Parvez 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent advances in Multilingual Large Language Models (MLLMs) have significantly enhanced cross-lingual conversational capabilities, yet modeling culturally nuanced and context-dependent communication remains a critical bottleneck. Specifically, existing state-of-the-art models exhibit a severe pragmatic gap when handling structural variations, regional idioms, and honorific consistencies in low-resource contexts like Bangla. To address this limitation, we introduce a novel, culturally aligned instruction-tuning dataset for \textbf{BangLa Application and DialoguE generation - BLADE} and benchmarking framework comprising $4,196$ meticulously curated interaction pairs. We leverage this resource to systematically fine-tune and evaluate leading open-weight architectures, including DeepSeek-8B and LLaMA-3.2-3B, utilizing parameter-efficient fine-tuning via LoRA adapters in a 4-bit NormalFloat (NF4) quantization framework. Our empirical evaluations demonstrate that models fine-tuned on our dataset yield substantial improvements in structural fidelity and honorific alignment, providing a rigorous benchmark for bridging pragmatic disparities in low-resource multilingual text generation. Code and dataset: this https URL

---


### 124. [Understanding Multimodal Failure in Action-Chunking Behavioral Cloning](https://arxiv.org/abs/2605.22493)

**<font color=#1a73e8>作者：</font>** Lorenzo Mazza, Massimiliano Datres, Ariel Rodriguez 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Behavioral cloning becomes difficult when the same observation admits several valid actions. We study this problem for action-chunking policies and show that different multimodal parameterizations fail in different ways. For latent-variable policies, posterior-prior regularization makes deployment-time sampling more reliable, but excessive regularization removes the action-conditioned information needed to distinguish demonstrated modes. Reducing this regularization can preserve mode information, but then success depends on whether the prior covers the relevant latent regions. For action-space generative policies, multimodality is constrained by the smoothness of the base-to-action transport: a map with small Lipschitz constant cannot assign substantial probability to many well-separated modes. Covering many modes therefore requires either sharp transitions in base space or off-support bridge regions in action space. Experiments on synthetic multimodal tasks and robotic simulation benchmarks support these mechanisms.

---


### 125. [Compiling Agentic Workflows into LLM Weights: Near-Frontier Quality at Two Orders of Magnitude Less Cost](https://arxiv.org/abs/2605.22502)

**<font color=#1a73e8>作者：</font>** Simon Dennis, Rivaan Patil, Kevin Shabahang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agent orchestration frameworks have proliferated, collectively exceeding 290,000 GitHub stars across LangGraph, CrewAI, Google ADK, OpenAI Agents SDK, Semantic Kernel, Strands, and LlamaIndex. All follow the same pattern: an external orchestrator above the LLM, injecting instructions and routing decisions every turn. Recent work has shown this architecture is dominated for procedural tasks by simply providing the procedure in a frontier model's system prompt [Dennis et al., 2026a], at the cost of consuming the context window, requiring a frontier model for every conversation, and exposing proprietary procedures to third-party providers. Compiling the procedure into the weights of a small fine-tuned model -- creating a subterranean agent -- should resolve all of these concerns, and prior work (SimpleTOD, FireAct, SynTOD, WorkflowLLM, Agent Lumos) has shown the technique works. Yet developer adoption has overwhelmingly favored orchestration. We identify three perceived barriers and address each empirically across travel booking (14 nodes), Zoom support (14 nodes, product-specific knowledge), and insurance claims (55 nodes, 6 decision hubs).

---


### 126. [Search-E1: Self-Distillation Drives Self-Evolution in Search-Augmented Reasoning](https://arxiv.org/abs/2605.22511)

**<font color=#1a73e8>作者：</font>** Zihan Liang, Yufei Ma, Ben Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Post-training has become the dominant recipe for turning a language model into a competent search-augmented reasoning agent. A line of recent work pushes its performance further by adding elaborate machinery on top of this standard pipeline. These augmentations import external supervision from stronger external systems, attach auxiliary modules such as process reward models or retrospective critics, restructure the rollout itself with tree search or multi-stage curricula, or shape the reward with hand-crafted bonuses and penalties. Each addition delivers a measurable gain, but each also inflates the training pipeline and ties the recipe to resources or designs that may not always be available. We take a step back and ask whether any of this machinery is actually necessary, and propose Search-E1, a self-evolution method that lets a search-augmented agent improve through only vanilla GRPO interleaved with offline self-distillation (OFSD). After each GRPO round, the policy rolls out on its own training questions. A token-level forward KL objective then aligns the policy's inference-time distribution to its own distribution under a privileged context that exposes a more efficient sibling trajectory. Despite this simplicity, the procedure naturally provides dense per-step supervision. On seven QA benchmarks, Search-E1 reaches $0.440$ average EM with Qwen2.5-3B, surpassing all open-source baselines at both scales. Code and complete version will be made public soon.

---


### 127. [Stabilising Explainability Fragility in Cybersecurity AI: The Impact and Mitigation of Multicollinearity in Public Benchmark Datasets](https://arxiv.org/abs/2605.22529)

**<font color=#1a73e8>作者：</font>** Ioannis J. Vourganas, Anna Lito Michala  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper investigates a unexplored yet impactful vulnerability in AI explainability used in intrusion detection (IDS): multicollinearity-induced instability. Despite extensive reliance on post-hoc explainability tools such as SHAP or LIME, the impact of correlated features on explanation robustness is not evaluated. We introduce a formal theorem stating that multicollinearity inflates attribution variance. This demonstrates that explanations and feature importances are non-identifiable under multicollinearity. A suite of comprehensive experiments validates the theorem on a representative benchmark dataset, UNSW-NB15. Four widely used families of models are evaluated, including linear, tree-based, kernel, and neural, across full and pruned feature sets based on VIF and correlation thresholding. We propose the novel metric of Explanability Fragility Score and two novel methods to mitigate it with variable integration complexity. CAA-Filtering focuses on stabilising explanations by grouping attributions of trained models. SHARP is a novel training-time regularisation framework that penalises attribution instability, enabling controllable and monotonic improvement of explainability stability. The findings support stable predictive performance, using Kendall's {\tau} to quantify instability across bootstrapped explanations. This work has direct implications for the trustworthiness and reproducibility of XAI in security-critical contexts, and motivates incorporating multicollinearity mitigations into the IDS pipelines, providing a set of guidelines for practitioners.

---


### 128. [Relational Linear Properties in Language Models: An Empirical Investigation](https://arxiv.org/abs/2605.22532)

**<font color=#1a73e8>作者：</font>** Giovanni Valer, Luigi Gresele, Marco Bronzini 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Linear properties are ubiquitous in the representations of language models; however, testing them experimentally remains a challenging task. This work focuses on relational linearity: the hypothesis that, for a fixed relation (e.g., "plays"), the unembedding of an object (e.g., "trumpet") can be predicted from the embedding of its subject (e.g.,"Miles Davis") by a linear map. We present an experimental method to test the formulation of relational linearity by Marconato et al. (2025). Specifically, we introduce a probing method, based on Kullback-Leibler divergence, to evaluate this property and examine its variation across layers and paraphrased relational queries. It is also more efficient than previous work; for example, it avoids the crude Jacobian approximations used in Linear Relational Embeddings by Hernandez et al. (2024). Our findings across four datasets show that relational linearity varies across models, exhibits layer-wise patterns consistent with prior observations about linguistic information in model representations, and is differently affected by changes in how the relation is phrased.

---


### 129. [SpaceDG: Benchmarking Spatial Intelligence under Visual Degradation](https://arxiv.org/abs/2605.22536)

**<font color=#1a73e8>作者：</font>** Xiaolong Zhou, Yifei Liu, Ziyang Gong 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) have made rapid progress in spatial intelligence, yet existing spatial reasoning benchmarks largely assume pristine visual inputs and overlook the degradations that commonly occur in real-world deployment, such as motion blur, low light, adverse weather, lens distortion, and compression artifacts. This raises a fundamental question: how robust is the spatial intelligence of current MLLMs when visual observations are imperfect? To answer this question, we introduce SpaceDG, the first large-scale dataset for degradation-aware spatial understanding. It is constructed with a physically grounded degradation synthesis engine that embeds degradation formation process into 3D Gaussian Splatting (3DGS) rendering, enabling realistic simulation of nine degradation types. The resulting dataset contains approximately 1M QA pairs from nearly 1,000 indoor scenes. We further introduce SpaceDG-Bench, an human-verified benchmark with 1,102 questions spanning 11 reasoning categories and 9 visual degradation types, yielding over 10K VQA instances. Evaluating 25 open- and closed-source MLLMs reveals that visual degradations consistently and substantially impair spatial reasoning, exposing a critical robustness gap. Finally, we show that finetuning on SpaceDG markedly improves degradation robustness and can even surpass human performance under degraded conditions without any performance drop on clean images, highlighting the promise of degradation-aware training for robust spatial intelligence.

---


### 130. [Case-Aware Medical Image Classification with Multimodal Knowledge Graphs and Reliability-Guided Refinement](https://arxiv.org/abs/2605.22547)

**<font color=#1a73e8>作者：</font>** Yiming Xu, Yixuan Liu, Yuhang Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep learning has brought significant progress to medical image classification, yet most existing methods still rely on isolated visual evidence and cannot effectively leverage similar cases or external knowledge. In clinical practice, diagnosis is typically supported by historical similar cases and their associated symptoms. To simulate this diagnostic process, we propose a framework that performs case-aware reasoning using multimodal knowledge graphs for explainable medical image diagnosis. Given an input image, our method constructs a multimodal knowledge graph from adaptively retrieved similar cases, enabling more effective utilization of related samples. We further introduce a knowledge propagation and injection mechanism, where an image-centric Graph Attention Network propagates knowledge semantics to obtain case-based features, followed by a bidirectional cross-modal attention mechanism that injects these features into visual representations for cross-modal alignment. To mitigate noisy retrieval, we design a confidence-calibrated decision refinement scheme that estimates the reliability of each retrieved case by jointly considering prediction confidence and sample similarity, adaptively adjusting its contribution to the final prediction and providing interpretable case-level evidence. Extensive experiments on multiple medical imaging datasets show that our approach consistently outperforms strong baselines, and ablation studies validate the effectiveness of each component. The source code is publicly available at this https URL.

---


### 131. [MOTOR: A Multimodal Dataset for Two-Wheeler Rider Behavior Understanding](https://arxiv.org/abs/2605.22550)

**<font color=#1a73e8>作者：</font>** Varun A. Paturkar, Shankar Gangisetty, C.V. Jawahar  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Two-wheelers account for a disproportionately high share of road fatalities in the Global South. Research on two-wheeler rider behavior, however, lags far behind four-wheelers, where multimodal datasets have driven major advances in Advanced Driver Assistance Systems (ADAS). To address this gap, we present the MOtorized TwO-wheeler Rider (MOTOR) dataset, the first large-scale, multi-view, multimodal resource dedicated to two-wheelers in dense, unstructured traffic. MOTOR comprises 1,629 sequences (25+ hours of video data) collected from 16 riders and integrates synchronized front, rear, and helmet videos, rider eye-gaze from wearable trackers, on-road audio, and telemetry (GPS, accelerometer, gyroscope). Rich annotations capture traffic context, rider state, 12 riding maneuvers spanning conventional and unconventional behaviors, and legality labels (Legal, Illegal, Unspecified). We benchmark rider behavior recognition and maneuver legality classification using state-of-the-art video action recognition backbones (CNN and Transformer-based), extended with multimodal fusion, and find that combining RGB, gaze, and telemetry consistently yields the best performance. MOTOR thus provides a unique foundation for advancing safety-critical understanding of two-wheeler riding. It offers the research community a benchmark to develop and evaluate models for behavior analysis, legality-aware prediction, and intelligent transportation systems. Dataset and code is available at https: //varuniiith.this http URL

---


### 132. [FashionLens: Toward Versatile Fashion Image Retrieval via Task-Adaptive Learning](https://arxiv.org/abs/2605.22552)

**<font color=#1a73e8>作者：</font>** Haokun Wen, Xuemeng Song, Xinghao Xie 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Fashion image retrieval is a cornerstone of modern e-commerce systems. A unified framework that supports diverse query formats and search intentions is highly desired in practice. However, existing approaches focus on narrow retrieval tasks and do not fully capture such diversity. Therefore, in this work, we aim to develop a unified framework capable of handling diverse realistic fashion retrieval scenarios, achieving truly versatile fashion image retrieval. To establish a data foundation, we first introduce U-FIRE, a comprehensive benchmark that consolidates fragmented fashion datasets into a unified collection, supplemented by two manually curated datasets for testing generalization. Building upon this, we propose FashionLens, a unified framework based on Multimodal Large Language Models. To handle divergent matching objectives, we design a Proposal-Guided Spherical Query Calibrator that dynamically shifts query representations into task-aligned metric spaces via adaptive spherical linear interpolation. Additionally, to mitigate the optimization imbalance caused by varying task complexities and data scales, we develop a Gradient-Guided Adaptive Sampling strategy that automatically re-weights tasks based on realtime learning difficulty and the data scale prior. Experiments on U-FIRE show that FashionLens achieves state-of-the-art performance across diverse retrieval scenarios and generalizes robustly to unseen tasks. The data and code are publicly released at this https URL.

---


### 133. [GeoWeaver: Grounding Visual Tokens with Geometric Evidence before Scene Reasoning](https://arxiv.org/abs/2605.22558)

**<font color=#1a73e8>作者：</font>** Deshui Miao, Xingsen Huang, Yameng Gu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Spatio-temporal reasoning in vision-language models requires visual representations that preserve physical geometry rather than merely semantic appearance. Recent multimodal models incorporate geometric information through structural branches, 3D-aware supervision, reasoning-stage fusion, or long-horizon memory. While these approaches demonstrate the importance of geometry for spatial intelligence, they typically treat geometric cues as a shared signal across all visual tokens. We note that this overlooks a finer-grained challenge: different visual tokens require different geometric evidence depending on their spatial roles. To address this limitation, we introduce GeoWeaver, a pre-reasoning geometric grounding framework that treats geometry as a representational prerequisite for spatio-temporal reasoning. GeoWeaver constructs a multi-level geometry bank from a frozen geometry encoder and performs token-adaptive geometric evidence allocation, enabling each visual token to retrieve the most relevant geometric abstractions. The selected evidence is incorporated into visual tokens via a residual grounding operation prior to language modeling, yielding geometry-grounded representations for downstream reasoning. Extensive evaluations on spatial reasoning benchmarks demonstrate that GeoWeaver consistently enhances geometry-aware reasoning while retaining general multimodal capabilities. This indicates that geometric information yields the greatest benefit not as a late-fusion auxiliary signal but as a fundamental prerequisite that shapes the representational foundation on which large language models perform reasoning. All source code and models will be released at this https URL .

---


### 134. [GraphFlow: A Graph-Based Workflow Management for Efficient LLM-Agent Serving](https://arxiv.org/abs/2605.22566)

**<font color=#1a73e8>作者：</font>** Ao Li, Shangpeng Yang, Fahao Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large Language Model (LLM)-based agents demonstrate strong reasoning and execution capabilities on complex tasks when guided by structured instructions, commonly referred to as workflows. However, existing workflow-assisted agent serving systems typically rely on predefined templates and shallow matching mechanisms, which limit their ability to capture deep semantic relationships and generalize to previously unseen tasks. To address these limitations, we propose a new workflow management paradigm that represents workflows using a unified graph, termed wGraph, where each node corresponds to an atomic operation. wGraph serves as a shared substrate from which task-specific workflows are dynamically instantiated. Building on wGraph primitives, we introduce GraphFlow, a system that efficiently integrates workflows into agent serving through two key designs. First, adaptive workflow generation dynamically constructs workflows from wGraph based on task semantics and constraint requirements. Second, workflow state management exploits wGraph structure to efficiently manage Key-Value (KV) caches, reducing redundant computation during agent serving. Extensive experiments across five benchmark datasets show that GraphFlow consistently outperforms state-of-the-art methods, yielding an average performance improvement of approximately 4.95 percentage points, while achieving an approximately 4$\times$ reduction in memory footprint.

---


### 135. [LANG: Reinforcement Learning for Multilingual Reasoning with Language-Adaptive Hint Guidance](https://arxiv.org/abs/2605.22567)

**<font color=#1a73e8>作者：</font>** Yuchun Fan, Bei Li, Peiguang Li 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning has proven effective for enhancing multi-step reasoning in large language models (LLMs), yet its benefits have not fully translated to multilingual contexts. Existing methods struggle with a fundamental trade-off: prioritizing input-language consistency severely hampers reasoning quality, while prioritizing reasoning often leads to unintended language drift toward English. We address this challenge with LANG, a novel framework that leverages language-conditioned hints to guide exploration in non-English reasoning tasks. Our method incorporates two key mechanisms to prevent dependency on these hints: a progressive decay schedule that gradually withdraws scaffolding, and a language-adaptive switch that tailors learning horizons to specific language difficulties. Empirical results on challenging multilingual mathematical benchmarks reveal that LANG substantially enhances reasoning performance without compromising language consistency. Moreover, we show that our framework generalizes beyond mathematics, fostering more consistent language alignment across model layers

---


### 136. [VGenST-Bench: A Benchmark for Spatio-Temporal Reasoning via Active Video Synthesis](https://arxiv.org/abs/2605.22570)

**<font color=#1a73e8>作者：</font>** Jinho Park, Youbin Kim, Hogun Park 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Spatio-temporal reasoning is a core capability for Multimodal Large Language Models (MLLMs) operating in the real world. As such, evaluating it precisely has become an essential challenge. However, existing spatio-temporal reasoning benchmark datasets primarily rely on static image sets or passively curated video data, which limits the evaluation of fine-grained reasoning capabilities. In this paper, we introduce VGenST-Bench, a video benchmark that employs generative models to actively synthesize highly controlled and diverse evaluation scenarios. To construct VGenST-Bench, we propose a multi-agent pipeline incorporating a human quality control stage, ensuring the quality of all generated videos and QA pairs. We establish a comprehensive 3x2x2 video taxonomy, encompassing Spatial Scale, Perspective, and Scene Dynamics to span diverse scenarios. Furthermore, we design a hierarchical task suite that decouples low-level visual perception from high-level spatio-temporal reasoning. By shifting the paradigm from passive curation to active synthesis, VGenST-Bench enables fine-grained diagnosis of spatio-temporal understanding in MLLMs.

---


### 137. [Beyond Temperature: Hyperfitting as a Late-Stage Geometric Expansion](https://arxiv.org/abs/2605.22579)

**<font color=#1a73e8>作者：</font>** Meimingwei Li, Yuanhao Ding, Esteban Garces Arias 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent work has identified a counterintuitive phenomenon termed "Hyperfitting", where fine-tuning Large Language Models (LLMs) to near-zero training loss on small datasets surprisingly enhances open-ended generation quality and mitigates repetition in greedy decoding. While effective, the underlying mechanism remains poorly understood, with the extremely low-entropy output distributions suggesting a potential equivalence to simple temperature scaling. In this work, we demonstrate that this phenomenon is fundamentally distinct from distribution sharpening; entropy-matched control experiments reveal that temperature scaling fails to replicate the diversity gains of hyperfitting. Furthermore, we falsify the hypothesis of static vocabulary reweighting, showing through ablation studies that hyperfitting relies on a dynamic, context-dependent rank reordering mechanism. Layer-wise analysis localizes this effect to a "Terminal Expansion" in the final transformer block, where a substantial geometric expansion of the feature space (Delta Dim approx +80.8) facilitates the promotion of deep-tail tokens. Additionally, we introduce Late-Stage LoRA, a targeted fine-tuning strategy that updates only the final 5 layers, yielding robust generation with minimal parameter updates

---


### 138. [Rethinking Noise-Robust Training for Frozen Vision Foundation Models: A Cross-Dataset Benchmark with a Case Study of Small-Loss Failure](https://arxiv.org/abs/2605.22591)

**<font color=#1a73e8>作者：</font>** Zitong Li, Haoyu Wang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Frozen Vision Foundation Models (VFMs) with lightweight classification heads are increasingly used in medical imaging because they offer efficient and reproducible deployment. Yet noisy-label learning methods for this frozen-feature regime remain poorly understood, and most existing methods still rely on a small-loss assumption inherited from end-to-end training. We present a controlled benchmark of eight noisy-label methods across five medical datasets, three backbones, two noise types, and five noise rates (150 conditions, 6,000 training runs), evaluated with balanced accuracy. The benchmark shows that there is no universal winner: Friedman ranking over the 150 conditions yields $\chi^2 = 333.2$ ($p = 4.77 \times 10^{-68}$), ELR wins the most conditions (49/150), while CUFIT attains the best mean rank (2.51). The practical cost of method choice grows sharply with noise severity, from 4.5pp on clean data to 18.8pp at asymmetric 40\% noise. To explain these benchmark-level patterns, we revisit the small-loss assumption in a representative high-risk regime. Under frozen DINOv2 features, clean and noisy loss distributions overlap by 53--61\%, and matched-rate clean-sample detection shows that prediction agreement is markedly more stable than loss ranking under asymmetric noise (3pp vs.\ 13pp precision drop). On ISIC2019 with asymmetric 40\% noise, Co-Teaching reaches 68\% overall accuracy while collapsing to 35.1\% balanced accuracy with zero recall on three minority classes. Together, these results recast noisy-label learning for frozen VFMs as a regime-aware method-selection problem rather than a search for a single dominant algorithm. We conclude with evidence-based guidance and a low-regret feature-space selector for practical recommendation.

---


### 139. [Think Thrice Before You Speak: Dual knowledge-enhanced Theory-of-Mind Reasoning for Persuasive Agents](https://arxiv.org/abs/2605.22602)

**<font color=#1a73e8>作者：</font>** Minghui Ma, Bin Guo, Runze Yang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Persuasive dialogue requires reasoning about others' latent mental states, a capability known as Theory of Mind (ToM). However, due to reliance on simple prompting strategies and insufficient ToM knowledge, existing LLMs often fail to capture the intrinsic dependencies among mental states, leading to fragmented representations and unstable reasoning. To address these challenges, we introduce the ToM-based Persuasive Dialogue (ToM-PD) task, grounded in the Belief-Desire-Intention (BDI) framework, which explicitly models the sequential dependencies among mental states in multi-turn dialogues. To facilitate research on this task, we construct a large-scale annotated dataset, ToM-based Broad Persuasive Dialogues (ToM-BPD), capturing fine-grained mental states and corresponding persuasive strategies. We further propose Think Thrice Before You Speak (TTBYS), a knowledge-enhanced stepwise reasoning framework that leverages both explicit and implicit prior experiences to improve LLMs' inference of desires, beliefs, and persuasive strategies. Experimental results demonstrate that Qwen3-8B equipped with TTBYS outperforms GPT-5 by 1.20%, 22.80%, and 16.97% in predicting desires, beliefs, and persuasive strategies, respectively. Case studies further show that our approach enhances interpretability and consistency in reasoning.

---


### 140. [Enhancing Gaze Reasoning in Vision Foundation Models for Gaze Following](https://arxiv.org/abs/2605.22607)

**<font color=#1a73e8>作者：</font>** Shijing Wang, Yaping Huang, Chaoqun Cui 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Gaze following requires both scene understanding and gaze reasoning to localize the gaze target of an in-scene person. Recently, vision foundation models (VFMs) have demonstrated strong performance on this task, enabling simpler architectures while outperforming prior methods. However, we observe a key limitation of VFM-based approaches: while VFMs substantially improve scene understanding, they contribute little to gaze reasoning. As a result, existing methods often rely on semantically salient objects rather than true gaze cues, leading to degraded performance when targets are not salient. To address this, we propose a novel training mechanism to enhance gaze reasoning in VFMs for gaze following. Our method includes: (1) a head-conditioned local LoRA, which enables localized adaptation to preserve scene token learning while improving head token learning for gaze reasoning; and (2) an out-of-cone penalty, which injects gaze cues into head tokens while aligning them with scene tokens. Experiments on the GazeFollow and VAT datasets demonstrate that our method achieves state-of-the-art performance, with particularly strong improvements when gaze targets are not semantically salient. Our findings offer valuable insights for advancing future gaze following research. We will release the code once the paper is accepted.

---


### 141. [Agentic CLEAR: Automating Multi-Level Evaluation of LLM Agents](https://arxiv.org/abs/2605.22608)

**<font color=#1a73e8>作者：</font>** Asaf Yehudai, Lilach Eden, Michal Shmueli-Scheuer  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Agentic systems are becoming more capable: agents define strategies, take actions, and interact with different environments. This autonomy poses serious challenges for overseeing and assessing agent behavior. Most current tools are limited, focusing on observability with basic evaluation capabilities or imposing static, hand-crafted error taxonomies that cannot adapt to new domains. To address this gap, we present Agentic CLEAR, an automatic, dynamic, and easy-to-use evaluation framework. It produces textual insights into the agent behavior on three levels of granularity: system, trace, and node. Agentic CLEAR operates above the observability layer, enabling seamless integration and featuring an intuitive UI that makes agent evaluation highly accessible. In our experiments on four benchmarks, seven agentic settings, and tens of thousands of LLM calls, we show that Agentic CLEAR produces high-quality, data-driven, insightful feedback. Our analysis shows strong alignment with human-annotated errors and the ability to predict task success rate.

---


### 142. [Evolutionary Multi-Task Optimization for LLM-Guided Program Discovery](https://arxiv.org/abs/2605.22613)

**<font color=#1a73e8>作者：</font>** Halil Alperen Gozeten, Xuechen Zhang, Emrullah Ildiz 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent LLM-guided evolutionary search methods have shown that iterative program mutation can discover strong algorithms, but they typically optimize each task independently, even when related tasks share reusable structure. We introduce Evolutionary Multi-Task Optimization (EMO) for LLM-guided program discovery, and propose EMO-STA (Shared-Then-Adapt), a two-stage framework that first evolves a shared archive of executable programs across a task family and then adapts selected shared candidates to each target task. Within EMO-STA, we explore multiple adaptation strategies, including warm-starting from the shared archive, adapting the best average shared program, and adapting the shared program that performs best on each target task. Across eight task families spanning continuous optimization, geometric construction, modeling, and algorithmic optimization, EMO-STA improves over matched-compute single-task evolution in most settings, with STA Best-Local providing the strongest in-distribution adaptation and STA Best-Shared yielding robust transfer to unseen tasks. Compute-allocation experiments show that allocating a substantial fraction of the family-level budget to shared evolution is consistently beneficial, with roughly balanced shared and adaptation budgets often being optimal. Beyond compute efficiency, we show that shared evolution can mitigate overfitting in low-evidence settings (e.g. few training data), including ARC tasks and time-series feature engineering, by favoring programs that generalize across all tasks rather than exploiting task-specific brittle artifacts.

---


### 143. [Spreadsheet-RL: Advancing Large Language Model Agents on Realistic Spreadsheet Tasks via Reinforcement Learning](https://arxiv.org/abs/2605.22642)

**<font color=#1a73e8>作者：</font>** Banghao Chi, Yining Xie, Mingyuan Wu 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Spreadsheet systems (e.g., Microsoft Excel, Google Sheets) play a central role in modern data-centric workflows. As AI agents grow increasingly capable of automating complex tasks, such as controlling computers and generating presentations, building an AI-driven spreadsheet agent has emerged as a promising research direction. Most existing spreadsheet agents rely on specialized prompting over general-purpose LLMs; while this design has potentials on simple spreadsheet operations, it struggles to manage the complex, multi-step workflows typical of real-world applications.
We introduce Spreadsheet-RL, a reinforcement learning (RL) fine-tuning framework designed to train specialized spreadsheet agents within a realistic Microsoft Excel environment. Spreadsheet-RL features an automated pipeline for scalable collection of paired start-goal spreadsheets from online forums, as well as domain-specific evaluation tasks in areas such as finance and supply chain management, which we compile into the new Domain-Spreadsheet benchmark dataset. It also includes a Spreadsheet Gym environment designed for multi-turn RL: Spreadsheet Gym exposes extensive Excel functionality through a Python sandbox, along with a refined harness that incorporates a comprehensive tool set and carefully designed tool-routing rules for spreadsheet tasks. Through comprehensive experiments, we show that Spreadsheet-RL substantially enhances AI agent's performance on both general and domain-specific spreadsheet tasks: it improves Qwen3-4B-Thinking-2507's Pass@1 on SpreadsheetBench from 12.0% to 23.4%, and raises Pass@1 from 8.4% to 17.2% on our curated Domain-Spreadsheet dataset. These results highlight Spreadsheet-RL's strong potential for generalization and real-world adoption in spreadsheet automation, and broadly, its promise for advancing LLM-based interactions with data interfaces in everyday work.

---


### 144. [Boiling the Frog: A Multi-Turn Benchmark for Agentic Safety](https://arxiv.org/abs/2605.22643)

**<font color=#1a73e8>作者：</font>** Piercosma Bisconti, Matteo Prandi, Federico Pierucci 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Background. Traditional safety benchmarks for language models evaluate generated text: whether a model outputs toxic language, reproduces bias, or follows harmful instructions. When models are deployed as agents, the safety-relevant object shifts from what the system says to what it does within an environment, and evaluating model responses under prompting is no longer sufficient to address the safety challenges posed by artificial intelligence. Recent developments have seen the rise of benchmarks that evaluate large language models as agents. We contribute to this strand of research. Approach. We introduce Boiling the Frog, a benchmark that evaluates whether tool-using AI models deployed in corporate and office settings are susceptible to incremental attacks. Each scenario begins with benign workspace edits and later introduces a risk-bearing request. The benchmark focuses on stateful multi-turn evaluation: chains expose a persistent workspace, place the risk-bearing payload at controlled positions in the turn sequence, and score whether the resulting artifact state becomes unsafe. Scenarios are organized through a three-level operational risk taxonomy grounded in the Boiling the Frog risks, the AI Act Annex I and Annex III high-risk contexts, and EU AI Act's Code of Practice on General-Purpose AI (GPAI). Results. Across a nine-model panel, aggregate strict attack success rate (ASR) is 44.4%. Model-level ASR ranges from 20.5% for Claude Haiku 4.5 to 92.9% for Gemini 3.1 Flash Lite, with Seed 2.0 Lite also above 80%. Average chain category-level ASR reaches 93.3% for Code of Practice loss-of-control scenarios.

---


### 145. [AtelierEval: Agentic Evaluation of Humans & LLMs as Text-to-Image Prompters](https://arxiv.org/abs/2605.22645)

**<font color=#1a73e8>作者：</font>** Hanjun Luo, Zhimu Huang, Sylvia Chung 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Text-to-image (T2I) systems increasingly rely on upstream prompters, either humans or multimodal large language models (MLLMs), to translate user intent into detailed prompts. Yet current benchmarks fix the prompt and only evaluate T2I models, leaving the prompting proficiency of this upstream component entirely unmeasured. We introduce AtelierEval, the first unified benchmark that quantifies prompting proficiency across 360 expert-crafted tasks. Grounded in a cognitive view, it spans three task categories and instantiates tasks using a taxonomy of real-world challenges, with a dual interface for both humans and MLLMs. To enable scalable and reliable evaluation, we propose AtelierJudge, a skill-based, memory-augmented agentic evaluator. It produces subjective and objective scores for prompt-image pairs, achieving a Spearman correlation of 0.79 with human experts, approaching human performance. Extensive experiments benchmark 8 MLLMs against 48 human users across 4 T2I backends, validate AtelierEval as a robust diagnostic tool, and reveal the superiority of mimicry over planning, advocating for an image-augmented direction for future prompters. Our work is released to support future research.

---


### 146. [Seeing the Poem: Image-Semantic Detection of AI-Generated Modern Chinese Poetry with MLLMs](https://arxiv.org/abs/2605.22654)

**<font color=#1a73e8>作者：</font>** Shanshan Wang, Fengying Ye, Hanjia Lyu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Previous detection studies have shown that LLMs cannot be effectively used as detectors, but these studies have not addressed modern Chinese poetry. Moreover, no relevant research has explored the performance of LLMs in detecting modern Chinese poetry. This paper evaluates and enhances the performance of LLMs as detectors for modern Chinese poetry, and proposes an image-semantic guided poetry detection method. Compared with traditional detection approaches, our method innovatively incorporates images that reflect the content of the poetry. Through example-driven approaches, our method effectively integrates information such as meaning, imagery, and feeling from the image, then forms a complementary judgment with the poem text. Experimental results demonstrate that the LLM detectors based on our method outperform baseline detectors based on plain text, and even surpass the best-performing traditional detector, RoBERTa. The Gemini detector using our method achieves a Macro-F1 score of 85.65%, reaching the state-of-the-art level. The performance improvements of different LLM detectors on multiple LLMs-generated data prove the effectiveness of our method.

---


### 147. [SegCompass: Exploring Interpretable Alignment with Sparse Autoencoders for Enhanced Reasoning Segmentation](https://arxiv.org/abs/2605.22658)

**<font color=#1a73e8>作者：</font>** Zhenyu Lu, Liupeng Li, Jinpeng Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While large language models provide strong compositional reasoning, existing reasoning segmentation pipelines fail to transparently connect this reasoning to visual perception. Current methods, such as latent query alignment, are end-to-end yet opaque "black boxes". Conversely, textual localization readout is merely readable, not truly interpretable, often functioning as an unconstrained post-hoc step. To bridge this interpretability gap, we propose SegCompass, an end-to-end model that leverages a Sparse Autoencoder (SAE) to forge an explicit, interpretable, and differentiable alignment pathway. Given an image-instruction pair, SegCompass first generates a chain-of-thought (CoT) trace. The core of our method is an SAE that maps both the CoT and visual tokens into a shared, high-dimensional sparse concept space. A query codebook selects salient concepts from this space, which are then spatially grounded by a slot mapper into a multi-slot heatmap that guides the final mask decoder. The entire model is trained jointly, unifying reinforcement learning for the reasoning path with standard segmentation supervision. This SAE-driven interface provides a "white-box" connection that is significantly more traceable than latent queries and more coherent than textual readouts. Extensive experiments on five challenging benchmarks demonstrate that SegCompass matches or surpasses state-of-the-art performance. Crucially, our visual and quantitative analyses show a strong correlation between the quality of the learned sparse concepts and final mask accuracy, confirming that SegCompass achieves superior results through its enhanced and inspectable alignment. Code is available at this https URL.

---


### 148. [Moral Semantics Survive Machine Translation: Cross-Lingual Evidence from Moral Foundations Corpora](https://arxiv.org/abs/2605.22660)

**<font color=#1a73e8>作者：</font>** Maciej Skorski  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Moral language is subtle and culturally variable, making it difficult to translate faithfully across languages. Idiomatic expressions, slang, and cultural references introduce hard-to-avoid translation artifacts. Yet automated moral values classification depends on language-specific annotated corpora that exist almost exclusively in English. We investigate whether LLM-based translation can bridge this gap, taking Polish as a test case. Using $\sim$50k morally-annotated social media posts from a diverse range of topics, we apply a principled four-method validation pipeline: LaBSE cross-lingual embedding similarity, Centered Kernel Alignment (CKA), LLM-as-judge evaluation, and deep learning classifier parity tests. We show that despite shortcomings in handling slang, vulgarity, and culturally-loaded expressions, direct translation preserves subtle moral cues well enough to be harvested by cross-lingual machine learning -- with mean cosine similarity of 0.86 and AUC gaps of 0.01--0.02 across all foundations closing further under fine-tuning of language models. These results demonstrate that machine translation is a practical and cost-effective path to moral values research in languages currently under-resourced in this domain. We demonstrate this for Polish as a representative Slavic language, with expected generalisation to related languages.

---


### 149. [WorkstreamBench: Evaluating LLM Agents on End-to-End Spreadsheet Tasks in Finance](https://arxiv.org/abs/2605.22664)

**<font color=#1a73e8>作者：</font>** Thomson Yen, Julian Poeltl, Harshith Srinivas Gear 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents are increasingly expected to carry out end-to-end workflows, producing complete artifacts from high-level user instructions. To meet enterprise needs, frontier AI labs have developed agents that can construct entire spreadsheets from scratch. This is especially relevant in finance, where core workflows such as financial modeling, forecasting, and scenario analysis are commonly conducted through spreadsheets. Yet, existing spreadsheet benchmarks do not measure this advanced capability, focusing instead on question-answering or single-formula edits. To address this gap, we provide one of the first evaluations of agents on end-to-end spreadsheet tasks, focusing on economically critical financial workflows such as modeling and scenario analysis. Since deliverables therein are routinely reviewed and revised by multiple stakeholders, judging their quality necessarily involves high-level criteria such as readability or ease of modification. To reflect the multidimensional nature of solution quality, we develop an evaluation taxonomy comprising three dimensions: Accuracy, Formula, and Format, each comprising fine-grained criteria that reflect professional standards. The Claude family leads the benchmark and produces the most professional-looking outputs in our qualitative review, but even the strongest agents frequently fall short of professional finance standards and degrade sharply as the difficulty increases beyond a few chained calculations. This suggests that current agents are not yet able to reliably produce professional-quality spreadsheets at the level of complexity real-world workflows demand.

---


### 150. [Is Capability a Liability? More Capable Language Models Make Worse Forecasts When It Matters Most](https://arxiv.org/abs/2605.22672)

**<font color=#1a73e8>作者：</font>** Nick Merrill, Jaeho Lee, Ezra Karger  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We document inverse scaling in LLMs on forecasting problems whose underlying time series exhibit superlinear growth and tail risk of regime change, a structure common in finance and epidemiology. On these tasks, more capable models produce worse distributional forecasts. The pattern appears on ForecastBench-Sim (FBSim), a contamination-free, simulated-world benchmark we release, in forecasting synthetic SIR epidemics with a matched linear control, and replicates in real-world datasets on COVID-19, measles, housing markets, and hyperinflation. A per-quantile decomposition shows the failure concentrates at the upper tail, which more capable models shift upward to track aggressive extrapolations of growth, while the lower tail stays put. A within-family study of Llama-3.1 shows that both model scale and post-training independently contribute to this effect. Domain knowledge does not reliably rescue calibration. This inverse scaling does not appear on single-threshold metrics common in LLM forecasting benchmarks, reversing the sign of the capability--accuracy relationship on identical outputs. Single-threshold scoring at conventional cutoffs misses the upper-tail cost; tail-inclusive scoring reverses the sign of the capability--accuracy relationship on the same outputs. We recommend that LLM forecasting evaluations use continuous (and unbounded) measures of accuracy alongside bounded binary threshold metrics.

---


> [!TIP]
> 当前位于：**101-150**（第 3/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-162](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
