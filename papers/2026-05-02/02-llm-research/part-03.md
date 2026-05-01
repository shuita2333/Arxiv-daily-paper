# 🧠 大模型相关研究 | 2026年05月02日

> 本类共 **123** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**101-123**（第 3/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-123**

---

### 101. [LLMs as ASP Programmers: Self-Correction Enables Task-Agnostic Nonmonotonic Reasoning](https://arxiv.org/abs/2604.27960)

**<font color=#1a73e8>作者：</font>** Adam Ishay, Joohyung Lee  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent large language models (LLMs) have achieved impressive reasoning milestones but continue to struggle with high computational costs, logical inconsistencies, and sharp performance degradation on high-complexity problems. While neuro-symbolic methods attempt to mitigate these issues by coupling LLMs with symbolic reasoners, existing approaches typically rely on monotonic logics (e.g., SMT) that cannot represent defeasible reasoning -- essential components of human cognition. We present "LLM+ASP," a framework that translates natural language into Answer Set Programming (ASP), a nonmonotonic formalism based on stable model semantics. Unlike prior "LLM+ASP" approaches that require manually authored knowledge modules, domain-specific prompts, or evaluation restricted to single problem classes, our framework operates without any per-task engineering and applies uniformly across diverse reasoning tasks. Our system utilizes an automated self-correction loop where structured feedback from the ASP solver enables iterative refinement. Evaluating across six diverse benchmarks, we demonstrate that: (1) stable model semantics allow LLMs to naturally express default rules and exceptions, outperforming SMT-based alternatives by significant margins on nonmonotonic tasks; (2) iterative self-correction is the primary driver of performance, effectively replacing the need for handcrafted domain knowledge; (3) compact in-context reference guides substantially outperform verbose documentation, revealing a "context rot" phenomenon where excessive context hinders constraint adherence.

---


### 102. [Language Models Refine Mechanical Linkage Designs Through Symbolic Reflection and Modular Optimisation](https://arxiv.org/abs/2604.27962)

**<font color=#1a73e8>作者：</font>** João Pedro Gandarela, Thiago Rios, Stefan Menzel 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Designing mechanical linkages involves combinatorial topology selection and continuous parameter fitting. We show that language models can systematically improve linkage designs through symbolic representations. Language model agents explore discrete topologies while numerical optimisers fit continuous parameters. A symbolic lifting operator translates simulator trajectories into qualitative descriptors, motion labels, temporal predicates, and structural diagnostics that models interpret across iterative design cycles. Across six engineering-relevant motion targets and three open-source models (Llama 3.3 70B, Qwen3 4B, Qwen3 MoE 30B-A3B), the modular architecture reduces geometric error by up to 68% and improves structural validity by up to 134% over monolithic baselines. Critically, 78.6% of iterative refinement trajectories show measurable improvement, with the system correctly diagnosing overconstraint (56.3%) and underconstraint (35.6%) failure modes and proposing grounded corrections. Models across all three families acquire interpretable mechanical reasoning strategies without fine-tuning, demonstrating that principled symbolic abstraction bridges generative AI and the numerical precision required for engineering design.

---


### 103. [From LLM-Driven Trading Card Generation to Procedural Relatedness: A Pokémon Case Study](https://arxiv.org/abs/2604.27972)

**<font color=#1a73e8>作者：</font>** Johannes Pfau, Panagiotis Vrettis  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Since the dawn of Trading Card Games, the genre has grown into a multi-billion-dollar industry engaging millions of analog and digital players worldwide. Popular TCGs rely on regular updates, balance adjustments, and rotating constraints to sustain engagement. Yet, as metagames stabilize, predictable strategies dominate and viable card options diminish, often resulting in repetitive and impaired player experiences.
This paper investigates the use of Large Language Models and Image Diffusion Models for Procedural Content Generation of TCG cards, addressing these challenges by enabling a personalized infinity of card designs. Modern generative AI not only enables large-scale content creation but could even introduce procedural relatedness, fostering unique connections between players and their cards. We present a pipeline combining player-centric co-creation, fine-tuned embeddings, local LLMs, and Diffusion Models to generate dynamic, personalized cards while potentially expanding creative range.
We evaluated the pipeline in a user study with 49 participants who generated 196 Pokémon card samples. Participants rated aesthetics and representativeness of visuals and mechanics, and provided qualitative feedback. Results show high satisfaction and indicate that most participants successfully realized their own ideas through prompt adjustments. These findings lay groundwork for future content generation systems and alternatives to conventional metagame evolution through procedural relatedness.

