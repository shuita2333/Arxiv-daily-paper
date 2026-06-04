# 🧠 大模型相关研究 | 2026年06月05日

> 本类共 **137** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**101-137**（第 3/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-137**

---

### 101. [Optimizing the Cost-Quality Tradeoff of Agentic Theorem Provers in Lean](https://arxiv.org/abs/2606.04883)

**<font color=#1a73e8>作者：</font>** Kári Rögnvaldsson, Chenhao Sun, Jasper Dekoninck 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used in workflows for generating formal proofs in Lean. These workflows often decompose problems into smaller lemmas, sample many proof attempts, and use compiler feedback to guide search. However, they can be prohibitively expensive, often spending substantial compute on attempts that ultimately fail. In this work, we address this problem with an action routing agent that consists of a data plane and a control plane. The data plane generates natural-language lemma decompositions, formalizes them in Lean, and samples proof attempts for the resulting theorem and lemma targets. The control plane observes previous failed Lean attempts, estimates both the likelihood of success and cost of another attempt, and decides whether to continue proving the current target or restart from a new breakdown. On a subset of PutnamBench, our agent decreases the cost by $25.8\%$ over a fixed-step baseline on average, preserving performance while using substantially less compute. These results suggest that failed Lean trajectories provide actionable signals for cost-aware resource allocation in agentic theorem proving.

---


### 102. [HD-DinoMoE: A Class-Aware Hierarchical Dual Mixture-of-Experts Network for Scleral Anomaly Segmentation in Complex Acquisition Scenarios](https://arxiv.org/abs/2606.04888)

**<font color=#1a73e8>作者：</font>** Yinxiang Yu, Maoxiang Chu, Qi Niu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Traditional Chinese Medicine (TCM) ocular inspection provides empirical cues for assessing scleral surface anomalies, but its clinical use remains subjective and difficult to quantify. To support intelligent and quantifiable ocular inspection, this study presents the TCM-inspired Artificial Intelligence Ocular Auxiliary Diagnosis System (TAO) and focuses on pixel-level scleral surface anomaly segmentation. For clinical and user-acquired images affected by multi-source distributional discrepancies, diverse anomaly morphologies, and scleral specular reflection (SSR), we propose HD-DinoMoE, a class-aware hierarchical dual mixture-of-experts network. HD-DinoMoE combines class-aware dual-stream DINOv3 feature fusion with class-specific multi-expert decoding to segment Vessels, Yellow and Black Spots, and Blood Spots. A three-stage backbone-frozen routing strategy stabilizes dual-backbone adaptation; Progressive Confidence Penalty (PCP) Loss reduces high-confidence false positives and segmentation leakage in SSR regions; and Class-Aware Adaptive Sample Weighting (CA-ASW) balances sample- and class-level training contributions. We further construct the Multi-label Scleral Anomaly Segmentation Dataset (ML-SASD), a new benchmark with Clinical, Wild, and Mix settings and pixel-wise annotations for three anomaly categories. On ML-SASD-Mix, HD-DinoMoE achieves a mean Dice of 72.11% and a mean Intersection-over-Union of 58.44%, while maintaining favorable boundary localization and specular-region false-positive control. It also shows competitive generalization on the Vessels subset of the public SBVPI dataset. These results indicate that HD-DinoMoE provides a feasible segmentation solution for TAO under complex acquisition scenarios. The code and data access information are available at this https URL.

---


### 103. [GRAIL: Gradient-Reweighted Advantages for Reinforcement Learning with Verifiable Rewards](https://arxiv.org/abs/2606.04889)

**<font color=#1a73e8>作者：</font>** Tej Deep Pala, Vernon Toh, Soujanya Poria  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (e.g. GRPO) is now a common way to improve mathematical reasoning in Large Language Models (LLMs). However, current methods usually broadcast one sequence-level advantage to all tokens, or use costly process reward models (PRMs) for step-level supervision. Uniform advantage distribution assumes that all tokens contribute equally to the final reward. This dilutes the gradient signal, since flawed reasoning steps and filler words are updated as strongly as valid logical inferences. To address this, we introduce Gradient-Reweighted Advantage (GRAIL), an intrinsic token-wise advantage reweighting method. GRAIL uses gradient-activation saliency to place more weight on tokens that are more locally sensitive to the final answer. Evaluations across five models from the Qwen3, R1-distilled and OctoThinker families show that GRAIL consistently outperforms GRPO. GRAIL achieved an average improvement of 3.60% in accuracy and 3.05% in Pass@3, demonstrating that fine-grained reasoning alignment can be achieved without process-level supervision.

---


### 104. [BreastGPT: A Multimodal Large Language Model for the Full Spectrum of Breast Cancer Clinical Routine](https://arxiv.org/abs/2606.04911)

**<font color=#1a73e8>作者：</font>** Yang Liu, Jiajin Zhang, Danyang Tu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Breast cancer remains a leading cause of cancer-related mortality among women. Its clinical management requires multimodal reasoning across a clinical workflow that spans \textit{screening}, \textit{diagnosis} and \textit{treatment planning}, where each stage involves distinct imaging modalities, task objectives, and reasoning patterns. However, constrained by data scarcity and model versatility, existing medical MLLMs are typically evaluated on isolated modalities or narrow task families, limiting their ability to support workflow-level clinical reasoning. In this work, we first introduce \textbf{BreastStage}, a workflow-aligned breast imaging instruction corpus comprising 1.86M instruction-following pairs curated from 17 sub-datasets across 5 imaging modalities and 136 task templates. Its held-out split, \textbf{BreastStage-Bench}, provides a comprehensive benchmark for evaluating multimodal reasoning across the breast cancer care continuum. Building on this corpus, we propose \textbf{BreastGPT}, a unified MLLM equipped with a dual-branch visual encoder and concept-preserving token compression to bridge the scale gap between standard radiology and gigapixel pathology. On BreastStage-Bench, BreastGPT achieves 75.66\% closed-ended accuracy and 89.92\% open-ended score, outperforming both general-purpose and medical-specific MLLMs across clinical stages and task formats. These results suggest that workflow-aligned data and cross-scale visual modeling are critical for clinically grounded medical MLLMs. All data, code, and model checkpoints are released at this https URL.

