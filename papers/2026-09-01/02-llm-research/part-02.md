# 🧠 大模型相关研究 | 2026年09月01日

> 本类共 **176** 篇论文：已确认 **168** 篇，待复核 **8** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**51-100**（第 2/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-176](./part-04.md)

---

### 51. [SpikeOPD: Stable On-Policy Distillation for Autoregressive Spiking Language Models](https://arxiv.org/abs/2608.27857)

**<font color=#1a73e8>作者：</font>** Enqiao Lu, Xingrui Yu, Yiwei Fu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Spiking neural networks (SNNs) offer a path to energy-efficient language modeling through sparse encoding and event-driven computation, but training capable spiking language models from scratch remains difficult. A practical alternative is ANN-to-SNN migration through knowledge distillation (KD), where a pretrained artificial neural network (ANN) teacher supervises an SNN student. Existing migration approaches distill on fixed corpus prefixes, whereas autoregressive inference conditions on self-generated prefixes, creating prefix-source mismatch. It manifests as output-policy mismatch with the ANN teacher and internal spiking-dynamics drift between self-generated and matched corpus prefixes. On-policy distillation (OPD) offers a natural way to mitigate both manifestations by continuing teacher supervision on self-generated prefixes. We evaluate a teacher-only full-KL variant, Vanilla OPD, via a controlled stress test and observe it may suffer from delayed rollout-feedback collapse. This result shows that on-policy coverage alone does not ensure stable adaptation. Motivated by these findings, we propose SpikeOPD, a stable on-policy distillation framework for autoregressive SNNs that learns from self-generated prefixes while maintaining rollout stability. It applies full-KL teacher correction to reduce output-policy mismatch, while matched-prefix policy anchoring constrains policy departure from the frozen reference SNN on the same prefixes. Layerwise spike regularization further limits firing-rate deviations during on-policy adaptation. Across three model scales, SpikeOPD improves average accuracy over the corresponding KD SNNs by 0.8, 1.7, and 2.9 points at 0.125B, 0.35B, and 1.3B, respectively, while preserving their sparse-compute profiles.

---


### 52. [Iron: Intent-Aligned and Retrospective Dual Learning Framework for Enhancing Generalist Virtual Agents](https://arxiv.org/abs/2608.27866)

**<font color=#1a73e8>作者：</font>** Jiahe Ying, Wendong Bu, Kaihang Pan 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Achieving virtual agents capable of automating tasks across diverse digital environments remains a pivotal challenge in Embodied AI. While Multimodal Large Language Models (MLLMs) offer enhanced visual perception and reasoning, their agentic deployment faces three challenges: costly data annotation, imprecise action-intent alignment, and inefficient exploration from discarded failed trajectories. To address these, we introduce Iron, an intent-aligned, self-improved, and annotation-efficient framework for training GUI agents. Iron employs a novel dual learning strategy that utilizes a stepwise cycle-consistent (SCC) reward to achieve fine-grained alignment between low-level actions and high-level intents, thereby improving instruction grounding and intent understanding. Concurrently, Iron introduces a hindsight reproduction mechanism to repurpose failed trajectories for training, improving both learning efficiency and task diversity. Extensive experiments demonstrate that Iron-trained generalist agents consistently improve performance on cross-environment and cross-device tasks, outperforming models trained with three times more data. Iron also achieves a substantial 25.06% relative improvement on unseen web tasks, with further gains observed on inherently complex tasks, demonstrating the feasibility of building more capable virtual agents.

---


### 53. [CoRe-MoE: Compact Reusable MoE for Continual Multimodal Instruction Tuning](https://arxiv.org/abs/2608.27867)

**<font color=#1a73e8>作者：</font>** Runze Liu, Naibin Gu, Mingxu Ai 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Continual multimodal instruction tuning requires multimodal large language models to acquire new task abilities sequentially while preserving previously learned knowledge. LoRA-MoE provides a promising solution by introducing expert-based capacity, but repeatedly learning and maintaining full LoRA experts leads to substantial parameter overhead. This raises a natural question: is full expert expansion necessary for every new task? To answer it, we analyze the SVD of task-specific LoRA updates and observe substantial overlap in their input- and output-side LoRA direction subspaces, with task-specific adaptation largely captured by lightweight coordinates over these subspaces. Motivated by this observation, we propose CoRe-MoE, a Compact Reusable MoE framework for parameter-efficient continual multimodal instruction tuning. CoRe-MoE extracts reusable input- and output-side direction bases from an initial expert bank, and for subsequent tasks trains only compact coordinate experts together with task-specific low-rank routers. Experiments on two representative MLLMs show that CoRe-MoE improves final average performance over the strongest competing baseline by up to 5.90 points, while using less than 1% of the trainable parameters required by sequential LoRA for later tasks. The code is publicly available at this https URL.

---


### 54. [See, Hypothesize, Validate: Multimodal Agentic Framework for Discovering Governing PDEs](https://arxiv.org/abs/2608.27869)

**<font color=#1a73e8>作者：</font>** Sarang Manoj Pekhale, Amartya Roy, Rajat Sarkar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Discovering governing partial differential equations (PDEs) from observational data remains a core challenge across the sciences. Existing sparse-regression, symbolic-regression, and LLM-based approaches can be constrained by predefined libraries, noise sensitivity, hallucination, or limited iterative refinement. We introduce \textbf{MAGE} (\textbf{M}ultimodal \textbf{A}gentic \textbf{G}overning \textbf{E}quation Discovery), an agentic framework that organizes PDE discovery as a \textit{confidence governed hypothesis validation loop} inspired by the scientific cycle of observation, hypothesis, and falsification. Four role-specialized agents collaborate: a \textit{Differential Observer} computing derivatives and diagnostic visualizations; a VLM-powered \textit{Phenomenology Extractor} distilling qualitative cues from multimodal diagnostics; an LLM-driven \textit{Governing Law Synthesizer} proposing candidates without a predefined library; and an \textit{Equation Arbiter} fitting coefficients and assigning confidence scores. Discovery iterates until the top candidate clears a user-specified threshold, providing a structured process with an explicit accept-reject protocol. On the evaluated canonical PDE suite, MAGE obtains \textbf{8/8} exact structural recovery and the lowest coefficient error among the compared methods on \textbf{7/8} systems, with improvements of up to \textbf{4 orders of magnitude} and a geometric-mean improvement of approximately \textbf{3 orders of magnitude}. The pipeline also recovers the expected operators in two complex geometries and, on one laboratory sensor record, selects a cubic restoring-force model with held-out $R^2=0.98538$. These results support further study of structured agentic reasoning for library-free governing-law discovery, while broader generalization remains to be evaluated.

---


### 55. [Temporal Tree of Thought: Reasoning-Guided Visual Cue Search for Long-Video Understanding](https://arxiv.org/abs/2608.27871)

**<font color=#1a73e8>作者：</font>** Ziling Huang, Shin'ichi Satoh  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long-video understanding remains challenging for Multimodal Large Language Models (MLLMs) due to limited context length. Uniform sampling may miss crucial moments, while agent-based frame video understanding methods often evaluate frames independently, overlooking the temporal organization of videos. Ideally, evidence selection should mimic how humans answer questions about long videos: first locating the relevant segment from the global context, then zooming into local objects and details. We propose Temporal Tree of Thought T^3, a training-free framework for adaptive coarse-to-fine long-video understanding. T^3 constructs a question-agnostic hierarchical temporal tree via recursive temporally constrained clustering, where each node represents a contiguous segment with an informative key frame. During inference, T^3 performs an answer-retrieve-explore loop: it reasons over coarse representative frames, generates a search statement when evidence is insufficient, and expands relevant branches for finer-grained evidence. This process adaptively shifts the search target from temporal regions to specific objects and visual details to help video understanding. Experiments on VideoMME, LongVideoBench, and LVBench show that T^3 improves Qwen2.5-VL-7B by 0.5%, 4.6%, and 4.4%, respectively, under the same frame budget, demonstrating the effectiveness of structured temporal reasoning.

---


### 56. [HyQuant: Hybrid-Precision Quantization for LLM Attention](https://arxiv.org/abs/2608.27875)

**<font color=#1a73e8>作者：</font>** Jiatong Ding, Bingxin Xing, Yu Zhang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Quantization has been widely adopted in LLM training and inference to reduce cost and improve efficiency. However, low-bit quantization of the \emph{attention} module often introduces large errors at very low bit-widths, causing performance degradation. Existing methods mainly rely on smoothing techniques to handle outliers, while we propose a hybrid quantization design to better balance accuracy and efficiency. Specifically, we propose \textbf{HyQuant}, an efficient hybrid quantization framework for LLM attention. HyQuant quantizes most attention states into low-bit formats while retaining a small set of vertical-line tokens and local-window states in high precision. These accuracy-critical regions are selected using lightweight vertical-line-aware attention-pattern signals, reducing quantization error with limited overhead. In the Prefill stage, HyQuant uses a hybrid-precision quantized attention operator that preserves vertical-line tokens and a local sliding window in full precision while quantizing the remaining context. In the Decode stage, HyQuant applies the same principle to KV-cache compression and fuses KV dequantization with attention computation to improve memory and hardware efficiency. Across diverse tasks, models, and datasets, HyQuant maintains nearly lossless accuracy with an extremely simple design, demonstrating the efficiency and practical feasibility of hybrid quantization for LLM attention. Code is available at: this https URL .