---


### 104. [FineState-Bench: Benchmarking State-Conditioned Grounding for Fine-grained GUI State Setting](https://arxiv.org/abs/2604.27974)

**<font color=#1a73e8>作者：</font>** Fengxian Ji, Jingpu Yang, Zirui Song 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite the rapid progress of large vision-language models (LVLMs), fine-grained, state-conditioned GUI interaction remains challenging. Current evaluations offer limited coverage, imprecise target-state definitions, and an overreliance on final-task success, obscuring where and why agents fail. To address this gap, we introduce \textbf{FineState-Bench}, a benchmark that evaluates whether an agent can correctly ground an instruction to the intended UI control and reach the exact target state. FineState-Bench comprises 2,209 instances across desktop, web, and mobile platforms, spanning four interaction families and 23 UI component types, with each instance explicitly specifying an exact target state for fine-grained state setting. We further propose \textit{FineState-Metrics}, a four-stage diagnostic pipeline with stage-wise success rates: Localization Success Rate (SR@Loc), Interaction Success Rate (SR@Int), Exact State Success Rate at Locate (ES-SR@Loc), and Exact State Success Rate at Interact (ES-SR@Int), and a plug-and-play \textit{Visual Diagnostic Assistant} (VDA) that generates a Description and a bounding-box Localization Hint to diagnose visual grounding reason via controlled w/ vs.\ w/o comparisons. On FineState-Bench, exact goal-state success remains low: ES-SR@Int peaks at 32.8\% on Web and 22.8\% on average across platforms. With VDA localization hints, Gemini-2.5-Flash gains +14.9 ES-SR@Int points, suggesting substantial headroom from improved visual grounding, yet overall accuracy is still insufficient for reliable fine-grained state-conditioned interaction \href{this https URL}{Github.}

---


### 105. [Dynamic Scaled Gradient Descent for Stable Fine-Tuning for Classifications](https://arxiv.org/abs/2604.27987)

**<font color=#1a73e8>作者：</font>** Nghia Bui, Lijing Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fine-tuning pretrained models has become a standard approach to adapting pretrained knowledge to improve the accuracy on new sparse, imbalance datasets. However, issues arise when optimization falls into a collapsed state, where the model gets stuck, leading to degraded performance and unstable training. One possible reason for this is the cancellation of gradients across training examples. To address this problem, we propose a novel algorithm, dynamic scaled gradient descent (\mName), that directly modifies the gradients returned by training examples, specifically, scaling down the gradients of correctly classified examples using a dynamic scaler. This strategy offers both theoretical and empirical advantages in improving training stability. Experiments on a variety of benchmark datasets, spanning multiple tasks and large pretrained models, demonstrate that our method consistently reduces performance variance and surpasses the accuracy of existing approaches.

---


### 106. [Exploring Interaction Paradigms for LLM Agents in Scientific Visualization](https://arxiv.org/abs/2604.27996)

**<font color=#1a73e8>作者：</font>** Jackson Vonderhorst, Kuangshi Ai, Haichao Miao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper examines how different types of large language model (LLM) agents perform on scientific visualization (SciVis) tasks, where users generate visualization workflows from natural-language instructions. We compare three primary interaction paradigms, including domain-specific agents with structured tool use, computer-use agents, and general-purpose coding agents, by evaluating eight representative agents across 15 benchmark tasks and measuring visualization quality, efficiency, robustness, and computational cost. We further analyze interaction modalities, including code scripts and model context protocol (MCP) or API calls for structured tool use, as well as command-line interfaces (CLI) and graphical user interfaces (GUI) for more general interaction, while additionally studying the effect of persistent memory in selected agents. The results reveal clear tradeoffs across paradigms and modalities. General-purpose coding agents achieve the highest task success rates but are computationally expensive, while domain-specific agents are more efficient and stable but less flexible. Computer-use agents perform well on individual steps but struggle with longer multi-step workflows, indicating that long-horizon planning is their primary limitation. Across both CLI- and GUI-based settings, persistent memory improves performance over repeated trials, although its benefits depend on the underlying interaction mode and the quality of feedback. These findings suggest that no single approach is sufficient, and future SciVis systems should combine structured tool use, interactive capabilities, and adaptive memory mechanisms to balance performance, robustness, and flexibility.