---


### 105. [Caliper: Probing Lexical Anchors versus Causal Structure in LLMs](https://arxiv.org/abs/2606.04915)

**<font color=#1a73e8>作者：</font>** Zhenyu Yu, Shuigeng Zhou  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models reach 50 to 70% accuracy on causal reasoning benchmarks such as CLadder, but it is unclear whether this reflects structural reasoning or lexical pattern matching. We introduce Caliper, a controlled perturbation that replaces semantic variable names with placeholder tokens while preserving the causal graph and probabilistic specification of each question. Across nine instruction-tuned LLMs from 3.8B to 671B and three causal reasoning benchmarks, lexical anonymization yields robust accuracy drops of +7.6, +27.0, and +11.1 pp on a local 3.8B-14B set, rising to +29.6 and +18.0 pp on CRASS and e-CARE across nine frontier models spanning the 2024-2026 generations. Of 40 engaged model-by-benchmark cells, 39 show a positive gap, and the gap collapses by 17x on CLadder's pseudoword subset. Structured scaffolding and few-shot in-context learning each narrow the gap, but mainly by lowering P0 accuracy on smaller models rather than recovering P1. Current instruction-tuned LLMs, evaluated zero-shot, show little evidence of structural causal reasoning once lexical anchors are removed.

---


### 106. [Toward Multi-Domain and Long-Tailed Quantization via Feature Alignment and Scaling](https://arxiv.org/abs/2606.04920)

**<font color=#1a73e8>作者：</font>** Chin-Yuan Yeh, Ting-An Chen, De-Nian Yang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Quantizing deep neural networks is essential for efficient inference on resource-constrained devices. However, most existing methods are designed for single-domain and class-balanced data, leaving practical settings with domain shifts or severe class imbalance underexplored. We address these challenges with Efficient Multi-Domain Alignment Quantization (EmaQ), which aligns domain distributions through a CDF-based projection and uses sensitivity-aware weight aggregation to stabilize multi-domain quantization. We further extend EmaQ to EmaQ-LT for long-tailed quantization by introducing class-conditioned variance scaling and confidence-based logit adjustment to mitigate majority-class overconfidence. Theoretical analyses establish convergence guarantees and motivate the proposed sensitivity and scaling mechanisms. Experiments on standard, multi-domain (Office-31, Digits), and long-tailed (SynDigits-LT, CIFAR-10-LT, CIFAR-100-LT) benchmarks show that EmaQ and EmaQ-LT achieve strong low-bit performance under domain shift and class imbalance.

---


### 107. [Geometry-Aware Distillation for Prompt Tuning Biomedical Vision-Language Models](https://arxiv.org/abs/2606.04922)

**<font color=#1a73e8>作者：</font>** Tran Dinh Tien, Zhiqiang Shen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Current prompt-based and adapter-based tuning of vision-language models (VLMs) is attractive for medical imaging, where clinical data sensitivity favors frozen backbones and annotations are limited. However, these methods typically optimize only the ground-truth class, treating all other classes as equally incorrect, ignoring clinically meaningful class relations and yielding unstable decision boundaries in limited-supervision settings. We propose Omni-Geometry Knowledge Distillation (OGKD), a new framework that injects class-relation structure into the teacher to produce directional targets that preserve the ground truth while respecting inter-class geometry. Using these targets, we develop two distillation losses: Global Geometry-Aware Distillation (GAD) operates on the global image token, and Label-Guided Geometry Distillation (LGD) applies the same geometry to attentive patch tokens to improve fine-grained alignment. Across comprehensive experiments and analyses on 11 widely-used medical datasets for base-to-novel and few-shot evaluations, our OGKD achieves substantially better performance, consistently improving accuracy by an average absolute gain of 1.7%-2.8% over all prior state-of-the-art VLM adaptation counterparts. It also robustly generalizes to unseen classes and yields more reliable predictions than other approaches. Our code is available at this https URL.

---


### 108. [Can Crowdsourcing Survive the LLM Era? A Community Survey on Human Data Collection](https://arxiv.org/abs/2606.04924)

**<font color=#1a73e8>作者：</font>** Aswathy Velutharambath, Neele Falk, Sofie Labat 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The widespread use of Large Language Models (LLMs) as writing tools challenges the validity of crowdsourced data, as crowdworkers may outsource tasks to models. To better understand how this is addressed, we surveyed 155 researchers in NLP and related disciplines about their experiences and opinions on collecting free-text responses via crowdsourcing. This paper provides an overview of practitioners' challenges, mitigation strategies, and the foreseen implications on data quality. 44% of respondents reported observing LLM usage in their crowdsourced data. While 93% of them had anticipated this, half were unsure what precautions to take. The most prevalent detection strategies are distinctive textual style patterns and unusually fast completion times. Overall, survey responses show that the research community is aware of the problem and taking measures, but existing efforts remain insufficient to fully address it. Finally, we derive a set of considerations to guide future crowdsourced free-text data collection in the era of LLMs.

---


### 109. [Data Attribution in Large Language Models via Bidirectional Gradient Optimization](https://arxiv.org/abs/2606.04928)

**<font color=#1a73e8>作者：</font>** Frédéric Berdoz, Luca A. Lanzendörfer, Kaan Bayraktar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are increasingly deployed across diverse applications, raising critical questions for governance, accountability, and data provenance. Understanding which training data most influenced a model's output remains a fundamental open problem. We address this challenge through training data attribution (TDA) for auto-regressive LLMs by expanding upon the inverse formulation: How would training data be affected if the model had seen the generated output during training? Our method perturbs the base model using bidirectional gradient optimization (gradient ascent and descent) on a generated text sample and measures the resulting change in loss across training samples. Our framework supports attribution at arbitrary data granularity, enabling both factual and stylistic attribution. We evaluate our method against baselines on pretrained models with known datasets, and show that it outperforms previous work on influence metrics, thereby enhancing model interpretability, an essential requirement for accountable AI systems.