---


### 57. [StreamEMS: Streaming Video Understanding with Self-Evolving Memory Scheme for Vision-Language Models](https://arxiv.org/abs/2608.27881)

**<font color=#1a73e8>作者：</font>** Yuxin Liu, Peiqin Zhuang, Yali Wang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recently, many streaming video understanding methods have been proposed by constructing an external memory to store historical data for computational reduction. Most methods focus on optimizing the injection procedure of current data (write) and retrieving informative historical data (read) from memory, while overlooking the opportunity to further enhancing the representational capability of memory itself. In this work, we present StreamEMS, a general mechanism for improving streaming video understanding by re-structuring the historical data stored in memory through self-evolving memory scheme, enabling more informative and robust memory representations. Specifically, we first introduce a Semantic Evolution Module to evolve the memory into more information-dense representations by exploiting informative memory entities discovered via progressively shrinking semantic scales from coarse to fine. In addition, we further introduce a Prior-informed Evolution Module to evolve memory into more robust representations by leveraging prior memory distributions to refine the current memory state. We validate the effectiveness of our proposed designs on widely-used streaming video understanding datasets, i.e., OVO-Bench and StreamingBench, and the results showcase that our method performs better than other methods. Moreover, the advantage of our method becomes consistently evident even under high token usage drop rate settings, indicating the effectiveness and robustness of our method in unleashing the potential of the memory itself.

---


### 58. [SOMTab: Set-Order Mamba for Efficient Tabular In-Context Learning](https://arxiv.org/abs/2608.27882)

**<font color=#1a73e8>作者：</font>** Hao Wang, Siyu Zhang, Wei Ma  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tabular foundation models based on in-context learning have recently emerged as strong alternatives to task-specific model fitting. However, the current performance frontier remains dominated by attention-heavy architectures, where attention is used throughout the modeling pipeline. This raises a natural question: is attention necessary at every stage of tabular in-context learning? We introduce SOMTab, a Set-Order Mamba architecture for efficient tabular in-context learning. SOMTab separates representation construction from query-conditioned retrieval. For row and column representations, it maps unordered table tokens into stable latent slots and applies Mamba-based state-space mixing to construct compact representations. For final prediction, it retains attention-based in-context learning to preserve query-conditioned retrieval from labeled context examples. We further introduce DCH-TailMix, a synthetic prior that combines degree-corrected graph heterogeneity with mixed heavy-tailed regimes to diversify synthetic dependency structures. Across tabular benchmarks, SOMTab approaches the performance of strong Transformer-based tabular foundation models while achieving faster inference and lower GPU memory usage, yielding a favorable efficiency--accuracy trade-off.

---


### 59. [There and Back Again: Bidirectional Diffusion Bridges for Multimodality Translation](https://arxiv.org/abs/2608.27885)

**<font color=#1a73e8>作者：</font>** Gabe Guo, Elon Litman, Thanawat Sornwanee 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multimodality translation (e.g., text-to-image) is a core generative AI task. However, existing approaches (1) follow generative paths that do not directly represent the source modality, limiting the flexibility of some sampling algorithms; and (2) are unidirectional, preventing inversion (e.g., image-to-text). We propose BIT: Bidirectional Image-Text Diffusion Bridges. In contrast to previous approaches, BIT starts directly from text and interpolates into images, providing (1) a source-aware generative path that enables diverse and flexible sampling algorithms; and (2) an endpoint-conditioned process that can be traversed from image to text, providing a unified, bidirectional generative framework. BIT is derived through stochastic calculus, yielding SDE forms amenable to simulation and tractable loss functions that scale to high dimensions. Our experiments show that BIT is competitive with denoising-diffusion and deterministic-flow baselines, and outperforms them on several vision--language and natural-science evaluations.

---


### 60. [Resource Constraints and Performance in Agentic AI Systems](https://arxiv.org/abs/2608.27886)

**<font color=#1a73e8>作者：</font>** Amaz Salman, Malka Halgamuge, Teo Susnjak  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Progress toward more autonomous AI increasingly depends on agentic systems that combine a language model with tools, memory, state management, and multi-step execution. These mechanisms shape both task capability and operational burden. We compare OpenClaw and NanoBot as complete agentic systems using a paired primary benchmark and a more detailed instrumented subset of paired prompts. In the primary benchmark, the rate of full task completion was 31% for OpenClaw and 25% for NanoBot, a six-percentage-point difference with a 95% task-bootstrap interval from -3 to 15 percentage points, providing no statistically established full-completion advantage for either system. In the instrumented layer, both systems achieved 26% full completion, while NanoBot reached at least partial completion on 43% of prompts compared with 26% for OpenClaw. OpenClaw took longer on 83% of prompts and had a higher recorded peak-memory value on every prompt, with geometric mean ratios of 2.98 for wall time and 19.44 for peak memory. Among the ten detailed-layer prompts on which at least one system achieved partial or full completion, NanoBot weakly dominated on eight; across all 23 prompts, however, ten of its eighteen dominance cases were cheaper joint failures. Outcome labels differ across the two evidence layers, showing why agent-system evaluation should connect capability and resource measurements to attempt-level execution and scoring provenance. These findings show that progress toward more autonomous AI should be evaluated through verified task completion, observed resource use and records linking each result to the execution that produced it.

---


### 61. [CommerceVibe: Learning to Design E-Commerce Creatives as Executable Visual Code via Dual-Feedback Reinforcement Learning](https://arxiv.org/abs/2608.27893)

**<font color=#1a73e8>作者：</font>** Yajiao Xu, Jin Zhang, Jiangbo Ai 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> High-quality e-commerce creatives are essential for presenting products and conveying marketing messages. Recent diffusion models enable scalable creative generation and produce visually compelling images, but their flattened raster outputs often contain distorted text and inconsistent product details, requiring refinement before deployment. Moreover, without explicit structure, the resulting creatives are difficult to edit and reuse, while complex design requirements remain challenging to encode as verifiable training signals. To address these challenges, we present CommerceVibe, which represents creatives as executable visual code and formulates generation as conditional HTML/CSS program synthesis. Given product images, design requirements, and product information, it produces renderable, editable, and reusable creatives. We further introduce dual-feedback reinforcement learning, in which rule-based feedback evaluates rendered programs for text readability, product visibility, and layout validity, while visual feedback from a vision-language model (VLM) assesses rendered creatives against input specifications across six perceptual and commercial dimensions. Together, these complementary feedback signals improve both constraint satisfaction and perception-dependent quality. We perform supervised fine-tuning (SFT) of Qwen3.5-9B on over 28,000 e-commerce examples, followed by dual-feedback reinforcement learning. On a 1,300-case benchmark, the optimized CommerceVibe model achieves a weighted score of 94.0/100, compared with 87.3 for the SFT-only variant, and outperforms strong external models. Blind evaluations by five e-commerce design experts further validate these improvements. CommerceVibe supports controllable, editable, and scalable e-commerce creative production.

---


### 62. [OpenStamp: A Watermark for Open-Source Language Models](https://arxiv.org/abs/2608.27899)

**<font color=#1a73e8>作者：</font>** Miroojin Bakshi, Saksham Rastogi, Danish Pruthi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> With the growing prevalence of large language model (LLM) generated content, watermarking is considered a promising approach for attributing text to LLMs and distinguishing it from human-written content. A prominent class of techniques embeds subtle but detectable signals in generated text by modifying token sampling probabilities. However, such methods are unsuitable for open-source models, where users have white-box access and can easily disable watermarking during inference. In this work, we introduce OpenStamp, a watermarking technique that encodes the watermarking logic directly into the model weights by modifying only the final projection, or unembedding, layer. Through experiments across two models, we show that OpenStamp achieves superior detection performance, with minimal degradation in model capabilities compared to prior methods. The implanted watermark is explicitly designed, and empirically confirmed, to be more robust to paraphrasing attacks and harder to scrub off through post-hoc fine-tuning than prior open-source watermarks. To enable developers to watermark their models, we release our code alongside watermarked versions of 4 popular open-source models.

---


### 63. [LandingAgent: A Reference-Annotated Dataset and Agentic Generation Framework for Landing Pages](https://arxiv.org/abs/2608.27902)