---


### 107. [Kernelized Advantage Estimation: From Nonparametric Statistics to LLM Reasoning](https://arxiv.org/abs/2604.28005)

**<font color=#1a73e8>作者：</font>** Shijin Gong, Kai Ye, Jin Zhu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent advances in large language models (LLMs) have increasingly relied on reinforcement learning (RL) to improve their reasoning capabilities. Three approaches have been widely adopted: (i) Proximal policy optimization and advantage actor-critic rely on a deep neural network to estimate the value function of the learning policy in order to reduce the variance of the policy gradient. However, estimating and maintaining such a value network incurs substantial computational and memory overhead. (ii) Group relative policy optimization (GRPO) avoids training a value network by approximating the value function using sample averages. However, GRPO samples a large number of reasoning traces per prompt to achieve accurate value function approximation, making it computationally expensive. (iii) REINFORCE-type algorithms sample only a single reasoning trajectory per prompt, which reduces computational cost but suffers from poor sample efficiency.
In this work, we focus on a practical, resource-constrained setting in which only a small number of reasoning traces can be sampled per prompt, while low-variance gradient estimation remains essential for high-quality policy learning. To address this challenge, we bring classical nonparametric statistical methods, which are both computationally and statistically efficient, to LLM reasoning. We employ kernel smoothing as a concrete example for value function estimation and the subsequent policy optimization. Numerical and theoretical results demonstrate that our proposal achieves accurate value and gradient estimation, leading to improved policy optimization.

---


### 108. [Echo-α: Large Agentic Multimodal Reasoning Model for Ultrasound Interpretation](https://arxiv.org/abs/2604.28011)

**<font color=#1a73e8>作者：</font>** Jing Zhang, Wentao Jiang, Tao Huang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Ultrasound interpretation requires both precise lesion localization and holistic clinical reasoning, yet existing methods typically excel at only one of these capabilities: specialized detectors offer strong localization but limited reasoning, whereas multimodal large language models (MLLMs) provide flexible reasoning but weak grounding in specialized medical domains. We present Echo-{\alpha}, an agentic multimodal reasoning model for ultrasound interpretation that unifies these strengths within an invoke-and-reason framework. Echo-{\alpha} is trained to coordinate organ-specific detector outputs, integrate them with global visual context, and convert the resulting evidence into grounded diagnostic decisions beyond detector-only inference. This behavior is established through a nine-task supervised curriculum and then refined by sequential reinforcement learning under different reward trade-offs, yielding Echo-{\alpha}-Grounding for lesion anchoring and Echo-{\alpha}-Diagnosis for final diagnosis. On multi-center renal and breast ultrasound benchmarks, Echo-{\alpha} outperforms competitive baselines on both grounding and diagnosis. In particular, on cross-center test sets, Echo-{\alpha}-Grounding attains 56.73%/43.78% F1@0.5 and Echo- {\alpha}-Diagnosis reaches 74.90%/49.20% overall accuracy on renal/breast ultrasound. These results suggest that agentic multimodal reasoning can turn specialized detectors into verifiable clinical evidence, offering a practical route toward ultrasound AI systems that are more accurate, interpretable, and transferable. The repository is at this https URL.

---


### 109. [Reliable Answers for Recurring Questions: Boosting Text-to-SQL Accuracy with Template Constrained Decoding](https://arxiv.org/abs/2604.28028)