---


### 110. [Sequential Data Poisoning in LLM Post-Training](https://arxiv.org/abs/2606.04929)

**<font color=#1a73e8>作者：</font>** Jack Sanderson, Yihan Wang, Xiaoqian Lu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> LLM post-training proceeds through multiple stages, e.g., supervised fine-tuning (SFT) followed by reinforcement learning from human feedback (RLHF) or direct preference optimization (DPO), where each stage draws data from different, potentially untrusted sources. Existing literature assumes data poisoning attacks may occur at each training stage, but neglects the possibility of multiple attackers. To study the trustworthiness of the entire post-training pipeline, we propose the threat model of sequential data poisoning, where multiple adversaries separately poison the SFT and preference datasets. Under this threat model, we identify the single-attacker illusion: each adversary, evaluated in isolation, appears to pose a negligible threat. Yet when adversaries collaborate across stages, the true vulnerability is revealed. In the SFT $\to$ DPO pipeline, their contributions are additive: splitting a fixed poison budget across stages outperforms concentrating it in either stage alone. In the SFT $\to$ PPO pipeline, their contributions are complementary: neither SFT nor reward model poisoning succeeds individually, yet their combination does. These findings show that security analyses of individual post-training stages systematically underestimate compound vulnerabilities that emerge only from their interaction. Code is available at this https URL.

---


### 111. [STaR-Quant: State-Time Consistent Post-Training Quantization for Diffusion Large Language Models](https://arxiv.org/abs/2606.04945)

**<font color=#1a73e8>作者：</font>** Xin Yan, Aqiang Wang, Zhenglin Wan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion large language models (DLLMs) have recently emerged as a promising alternative to autoregressive LLMs by generating text through iterative masked denoising with bidirectional context. However, their large model sizes and iterative denoising process introduce substantial memory and computational overhead, motivating post-training quantization for efficient deployment. In this paper, we identify two key challenges for low-bit DLLM quantization: state-dependent activation disparity and temporal error accumulation. Masked and unmasked tokens exhibit different activation distributions within each denoising step, while quantization errors can accumulate across steps during iterative decoding. To address these challenges, we propose STaR-Quant, a state-time consistent PTQ framework for DLLMs. STaR-Quant introduces State-Guided Activation Transformation (SGAT) to assign masked and unmasked tokens to different activation transformation spaces with a unified static weight-side transformation. It further introduces Temporal Attention Compensation (TAC) to correct the quantized attention representation via a lightweight block-diagonal affine mapping. Experiments on representative DLLMs demonstrate that STaR-Quant consistently improves low-bit weight-activation quantization over strong PTQ baselines, while delivering up to 1.69x speedup and 3.14x memory saving over FP16 deployment.

---


### 112. [SemBlock: Semantic Boundary Dynamic Blocks for Diffusion LLMs](https://arxiv.org/abs/2606.04964)

**<font color=#1a73e8>作者：</font>** Xinrui Song, Zhuoran Wang, Mingju Gao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Diffusion language models (DLMs) generate text through iterative denoising, and blockwise decoding improves their practicality by committing tokens in local blocks. However, existing blockwise methods typically rely on fixed block sizes or delimiter-based runtime signals, which do not necessarily align with semantic boundaries. In this paper, we propose SemBlock, a semantic-boundary-driven dynamic block decoding framework for diffusion LLMs. SemBlock formulates dynamic block construction as semantic boundary prediction and trains lightweight predictors on frozen LLaDA hidden states. To provide supervision, we construct SemBound, a semantic-boundary dataset that derives boundary labels from discourse units, reasoning steps, and implementation spans across natural language, math, and code tasks. During inference, SemBlock uses predicted boundary probabilities to select the ending position of each dynamic block. Experiments on GSM8K, IFEval, MATH, and HumanEval show that SemBlock consistently improves over fixed-block decoding and AdaBlock. Our code is publicly available: this https URL.

---


### 113. [SAID: Accelerating Diffusion-Based Language Models via Scaffold-Aware Iterative Decoding](https://arxiv.org/abs/2606.04974)

**<font color=#1a73e8>作者：</font>** Na Li, Chengda Wang, Mingju Gao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Diffusion large language models (DLLMs) enable non-autoregressive generation by iteratively denoising corrupted token sequences with bidirectional context. Despite their ability to update multiple positions in parallel, inference remains costly due to the many denoising steps required for high-quality generation. We propose SAID, a Scaffold-Aware Iterative Decoding framework that accelerates DLLMs by reallocating computation across tokens. SAID first spends denoising computation on scaffold tokens to establish the coarse semantic structure, and then completes predictable detail tokens with fewer steps. We further adapt SAID to block-wise diffusion decoding and introduce Confidence-Hierarchical Layered Generation (CHLG), which assigns additional steps only to low-confidence tokens. Experiments on LLaDA-8B and LLaDA 1.5 across math, coding, and knowledge benchmarks show that SAID significantly accelerates DLLM inference with a maximum speedup of 9.1x while maintaining competitive performance. Our code is publicly available: this https URL.

---


### 114. [Probing Outcome-Level Resemblance and Mechanism-Level Alignment in LLM Risk Decisions: Evidence from the St. Petersburg Game](https://arxiv.org/abs/2606.04978)

**<font color=#1a73e8>作者：</font>** Chensong Huang, Changyu Chen, Chenwei Lin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLMs can appear cautious in risk decision-making tasks, yet cautious-looking outputs do not necessarily indicate alignment with human decision-making mechanisms. We investigate this distinction using the St. Petersburg game as a controlled testbed, a classical paradox in which the expected payoff is infinite, yet humans typically report low, finite willingness to pay. We evaluate 28 LLMs with a structured prompt suite that includes the original game; controlled decision variants that perturb truncation, repeated play, numeric endowment, and occupational identity; a human-perspective prompt that asks models to reason as human decision makers; and paired comparisons between base models and their instruction-tuned counterparts. In the original game, most models generate finite bids, creating the appearance of human-like risk behavior. However, this outcome-level resemblance masks substantial mechanism-level differences. The controlled variants reveal that rather than maintaining human-like behavior seen in the original game, models often shift to conditionally and computationally rational behavior. Human-cue prompting and instruction tuning often lower bids and reduce some visible pathologies, but most mechanism-level response patterns remain largely unchanged. These findings show that behavioral alignment in risk decision-making can be surface-level: LLMs may produce human-like risk decisions without exhibiting human-consistent mechanisms. High-stakes evaluations of LLM decision-making should therefore move beyond outcome similarity and examine whether the alignment is supported by mechanism-level consistency.