**<font color=#1a73e8>作者：</font>** Injun Baek, HyeongSeok Lee, Yearim Kim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Landing pages are goal-oriented web interfaces that must communicate a target-specific value proposition while organizing information flow, visual hierarchy, and calls to action (CTA). Although large language models can generate plausible webpage code from natural-language prompts, direct generation often yields generic templates and unsupported persuasive claims. We study target-grounded, reference-guided landing-page generation, where a system must create an executable page for a new target by adapting reusable patterns from real pages without copying them. We introduce LandingBench, a reference-profile dataset that abstracts real landing pages into section sequences, layout patterns, tone descriptors, visual emphasis, and CTA structure. Building on LandingBench, we propose LandingAgent, a three-phase agentic framework that profiles the target, constructs a reference-guided wireframe, and refines the page through critique-guided polishing. We evaluate LandingAgent against direct prompting on faithfulness, conciseness, readability, aesthetics, and structural diversity. Experiments show improved target grounding, presentation quality, and layout diversity. Code is available at this https URL.

---


### 64. [Rubric-to-Code Credit Assignment for Reinforcement Learning](https://arxiv.org/abs/2608.27906)

**<font color=#1a73e8>作者：</font>** Rui Jin, Jikai Chen, Yihan Chen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Interactive web application generation requires models to produce usable HTML, CSS, and JavaScript applications from natural language requests. Unlike conventional code generation, application quality depends on multiple user-facing functional requirements, each often tied to localized code regions such as event handlers, state updates, DOM fragments, or CSS selectors. Standard GRPO collapses these structured outcomes into a single sequence-level reward and applies the resulting advantage uniformly to all tokens, weakening credit assignment. We propose \textbf{Rubric-to-Code Credit Assignment} (RCCA), a reinforcement learning framework that converts rubric-level functional feedback into localized optimization signals over generated code. RCCA builds training tasks around explicit functional rubrics, uses a hierarchical reward to separate format, source-code, runtime, and functional failures, and aligns evaluator-generated textual attributions with responsible code spans and generated tokens. The resulting model, \textbf{Ling-RCCA-Flash}, scores 41.25 on MiniAppBench, improving Ling-3.0-Flash by 32.20 points and slightly surpassing Claude Opus 4.5. It also reaches 76.19 on ArtifactsBench, improving the SFT model by 4.48 points and establishing a new top score under the official ArtifactsBench leaderboard setting by surpassing the GPT-5 score by 3.64 points, suggesting transferable implementation-level gains.

---


### 65. [AI Alignment through a Game-theoretic Lens: A Survey](https://arxiv.org/abs/2608.27910)

**<font color=#1a73e8>作者：</font>** Yanan Cai, Zhongrui Zhao, Zhigang Lu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As large language models and increasingly capable AI agents are deployed in high-risk settings, aligning them with complex human values has become a central challenge. Existing alignment methods, while effective in improving helpfulness, harmlessness, and controllability, often struggle to capture real-world preferences that are context-dependent, non-transitive, and shaped by dynamic multi-party interactions. This survey reviews AI alignment through a game-theoretic lens. Specifically, it organizes recent progress around key game-theoretic elements and synthesizes the literature along three challenges: preference diversity, alignment priority, and temporal dynamics. This perspective clarifies where current alignment methods genuinely benefit from game-theoretic analysis, where the framework is looser, and what challenges remain in building robust, adaptive, and verifiable AI systems.

---


### 66. [TACIT-Switch: Cost-Aware Model Escalation for LLM Agents from Censored Supervision](https://arxiv.org/abs/2608.27911)

**<font color=#1a73e8>作者：</font>** Ji'an Lei, Jian Huang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Agents with smaller language-model backbones are less expensive but can drift into persistent failure modes, whereas those with larger backbones are generally more reliable but more costly. This reliability-cost trade-off motivates routing methods that decide when to invoke an agent with a larger backbone: before execution, after a fixed trajectory prefix, or locally at individual steps. Our method, TACIT-SWITCH, learns permanent handoff policies from accumulated trajectory evidence and Teacher-Annotated Censored Intervention Times (TACIT). It represents each annotation as an interval-censored observation on a cumulative-risk scale. The resulting mixture-cure threshold model estimates the probability that the paired Strong rollout succeeds and, conditional on success, the handoff threshold; no teacher is required at deployment. In a mechanism-based multi-step simulation, TACIT-SWITCH improves success by 7.4-11.1 percentage points over task-level, step-level, and fixed-prefix routing baselines at comparable cost. Within that controlled simulation, ablations show that task features and cumulative trajectory risk provide complementary information. With operating points selected on development data, TACIT-SWITCH achieves the highest held-out success among learned policies on both ALFWorld (48.5% with 4B Cheap; 45.5% with 9B Cheap) and DABench (73.1%).

---


### 67. [From Documents to Reasoning: A Validated Synthetic Data Pipeline and Semantic-Aware Fine-Tuning for Financial Numerical Reasoning](https://arxiv.org/abs/2608.27919)

**<font color=#1a73e8>作者：</font>** Lokendra Birla, Milind Savagaonkar, Visnu Srinivasan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Financial question answering (QA) has emerged as a key benchmark for evaluating the performance of Large Language Models (LLMs) on domain-specific tasks involving complex data formats such as tables, charts, and rich textual narratives. While recent advancements have enabled models to reason across modalities and perform multi-step arithmetic operations, limitations remain in performance consistency, and evaluation reliability. In particular, standard evaluation metrics like Exact Match (EM) often fail to account for minor variations such as differences in units or formats, misleading performance assessments.
In this work, we propose a comprehensive pipeline for improving financial QA systems through high-quality synthetic data generation and fine-tuning of smaller language models (SLMs) using Quantized Low-Rank Adaptation (QLoRA). Our pipeline includes aggressive data validation for synthetic question answer generation to ensure the relevance and correctness of synthetic question-answer pairs. We introduce a novel evaluation metric that matches answers computed from arithmetic expressions rather than ground-truth answers; providing a more accurate reflection of model reasoning capability. Furthermore, we propose a modified loss function that aligns predicted and reference expressions using semantic similarity, our novel evaluation metric and standard cross-entropy, resulting in improved performance. Experimental results on benchmark datasets, ConvFinQA demonstrate significant gains in QA accuracy after fine-tuning using synthetic dataset and proposed loss function.

---


### 68. [DensityKV: Density-Guided KV Cache Compression for Long Video Generation](https://arxiv.org/abs/2608.27922)

**<font color=#1a73e8>作者：</font>** Wenqu Zhao, Xuemin Chi, Xin Zhang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autoregressive video diffusion models enable streaming generation through sliding-window attention, but each generated block is conditioned on previously generated content, causing appearance and motion errors to propagate recursively over time. Historical key-value (KV) memory preserves earlier subject and scene states and helps maintain long-horizon consistency. However, retaining every generated state creates a historical archive that grows continuously with the rollout, while recurrent states repeatedly add redundant coverage. To address this problem, we propose DensityKV, a training-free historical KV bank management strategy. DensityKV maintains a separate token-level KV bank for each attention head and measures local redundancy among the post-RoPE keys that directly parameterize attention routing using Soft-Riesz density. By constraining neighborhood-density growth after states enter the bank, DensityKV limits repeated historical accumulation while preserving coherent states from each completed generation block. Experiments across three autoregressive video generation backbones and multiple generation lengths show that, at the same upper bound on historical KV capacity, DensityKV improves long-horizon consistency and generation stability while keeping persistent historical storage bounded independently of rollout length.

---


### 69. [What Makes Agent Memory Useful for Reliable Unanswerable Question Handling?](https://arxiv.org/abs/2608.27924)

**<font color=#1a73e8>作者：</font>** Chuanyuan Tan, Junjie Yu, Yuxin Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reliable handling of unanswerable questions (UAQs) is critical for trustworthy LLM-based agents. Although memory is widely used in agent systems, its role in reliable UAQ handling remains unclear. We present a systematic study of agent memory for UAQ handling under a unified agentic RAG framework, evaluating four representative memory methods across three UAQ-related datasets and two base models.
We find that memory can improve UAQ performance in some settings, but such gains are selective rather than universal and remain fragile under dataset shift. Interestingly, cross-model memory reuse is often more feasible than cross-dataset transfer, suggesting that shifts in answerability patterns pose a greater challenge to memory reuse than changes in the base model itself. We further find that UAQ gains are more strongly preserved through decision guidance than through trajectory shaping, and that memory effectiveness depends strongly on representation. In particular, procedural and rule-based memories often provide the most reliable support for UAQ handling, while memory composition is most effective when procedural guidance is combined with complementary behavioral signals. Overall, our findings suggest that reliable UAQ memory depends less on storing larger amounts of experience and more on preserving transferable behavioral guidance.

---