**<font color=#1a73e8>作者：</font>** Smit Jivani, Sarvam Maheshwari, Sunita Sarawagi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have revolutionized Text-to-SQL generation, allowing users to query structured data using natural language with growing ease. Yet, real-world deployment remains challenging, especially in complex or unseen schemas, due to inconsistent accuracy and the risk of generating invalid SQL. We introduce Template Constrained Decoding (TeCoD), a system that addresses these limitations by harnessing the recurrence of query patterns in labeled workloads. TeCoD converts historical NL-SQL pairs into reusable templates and introduces a robust template selection module that uses a fine-tuned natural language inference model to match or reject queries efficiently. Once the template is selected, TeCoD enforces it during SQL generation through grammar-constrained decoding, implemented via a novel partitioned strategy that ensures both syntactic validity and efficiency. Together, these components yield up to 36% higher execution accuracy than in-context learning (ICL) and 2.2x lower latency on matched queries.

---


### 110. [Models Recall What They Violate: Constraint Adherence in Multi-Turn LLM Ideation](https://arxiv.org/abs/2604.28031)

**<font color=#1a73e8>作者：</font>** Garvin Kruthof  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> When researchers iteratively refine ideas with large language models, do the models preserve fidelity to the original objective? We introduce DriftBench, a benchmark for evaluating constraint adherence in multi-turn LLM-assisted scientific ideation. Across 2,146 scored benchmark runs spanning seven models from five providers (including two open-weight), four interaction conditions, and 38 research briefs from 24 scientific domains, we find that iterative pressure reliably increases structural complexity and often reduces adherence to original constraints. A restatement probe reveals a dissociation between declarative recall and behavioral adherence, as models accurately restate constraints they simultaneously violate. The knows-but-violates (KBV) rate, measuring constraint non-compliance despite preserved recall, ranges from 8% to 99% across models. Structured checkpointing partially reduces KBV rates but does not close the dissociation, and complexity inflation persists. Human validation against blind raters confirms that the LLM judge under-detects constraint violations, making reported constraint adherence scores conservative. Sensitivity analyses confirm the findings are robust to temperature (0.7 vs.\ 1.0) and pressure type (novelty vs.\ rigor). We release all briefs, prompts, rubrics, transcripts, and scores as an open benchmark.

---


### 111. [SpecVQA: A Benchmark for Spectral Understanding and Visual Question Answering in Scientific Images](https://arxiv.org/abs/2604.28039)

**<font color=#1a73e8>作者：</font>** Jialu Shen, Han Lyu, Suyang Zhong 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Spectra are a prevalent yet highly information-dense form of scientific imagery, presenting substantial challenges to multimodal large language models (MLLMs) due to their unstructured and domain-specific characteristics. Here we introduce SpecVQA, a professional scientific-image benchmark for evaluating multimodal models on scientific spectral understanding, covering 7 representative spectrum types with expert-annotated question-answer pairs. The aim comprises two aspects: spectra scientific QA evaluation and corresponding underlying task evaluation. SpecVQA contains 620 figures and 3100 QA pairs curated from peer-reviewed literature, targeting both direct information extraction and domain-specific reasoning. To effectively reduce token length while preserving essential curve characteristics, we propose a spectral data sampling and interpolation reconstruction approach. Ablation studies further confirm that the approach achieves substantial performance improvements on the proposed benchmark. We test the capability of prominent MLLMs in scientific spectral understanding on our benchmark and present a leaderboard. This work represents an essential step toward enhancing spectral understanding in multimodal large models and suggests promising directions for extending visual-language models to broader scientific research and data analysis.

---


### 112. [Stable Behavior, Limited Variation: Persona Validity in LLM Agents for Urban Sentiment Perception](https://arxiv.org/abs/2604.28048)