---


### 115. [AlphaQ: Calibration-Free Bit Allocation for Mixture-of-Experts Quantization](https://arxiv.org/abs/2606.04980)

**<font color=#1a73e8>作者：</font>** Wanqi Yang, Yuexiao Ma, Alexander Conzelmann 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mixture-of-Experts (MoE) architectures scale model capacity through sparse expert activation, but their deployment remains memory-bound because all expert weights must reside in memory. Mixed-precision quantization can substantially reduce this footprint by assigning different bit-widths to different experts. Existing approaches, however, typically rely on calibration data to estimate expert importance and determine bit allocation. For frontier MoE LLMs, the original training data, and hence the true training distribution, is proprietary and inaccessible. As a result, calibration sets are inevitably imperfect surrogates, and this can misestimate expert utilization and lead to suboptimal bit allocation. Motivated by the substantial cross-expert quality variability observed in modern MoE models, and by the success of Heavy-Tailed Self-Regularization (HT-SR) theory at predicting neural network model quality without access to training or testing data, we propose AlphaQ, a calibration-free bit-allocation method for MoE quantization. AlphaQ draws on HT-SR theory and follows a simple principle: experts with more heavy-tailed weight spectra are typically better trained and hence should receive higher bit-widths, while experts with weaker heavy-tailed structure can be quantized more aggressively. AlphaQ operationalizes this principle by measuring expert-wise spectral heavy-tailedness and solving a budget-constrained optimization problem that minimizes total quantization error under a global bit-budget constraint. Across several MoE models, AlphaQ consistently outperforms calibration-based baselines under matched bit budgets. Notably, on Qwen1.5-MoE, AlphaQ achieves near full-precision accuracy with an average expert precision of only 3.5 bits, while delivering more than 4$\times$ memory compression. Our code is available at this https URL.

---


### 116. [Food-R1: A Unified Multi-Task Food Vision-Language Model with Reinforcement Learning](https://arxiv.org/abs/2606.04986)

**<font color=#1a73e8>作者：</font>** Yu Zhu, Yongkang Li, Wenjie Zhu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent studies have explored Vision-Language Models (VLMs) for food analysis. However, most existing methods rely primarily on supervised fine-tuning (SFT), which often limits reasoning and generalization capabilities. Moreover, high-quality large-scale nutritional annotations remain scarce. To address these issues, we introduce CalorieBench-80K, a large-scale benchmark with curated calorie labels and dietary advice annotations. To the best of our knowledge, it is the first food image benchmark to incorporate Chain-of-Thought (CoT) annotations for calorie reasoning. We also propose Food-R1, a unified food VLM trained in a multi-task learning paradigm to equip the model with broad capabilities. Food-R1 undergoes CoT-based cold-start instruction tuning, followed by reinforcement fine-tuning (RFT) using Group Relative Policy Optimization (GRPO) to improve reasoning and performance. Experiments on CalorieBench-80K and representative benchmarks show that Food-R1 consistently outperforms strong baselines across food-related tasks. The code, model weights, and benchmark annotations are available at the project repository.

---


### 117. [PhysDox: Benchmarking LLMs on Physical Feasibility Auditing of Physiological Sensing Protocols](https://arxiv.org/abs/2606.05003)

**<font color=#1a73e8>作者：</font>** He Liu, Boyuan Gu, Shuaiqi Cheng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) increasingly assist in experimental design, yet fluent protocols often remain physically infeasible. We introduce PhysDox, a physical feasibility auditing benchmark for biomedical protocols comprising a 683-sample expert-curated Gold set and a 5,000-sample Silver set across six sensing domains. We formulate the task as a two-stage evaluation: severity detection classifying protocols as valid, minor, or fatal, followed by the constraint-level diagnosis of fatal violations. Evaluating 6 LLMs across 4 inference strategies yields a peak Stage-1 macro-F1 of only 53.0. Moreover, strong oracle diagnosis collapses during end-to-end evaluation due to correlated cascade errors. Error analysis reveals scaffold bias, where models conflate procedural completeness with physical validity. Consequently, implicit constraints exhibit a 2 times higher miss rate than explicit hardware violations, supported by strong statistical correlation at $\rho{=}0.81$ and $p{<}0.01$. Trace analysis of false negatives exposes a 54%--46% split between attention and judgment failures, ultimately demonstrating that protocol auditing demands calibrated feasibility reasoning rather than factual recall or longer rationales.

---


### 118. [DAR: Deontic Reasoning with Agentic Harnesses](https://arxiv.org/abs/2606.05009)

**<font color=#1a73e8>作者：</font>** Guangyao Dou, William Jurayj, Nils Holzenberger 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Deontic reasoning is the task of answering questions by applying explicit rules and policies to case-specific facts, for example computing tax liability under a statute or determining the outcome of an immigration appeal. A key technical challenge for LLM-based deontic reasoning is that the relevant ruleset can be long and cross-referenced, so models may still fail to locate the rules needed for a particular reasoning step. We introduce Deontic Agentic Reasoning (DAR), an agentic reasoning setup in which the model interacts with the statutes on demand. We evaluate DAR under multiple harnesses on hard subsets of DeonticBench. Across these settings, we find that agentic harnesses can push the frontier on deontic reasoning tasks, but improvements are not uniform: weaker models often degrade on numerical tasks while consuming far more tokens.

---


### 119. [Depth-Attention: Cross-Layer Value Mixing for Language Models](https://arxiv.org/abs/2606.05014)