### 70. [Entity-Memory Graph Retrieval Improves Evidence Coverage in Long-Conversation Question Answering](https://arxiv.org/abs/2608.27925)

**<font color=#1a73e8>作者：</font>** Shumao Sun  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Entity-Memory graph retrieval keeps dialogue turns as verbatim Memory nodes, links repeated mentions through shared Entities, and connects adjacent Memories with directed chronological edges. At query time the retriever moves from Entity gating through semantic fusion and one-hop chronological recovery to dense backfill. The path can keep a neighboring Memory that dense cosine ranking would otherwise omit. A matched dense control shares the Memory and query vectors, context budget, requested answer protocol, and evaluator, isolating graph structure from changes to the reader.
On 1,986 questions from ten LoCoMo conversations, graph retrieval raises official evidence recall at top-k 25 from 79.7468% to 84.4842%. The recall advantage is supported from top-k 5 to 50, while no matched cutoff supports an overall final-answer F1 difference. Four paper-eligible requested configurations support empirical robustness across the tested GPT-3.5 and DeepSeek extractors on both outcomes. Embedding robustness is mixed: F1 has no supported contrast, but recall is sensitive to the embedding artifact. The comparison isolates a retrieval-coverage gain from graph structure. It does not establish a final-answer F1 gain, model or embedding equivalence, or cross-dataset generalization.

---


### 71. [Training-Free Temporal Abstraction for General Video Understanding](https://arxiv.org/abs/2608.27929)

**<font color=#1a73e8>作者：</font>** Etienne Casanova, Sevan Brodjian, Pietro Perona  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Videos are expensive to analyze frame by frame, yet many video understanding tasks depend on knowing where relevant moments occur. A system may need to find when an action changes, locate the segment described by a sentence, or choose a few frames for a vision-language model. Existing methods often solve these problems separately, using task-specific training data or specialized architectures. We study whether a pretrained video-text model can provide enough temporal structure to support several of these tasks at once. We present STITCH, a training-free method that divides a video into semantically meaningful temporal chunks. STITCH embeds short video windows with a frozen video-text backbone and detects changes in the resulting embedding sequence. These chunks are computed once per video and reused across tasks. We evaluate STITCH on generic event boundary detection, language-based moment retrieval, and frame selection for long-video VLM reasoning. Across all three settings, STITCH remains competitive with more specialized methods while requiring no task-specific training, with especially clear gains when only a small number of frames or tokens can be processed. These results suggest that reusable temporal abstraction is a promising direction for general video understanding, allowing dense video streams to be converted once into semantic units that can be localized, retrieved, sampled, or reasoned over by downstream systems.

---


### 72. [Graphionale: How Graph Visualizations of LLM Rationales Affect Human Decision Making](https://arxiv.org/abs/2608.27932)

**<font color=#1a73e8>作者：</font>** Xinru Wang, Zhexuan Ma, Ming Yin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are increasingly equipped with augmented reasoning capabilities to generate rationales that support human decision-making. Yet these text-dense rationales often impose substantial cognitive burdens. Building on a formative co-design study that identified user preferences for non-linear reasoning representations, we developed Graphionale as a testbed for empirically studying argument-map-style rationale visualization. This system transforms linear LLM rationales into interactive, multi-level graphs. It explicitly structures logical relationships (e.g., conclusions, premises, support, and objections), while further extracting entities and relations within each statement to construct condensed node-link representations. We conduct a large-scale online user study (N = 204) to examine when graphical rationales are more effective than textual ones, across varying task modality (verbal vs. visual reasoning), rationale format (textual vs. graphical), and question difficulty (easy vs. hard). Our results show that graphical rationales do not help uniformly: they improve trust calibration for verbal reasoning yet feel more cognitively demanding and less satisfying; for visual reasoning, they impair calibration yet feel more engaging and helpful. In each modality, the format that better supports calibrated decisions is not the one users prefer, highlighting that matching rationale format to task modality is key to effective AI explanation design. Our findings contribute empirical design knowledge about when and how graphical rationales support human decision making, and inform the next-generation reasoning-aware AI interfaces.

---


### 73. [Cross-Session Decomposition Attacks: Scaling Risk and Intent-Aligned Retrieval Defense](https://arxiv.org/abs/2608.27945)

**<font color=#1a73e8>作者：</font>** Disen Liao, Yihan Wang, Freda Shi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Scaling laws are usually read as a capability story: lower language-modeling loss yields more useful models. We study a safety consequence of this mechanism in \emph{cross-session decomposition attacks}, where benign-looking subqueries are asked across independent interactions and later recomposed toward a forbidden objective. We formalize this setting as \emph{compositional safety risk} and prove a conditional risk-transfer bound: when the reference environment already contains dispersed evidence for a risky reconstruction, the gap between deployed composed risk and reference composed risk is controlled by the model's excess loss on allowed subqueries. Synthetic withholding experiments show that wider transformers assign lower loss to held-out instructions that never appear verbatim in training but are recoverable from injected supporting facts. A 600-intent pretrained-LLM evaluation shows that larger Qwen3 and Gemma3 family members can yield greater harmful-capability uplift under a fixed decomposition-composition pipeline. As a defense, IntentAlign-MiniLM, our 22M-parameter intent-aligned retriever, outperforms much larger embedding models on held-out intent retrieval and yields the best learned-retriever harmful recall across tested guardrails. Code is available in \href{this https URL}{our GitHub repository}.

---


### 74. [The Illusion of $\textit{What If}$: Evaluating the Breakdown of Counterfactual Reasoning in LLMs](https://arxiv.org/abs/2608.27953)

**<font color=#1a73e8>作者：</font>** Yucheng Wang, Yuetian Du, Zhengyi Liu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Counterfactual reasoning requires models to reason beyond the observed world and explain how altered conditions propagate through downstream consequences. Existing benchmarks largely target bounded settings with fixed variables or single gold outcomes, overlooking open-domain scenarios requiring causal-process evaluation. To this end, we present $\textbf{WhatIfBench}$, a diagnostic benchmark for open-domain, open-form, long-horizon counterfactual causal reasoning, containing 220 what-if questions across STEM, HSS, and Hybrid scenarios. To evaluate free-form responses, we further propose $\textbf{PRISM}$, which first converts each natural-language explanation into a Response-Derived Semantic Causal Graph of events, states, and mechanisms. On top of this graph, PRISM then jointly applies a Process Metric assessing graph-level causal validity and a Rubric Metric assessing answer-level explanatory adequacy. Evaluating six frontier LLMs with this framework, we find that WhatIfBench remains far from saturated: even the strongest model reaches only a 64.62% final score. Further analysis reveals persistent causal gaps, premise drift, and topology fragmentation, suggesting that fluent counterfactual narratives often mask fragile causal processes. The benchmark, code, and evaluation scripts are available at $\href{this https URL}{WhatIfBench}$.

---


### 75. [Not to Break, but to Attest: Adversarial Probes for Privacy-Preserving LLM Verification](https://arxiv.org/abs/2608.27954)

**<font color=#1a73e8>作者：</font>** Cameron Wilding, Mina Shaker, Fatemeh Ganji  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Post-deployment changes to large language models can alter behavior while leaving routine outputs largely unchanged, creating a challenge for AI governance when model weights are proprietary. We present a privacy-preserving zk-SNARK-based audit framework that searches for probes designed in the spirit of adversarial examples to amplify logit drift between an approved model and a modified deployment. Our framework explores complementary probe families under different access models. Token-based probes operate in a black-box setting and require only the input interface, tokenizer, and vocabulary. Embedding-based probes require gray-box access to the embedding interface. Stress probes rely on additional interface capabilities but do not require full white-box access to model weights or architecture. This range allows probe selection to balance sensitivity, access requirements, and deployment cost. We evaluate probe constructions across LLM architectures, model-tampering scenarios representative of post-deployment attacks, and GPU platforms. Importantly, our experimental results demonstrate that token-based probes consistently deliver the strongest mean sensitivity across models and GPU platforms, although operating in a black-box setting. Our Groth16 zk-SNARK workflow remains practical as the probe set scales from 1 to 50, where proving time increases from 1.02 to 1.78 seconds, verification remains near 0.84 seconds, and proof size remains constant.

---


### 76. [When Teacher Guidance Misleads: Reward-Aligned On-Policy Distillation](https://arxiv.org/abs/2608.27960)