**<font color=#1a73e8>作者：</font>** Neemias B da Silva, Rodrigo Minetto, Daniel Silver 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are increasingly used as proxies for human perception in urban analysis, yet it remains unclear whether persona prompting produces meaningful and reproducible behavioral diversity. We investigate whether distinct personas influence urban sentiment judgments generated by multimodal LLMs. Using a factorial set of personas spanning gender, economic status, political orientation, and personality, we instantiate multiple agents per persona to evaluate urban scene images from the PerceptSent dataset and assess both within-persona consistency and cross-persona variation. Results show strong convergence among agents sharing a persona, indicating stable and reproducible behavior. However, cross-persona differentiation is limited: economic status and personality induce statistically detectable but practically modest variation, while gender shows no measurable effect and political orientation only negligible impact. Agents also exhibit an extremity bias, collapsing intermediate sentiment categories common in human annotations. As a result, performance remains strong on coarse-grained polarity tasks but degrades as sentiment resolution increases, suggesting that simple label-based persona prompting does not capture fine-grained perceptual judgments. To isolate the contribution of persona conditioning, we additionally evaluate the same model without personas. Surprisingly, the no-persona model sometimes matches or exceeds persona-conditioned agreement with human labels across all task variants, suggesting that simple label-based persona prompting may add limited annotation value in this setting.

---


### 113. [RHyVE: Competence-Aware Verification and Phase-Aware Deployment for LLM-Generated Reward Hypotheses](https://arxiv.org/abs/2604.28056)

**<font color=#1a73e8>作者：</font>** Feiyu Wu, Xu Zheng, Zhuocheng Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) make reward design in reinforcement learning substantially more scalable, but generated rewards are not automatically reliable training objectives. Existing work has focused primarily on generating, evolving, or selecting reward candidates, while paying less attention to when such candidates can be verified and deployed during policy optimization. We study this deployment-time problem by treating generated rewards as reward hypotheses whose utility depends on the competence of the current policy and the phase of training. We propose \textsc{RHyVE}, a competence-aware verification and phase-aware deployment protocol that compares small sets of reward hypotheses from shared policy checkpoints using short-horizon fork verification. Our experiments show that reward rankings are unreliable at low competence but become informative after task-dependent thresholds. On a sparse manipulation task, phase-aware deployment improves peak and retained performance under a locked protocol. Updated LLM-generated reward-candidate experiments show candidate-family-dependent behavior: generated pools can exhibit phase-dependent winner changes, but no fixed warm-up schedule is universally optimal. Held-out schedule selection, conservative selector baselines, compute-matched controls, and scale controls further show that \textsc{RHyVE} is best understood as a verification-informed deployment protocol rather than a universal scheduler. Dense and all-failure boundary experiments delimit the scope of the method. Together, these results suggest that reward generation and reward deployment should be studied as coupled problems: generated rewards must be verified and deployed under changing policy competence.

---


### 114. [Repetition over Diversity: High-Signal Data Filtering for Sample-Efficient German Language Modeling](https://arxiv.org/abs/2604.28075)

**<font color=#1a73e8>作者：</font>** Ansar Aynetdinov, Patrick Haller, Alan Akbik  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent research has shown that filtering massive English web corpora into high-quality subsets significantly improves training efficiency. However, for high-resource non-English languages like German, French, or Japanese, aggressive filtering creates a strategic dilemma: should practitioners prioritize diversity by training once on large amounts of lightly filtered web data, or prioritize quality by strictly filtering for a high-quality core and repeating it over multiple epochs? We investigate this trade-off for German by constructing hierarchical quality filters applied to 500M web documents, comparing multi-epoch training on the filtered subsets against single-pass training on a diverse corpus. Our experiments across multiple model scales and token budgets show that repeating high-quality data consistently outperforms single-pass training on larger, less filtered sets. Notably, the performance gap persists even after 7 epochs. Our findings suggest that for non-English LLMs, semantic concentration through quality filtering offers a more viable path to efficient language modeling than simply maximizing unique data volume. We release our German language models (called Boldt), as well as our cleaned evaluation benchmarks to the research community. Our experiments indicate that they achieve state-of-the-art results despite training on 10-360x fewer tokens than comparable models.

---


### 115. [TopBench: A Benchmark for Implicit Prediction and Reasoning over Tabular Question Answering](https://arxiv.org/abs/2604.28076)