**<font color=#1a73e8>作者：</font>** Boyi Zeng, Yiqin Hao, Zitong Wang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Self-attention selects information freely across the sequence, but across depth, Transformers merely add each layer's output to the residual stream, so later layers cannot selectively reuse earlier-layer representations. Recent cross-layer methods improve this flow but operate on hidden states outside attention, adding state beyond the key-value cache at inference--a cost that becomes increasingly salient as modern LLMs compress the cache with grouped-query and multi-head latent attention. We introduce Depth-Attention, which performs this selection inside the attention module itself: before a layer attends over the sequence, its query attends over the keys of earlier layers at the same token position and mixes their values into the value that self-attention then reads. Because Depth-Attention reuses the standard attention queries, keys, and value-cache slots, storing depth-mixed values in place of the original values, it adds no parameters and introduces no persistent inference state beyond the standard key-value cache--the same cache size as a vanilla decoder and less than hidden-state-based cross-layer methods. On Qwen3-style decoders at 1.5B and 3B parameters, Depth-Attention attains the lowest perplexity and the highest average downstream accuracy, improving over the vanilla Transformer by up to 2.3 accuracy points and surpassing strong cross-layer baselines in perplexity and average accuracy, while adding under 0.01% extra arithmetic FLOPs and no additional persistent inference state. The gains hold from 360M to 3B parameters and extend to looped Transformers.

---


### 120. [Invariant Gradient Alignment for Robust Reasoning Distillation](https://arxiv.org/abs/2606.05025)

**<font color=#1a73e8>作者：</font>** Zehua Cheng, Wei Dai, Jiahao Sun  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) suffer from shortcut learning: they systematically fail on out-of-distribution (OOD) inputs whose semantic surface differs from training data, even when the logical structure is identical. This undermines knowledge distillation pipelines that transfer chain-of-thought reasoning to smaller students. We introduce Invariant Gradient Alignment (IGA), a training framework that aligns gradient updates across semantically diverse but logically isomorphic examples via three innovations: (i) Logical Isomer Sets, groups of problems sharing identical logical structure across distinct semantic domains (mathematics, medicine, law, science); (ii) a differentiable \emph{Continuous Gradient Conflict Mask}, that suppresses parameter dimensions with high cross-domain gradient variance while preserving invariant directions; and (iii) a truncated SVD projection of the masked gradient back onto the LoRA low-rank manifold, maintaining parameter efficiency throughout. Theoretically, IGA yields tighter OOD generalization bounds than ERM, scaling with the number of isomer domains, and converges at the standard SGD rate under mild regularity. Empirically, IGA outperforms eight baselines across four benchmarks with accuracy gains up to 14.3 pp over ERM-SFT and a Logical Consistency Score of 0.031 versus 0.142 -- a fourfold improvement in representational invariance.

---


### 121. [Validity Threats for Foundation Model Research](https://arxiv.org/abs/2606.05029)

**<font color=#1a73e8>作者：</font>** Gunnar König, Martin Pawelczyk, Ulrike von Luxburg 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Controlled experiments are the backbone of machine learning research, but at the scale of modern foundation models, they have become prohibitively expensive. Instead, the community increasingly relies on research strategies that approximate the ideal experiment at a fraction of the cost: proxy experiments and scaling laws, observational studies with publicly available models, and single-run designs that leverage variation within individual training runs. In this work, we argue that there is no free lunch when approximating large-scale experiments on a compute budget. Specifically, savings in compute come at the cost of validity threats -- hidden and sometimes untestable assumptions that, when violated, can invalidate research claims. To help navigate such threats, we propose an evaluation framework that casts foundation model research as a causal inference problem. Within this framework, we evaluate different research strategies through four types of validity adapted from the empirical social sciences -- statistical, internal, external, and construct validity. We find that each strategy comes with a characteristic validity profile: proxy experiments trade external and construct validity for statistical and internal validity; observational studies face confounding and effect heterogeneity; and single-run designs are strained by interference between treated units. This analysis reveals several validity threats that have received insufficient attention in the literature. Overall, our evaluation framework provides researchers with a practical toolkit for scrutinizing validity threats in foundation model research~designs.

---


### 122. [Imbuing Large Language Models with Bidirectional Logic for Robust Chain Repair](https://arxiv.org/abs/2606.05030)

**<font color=#1a73e8>作者：</font>** Zehua Cheng, Wei Dai, Jiahao Sun 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Autoregressive chain-of-thought (CoT) reasoning in large language models (LLMs) is fundamentally forward-directed: each step conditions only on prior tokens. This unidirectional inductive bias renders even capable models susceptible to error snowballing, wherein a single logical or arithmetic mistake in an early step irreversibly corrupts the entire reasoning chain. We introduce Teleological Reasoning Infilling (\TRI{}), a training framework that endows decoder-only transformers with a native \emph{goal-conditioned bridging} capability. The key insight is to reframe erroneous reasoning segments as fill-in-the-middle (FIM) tasks: given a verified prefix premise $P$, a verified downstream milestone $S$, and the original query $Q$, the model must synthesise the logical bridge $M$ that connects $P$ to $S$ rigorously and completely. To achieve this with standard causal architectures, we introduce a Prefix-Suffix-Middle (PSM) sequence rearrangement with three non-overlapping sentinel tokens, enabling $M$ to attend to both $P$ and $S$ without any structural modification to the self-attention mechanism. Training proceeds in two stages: (i) Supervised Fine-Tuning (SFT) on symbolically verified $(P, S, M)$ triples extracted from formal mathematics corpora, and (ii) Direct Preference Optimisation (DPO) with a deterministic symbolic verifier (Lean 4 / Python) as the sole reward oracle, eliminating LLM-judge sycophancy. At inference, TRI operates as a surgical repair module within a dual-system loop: a causal draft model generates an initial trace, the verifier pinpoints failures, and TRI infills only the damaged segment, leaving verified sections intact. Comprehensive experiments on three benchmarks demonstrate that TRI achieves state-of-the-art performance across all tasks, while reducing per-problem token expenditure by 31.2%.

---