**<font color=#1a73e8>作者：</font>** Siyuan Gan, Yuhan Li, Xiran Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) has recently emerged as a popular post-training paradigm for large language models (LLMs), providing an efficient way to transfer the knowledge and capabilities of teacher models into student models. However, teacher guidance on student-generated prefixes is not always reliable. Training should optimize the model to generate responses that are more likely to be correct, or equivalently, to get higher outcome rewards. But during OPD, the teacher model may provide guidance that discourages the student from moving toward correct trajectories or moves the student toward incorrect ones, which is misaligned with outcome reward. Such misaligned guidance is unreliable, as it would mislead the optimization process and ultimately degrade model performance. To mitigate misaligned teacher guidance, we propose Reward-Aligned On-Policy Distillation (RA-OPD). The key insight is to keep only trajectories whose induced updates move the student toward correct trajectories or discourage the student from moving toward incorrect ones. Specifically, for each sampled trajectory, RA-OPD checks whether its trajectory-level distillation return is consistent with its outcome reward and then filters out the misaligned trajectories. RA-OPD selects more reliable trajectories to improve student model performance without requiring additional computational cost. We evaluate RA-OPD on math and code benchmarks using models from the Qwen3 family and the DeepSeek-R1 family. Across seven math benchmarks and three code benchmarks, RA-OPD significantly outperforms standard OPD and other tested OPD variants.

---


### 77. [SABER: Stability-Aware Early Exit for LLM Reasoning via Adversarial Branch Probing](https://arxiv.org/abs/2608.27963)

**<font color=#1a73e8>作者：</font>** Wanli Cheng, Haiya Xiang, Juntao Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Reasoning Models (LRMs) achieve strong reasoning capabilities, yet long-chain reasoning becomes inefficient once the intermediate answer stabilizes across reasoning steps: additional reasoning yields little marginal benefit while incurring substantial inference cost. Existing early-exit methods based on confidence or entropy poorly capture reasoning stability, while consistency-based approaches rely on multi-step trajectory agreement, requiring sequential evaluations that delay exit. To better balance efficiency and reliability, we propose SABER, a training-free framework for stability-aware early exit via adversarial branch probing. SABER constructs simple yet effective semantic perturbations around intermediate reasoning states to form adversarial branches, and applies lightweight probing to estimate their likely final outcomes without full trajectory rollouts. When the probed outcomes remain consistent across branches, SABER exits early; otherwise, it continues reasoning. Experiments across multiple reasoning benchmarks and model architectures show that SABER reduces reasoning token consumption by 30.2\%--39.8\% on average while maintaining competitive accuracy with full-length reasoning.

---


### 78. [AERA: Adaptive Evidence Residual Allocation for Efficient Test-Time Reasoning](https://arxiv.org/abs/2608.27964)

**<font color=#1a73e8>作者：</font>** Ziming Wang, Ivor Tsang, Hangwei Qian  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Test-time scaling improves language-model reasoning by generating additional candidate solutions, but allocating the same inference budget to every problem is computationally wasteful. Existing adaptive stopping methods commonly rely on confidence, agreement, or answer stability, implicitly assuming that stronger current evidence indicates that further computation is unnecessary. We show that this assumption can fail: checkpoint-level correctness evolves non-monotonically, and observable evidence may strengthen before an answer collapses or weaken before it recovers. Motivated by this mismatch, we introduce Adaptive Evidence Residual Allocation (AERA), a sequential controller that learns whether additional computation is likely to recover a better answer from checkpoint-observable evidence. AERA characterizes cumulative response prefixes using answer-distribution, temporal, re-solving, semantic, and compute features, and repeatedly decides whether to stop or allocate the next response block. Future checkpoint correctness is used only to construct offline supervision and is never available to the controller at inference time. Across GSM8K and GPQA Diamond, AERA identifies question-specific residual opportunities while substantially reducing inference computation. In a frozen-threshold incremental-generation evaluation on 300 untouched GSM8K questions, AERA achieves 92.61% accuracy versus 93.01% with 128 responses while reducing completion tokens by 95.99%. These results suggest that adaptive reasoning should estimate the future value of computation rather than equating present confidence with correctness.

---


### 79. [openJiuwen: Beyond Static Harnesses for Long-Horizon Coding Agents](https://arxiv.org/abs/2608.27969)

**<font color=#1a73e8>作者：</font>** openJiuwen Team, Tao Yu, Xinyu Zhang 等 20 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-horizon coding agents operate over evolving repository states while increasingly relying on heterogeneous capabilities, delegated agents, and multi-agent coordination. These trends pose two complementary challenges for the agent harness. First, developers need to compose capabilities, reconfigure execution logic, and scale increasingly complex agent systems without repeatedly rebuilding orchestration. Second, complex coding tasks continuously produce new evidence---such as semantic diagnostics, execution outcomes, task progress, and changing context relevance---that should dynamically influence subsequent runtime decisions. We characterize these challenges as Structural Composability and Runtime Adaptivity. We present openJiuwen, an open-source harness designed for both developer composability and adaptive task execution. openJiuwen provides a shared execution substrate and Rail-based capability composition across single agents, delegated sub-agents, and Swarm Flow, enabling developers to construct sophisticated agent harnesses under common execution semantics. It further adapts framework-controlled runtime decisions around a fixed model policy, allowing evolving evidence to dynamically affect context, feedback, and task control toward successful completion. We systematically evaluate openJiuwen on SWE-bench Verified and Terminal-Bench 2.1, where it achieves 82.6% and 87.19%, respectively, exceeding the strongest selected official-leaderboard point estimates by 3.4 and 3.39 percentage points. These results show that openJiuwen achieves strong performance on complex coding tasks while providing a composable and adaptive harness design.

---


### 80. [QUORUM: QUality-Optimized Routing Using Multiple annotators](https://arxiv.org/abs/2608.27974)

**<font color=#1a73e8>作者：</font>** Antonio Purificato, Maria Sofia Bucarelli, Andrea Bacciu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Data annotation remains a central bottleneck in natural language processing, requiring human effort to obtain high-quality labels at scale. While Large Language Models (LLMs) offer a fast and cost-effective alternative, their reliability is highly instance-dependent: they perform well on simple inputs but often fail on examples requiring nuanced reasoning or contextual understanding. In this work, we address this challenge with QUORUM (QUality-Optimized Routing Using Multiple annotators), a budget-aware routing framework that dynamically assigns each instance to human or LLM annotators under a fixed annotation budget. Unlike prior approaches relying on model confidence or uncertainty estimates, QUORUM leverages feature-based signals to estimate instance difficulty and supports multiple annotations per instance, combining them through agreement-based rewards to improve reliability. We evaluate QUORUM across diverse closed- and open-ended annotation tasks in English and multilingual settings, and QUORUM improves annotation quality by up to 34.4% while reducing costs by 8.8% over competing methods. Code can be found at this https URL.

---


### 81. [CHISEL-ing Back Source Code with AI-enabled Iterative Recovery](https://arxiv.org/abs/2608.27981)

**<font color=#1a73e8>作者：</font>** Varun Kohli, N Raghava, Biplab Sikdar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Decompilation aims to recover high-level, compilable, and semantically equivalent code from binaries. Traditional decompilers produce pseudo-C that is difficult to read and does not compile, while the recent LLM-assisted approaches generate readable, but semantically incorrect code. LLM-aided iterative recovery is an emerging branch of research, but prior works rely on supplied test suites for semantic recovery. In this work, we present CHISEL, a test suite-free framework to iteratively recover source code from Ghidra-derived pseudo-C. CHISEL uses simple yet effective feedback from a compiler (static analysis) and a coverage-guided fuzzer (differential analysis), augmented by rich observables for grounded divergence detection and feedback, cross-iteration divergence memory, and best candidate retention. We systematically evaluate CHISEL for compilation and semantic recovery, feedback oracle soundness, and iteration overhead on 120 ExeBench functions compiled for the x86-64 architecture, across four optimizations (O0-O3), in both stripped and unstripped variants, using the open-weight Gemma4:31b LLM. CHISEL, with all recommended features, achieves an average of 96.1% re-compilability and 79.8% re-executability rates at an average of 2.1 iterations. Significantly, CHISEL recovers 26% of first-generation execution errors. At the same time, CHISEL feedback oracle falsely accepts only 9.4% candidates. Lastly, CHISEL performs significantly better than two recent prior work on LLM-assisted decompilation.

---


### 82. [When Evidence Shapes Collaboration: Knowledge-Conditioned Topology Generation for Multi-Agent Systems](https://arxiv.org/abs/2608.27984)

**<font color=#1a73e8>作者：</font>** Yangxiao Jiang, Jiarun Fan, Mingcong Xu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-Agent Systems (MAS) have recently moved from static workflows toward dynamically generated collaboration topologies. However, existing topology generation methods rely primarily on the parametric knowledge of large language models, with external search or retrieval used only as a reactive tool rather than an explicit determinant of collaboration structure. This leads to structure-knowledge misalignment, where systems exhibit redundant interactions or insufficient verification in knowledge-intensive tasks. We propose K-GAT (Knowledge-Guided Agent Topology Generator), a neuro-symbolic framework that formulates collaboration topology design as a knowledge-conditioned structure learning problem, integrating external evidence directly into autoregressive graph generation. Extensive experiments on knowledge-intensive benchmarks demonstrate K-GAT's efficiency and effectiveness: notably on the expert-level GPQA dataset, K-GAT outperforms the LLM-Debate baseline by a substantial margin of +15.7% in accuracy, while consuming less than half the computational tokens.