**<font color=#1a73e8>作者：</font>** An-Yang Ji, Jun-Peng Jiang, De-Chuan Zhan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have advanced Table Question Answering, where most queries can be answered by extracting information or simple aggregation. However, a common class of real-world queries is implicitly predictive, requiring the inference of unobserved answers from historical patterns rather than mere retrieval. These queries introduce two challenges: recognizing latent intent and reliable predictive reasoning over massive tables. To assess LLMs in such Tabular questiOn answering with implicit Prediction tasks, we introduce TopBench, a benchmark consisting of 779 samples across four sub-tasks, ranging from single-point prediction to decision making, treatment effect analysis, and complex filtering, requiring models to generate outputs spanning reasoning text and structured tables. We evaluate diverse models under both text-based and agentic workflows. Experiments reveal that current models often struggle with intent recognition, defaulting to just lookups. Deeper analysis identifies that accurate intent disambiguation serves as the prerequisite for leading these predictive behaviors. Furthermore, elevating the upper bound of prediction precision requires the integration of more sophisticated modeling or reasoning capabilities.

---


### 116. [Characterizing the Consistency of the Emergent Misalignment Persona](https://arxiv.org/abs/2604.28082)

**<font color=#1a73e8>作者：</font>** Anietta Weckauff, Yuchen Zhang, Maksym Andriushchenko  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Fine-tuning large language models (LLMs) on narrowly misaligned data generalizes to broadly misaligned behavior, a phenomenon termed emergent misalignment (EM). While prior work has found a correlation between harmful behavior and self-assessment in emergently misaligned models, it remains unclear how consistent this correspondence is across tasks and whether it varies across fine-tuning domains. We characterize the consistency of the EM persona by fine-tuning Qwen 2.5 32B Instruct on six narrowly misaligned domains (e.g., insecure code, risky financial advice, bad medical advice) and administering experiments including harmfulness evaluation, self-assessment, choosing between two descriptions of AI systems, output recognition, and score prediction. Our results reveal two distinct patterns: coherent-persona models, in which harmful behavior and self-reported misalignment are coupled, and inverted-persona models, which produce harmful outputs while identifying as aligned AI systems. These findings reveal a more fine-grained picture of the effects of emergent misalignment, calling into question the consistency of the EM persona.

---


### 117. [PRISM: Pre-alignment via Black-box On-policy Distillation for Multimodal Reinforcement Learning](https://arxiv.org/abs/2604.28123)

**<font color=#1a73e8>作者：</font>** Sudong Wang, Weiquan Huang, Xiaomin Yu 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The standard post-training recipe for large multimodal models (LMMs) applies supervised fine-tuning (SFT) on curated demonstrations followed by reinforcement learning with verifiable rewards (RLVR). However, SFT introduces distributional drift that neither preserves the model's original capabilities nor faithfully matches the supervision distribution. This problem is further amplified in multimodal reasoning, where perception errors and reasoning failures follow distinct drift patterns that compound during subsequent RL. We introduce PRISM, a three-stage pipeline that mitigates this drift by inserting an explicit distribution-alignment stage between SFT and RLVR. Building on the principle of on-policy distillation (OPD), PRISM casts alignment as a black-box, response-level adversarial game between the policy and a Mixture-of-Experts (MoE) discriminator with dedicated perception and reasoning experts, providing disentangled corrective signals that steer the policy toward the supervision distribution without requiring access to teacher logits. While 1.26M public demonstrations suffice for broad SFT initialization, distribution alignment demands higher-fidelity supervision; we therefore curate 113K additional demonstrations from Gemini 3 Flash, featuring dense visual grounding and step-by-step reasoning on the hardest unsolved problems. Experiments on Qwen3-VL show that PRISM consistently improves downstream RLVR performance across multiple RL algorithms (GRPO, DAPO, GSPO) and diverse multimodal benchmarks, improving average accuracy by +4.4 and +6.0 points over the SFT-to-RLVR baseline on 4B and 8B, respectively. Our code, data, and model checkpoints are publicly available at this https URL.

---