### 123. [MetaPoint: Unlocking Precise Spatial Control in Agentic Visual Generation](https://arxiv.org/abs/2606.05031)

**<font color=#1a73e8>作者：</font>** Dewei Zhou, Xinyu Huang, Xun Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generative visual models fundamentally struggle with precise spatial control. This arises from a core disconnect: models can process textual descriptions of space but cannot directly map numerical coordinates onto the 2D image canvas. We introduce MetaPoint, a method that bridges this gap by representing a continuous 2D coordinate as a single, special token. Crucially, MetaPoint requires no new architectural components; it directly leverages the model's inherent positional encoding schemes to interpret these coordinates, treating our token as a virtual point on the canvas. This lightweight approach enables pixel-level control of an object's position with one token or its bounding box with two, all without requiring architectural changes or bespoke attention masking. The MetaPoint tokens are designed to be compositional, serving as spatial primitives. This allows a planner agent to decompose a high-level user request into a structured sequence of primitives for the generator. By providing a simple, precise, and scalable building block for spatial control, MetaPoint unlocks more powerful compositional generative agents and enables intuitive, interactive editing systems.

---


### 124. [Strabo: Declarative Specification and Implementation of Agentic Interaction Protocols](https://arxiv.org/abs/2606.05043)

**<font color=#1a73e8>作者：</font>** Samuel H. Christie V, Amit K. Chopra, Munindar P. Singh  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The last few years have witnessed major advances in the modeling and implementation of multiagent systems based on declarative interaction protocols. Our contribution, Strabo, establishes the relevance of these advances to ongoing industry efforts in Agentic AI. Specifically, we consider UCP, the Universal Commerce Protocol, a recent Google-led effort to standardize e-commerce interactions for AI agents. Our exercise is in two parts. One, we model the part of UCP dealing with checkouts as a declarative Langshaw protocol and implement agents using Peach, a programming model for Langshaw. This part of the exercise brings out the advantages of formal, declarative specifications. Two, we show that Peach agents can interoperate with UCP agents implemented by Google, thereby establishing the fidelity of our approach with respect to UCP. Such interoperation enables the incremental introduction of declarative protocols and agents into a conventional setting, indicating a pathway by which EMAS ideas could influence practice without demanding a wholesale update.

---


### 125. [UniCAD: A Unified Benchmark and Universal Model for Multi-Modal Multi-Task CAD](https://arxiv.org/abs/2606.05058)

**<font color=#1a73e8>作者：</font>** Jingyuan Chen, Sheng Jin, Haopeng Sun 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Computer-Aided Design (CAD) underpins modern engineering and manufacturing by enabling the creation of precise, editable 3D models. However, CAD research typically studies tasks in isolation, and multi-modal, multi-task learning for CAD is hindered by the absence of a unified benchmark. To address this gap, we introduce UniCAD, a comprehensive benchmark for multi-modal CAD learning that covers point-to-CAD reconstruction, text/image-to-CAD generation, and CAD question answering across diverse input modalities. Alongside the benchmark, we present UniCAD-MLLM, a universal multi-modal large language model that ingests text, images, sketches, and point clouds and performs these heterogeneous tasks in an end-to-end fashion within a single framework. Extensive experiments on the UniCAD and Fusion360 benchmarks demonstrate that UniCAD-MLLM achieves state-of-the-art performance across all tasks, outperforming existing task-specific and multi-task baselines. We will release the dataset, code, and pretrained models to accelerate future research.

---


### 126. [Fast & Faithful Function Vectors](https://arxiv.org/abs/2606.05079)

**<font color=#1a73e8>作者：</font>** Minh An Pham, Anton Segeler, Thomas Wiegand 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Function vectors (FVs) are task representations elicited during in-context learning that can be used to steer Large Language Models (LLMs). However, design choices in their formulation remain underexplored. In this work, we study the impact of varying FV definitions for instructions along two degrees of freedom: attention head selection and steering. For head selection, using gradient-based attributions with Layer-wise Relevance Propagation (LRP) substantially improves efficiency as well as accuracy. For FV steering, applying it in a distributed manner yields a higher accuracy compared to simple aggregation. Our code is publicly available.

---


### 127. [Automatic Generation of Titles for Research Papers Using Language Models](https://arxiv.org/abs/2606.05085)

**<font color=#1a73e8>作者：</font>** Tohida Rehman, Debarshi Kumar Sanyal, Samiran Chattopadhyay  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The title of a research paper conveys its primary idea and, occasionally, its conclusions in a clear and concise manner. Choosing an appropriate title is often challenging, and automated title generation can assist authors in this task. In this work, we propose a technique to generate paper titles from abstracts using open-weight pre-trained and large language models. We use the CSPubSum and LREC-COLING-2024 datasets and introduce a new dataset, SpringerSSAT, curated from four Springer journals in the social sciences. Additionally, we use GPT-3.5-turbo in a zero-shot setting to generate titles. Model performance is evaluated with ROUGE, METEOR, MoverScore, BERTScore, and SciBERTScore metrics. Our experiments show that fine-tuned PEGASUS-large outperforms other models, including fine-tuned LLaMA-3-8B and zero-shot GPT-3.5-turbo, across most metrics. We further demonstrate that ChatGPT can generate creative paper titles. Overall, AI-generated titles are generally appropriate and reliable.

---


### 128. [Light or Full Verb? A Minimal-Pair Dataset for Probing Phraseological Competence in Language Models](https://arxiv.org/abs/2606.05087)

**<font color=#1a73e8>作者：</font>** Francesca Franzon, Nicolas Rosàs Gómez, Leo Wanner  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Frequent English verbs such as 'have' and 'make' can function either as collocates in light-verb constructions or as full lexical predicates, as in 'make a decision' vs. 'make a cake'. Whether language models represent this distinction remains unclear. We introduce a large-scale controlled dataset of minimally varying English sentence series in which the same context contains the same verb in light-verb and full-verb uses. Two probing experiments show that language models differentiate between these uses even in minimal contexts and exhibit separable patterns across object types. We release the dataset, generation code, and materials as a reusable resource. The framework supports extensions to broader contexts, additional verbs, and other languages.