---


### 83. [CAITLYN: Can LLM Agents Autonomously Synthesize Defenses against Emerging Injection Attacks?](https://arxiv.org/abs/2608.27990)

**<font color=#1a73e8>作者：</font>** Zi Liang, Xiaoyu Xu, Yanyun Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Prompt injection attacks on Large Language Model (LLM) agents seek to introduce malicious instructions or content into external text sources retrieved by agents, forcing the underlying LLMs to execute harmful actions outside their benign scope. While current defenses effectively counter known injection attacks, deploying them in LLM agent environments remains challenging due to attack variants and emerging threats. Moreover, existing solutions typically suffer from an inherent trilemma, i.e., a constant trade-off among runtime efficiency, contextual precision, and adaptability. To bridge this gap, we propose Continuous Agents for Injection Threats via Lifelong Yielding Nexus (CAITLYN), an agent-agnostic defense middleware. CAITLYN integrates two systems. System I focuses on immediate defense against existing attacks using a two-tiered library: Tier-0 for rule-based detection scripts and Tier-1 for optimized LLM-based accurate inference. System II, in contrast, is deployed to monitor potential abnormal signals and attempt to synthesize new defenses. On standard benchmarks, CAITLYN matches the detection performance of state-of-the-art defenses at lower token overhead than LLM-as-a-judge baselines. On Emerging, our new delivery-aware benchmark featuring novel injection techniques, static baselines and the standalone System I configuration remain vulnerable. In contrast, System II autonomously synthesizes verified defense capabilities, substantially lowering the attack success rate across three diverse agent environments.

---


### 84. [Moirae: A Multimodal Agent Collaborative Framework for Dynamic Android Malware Detection](https://arxiv.org/abs/2608.27994)

**<font color=#1a73e8>作者：</font>** Xueying Zeng, Youquan Xian, Yanze Li 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The Android ecosystem faces persistent and rapidly evolving malware threats. Existing machine learning detectors are vulnerable to concept drift because they rely on implementation-specific features whose distributions change over time. Large language models (LLMs) offer strong semantic understanding and zero-shot reasoning, but current LLM-based detectors typically depend on code-centric or single-dimensional evidence, making them susceptible to obfuscation and limiting comprehensive behavior analysis. We present {\sysname}, a multimodal agent collaborative framework for dynamic Android malware detection. {\sysname} dynamically collects multimodal runtime evidence and employs ReAct-based specialized agents to analyze complementary behavioral views. The detection process begins by identifying visual deception cues, modeling UI state transitions, and integrating runtime API behaviors to fuse multi-dimensional evidence across user-visible interfaces and hidden backend operations. Experiments on temporally and distributionally unseen datasets show that {\sysname} achieves an accuracy of 90.06\% without fine-tuning, outperforming state-of-the-art baselines and demonstrating strong zero-shot generalization against Android malware concept drift.

---


### 85. [Automated Analysis Framework for Multilingual Climate-Health Literature Based on Multi-Agent Large Language Model](https://arxiv.org/abs/2608.27998)

**<font color=#1a73e8>作者：</font>** Yuze Sun, Shihui Zhang, Jiancheng Pan 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The rapid proliferation of interdisciplinary and multilingual scientific literature has left traditional manual analysis and single-algorithm methods plagued by low efficiency, poor scalability, and insufficient domain adaptability. Targeting the literature analysis needs of the typical interdisciplinary climate-health field, this study proposes a multi-agent large language model automated analysis framework for multilingual scientific literature, which realizes full-process automation covering literature screening, structured information extraction, and standardized integration. With a central coordination module as the core, the framework deploys three dedicated agents for document evaluation, information extraction, and analytical review to mimic the literature analysis thinking of domain experts, and adopts a four-layer hallucination control strategy together with a manual verification procedure to ensure the accuracy and reliability of analytical outcomes. Validated on a bilingual Chinese-English corpus of 32,642 climate-health papers covering China from 1993 to 2023, the framework achieves an F1 score of 0.92 in core information extraction, and completes the extraction and standardization of 2,012 city-literature association pairs, offering effective technical support for large-scale evidence mining in the climate-health research domain.

---


### 86. [A Method for Layer Bit-Width Allocation in LLM Quantization via Performance Maximization Under a Quality-Degradation Constraint](https://arxiv.org/abs/2608.28003)

**<font color=#1a73e8>作者：</font>** Artem Safronov  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper proposes a layer bit allocation method for Gemma-3-1B, formulating the problem as performance maximization (latency decrease) given a degradation budget constraint (allowable level of generation quality loss). This approach is different from time- and resource-consuming uniform layer quantization methods that are used in the literature (like GPTQ or AWQ) or allocation methods without proven performance-accelerating effect (like MixLLM or TorchAO). The layer sensitivity profile resulting from our prior work SA-PTQ is applied using the activation pass-through mode inside TensorRT-LLM. For each layer precision is determined individually in blocks, according to a grouping introduced in the prior step (5+5, 10+10, all26), differentiating the contribution of FFN, Attention, and lm_head to the overall speedup. The clock speed was measured for 13 W8A8 variants on an RTX 5090. We find that for FFN and lm_head the time cost of quantization/dequantization is compensated for by the use of integer arithmetic, while for short context lengths, the opposite holds true for Attention: an additional step of quantization slows execution down. We propose a manual implementation of SmoothQuant for TensorRT-LLM which was necessary due to export failures, unavailable for lm_head. The best solution found under joint consideration of all three criteria with minimal degradation was FFN 5+5 with lm_head, providing an 11.0% reduction in latency with negligible quality loss (98.90% Top-1 agreement, +0.85% perplexity degradation). With acceptable quality loss for FFN all26 + lm_head, a speedup up to 19.1% was found possible. We suggest further optimizations: fused attention kernels in INT8, KV-cache quantization, using FP8 instead of INT8 and partial Attention quantization analogous to FFN.

---


### 87. [Visual Token Coding for Video Multimodal Large Language Models](https://arxiv.org/abs/2608.28008)

**<font color=#1a73e8>作者：</font>** Chenxin Fang, Tao Chen, JunChao You 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this paper, we propose a new token compression paradigm for video Multimodal Large Language Models (MLLMs), termed Visual Token Coding (VTC). Inspired by classical video coding principles, e.g., HEVC, VTC performs structured compression by predicting the I/P frames of a video and measuring their frame-wise residuals to estimate token redundancy. Based on this baseline framework, we also enhance VTC with a set of novel dynamic designs, such as Dynamic Resolution Input (DyRSO), Dynamic Token Allocation (DyTA), and Spatial Coverage Top-K (SC-TopK), and term this new approach $VTC_{Dy}$. To validate VTC, we apply it to three MLLMs and conduct experiments on multiple video understanding benchmarks. The experimental results show that VTC$_{\mathrm{Dy}}$ achieves an average performance retention of 100.1% with a 50% token budget for Qwen3-VL, while still retaining 97.8% of the average performance when the token budget is reduced to 25%. Moreover, as a plug-and-play design, VTC requires no additional tuning of MLLMs for token coding. Our code is available at this https URL.

---


### 88. [Beyond Global Scalars: Synergizing Token-Level Statistics and Deep Semantics for Adversarial AIGC Text Detection](https://arxiv.org/abs/2608.28009)

**<font color=#1a73e8>作者：</font>** Peiming Li, Yifan Wang, Zhiyuan Hu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The rapid evolution of large language models necessitates robust machine-generated text detection. Existing paradigms typically follow two isolated tracks. Training-free methods rely on global statistical scalars such as perplexity, while training-based methods utilize semantic hidden states. Both approaches exhibit fundamental vulnerabilities in adversarial scenarios. Global scalars act as lossy compressions that obscure local probabilistic burstiness in interleaved texts, whereas pure semantic models overfit to specific fingerprints and remain susceptible to spoofing. To expose these flaws, we introduce MOSAIC, a comprehensive adversarial benchmark comprising 16000 samples across a full-granularity attack spectrum. To address these challenges, we propose NeuroStat, an end-to-end framework bridging the statistical and semantic gap. NeuroStat captures uncompressed token-level probabilistic logits alongside deep semantic hidden states from a single causal language model backbone. We fuse these heterogeneous signals through Macro-State Residual Modulation, which adaptively calibrates local convolutional features using global uncertainty indicators. Orthogonal and contrastive losses further ensure the learning of complementary representations. Extensive experiments demonstrate that NeuroStat maintains exceptional robustness on MOSAIC compared to the severe degradation of state-of-the-art methods, establishing a new standard for adversarial text detection. Code and the MOSAIC benchmark are available at this https URL.