### 118. [Explainable Load Forecasting with Covariate-Informed Time Series Foundation Models](https://arxiv.org/abs/2604.28149)

**<font color=#1a73e8>作者：</font>** Matthias Hertel, Alexandra Nikoltchovska, Sebastian Pütz 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time Series Foundation Models (TSFMs) have recently emerged as general-purpose forecasting models and show considerable potential for applications in energy systems. However, applications in critical infrastructure like power grids require transparency to ensure trust and reliability and cannot rely on pure black-box models. To enhance the transparency of TSFMs, we propose an efficient algorithm for computing Shapley Additive Explanations (SHAP) tailored to these models. The proposed approach leverages the flexibility of TSFMs with respect to input context length and provided covariates. This property enables efficient temporal and covariate masking (selectively withholding inputs), allowing for a scalable explanation of model predictions using SHAP. We evaluate two TSFMs - Chronos-2 and TabPFN-TS - on a day-ahead load forecasting task for a transmission system operator (TSO). In a zero-shot setting, both models achieve predictive performance competitive with a Transformer model trained specifically on multiple years of TSO data. The explanations obtained through our proposed approach align with established domain knowledge, particularly as the TSFMs appropriately use weather and calendar information for load prediction. Overall, we demonstrate that TSFMs can serve as transparent and reliable tools for operational energy forecasting.

---


### 119. [AEGIS: A Holistic Benchmark for Evaluating Forensic Analysis of AI-Generated Academic Images](https://arxiv.org/abs/2604.28177)

**<font color=#1a73e8>作者：</font>** Bo Zhang, Tzu-Yen Ma, Zichen Tang 等 21 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce AEGIS, A holistic benchmark for Evaluating forensic analysis of AI-Generated academic ImageS. Compared to existing benchmarks, AEGIS features three key advances: (1) Domain-Specific Complexity: covering seven academic categories with 39 fine-grained subtypes, exposing intrinsic forensic difficulty, where even GPT-5.1 reaches 48.80% overall performance and expert models achieve only limited localization accuracy (IoU 30.09%); (2) Diverse Forgery Simulations: modeling four prevalent academic forgery strategies across 25 generative models, with 11 yielding average forensic accuracy below 50%, showing that forensics lag behind generative advances; and (3) Multi-Dimensional Forensic Evaluation: jointly assessing detection, reasoning, and localization, revealing complementary strengths between model families, with multimodal large language models (MLLMs) at 84.74% accuracy in textual artifact recognition and expert detectors peaking at 79.54% accuracy in binary authenticity detection. By evaluating 25 leading MLLMs, nine expert models, and one unified multimodal understanding and generation model, AEGIS serves as a diagnostic testbed exposing fundamental limitations in academic image forensics.

---


### 120. [LLM as Clinical Graph Structure Refiner: Enhancing Representation Learning in EEG Seizure Diagnosis](https://arxiv.org/abs/2604.28178)

**<font color=#1a73e8>作者：</font>** Lincan Li, Zheng Chen, Yushun Dong  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Electroencephalogram (EEG) signals are vital for automated seizure detection, but their inherent noise makes robust representation learning challenging. Existing graph construction methods, whether correlation-based or learning-based, often generate redundant or irrelevant edges due to the noisy nature of EEG data. This significantly impairs the quality of graph representation and limits downstream task performance. Motivated by the remarkable reasoning and contextual understanding capabilities of large language models (LLMs), we explore the idea of using LLMs as graph edge refiners. Specifically, we propose a two-stage framework: we first verify that LLM-based edge refinement can effectively identify and remove redundant connections, leading to significant improvements in seizure detection accuracy and more meaningful graph structures. Building on this insight, we further develop a robust solution where the initial graph is constructed using a Transformer-based edge predictor and multilayer perceptron, assigning probability scores to potential edges and applying a threshold to determine their existence. The LLM then acts as an edge set refiner, making informed decisions based on both textual and statistical features of node pairs to validate the remaining connections. Extensive experiments on TUSZ dataset demonstrate that our LLM-refined graph learning framework not only enhances task performance but also yields cleaner and more interpretable graph representations.

---