---


### 129. [Knowledge Index of Noah's Ark](https://arxiv.org/abs/2606.05104)

**<font color=#1a73e8>作者：</font>** Sheng Jin, Minghao Liu, Yunze Xiao 等 27 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Knowledge benchmarks for LLMs face three issues: scaling-driven designs that do not operationalize disciplinary representativeness; flat-payment annotation that permits lazy consensus; and unaudited ranking instability under bounded test budgets. We introduce KINA, an 899-item benchmark across 261 fine-grained disciplines, with two formal results. First, we cast representativeness as a coverage-style objective over expert-elicited anchors and operationalize disciplinary representativeness through a proxy, yielding a (1-1/e) greedy approximation (Proposition 1); the guarantee applies to the proxy, not to population representativeness. Second, we prove a bonus-on-bar tournament weakly FOSD-dominates flat payment in released-review quality, with incentive-compatibility threshold B > Delta C / Delta p_min (Theorem 1). Evaluating 42 models from 13 labs, the top model, Gemini-3.1-Pro-Preview, reaches 53.17%, followed by Claude-Opus-4.6 at 49.92% and GPT-5.4 at 48.55%, leaving substantial headroom below saturation. The full leaderboard shows a tiered structure rather than a smooth total order: a small frontier tier lies above 48%, a dense strong-model tier spans roughly 38-45%, and low-performing models remain only modestly above the 10% chance baseline. Tool augmentation adds up to 5.17 points across the five tool-use evaluations, with gains varying substantially across models. We report bootstrap ranking-stability statistics to make bounded-budget variance explicit and to discourage over-interpretation of adjacent ranks.

---


### 130. [Arithmetic Pedagogy for Language Models](https://arxiv.org/abs/2606.05106)

**<font color=#1a73e8>作者：</font>** Andhika Bernard Lumbantobing, Hokky Situngkir  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We investigate whether methods of human mathematics pedagogy can guide the training of language models toward arithmetic reasoning. Building on the GASING method -- an Indonesian pedagogy that solves basic arithmetic through a left-to-right procedure aligned with the causal order of token generation -- we operationalize each operation as a computational procedure whose execution trace is serialized into natural-language Chain-of-Thought (CoT) supervision. A small GPT-2 decoder (86M parameters) with a syllabic-agglutinative TOBA tokenizer for Indonesian is trained from scratch on this data using only a next-token prediction objective, without reinforcement learning or reward-based optimization. Monitoring training reveals three distinct learning phases, and mechanistic analyses -- attention-masking interventions on the CoT information graph, residual-stream probing, and logit-lens inspection -- show that the model first internalizes a procedural pathway and subsequently develops an associative, ``mental-arithmetic'' capacity that retrieves intermediate results without explicit step-by-step computation. The trained model reaches over 80% accuracy on held-out problems and attains competitive performance against substantially larger language models, indicating that targeted, pedagogically grounded training can yield strong and economical arithmetic capability at small scale.

---


### 131. [Who Needs Labels? Adapting Vision Foundation Models With the Metadata You Already Have](https://arxiv.org/abs/2606.05107)

**<font color=#1a73e8>作者：</font>** Elouan Gardès, Seung Eun Yi, Kartik Ahuja 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We propose a label-free approach to adapt powerful but generic vision foundation models to specialized scientific domains. Standard supervised fine-tuning is often ill-suited to these settings: labels are scarce, and task-specific training can collapse the model's generality and hurt robustness. We instead leverage metadata to adapt representations to new domains in a self-supervised manner. Our method, FINO, combines a standard self-supervised objective with flexible metadata guidance that handles both highly granular discrete metadata and continuous metadata. It encourages the representation to preserve informative factors while suppressing spurious ones. Across subcellular fluorescence microscopy, Earth observation, wildlife monitoring, and medical imaging, FINO consistently outperforms standard unsupervised domain adaptation and fully supervised adaptation. It also exceeds highly-specialized domain-specific state of the art, while using no task labels for backbone adaptation and only lightweight probes for supervision.

---


### 132. [RePercENT: Scaling Disentangled Representation Learning Beyond Two Modalities](https://arxiv.org/abs/2606.05109)

**<font color=#1a73e8>作者：</font>** Vasiliki Rizou, Pascal Frossard, Dorina Thanou  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> To leverage the full potential of multimodal data, we need representations that go beyond the state-of-the-art alignment and fusion approaches and exploit all cross-modal interactions without sacrificing modality-specific information. Learning disentangled representations is a principled way to identify these underlying shared and unique factors that are hidden in observational data. However, while multimodal disentanglement is a compelling paradigm, existing methods are largely confined to the two-modality regime due to its inherent scalability bottleneck. To address this, we propose RePercENT, a self-supervised framework designed to surpass these limitations and unlocks scalable pairwise disentanglement beyond two modalities. Through a multimodal `plug-and-play' architecture, our approach operates directly on pre-extracted embeddings, eliminating the need for extensive joint pre-training while making no assumptions regarding the underlying modalities or foundation model backbones. Moreover, we introduce a joint optimization objective for simultaneously deriving the shared and unique components, and provide formal theoretical guarantees that characterize the optimality of our solution. Across diverse modalities and tasks, RePercENT successfully recovers disentangled components while maintaining competitive performance and significantly reducing computational complexity.

---


### 133. [Evaluating Large Language Models in Dynamic Clinical Decision-Making with Standardized Patient Cases](https://arxiv.org/abs/2606.05112)