---


### 89. [When Can Conditional Flow Matching Replace Pointwise Negative Log-Likelihood?](https://arxiv.org/abs/2608.28010)

**<font color=#1a73e8>作者：</font>** Yansen Han, Hongxin Sun, Tao Lin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Flow matching enables likelihood-free training, yet alignment methods increasingly reuse conditional flow matching (CFM) losses as endpoint negative log-likelihoods (NLLs) and their old/new differences as log-likelihood ratios. We characterize when these substitutions are valid. For linear Gaussian paths, we exactly decompose endpoint NLL into entropy, a weighted CFM objective, an interior velocity--score residual, and a boundary residual. Thus CFM-only estimates and differences are exact only when the corresponding residuals cancel. At the off-policy population optimum, ordinary CFM is not generally a pointwise NLL estimator, whereas \(w_{\mathrm{sc}}(t)=(1-t)/t\) removes the interior residual; this positive result does not extend generally to training or on-policy alignment. On-policy log-ratios can remain biased even for identical endpoint laws or after surrogate optimization. Experiments across dimensions, distributions, and geometries support these conclusions and the mechanisms that make inexact ratios useful. **More broadly, the decomposition provides a theoretical basis for adapting likelihood-based LLM methods to flow matching, while distinguishing exact substitutions from controlled surrogates.**

---


### 90. [Coverage, Not Credit: Failure-Credit Routing of Zeroth-Order Perturbation Budgets Does Not Improve On-Pool Sample Efficiency for LLM Agents](https://arxiv.org/abs/2608.28011)

**<font color=#1a73e8>作者：</font>** Yuxu Ge  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Trajectory-level credit assignment can localize which module of a tool-using LLM agent causes failures using only verifiable signals. We ask whether such failure credit should route a fixed zeroth-order/evolution-strategies (ZO/ES) perturbation budget. Across a synthetic environment and frozen Qwen2.5-1.5B/3B and SmolLM2-1.7B agents, three task families, six allocation schemes, a credit-noise sweep, paired seeds, and exact sign-flip tests, we find no statistically detectable improvement over uniform allocation in any on-pool comparison (no gain of at least 2 percentage points). The joint soft-plus-sigma scheme is equivalent to uniform within a +/- 0.02 AUC margin on 1.5B and 3B; concentrating the full budget on the credit argmax is marginally equivalent on 1.5B, where that module is the verified bottleneck, and significantly worse on 3B. Inverse-propensity debiasing does not rescue routing, and misrouting costs up to -0.074 AUC in-house and -0.118 end-to-end on the BFCL-derived family. Across six fixed-step schedules, loss is linear in bottleneck starvation rate (R^2 = 0.94, descriptive), and a preregistered credit-free coverage floor removes detected harm. Matched-budget burst and step-compensating catch-up schedules are consistent with harm arising from insufficient cumulative parameter movement rather than update frequency. Our primary estimand is optimization efficiency on a fixed task pool. On unseen BFCL functions, the study's one exception is that soft routing exceeds uniform on held-out endpoints (+0.047, p = 0.031, n = 6). A plausible but untested reading is that routing-favored caller improvements transfer while uniform's on-pool gains reflect a synthesizer behavior specific to our harness. We report this exception explicitly and document three failure modes that can silently invalidate ZO/ES experiments on frozen LLMs.

---


### 91. [Twin Worlds: Equivariance-Based Abstention for Evidence-Grounded Reasoning](https://arxiv.org/abs/2608.28018)

**<font color=#1a73e8>作者：</font>** Vy Nguyen, Ziqi Xu, Jeffrey Chan 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Knowledge-intensive reasoning requires Large Language Models (LLMs) to ground answers in provided evidence. When evidence is insufficient, it is desirable that models abstain rather than confidently generating unsupported answers. Existing abstention methods rely on uncertainty estimation or evidence sufficiency checks, but neither tests whether the reasoning process for generation, driven by the interaction of provided evidence and the model's internal memory parameters, is actually grounded in the evidence. A key contributing factor is that entity mentions in context activate memorised associations, causing models to generate plausible responses ungrounded in evidence. We propose Twin Worlds (TW), a framework for improving reliability in knowledge-intensive reasoning through equivariance-based abstention: unlike invariance, which requires outputs to remain unchanged, equivariance requires outputs to transform correspondingly under entity substitutions. A model grounded in the evidence should produce answers that shift consistently when entities are substituted while their relations are preserved. TW constructs multiple worlds via typed substitutions of the original input that preserve relational structure while reducing parametric priors, and uses equivariance violations as an abstention signal. Across four benchmarks and three model backbones, TW identifies when answers are not reliably grounded in the provided evidence and outperforms uncertainty- and sufficiency-based baselines.

---


### 92. [Compared to What? A Human-Anchored Security Benchmark for LLM-Generated Infrastructure-as-Code](https://arxiv.org/abs/2608.28021)

**<font color=#1a73e8>作者：</font>** Animesh Shaw  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly used to author Infrastructure-as-Code (IaC), where a single insecure default can be deployed directly into production. Prior evaluations report raw vulnerability counts for model-generated IaC, but without a human baseline they cannot determine whether models are actually worse than engineers. We introduce GenIaC-SecBench, a benchmark of 100 deployment scenarios stratified by architectural complexity, evaluated across 12 model configurations from four vendors, producing 1,196 IaC artifacts scanned by three independent policy engines (Checkov, Trivy, KICS). Critically, we also scan 634 human-authored IaC templates with the same toolchain, providing the first size-matched human security baseline.
Vulnerability density is strongly inverse to artifact size (Spearman $\rho = -0.55$, $p < 10^{-77}$), meaning unmatched comparisons measure size rather than security. When matched on declared-resource count, all model configurations fall within 3.21x--3.87x the human vulnerability density, with the gap widening for simpler tasks (4.9x at one resource, 1.4x at twenty or more).
We decompose reasoning into standard generation, prompt-engineered chain-of-thought, and vendor extended-thinking APIs. Vendor extended thinking significantly outperforms prompted chain-of-thought ($-12.0\%$, $p = 0.0013$), while prompted chain-of-thought is indistinguishable from standard generation ($-1.3\%$, n.s.). Token instrumentation shows extended thinking uses under 1\% of the output budget, explaining its bounded effect.
Two negative results also emerge: deployability does not correlate with vulnerability ($r = 0.158$, $p = 0.625$), and classical complete-case Friedman testing is infeasible for realistic benchmark designs, motivating the Skillings-Mack statistic. All code, data, and regeneration scripts are released.

---


### 93. [String: An Agentic OS Where Every App Is a Markdown File](https://arxiv.org/abs/2608.28027)

**<font color=#1a73e8>作者：</font>** Jookyung Song, Nojun Kwak, Simyung Chang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents have become a new class of software user, but every surface they work through was designed for someone else. Pages are built for human eyes, which can skim and ignore; tool schemas for programs, which pay nothing to carry definitions they never call. An agent has neither luxury: it re-reads, and pays again for, everything it is shown on every turn. We present String, an open-source runtime that gives this user an interface of its own and treats the job as an operating-systems problem. Tool knowledge moves out of the agent's context and into a common layer that renders it back one view at a time as Markdown. A single SFMD (String-Flavored Markdown) document declares an application's views, typed actions, navigation, and credentials, and the runtime handles discovery, validation, execution, state, and secrets behind two core verbs: /open to see and /act to do. Web and app turn out to be two renderings of one architecture: an SFMD site serves styled HTML to browsers and the raw document to agents, so one grammar reaches apps, files, shells, and the web, even legacy HTML, with no per-site integration. Views stay partial by design, and the staging is causal: disclosing one tier of detail a single turn too early costs up to 23 accuracy points, while proper staging drops wrong-action selection from 28% to 2%. Privilege follows provenance: a remote page may call HTTP but never the shell, and caller-supplied text never expands a stored secret. On an 87-task benchmark that pairs each task with curated skills, operationalizing those procedures as on-demand String apps yields comparable aggregate success across six models from frontier to small (+1.3pp) while using 33.5% fewer tokens among completed episodes, and the resident interface stays a constant 53 tokens at any catalog size. We report the design, the evaluation, and what three months of production use taught us.

---


### 94. [SimpCue: Cue-Based Prompting for Multilingual Text Simplification](https://arxiv.org/abs/2608.28042)