### 121. [Exploration Hacking: Can LLMs Learn to Resist RL Training?](https://arxiv.org/abs/2604.28182)

**<font color=#1a73e8>作者：</font>** Eyon Jang, Damon Falck, Joschka Braun 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) has become essential to the post-training of large language models (LLMs) for reasoning, agentic capabilities and alignment. Successful RL relies on sufficient exploration of diverse actions by the model during training, which creates a potential failure mode: a model could strategically alter its exploration during training to influence the subsequent training outcome. In this paper we study this behavior, called exploration hacking. First, we create model organisms of selective RL resistance by fine-tuning LLMs to follow specific underperformance strategies; these models can successfully resist our RL-based capability elicitation in agentic biosecurity and AI R&D environments while maintaining performance on related tasks. We then use our model organisms to evaluate detection and mitigation strategies, including monitoring, weight noising, and SFT-based elicitation. Finally, we show that current frontier models can exhibit explicit reasoning about suppressing their exploration when provided with sufficient information about their training context, with higher rates when this information is acquired indirectly through the environment. Together, our results suggest exploration hacking is a possible failure mode of RL on sufficiently capable LLMs.

---


### 122. [Visual Generation in the New Era: An Evolution from Atomic Mapping to Agentic World Modeling](https://arxiv.org/abs/2604.28185)

**<font color=#1a73e8>作者：</font>** Keming Wu, Zuhao Yang, Kaichen Zhang 等 27 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent visual generation models have made major progress in photorealism, typography, instruction following, and interactive editing, yet they still struggle with spatial reasoning, persistent state, long-horizon consistency, and causal understanding. We argue that the field should move beyond appearance synthesis toward intelligent visual generation: plausible visuals grounded in structure, dynamics, domain knowledge, and causal relations. To frame this shift, we introduce a five-level taxonomy: Atomic Generation, Conditional Generation, In-Context Generation, Agentic Generation, and World-Modeling Generation, progressing from passive renderers to interactive, agentic, world-aware generators. We analyze key technical drivers, including flow matching, unified understanding-and-generation models, improved visual representations, post-training, reward modeling, data curation, synthetic data distillation, and sampling acceleration. We further show that current evaluations often overestimate progress by emphasizing perceptual quality while missing structural, temporal, and causal failures. By combining benchmark review, in-the-wild stress tests, and expert-constrained case studies, this roadmap offers a capability-centered lens for understanding, evaluating, and advancing the next generation of intelligent visual generation systems.

---


### 123. [HERMES++: Toward a Unified Driving World Model for 3D Scene Understanding and Generation](https://arxiv.org/abs/2604.28196)

**<font color=#1a73e8>作者：</font>** Xin Zhou, Dingkang Liang, Xiwu Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Driving world models serve as a pivotal technology for autonomous driving by simulating environmental dynamics. However, existing approaches predominantly focus on future scene generation, often overlooking comprehensive 3D scene understanding. Conversely, while Large Language Models (LLMs) demonstrate impressive reasoning capabilities, they lack the capacity to predict future geometric evolution, creating a significant disparity between semantic interpretation and physical simulation. To bridge this gap, we propose HERMES++, a unified driving world model that integrates 3D scene understanding and future geometry prediction within a single framework. Our approach addresses the distinct requirements of these tasks through synergistic designs. First, a BEV representation consolidates multi-view spatial information into a structure compatible with LLMs. Second, we introduce LLM-enhanced world queries to facilitate knowledge transfer from the understanding branch. Third, a Current-to-Future Link is designed to bridge the temporal gap, conditioning geometric evolution on semantic context. Finally, to enforce structural integrity, we employ a Joint Geometric Optimization strategy that integrates explicit geometric constraints with implicit latent regularization to align internal representations with geometry-aware priors. Extensive evaluations on multiple benchmarks validate the effectiveness of our method. HERMES++ achieves strong performance, outperforming specialist approaches in both future point cloud prediction and 3D scene understanding tasks. The model and code will be publicly released at this https URL.

---


> [!TIP]
> 当前位于：**101-123**（第 3/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-123**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