**<font color=#1a73e8>作者：</font>** Cheng Liang, Pengcheng Qiu, Ya Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly proposed as clinical agents, yet static, single-turn benchmarks cannot capture how a model dynamically delivers care across an encounter: gathering information, planning treatment, and adapting longitudinal management across successive patient states. Medical education has long addressed an analogous challenge through standardized patients (SPs): trained actors who consistently portray clinical cases, enabling realistic practice and objective, scripted assessment. Here we introduce MedSP1000, an SP-derived interactive benchmark for clinical-agent evaluation, including 1,638 SP cases with 24,602 trajectory-level peer-reviewed rubrics. MedSP1000 converts peer-reviewed SP teaching cases into executable scenarios with defined SP case scripts, clinical environment contexts, and human-validated structured rubric. In each simulation evaluation run, a clinical agent interacts in closed loop with a patient agent and an environment controller, and its behaviour is scored throughout the encounter against expert criteria specified in the original materials. Applying MedSP1000 to a range of general-purpose and medically specialized LLMs, we find that performance on static benchmarks does not reliably translate to such educational scenarios. The best-performing model, GPT-5.5, completes only 60.4% of expert-defined rubric items, whereas the strongest medically specialized model reaches 40.0%; increasing test-time compute produces no measurable gain. These results suggest that current LLMs, including agentic systems tuned for medicine, are not yet reliable enough to be safely integrated into actual clinical practice. More broadly, MedSP1000 shows how process-level, SP-style evaluation can reveal clinically relevant failure modes that single-turn benchmarks miss.

---


### 134. [Self-Evaluation Is Already There: Eliciting Latent Judge Calibration in Base LLMs with Minimal Data](https://arxiv.org/abs/2606.05122)

**<font color=#1a73e8>作者：</font>** XiuYu Zhang, Yi Shan, Junfeng Fang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly evaluated by other models, raising a natural question: can a model predict how a judge will score its own output? We find that the ability is largely present before any targeted training: prompted few-shot, a base model already predicts an external judge's multi-attribute quality scores on open-ended responses well above chance across three benchmarks. We introduce Self-Evaluation Elicitation (SEE), a method that surfaces this latent ability through a short cycle comprising a calibration-coupled reinforcement learning phase that improves the answer and predicts the judge, followed by a masked distillation phase that sharpens the prediction while leaving the answer untouched. From 160 unique examples, roughly 31x fewer than a reinforcement learning baseline, SEE improves held-out calibration across three benchmarks while preserving answer quality. The elicited self-evaluation is sharply localized within the model's own token distribution and stable across judges it was never trained against, indicating a transferable notion of quality rather than a single judge's preference. These results reframe judge-aligned self-evaluation as a problem of elicitation rather than acquisition.

---


### 135. [Towards Efficient and Evidence-grounded Mobility Prediction with LLM-Driven Agent](https://arxiv.org/abs/2606.05130)

**<font color=#1a73e8>作者：</font>** Linyao Chen, Qinlao Zhao, Zechen Li 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Individual-level mobility prediction is central to urban simulation, transportation planning, and policy analysis. Supervised sequence models achieve strong accuracy but require task-specific training and offer limited decision-level transparency. Recent LLM-based methods improve interpretability, yet mostly rely on static prompts and single-pass inference, limiting their ability to seek additional evidence when mobility signals are weak or conflicting. We propose \method{}, a training-free LLM-driven agent framework that formulates next-location prediction as adaptive evidence-controlled decision making. \method{} resolves routine cases through a fast path based on historical regularity, while ambiguous cases trigger iterative tool use over recent trajectories, historical behavior, stay-move likelihood, and geographical evidence. Across three mobility datasets, AgentMob achieves the strongest overall performance among training-free LLM-based methods, with GPT-5.4 reaching 71.42\% Acc@1 on BW, 33.14\% on YJMob100K, and 33.50\% on Shanghai ISP. On BW non-fast-path cases, the LLM controller improves Acc@1 from 30.65\% to 48.62\% over a same-tool statistical baseline, showing that its main benefit lies in resolving ambiguous predictions through adaptive evidence gathering. Our code is available at this https URL.

---


### 136. [Activation-Based Active Learning for In-Context Learning: Challenges and Insights](https://arxiv.org/abs/2606.05134)

**<font color=#1a73e8>作者：</font>** Yaseen M. Osman, Geoff V. Merrett, Stuart E. Middleton  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Deep active learning has previously been explored for LLM in-context sample selection, but not with methods that utilise recent advances in understanding of transformer activations. In this paper, we test the hypothesis that model activations could provide a fine-grained signal to optimise the selection of in-context examples. We present the most comprehensive analysis to date of MLP activation-based deep active learning methods applied to in-context learning, including how different attention masking strategies impact active learning across diverse classification and generative datasets, using both Llama-3.2-3B and Qwen2.5-3B base models. However, we find a negative result: MLP outputs, viewed through the lenses of massive activations or the first four moments, do not correlate with example quality or task performance. Specifically, the absolute Spearman correlation coefficient is at most 0.33 for all tasks and models we tested, showing that such activation-based sampling should not be used for in-context learning. We hypothesise that this may be due to superposition, whereby models represent more features than they have dimensionality, suggesting that methods like Sparse Autoencoders (SAEs) may be a promising future direction.

---


### 137. [STRIDE: Training Data Attribution via Sparse Recovery from Subset Perturbations](https://arxiv.org/abs/2606.05165)

**<font color=#1a73e8>作者：</font>** Rishit Dagli, Abir Harrasse, Luke Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Training Data Attribution (TDA) seeks to trace a model's predictions back to its training data. The gold standard for TDA relies on causal interventions, observing how a model changes when data is added or removed, but repeated retraining is computationally challenging for Large Language Models (LLMs). Consequently, most approaches approximate this effect in the parameter space using gradients. However, tracking gradients across billions of parameters is not only prohibitively expensive but relies on local approximations. In this work, we propose a shift: rather than estimating parameter changes, we model the functional effect of training data in the activation space. We introduce STRIDE (Steering-based Training Data Influence Decomposition), a framework that formulates TDA as a sparse recovery problem in the spirit of compressive sensing. STRIDE learns lightweight "steering operators" that mimic the behavioral shift caused by training on data subsets. By measuring how these operators perturb test predictions, we recover individual training example influences via sparse linear decomposition. STRIDE achieves state-of-the-art for LLM pre-training attribution while being an order of magnitude ($13\times$) faster than previous art. We further validate its practical utility through downstream applications including data selection, data contamination, and qualitative analysis.

---


> [!TIP]
> 当前位于：**101-137**（第 3/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-137**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