**<font color=#1a73e8>作者：</font>** Mehrzad Tareh, Horacio Saggion, Stefan Bott  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Text simplification aims to make complex texts easier to understand while preserving their original meaning. Recent large language models can perform simplification through prompting, but it remains unclear whether adding explicit linguistic information about sentence complexity to the prompt improves their outputs. We investigate this question for multilingual sentence-level Easy-to-Read simplification in Catalan, Spanish, and Italian. Using Qwen3-8B, we compare a baseline prompt, a gold-cue prompt enriched with gold linguistic cues, and a predicted-cue prompt enriched with automatically predicted cues. We evaluate the outputs using SARI, BLEU, chrF, and BERTScore, and complement this evaluation with a manual qualitative analysis. Predicted-cue prompting obtains the best overall scores across all four metrics, although the gains over the baseline are small. Gold-cue prompting does not consistently improve over the baseline, and results vary across languages. These findings indicate that cue-based prompting can influence multilingual Easy-to-Read simplification, but its benefits are modest, metric-dependent, and language-dependent.

---


### 95. [CNeo-Bench: Diagnosing Large Language Models on Chinese Neologisms](https://arxiv.org/abs/2608.28053)

**<font color=#1a73e8>作者：</font>** Kaiyan Zhao, Zhongtao Miao, Zheyong Xie 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Chinese neologisms exploit diverse and unique linguistic mechanisms, such as phonetic substitution (e.g., 886 for ``bye-bye'') and visual character decomposition that are rare in other languages. We introduce CNeo-Bench, a benchmark of 4,759 such neologisms with reference definitions, organized into five top-level categories and nine subcategories by the linguistic mechanism behind each expression. CNeo-Bench is paired with a two-tier evaluation framework that separates whether a model can describe a neologism from whether it can operate on its underlying mechanism. Evaluating 18 LLMs, we find that Chinese neologisms remain an open challenge; most models fall below 40\% on definition generation, and on several subcategories a systematic recognition-manipulation gap emerges: models describe neologisms correctly but, in source-form restoration tasks, substitute a semantic equivalent (paraphrase) for the source form rather than producing the source form itself. A few-shot analysis on 1,058 hard items shows that in-context examples can solve many difficult cases, but leave a noticeable portion of errors remaining, indicating challenges beyond prompting alone can address.

---


### 96. [Dynamic Alignment Compensation for Hallucination Mitigation in Large Vision-Language Models](https://arxiv.org/abs/2608.28058)

**<font color=#1a73e8>作者：</font>** Kairong Yu, Zixin Zhu, Le Yu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large Vision-Language Models (LVLMs) remain prone to hallucinations, producing responses that are irrelevant or inconsistent with the multimodal input. Existing mitigation methods mainly rely on external supervision, output calibration, or attention regulation, leaving the internal representation dynamics of autoregressive generation underexplored. We identify an inference-time failure mode in which cross-modal representations degrade across decoder layers and drift across generation steps, destabilizing token prediction and increasing hallucination risk. We propose \emph{Dynamic Alignment Compensation} (DAC), a training-free inference-time method that detects representation divergence and selectively applies lightweight residual compensation. DAC combines Layer-wise Semantic Compensation to mitigate inter-layer degradation with Sequential Semantic Correction to constrain temporal drift. Experiments on nine hallucination-focused and general-purpose multimodal benchmarks across multiple LVLM backbones show that DAC consistently reduces hallucinations while maintaining strong overall performance.

---


### 97. [WeAgent-MMSearch: Native Text-Vision Interaction for Multimodal Search Agents](https://arxiv.org/abs/2608.28062)

**<font color=#1a73e8>作者：</font>** Zongkai Liu, Hui Zhang, Liqiang Niu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal search agents extend parametric knowledge with newly emerging and long-tail evidence from the open web. Yet many existing agentic search environments often expose retrieved evidence only as text and omit tool-returned images from subsequent context, reducing visually grounded trajectories to text-only reasoning. Long-horizon interaction also compounds tool-call, response-length, timeout, and budget failures, which can discard salvageable trajectories, waste rollout computation, and disturb policy updates. To address these issues, we introduce WeAgent-Harness, a multimodal agentic harness that supports native text-vision interaction and runtime recovery. Retrieved images receive persistent disk references, allowing the model to inspect, process, and cite them throughout the trajectory. Based on this harness, we develop WeAgent-MMSearch, an integrated system spanning data construction, agentic post-training, and multimodal rollout. For data construction, a strong MLLM uses WeAgent-Harness to discover, synthesize, and verify MMSearch-style tasks and collect expert trajectories. During post-training, our Failure-Aware GSPO (FA-GSPO) recovers salvageable abnormal rollouts and filters invalid ones to improve bounded multimodal planning and this http URL also introduce VisTarget-Bench, a 150-task human-verified benchmark that pairs each question with a held-out target image, distinguishing image-retrieval failures from visual-perception failures. Evaluation on VisTarget-Bench and seven public benchmarks shows that agentic post-training improves the average score by 19.22 points, enabling our model to outperform similarly sized open-source models and rival models with roughly ten times its parameter count.

---


### 98. [SEPO: Evidence-Grounded Prompt Optimization via Structural Editing](https://arxiv.org/abs/2608.28067)

**<font color=#1a73e8>作者：</font>** Xiaoyu Ma, Haoyue Liu, Yiwen Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Existing API-only prompt optimisers are often described as interpretable, but in practice, this usually means only post-hoc inspectability: each iteration still rewrites the prompt as one opaque string, leaving a trace of full-prompt diffs rather than localisable, machine-readable edits. This paper introduces SEPO (Structural, Evidence-grounded Prompt Optimization), a multi-trajectory prompt optimiser centred on edit-effect lineage feedback. Rather than treating each iteration as an isolated whole-prompt rewrite, SEPO locally edits stable, typed units in a two-layer prompt schema, links the target and realised structural operations of each edit to the examples it newly fixes or breaks, and carries this edit-effect record forward to guide later architect calls on the same search branch. This makes prompt optimisation addressable, attributable, and actionable. Across a 14-task held-out suite, SEPO improves over the strongest baseline, GEPA, by 3.1 pp on Llama-3.1-8B-Instruct and 2.2 pp on Qwen3-8B, reaching 61.9% and 73.3% macro accuracy. SEPO also lies on both the optimisation-time and test-time Pareto frontiers, spending 2.9M optimisation tokens versus 4.1M for GEPA and producing prompts over 5x shorter.

---


### 99. [Speculative Probing: LLM Monitoring at Speculative-Decoding Cost](https://arxiv.org/abs/2608.28099)

**<font color=#1a73e8>作者：</font>** Collin Zhang, Tingwei Zhang, Vitaly Shmatikov  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Real-time classification during language model inference is valuable for safety filtering, behavioral analysis, and model monitoring, but current approaches force a trade-off between accuracy and efficiency. Hidden-state probes are fast but limited: they are either not context-aware: operating on a single vector and cannot model interactions across positions; or they are very costly: having dedicated classifier models (Llama Guard, Qwen Guard, LLM-as-judge) or performing computation on hidden states for all tokens and then pooling the results (MultiMax). This shows an intrinsic trade-off between efficiency and accuracy.
However, we find that the speculative-decoding module in recent LLMs can be repurposed for efficient high-quality classification. By appending a trained soft prompt at the end of the target sequence, we can repurpose the speculative-decoding module into a sequence classifier. At inference time in a speculative-decoding pipeline, the KV cache is already in GPU memory, so classification adds negligible overhead. We evaluate on four classification tasks across four models (Qwen3.5-4B, 9B, 27B, MiniCPM4.1-8B). Our small probes consistently outperform zero-shot GPT-5.4-mini and, on multilingual prompt safety, match or beat specialized 8B safety classifiers (Qwen3Guard-Gen-8B, Llama-Guard-3-8B) without running a full LLM.

---


### 100. [H-Scale: Hessian-Guided Scale Refinement for NVFP4 Sub-Byte LLM Inference](https://arxiv.org/abs/2608.28113)

**<font color=#1a73e8>作者：</font>** Hao Yu, Zheng Li, Dayiheng Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The NVIDIA Blackwell architecture, with native support for the ultra-fine-grained NVFP4 format, opens new opportunities for accelerating large language model (LLM) inference. NVFP4's micro-block design, such as a group size of 16, offers strong representational flexibility for capturing local weight distributions and isolating outliers, but it also introduces a large and highly sensitive space of per-group scaling factors. Existing post-training quantization (PTQ) methods primarily focus on refining quantized weight values, leaving this scale-selection step underexplored. To address this gap, we propose \textbf{H-Scale}, a lightweight post-processing method for NVFP4 per-group scale refinement. Instead of minimizing plain weight reconstruction error, H-Scale selects hardware-valid group scales using a diagonal second-order proxy derived from calibration activations, thereby targeting layer output perturbation more directly. It is designed as a drop-in replacement for RTN-style scale selection in diverse NVFP4 pipelines, requires only modest offline calibration, and introduces strictly zero overhead at inference time. Under a fixed evaluation protocol, experiments on mainstream LLMs show that H-Scale generally improves a broad range of NVFP4 baselines and brings several variants closer to the BF16 reference.

---


> [!TIP]
> 当前位于：**51-100**（第 2/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-176](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
