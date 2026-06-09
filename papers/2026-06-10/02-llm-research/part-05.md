# 🧠 大模型相关研究 | 2026年06月10日

> 本类共 **331** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**201-250**（第 5/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-331](./part-07.md)

---

### 201. [Analyzing the Correlation Between Hallucinations and Knowledge Conflicts in Large Language Models](https://arxiv.org/abs/2606.08705)

**<font color=#1a73e8>作者：</font>** Lucrezia Laraspata, Giovanna Castellano, Gennaro Vessio  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Hallucinations -- factually incorrect or unverifiable outputs -- remain one of the most challenging limitations of Large Language Models (LLMs), especially in knowledge-intensive tasks. One proposed explanation is internal knowledge conflicts arising from fixed, outdated training data. This paper investigates whether internal representations linked to knowledge conflicts correlate with hallucination behaviors in LLMs.
Using probing techniques inspired by two prior works, we analyzed activations from hidden, attention, and MLP layers, as well as output logits, across predefined tasks. We probed LLaMA-3-8B on hallucination detection benchmarks and Falcon-7B on a knowledge conflict dataset. Our findings show that, although conceptually related, hallucination activation patterns cannot be fully reduced to or explained by knowledge conflict representations.
Nonetheless, probing proves a robust tool across multiple languages and activation types, supporting its role in improving LLM interpretability. This work advances the broader understanding of hallucinations in LLMs and underscores the value of fine-grained analysis of their internal behavior.

---


### 202. [PRPO: Perception-Reinforced Policy Optimization via Token-Level Dynamic Advantage Reshaping](https://arxiv.org/abs/2606.08708)

**<font color=#1a73e8>作者：</font>** Qiming Li, Tianlun Li, Xiaolong Cheng 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reinforcement Learning with Verifiable Rewards (RLVR) has become an effective paradigm for improving the reasoning capability of Large Vision-Language Models (LVLMs). However, existing RLVR methods primarily rely on trajectory-level outcome rewards, which assign identical learning signals across all generated tokens. This coarse-grained credit assignment is fundamentally mismatched to multimodal reasoning, where only a sparse subset of tokens is causally grounded in visual evidence. Consequently, these pivotal perceptual tokens receive weak supervision and are often overwhelmed by language priors or reasoning-template tokens. To address this limitation, we propose Perception-Reinforced Policy Optimization (PRPO), a token-level reinforcement learning framework that explicitly identifies and reinforces pivotal perceptual tokens within long-horizon multimodal reasoning trajectories. PRPO introduces Robust Visual Dependency (RVD), a principled metric that identifies tokens whose predictions are both visually grounded and perturbation-stable, filtering out brittle or noisy visual tokens. Based on RVD, we further propose Perceptual Advantage Reshaping (PAR), a token-level credit assignment technique that amplifies perceptually informative tokens while preserving stable gradients for non-perceptual tokens. Extensive experiments on seven multimodal reasoning benchmarks demonstrate that PRPO consistently outperforms strong LVLM baselines across both 3B and 7B model scales, achieving average gains of 23.3% and 21.1%, respectively. PRPO achieves state-of-the-art performance with improved training efficiency and stronger cross-task generalization. Our findings highlight the importance of fine-grained credit assignment for scalable multimodal reinforcement learning.

---


### 203. [Artificial Intelligence for Mathematical Reasoning: An Integrated Survey of Language Models, Neuro-symbolic Systems, and Verified Discovery](https://arxiv.org/abs/2606.08728)

**<font color=#1a73e8>作者：</font>** Syed Rifat Raiyan, Mohsinul Kabir, Hasan Mahmud 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Mathematical reasoning has long served as a stringent test of machine intelligence; over the past decade, it has moved from a niche problem within NLP to one of the most consequential AI frontiers. This survey provides a unified account of the field's evolution, from early rule-based math word problem (MWP) solvers and template-driven geometry systems, through neural expression generation and LLM prompting, to contemporary reasoning models, multi-agent systems, neuro-symbolic theorem provers, and verified discovery workflows. We organize the landscape along four axes: (i) informal reasoning over text and diagrams, spanning MWP solving, multimodal geometry, and VLMs; (ii) formal reasoning in proof assistants, including autoformalization, tactic prediction, compiler-guided repair, and proof search; (iii) mathematical discovery, where systems propose constructions, improve bounds, or assist attacks on open problems; and (iv) the inference and training-time techniques, including CoT prompting, tool use, process reward models, and RLVR, that increasingly connect generation with verification. We catalog major benchmarks across grade-school arithmetic, competition mathematics, geometry, formal proving, multimodal and multilingual reasoning, and expert evaluation, and we examine benchmark saturation, contamination, reporting mismatches, and the distinction between pass@1, majority voting, and verifier-assisted pass@$k$. We critically assess failure modes: brittleness under perturbation, reward hacking, multimodal grounding failures, fragile formalization, and the energy cost of reasoning-scale inference. Drawing on recent perspectives from working mathematicians, we identify future directions centered on verified-discovery workflows, reasoning efficiency, and infrastructure to make AI-assisted formalization broadly usable. Companion materials: this https URL.

---


### 204. [RadOT-Eval: Auditable Structured-Evidence Transport for Radiology Report Evaluation](https://arxiv.org/abs/2606.08769)

**<font color=#1a73e8>作者：</font>** Weixin Liu, Juming Xiong, Yang Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automatic evaluation is critical for high-stakes text generation, where errors often involve omitted findings, hallucinated content, polarity reversals, location changes, uncertainty mismatches, and temporal-comparison errors rather than low surface similarity alone. Radiology report generation provides a challenging test case because generated reports must preserve structured clinical evidence across sources. We present RadOT-Eval, an interpretable structured-evidence optimal transport framework for offline auditing of radiology report generation. RadOT-Eval decomposes reference and candidate reports into attribute-structured clinical evidence units, aligns corresponding evidence using entropy-regularized optimal transport, and uses clinically meaningful side-channel discrepancies in a monotone risk model to predict error burden. All transport, feature, and readout choices are selected using the ReXVal dataset, and the frozen system is evaluated on the independent RadEvalX dataset. RadOT-Eval achieves Spearman correlations of 0.715, 0.548, and 0.399 with total, clinically significant, and clinically insignificant annotated error burden, respectively, yielding higher point estimates than standard evaluation metrics and the open-source large language model (LLM)-based evaluator GREEN-radllama2-7B. In a frozen auxiliary corruption-sensitivity stress test on ReXErr-v1, RadOT-Eval achieves 0.768 AUROC and a 0.990 corrupted-greater-than-clean paired win rate. These results show that structured evidence transport provides an auditable, rank-oriented evaluation tool for high-stakes generated clinical text under ReXVal-only model selection and frozen RadEvalX testing.

---


### 205. [Reformulate LLM Reinforcement Learning for Efficient Training under Black-box Discrepancy](https://arxiv.org/abs/2606.08779)

**<font color=#1a73e8>作者：</font>** Jiashun Liu, Runze Liu, Xu Wan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement Learning (RL) has emerged as a pivotal post-training paradigm, yet it frequently suffers from unpredictable sub-optimum performance or even training collapses. Recent findings attribute these failures to a hidden train-inference discrepancy (or mismatch), stemming from the disparate underlying engines and architecture. We find that the training policy can actively self-correct such a discrepancy when provided with an appropriate learning signal. Then, we further empirically identify a discrepancy tolerance region: within this region, aggressively narrowing the discrepancy can suppress policy exploration and reduce learning efficiency, whereas outside this region, reducing excessive discrepancy improves optimization consistency and raises the achievable local performance ceiling. According to such findings, we formulate this problem as a Discrepancy-Constrained Markov Decision Process (DCMDP), where reward maximization is coupled with a constraint that aligns training-Inference behavior, achieving stable dual-objective optimization. To adaptively balance performance improvement and discrepancy control, we introduce a Lagrangian relaxation mechanism that dynamically adjusts the relative weight of the two objectives according to the current degree of discrepancy violation. This enables stable dual-objective optimization: the policy is allowed to explore freely within the tolerance region, while being guided back when the discrepancy exceeds the safe boundary. Empirically, DCMDP significantly improves the performance of 8B dense model (Qwen-3-8b) and 30B Mixture-of-Expert model (Qwen-3-30bA3b), and enables a heterogeneous training paradigm, where LLMs can be optimized in high-fidelity training setup while being explicitly aligned for low-cost, resource-constrained inference deployment.

---


### 206. [MaskAlign: Token-Subset Representation Alignment for Efficient Diffusion Training](https://arxiv.org/abs/2606.08788)

**<font color=#1a73e8>作者：</font>** Lianyu Pang, Tianlin Pan, Cheng Da 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Representation alignment with pretrained vision models has recently shown strong potential for accelerating diffusion transformer training. By aligning intermediate diffusion features with clean-image representations from self-supervised vision encoders, existing methods improve convergence and generation quality. However, such alignment also introduces a non-trivial constraint: diffusion models operate on noisy inputs whose usable information varies across timesteps, while the reference features are extracted from clean images. In this paper, we revisit this mismatch from a token-level perspective. We find that, under full-token representation alignment, tokens with large alignment-gradient norms exhibit a stable spatial preference, suggesting that the alignment objective does not affect all tokens uniformly and may encourage the model to rely on the complete set of clean-image tokens. To address this issue, we propose MaskAlign, a token-subset representation alignment method that applies alignment to randomly sampled token subsets during training. By exposing the model to different token subsets across iterations, MaskAlign reduces the dependence of representation alignment on the complete token set and encourages alignment behavior that is more stable under token-subset perturbations. To mitigate the information loss caused by directly dropping tokens, we further introduce a lightweight pre-mask token mixing block that shares information across tokens before masking.

---


### 207. [RAILS: Verification-Native Clearing For Agentic Commerce](https://arxiv.org/abs/2606.08790)

**<font color=#1a73e8>作者：</font>** Adrian de Valois-Franklin, Alex Bogdan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Autonomous agents negotiate, purchase, deploy code, and move funds, but no neutral mechanism determines whether they
met their delegated obligation, who is responsible when they did not, or which settlement action follows. This is the
agentic clearing problem. Tool protocols (MCP), inter-agent communication (A2A), payment rails (x402), mandate and
network agent protocols (AP2, Visa, Mastercard), and settlement-risk standards each assume that determination and none
produce it.
Clearing is the missing primitive. Payment is not clearing. Authorization is not clearing. LLM-as-judge evaluation is
not clearing. Settlement-risk escrow is not clearing: it consumes clearing decisions.
RAILS (Real-Time Agent Integrity & Ledger Settlement) is the integrity and clearing layer for agentic commerce,
spanning a per-output reliability score, a published reliability record, and a clearing function that consumes them.
The clearing protocol at its core closes that gap. Seven primitives (Obligation Object, Evidence Envelope,
Verification Mesh, Clearing Decision, Settlement Instruction, Clearing Passport, Finality Rules), bound by a formal
model of admissibility-graded verification, together yield a soundness property: no financially material settlement is
supported by evidence below the obligation's admissibility floor. The property is falsifiable against the spec. We
are not aware of a prior agent-commerce verification mechanism that states a property of this kind. The approaches
nearest to it emit a pass, a delivery guarantee, a bare score, or an equilibrium.
This paper specifies that clearing protocol.

---


### 208. [The Amplifying Mirror: Locating and Steering the Partisan Direction inside a Large Language Model](https://arxiv.org/abs/2606.08792)

**<font color=#1a73e8>作者：</font>** Wendy K. Tam  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models are rapicly replacing search engines as the primary interface between people and information. Unlike search engines, which retrieve existing content, LLMs generate novel text shaped by internal representations learned during training. Here we show that partisan political identity is encoded in the model's activation space, and that this direction directly shapes generation. Using 190,491 tweets from sitting members of the U.S. Congress as labeled training data, we train linear probes on the hidden states of the Llama 3.1 8B Instruct model. We identify a single geometric axis at layer 18 that separates Republican from Democratic text with an AUC of 0.945 and a Cohen's d of 1.94, and use sparse autoencoders to decompose that axis into interpretable partisan features. Causally intervening along this axis, ablating or amplifying the partisan component mid-generation, produces systematic shifts in the model's output. We witness stance reversals, register shifting, and structured fabrications of authority. Our results demonstrate that partisan bias in language models is not a vague emergent property but a learned geometric feature that can be precisely located and steered. Partisan bias is not a bug to be patched, but a structural property of how these models encode information about their users. As LLMs displace search engines as the interface to knowledge, understanding that product design (and its consequences) will be essential for navigating the legal, social, and political transitions from an information ecosystem that is curated to one that is generated.

---


### 209. [STAR: Rethinking MoE Routing as Structure-Aware Subspace Learning](https://arxiv.org/abs/2606.08814)

**<font color=#1a73e8>作者：</font>** Sumin Park, Noseong Park  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Mixture-of-Experts (MoE) scales model capacity efficiently by selectively routing inputs to a specialized subset of experts. However, input-expert specialization, the core motivation of MoE, critically depends on whether the router is actually aware of input structure. In practice, MoE routing is typically implemented as a shallow linear projection with limited awareness of input representation, which often leads to unstable routing. We propose STAR, a Structure Aware Routing that rethinks MoE routing as a subspace learning problem by augmenting standard learnable routing with an evolving principal subspace that tracks dominant input structure via Generalized Hebbian Algorithm (GHA). By aligning routing decisions directly with input structure, STAR enables stable expert specialization. We evaluate STAR on controlled synthetic setup and large-scale language and vision tasks, where it consistently improves routing quality and downstream performance over strong MoE baselines. Moreover, optional test-time subspace updates further enhance routing robustness and generalization under input distribution shifts.

---


### 210. [Knowledge Graphs and Reasoning LLMs for Finding Simple Yet Effective Transcriptomic Perturbation Predictors](https://arxiv.org/abs/2606.08816)

**<font color=#1a73e8>作者：</font>** Jake Fawkes, Liam Hodgson, Jason Hartford  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Predicting the effect of an unseen gene knockout perturbation on transcriptomic gene expression remains a highly challenging problem for virtual cell models. Recent progress has been made by leveraging biological knowledge graphs to provide a notion of similar perturbation, allowing for improved extrapolation beyond the set of training perturbations. In this work, we demonstrate that the simplest model to leverage these assumptions - a K-nearest neighbour from the knowledge graph - achieves highly competitive performance on this task, and that this can be improved further using LLMs optimised via reinforcement learning (RL) for predictive performance. Specifically, we find that the K-nearest neighbour approach beats almost all methods on out-of-distribution perturbation prediction, and when a reasoning LLM is trained via RL to make changes to the neighbourhood, it obtains equivalent performance to current state of the art methods on the cell lines from Replogle et al. (2022). We also demonstrate that the RL training improves the LLM's performance on the downstream task of differential expression prediction, despite not being trained on this directly. Overall, these findings demonstrate the efficacy of knowledge graphs as model priors, and show early signs that RL can refine LLMs into generalizable tools for predicting complex biological responses.

---


### 211. [Inference-Time Conformal Reasoning with Valid Factuality Control for Large Language Models](https://arxiv.org/abs/2606.08831)

**<font color=#1a73e8>作者：</font>** Ting Wang, Yuanjie Shi, Yan Yan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) increasingly perform multi-step reasoning, where intermediate claims form implicit directed acyclic graphs whose node correctness is structurally conditioned on their ancestors. This makes factuality uncertainty structural, rather than a trivial accumulation of node-wise errors, and necessitates inference-time uncertainty quantification over the reasoning structure. While conformal prediction (CP) offers flexible user-specified factuality control, existing work remains post-hoc and cannot intervene during generation. To fill the gap between CP's flexibility and its post-hoc limitation, we propose an \emph{Inference-Time Conformal Reasoning (ITCR)} framework that integrates CP directly into reasoning graph generation. ITCR learns a structure-level factuality uncertainty function that aggregates claim-level factuality signals over reasoning graphs without complex modeling assumptions. We then design the non-conformity score based on graph-level factuality uncertainty and calibrate the conformal threshold to decide when to stop generation. We theoretically show such generation is nested, yielding valid coverage guarantees for factuality control. Experiments over multiple datasets and coverage objectives demonstrate empirically valid coverage. In downstream reasoning tasks, inference-time calibrated graphs yield more accurate generation than post-hoc pruned graphs.

---


### 212. [Beyond Pass Rate: A Multilingual, Execution-Grounded Evaluation of Open Code LLMs](https://arxiv.org/abs/2606.08840)

**<font color=#1a73e8>作者：</font>** Sayed Erfan Arefin  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Code generation models are typically compared using compact execution benchmarks and aggregate pass rates, but such summaries obscure how performance varies across programming languages, problem families, and failure modes. We present a large-scale, execution-grounded evaluation of 9 openly accessible LLMs specialized for coding on 2,707 free LeetCode problems across 12 programming languages. Our corpus contains 325,343 problem-model-language jobs, each linked to prompt metadata, extracted code, LeetCode execution outcomes, and static-analysis signals. The results show that current open models remain far from the human acceptance reference: the best model, Yi-Coder-9B-Chat, reaches 23.64% mean correctness, compared with a 57.2% human acceptance baseline. Rankings are also slice-dependent: Qwen2.5-Coder-14B-Instruct is strongest on hard problems and distinct-problem coverage, while Gemma-2-27B-IT achieves the highest all-language lint pass rate. Failure analysis shows that compile errors account for 63.25% of non-accepted best submissions, indicating that many failures occur before semantic correctness can be tested. Static quality further diverges from functional correctness. Together, these findings show that multilingual, artifact-preserving evaluation reveals tradeoffs hidden by single-language or single-metric leaderboards.

---


### 213. [BLM-SGAN: Bidirectional Language Modeling for Semantic-Spatial Text-to-Image Generation](https://arxiv.org/abs/2606.08847)

**<font color=#1a73e8>作者：</font>** Ahmed Abdelmoneim Mazrou, Haidy Maher El-Amir, Ali Hamdi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite the success of image generation from text descriptions, it still faces challenges that are difficult to overcome in domains such as natural language processing (NLP) and computer vision (CV). Recent advancements in text-to-image (T2I) models, particularly those utilizing generative adversarial networks (GANs), have significantly improved the synthesis of realistic images across various domains. However, existing GAN-based T2I models still encounter key challenges, such as difficulty in capturing long-range dependencies, vanishing gradients, and the limitations of sequential processing. To address these issues, we introduce BLM-SGAN, a novel model that incorporates Bidirectional Language Modeling for Semantic-Spatial Text-to-Image Generation. BLM-SGAN leverages BERT's attention mechanisms to capture rich contextual information and efficiently manage extended sequences. Our model demonstrates state-of-the-art performance, with an Inception Score (IS) of 5.45 +/- 0.08, surpassing several competitive models such as SSA-GAN, DF-GAN, SD-GAN, and AttnGAN. BLM-SGAN effectively generates highly realistic images of birds from detailed text descriptions. The implementation code is available at: this https URL.

---


### 214. [Can the Environment Speak for Itself? $T^{2}$-GRPO: A Turn-Trajectory Group Relative Policy Optimization for Caregiver Agents](https://arxiv.org/abs/2606.08875)

**<font color=#1a73e8>作者：</font>** Yutong Song, Jiang Wu, Pengfei Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Optimizing large language models (LLMs) for long-horizon caregiver agents requires balancing delayed task objectives with immediate environment dynamics, such as patient distress and resistance. In dementia care, this balance is especially difficult: trajectory level rewards are too sparse for turn level credit assignment, while external LLM-based evaluators are costly and can misread fragmented or indirect patient responses. To address this issue, we propose \textbf{T}urn-\textbf{T}rajectory \textbf{G}roup \textbf{R}elative \textbf{P}olicy \textbf{O}ptimization (\textbf{T$^{2}$-GRPO}), a framework that decouples caregiver RL into two normalized reward horizons and enforces safety through a binary hard veto. $T^2$-GRPO derives dense turn-level rewards directly from environment state transitions, measuring changes in patient distress and resistance from a frozen dementia patient simulator. These environment-grounded rewards are combined with trajectory-level evaluations through independent centered-rank normalization, which preserves heterogeneous reward signals and mitigates reward collapse. Extensive experiments on dementia caregivers show that T $^{2}$-GRPO outperforms competitive baselines, indicating a substantial improvement for emotionally sensitive caregiver scenarios that effectively handles immediate patient feedback, long-term care outcomes, and safety constraints.

---


### 215. [Are Reasoning Vision-Language Models Robust to Semantic Visual Distractions?](https://arxiv.org/abs/2606.08894)

**<font color=#1a73e8>作者：</font>** Yizheng Sun, Mochuan Zhan, Yanan Ma 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reasoning Vision-Language Models (VLMs) achieve strong performance on complex multimodal tasks, but reliable real-world application requires handling visual inputs that are messier than clean, curated benchmarks. Existing works mainly evaluate such reliability of VLMs through input corruptions, such as noise, blur and weather effects, which make visual evidence harder to perceive. This leaves a critical reliability failure mode underexplored: a model may perceive the evidence correctly, yet reason from plausible but irrelevant and distracting evidence and propagate this mistake to its final answer. To address this gap, we introduce \textbf{Distract-Bench}, a benchmark for evaluating VLM robustness to \textbf{semantic visual distractions}, defined as meaningful but task-irrelevant visual cues added to inputs while preserving the ground-truth answer. We comprehensively evaluate eight leading open-source and two closed-source VLMs across conventional vision corruptions and Distract-Bench. Our results show that Distract-Bench exposes a robustness failure distinct from vision corruptions: reasoning VLMs largely track their non-reasoning base models under perceptual degradation, but show consistently lower robustness to semantic distractions. Further analysis shows that these distractions often enter the reasoning process of VLMs, are treated as evidence, and lead to incorrect answers. Together, these findings reframe robustness evaluation for reasoning VLMs, shifting the focus from degraded perception to distractions for reliable real-world visual reasoning. Our data and code are available at this https URL.

---


### 216. [FAME: Forecastability-Aware Mixture of Experts for Heterogeneous Time Series Forecasting](https://arxiv.org/abs/2606.08896)

**<font color=#1a73e8>作者：</font>** Qianyang Li, Xingjun Zhang, Shaoxun Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large-scale retail and industrial forecasting systems contain many heterogeneous time series whose lifecycle, sparsity, volatility, seasonality, spectral patterns, and contextual sensitivity differ substantially. A single forecasting model rarely performs well across all regimes, while dense ensembles increase inference cost and provide limited insight into expert suitability. This paper studies forecastability-aware expert routing: learning how data characteristics determine the suitability of forecasting experts. We propose \method{}, a sparse mixture-of-experts framework that represents each series with a multidimensional forecastability fingerprint, mines expert-suitability targets from validation performance, and trains a cost-aware sparse router to activate a small budgeted set of experts for each series. Using a production-scale vending-machine sales dataset from Shandong New Beiyang (SNBC), where the forecasting component has been integrated into the replenishment-planning pipeline, together with public retail benchmarks, we show that expert suitability varies systematically across data regimes. On the industrial dataset with 5,000+ machines and 60M+ transactions, \method{} Top-2 reduces MSE by 12.4\% over the strongest single expert, LightGBM, while executing 1.92 experts per series on average. The deployed component produces demand forecasts, while inventory-oriented gains are estimated by an offline replay simulator under a fixed replenishment policy rather than by online intervention. The framework turns heterogeneous sales forecasting from heuristic model selection into data mining of forecastability patterns and expert specialization. Code is available at this https URL

---


### 217. [Order Matters: Unveiling the Hidden Impact of Macro Placement Sequences via Proxy-Guided LLM Evolution](https://arxiv.org/abs/2606.08904)

**<font color=#1a73e8>作者：</font>** Shibing Mo, Jing Liu, Jianchu Xu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Macro placement is a fundamental step in modern chip physical design, playing a crucial role in determining the solution quality of high-dimensional combinatorial optimization problems. Despite recent advancements in machine learning for spatial coordinate determination, the temporal dimension of placement sequencing remains largely governed by static heuristics. In this work, we demonstrate that the placement sequence is not merely a preprocessing step but a decisive factor in optimization, where suboptimal early decisions trigger irreversible domino effects that constrain the solution space. To harness this unexplored dimension, we propose \textbf{OrderPlace}, a proxy-guided LLM evolution framework for automatically discovering macro placement order strategies. Instead of relying on manually crafted heuristics such as area- or connectivity-based ordering, OrderPlace explores a broader space of code-level policies, ranging from static scoring metrics to dynamic physics-inspired mechanisms. To mitigate the prohibitive cost of evaluating sequences, we introduce a lightweight proxy evaluation mechanism that efficiently filters candidates using a deterministic greedy probe. Experimental results on the standard ISPD 2005 benchmarks demonstrate that OrderPlace discovers novel ordering strategies. Compared with WireMask-EA and the state-of-the-art method EGPlace, OrderPlace reduces wirelength by 34.04\% and 14.08\%, respectively.

---


### 218. [DifferSeg: Towards Diverse Multimodal Binary Segmentation via Differential Perception and Frequency Guidance](https://arxiv.org/abs/2606.08906)

**<font color=#1a73e8>作者：</font>** Qiangqiang Zhou, Jiawei Xu, Yong Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In many binary segmentation tasks, most multimodal methods rely on fixed feature concatenation for cross-modal interaction and straightforward decoder designs dominated by low-frequency semantics. %ToDO: %
However, they ignore two key challenges: one is the lack of an adaptive mechanism to handle modality discrepancies and complementarity, and the other is the absence of an efficient decoding strategy to balance both high- and low-frequency representations. %
In this work, we propose a simple yet general multimodal binary segmentation framework, termed DifferSeg, to address both problems simultaneously. With the help of the differential perception fusion (DPF) module, DifferSeg employs learnable differential operators to adaptively align multimodal features and enhance their complementarity through residual fusion, effectively mitigating modality mismatch and fusion redundancy. %
In addition, we design a frequency-guided decoder (FGD) that builds cross-frequency interactions and multi-path upsampling to maintain consistency between detailed high-frequency structures and semantic low-frequency representations, ensuring fine-grained boundary recovery and noise suppression. %
Benefiting from these designs, DifferSeg can be easily generalized to diverse binary segmentation tasks, including both natural and medical modalities. Without bells and whistles, it consistently surpasses 67 state-of-the-art methods across 29 public datasets involving 18 downstream tasks, demonstrating superior generalization and segmentation this http URL and pretrained models will be available at the Link.

---


### 219. [Failure-Aware Refinement of Vision-Language Model for Lithography Defect Detection](https://arxiv.org/abs/2606.08908)

**<font color=#1a73e8>作者：</font>** Pangyun Jeong, Jiyeong Kong, Yuehua Hu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Semiconductor lithography inspection requires reliable detection of small pattern defects such as bridge, burr, pinch, and contamination. In this study, we propose a two-stage vision-language framework that combines initial defect detection with prediction refinement. In the first stage, Qwen3-VL is fine-tuned with LoRA as a vision-language adapter to predict defect counts, defect categories, and normalized bounding boxes from lithography images. However, direct fine-tuning may still produce common test-time errors, including false positives, missed defects, and incorrect defect types. To address this limitation, the second stage trains a refinement module using first-stage prediction failures and their corrected labels, allowing the model to review and revise initial outputs. By learning from cases where the initial adapter fails, the refinement process improves defect inference beyond single-stage fine-tuning.

---


### 220. [Vibe Visualizing: How Visualization Novices Try (and Fail) to Generate and Interpret Visualizations with Conversational AI](https://arxiv.org/abs/2606.08914)

**<font color=#1a73e8>作者：</font>** Sam Yu-Te Lee, Yun-Hsin Kuo, Chifang Chou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Conversational AI has enabled users to generate and interpret visualizations through natural language, significantly lowering the technical barrier to entry. The increased accessibility brings visualization novices into data visualization, but also exposes them to misinformation and misinterpretations. We are motivated to examine what issues can arise in interactions with current conversational AI, whether visualization novices can recognize such issues, and how they respond to them. To examine these questions, we conducted a user study on ChatGPT with 20 visualization novices, collecting their conversation logs, semi-structured interview transcripts, and Likert-scale questionnaire responses. Through thematic analysis, we developed a codebook that covers AI execution compliance, issues of AI-generated visualizations, patterns of AI responses, and prompting patterns of users. We summarized four themes, including the quality of outcomes, recurring errors from ChatGPT, misuse by users, factors that affect user trust, confidence, and verification behavior, and human-AI collaboration dynamics. To demonstrate the generalizability of our codebook and findings, we replayed the initial user prompts on Gemini and Claude and compared the outcomes, which revealed distinct failure modes for each model. Based on the results of all analyses, we derive a set of design recommendations for future AI-assisted visualization systems. We conclude with discussions on literacy gaps, diverse human-AI collaboration dynamics, and implications for agentic visualization.

---


### 221. [When Vision Misleads, Let Location Speak: A Worldwide Image Geo-Localization Method via Location Attention Mechanism and Large Multimodal Models](https://arxiv.org/abs/2606.08918)

**<font color=#1a73e8>作者：</font>** Junchao Cui, Wenqi Shi, Xuanzi Ma 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Worldwide image geo-localization aims to determine the capture location of an image on a global scale. Existing methods often mislocalize images by matching them to visually similar scenes from different geographic regions, which limits reliability in practical applications. To address this issue, we propose TransGeoCLIP, a novel retrieval-based framework that integrates a location attention mechanism and large multimodal models (LMMs). Using the Transformer encoder with location attention to encode GPS coordinates, TransGeoCLIP can effectively distinguish geographic features among visually similar images. The framework consists of two stages: 1) Retrieval database construction, which employs Transformers equipped with location attention mechanisms to encode labeled GPS coordinates and enhance location semantics, subsequently enables joint image-text-GPS embedding through CLIP; 2) Retrieval-augmented inference, which leverages LMMs to infer the final image location prediction from retrieved database results. Extensive experimental results on diverse datasets, including IM2GPS, IM2GPS3k, YFCC4k, and YFCC26k, demonstrate that TransGeoCLIP significantly enhances localization performance for visually similar images. Particularly, street-level localization accuracy (within 1 km error) is substantially improved, surpassing state-of-the-art methods by 1.5%, 1.07%, 7.18%, and 9.75% on these benchmarks, respectively.

---


### 222. [Multilingual Sentiment Aware Text Summarization A Reinforcement Learning Approach for Consistency Maintenance](https://arxiv.org/abs/2606.08940)

**<font color=#1a73e8>作者：</font>** Mikhail Krasitskii, Alexander Gelbukh, Olga Kolesnikova 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reinforcement Learning from Human Feedback (RLHF) has significantly improved the quality and fluency of large language models in text summarization. However, its impact on affective properties remains insufficiently understood. In this work, we study sentiment drift, a systematic shift toward neutral sentiment in RLHF-based summarization outputs compared to source texts. We conduct extensive experiments across multiple datasets, model architectures, and eight languages to analyze how alignment objectives influence sentiment preservation. Our results show that sentiment drift is a consistent phenomenon that becomes stronger with increased KL regularization strength, indicating a trade-off between alignment stability and affective fidelity. To explain this behavior, we introduce a Policy Attribution framework that decomposes the RLHF objective and quantifies the contribution of its components. Our analysis reveals that KL regularization is the primary driver of sentiment suppression across all settings. Based on these findings, we propose a sentiment-aware modification of the KL regularization term, which selectively reduces constraints on sentiment-bearing tokens. Empirical results demonstrate that this approach mitigates sentiment drift while maintaining summarization quality. Overall, our findings highlight a fundamental limitation of current alignment methods: while they improve factual consistency and safety, they may unintentionally suppress emotional expressiveness. This motivates the development of alignment strategies that explicitly account for affective preservation.

---


### 223. [From Hazard Functions to Language Space: Cox-Supervised Distillation of Survival Risk into a Large Language Model](https://arxiv.org/abs/2606.08945)

**<font color=#1a73e8>作者：</font>** Nicholas I-Hsien Kuo, Blanca Gallego, Louisa Jorm  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We investigate whether information about time-to-event risk estimated by a Cox proportional hazards model can be transferred into a generative large language model. We propose a text-based survival modelling pipeline in which structured clinical covariates are converted into text prompts and a Qwen-based large language model is fine-tuned to generate patient-specific survival risk using Cox model predictions as a training target. Across GBSG2, ACTG320, and WHAS500, the model achieves competitive held-out discrimination and calibration despite being trained as a text-generation task rather than with a conventional survival-analysis loss. We further analyse the geometry of the model's hidden states, where t-SNE visualisations reveal smooth risk gradients in latent space, suggesting that the model represents survival risk as a continuous structure rather than isolated risk categories. Together, these findings suggest that large language models can internalise survival-risk structure while supporting calibrated prediction, providing a route towards time-to-event reasoning in language models.

---


### 224. [NutriMLLM: Multimodal Large Language Models for Dietary Micronutrient Analysis](https://arxiv.org/abs/2606.08948)

**<font color=#1a73e8>作者：</font>** Runze Yan, Minxiao Wang, Jiaying Lu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Comprehensive estimation of dietary micronutrients from food images could improve clinical nutrition care, but training such models requires large multimodal datasets linking diverse foods to complete nutrient profiles. We first show that existing multimodal large language models (MLLMs), including leading proprietary models, are unreliable for this task. Across five model families and four independent evaluation benchmarks (ASA24, SNAPMe, FNDDS, and NutriBench), models frequently abstained or returned statistically implausible values. To address this gap without costly expert annotation, we repurposed a decade of population-scale 24-hour dietary recalls as structured prompts for text-to-image generation. This pipeline produced a synthetic corpus of about 1.1 million image-description-nutrient triplets, each pairing a generated food image with a complete 65-nutrient label. To our knowledge, this is the largest synthetic food-image corpus with comprehensive micronutrient annotation planned for public release upon publication. Fine-tuning Qwen3-VL (2B/4B/8B/30B) and GLM-4.6V-Flash on this corpus yielded NutriMLLM, the first family of vision-language models specialized for comprehensive dietary micronutrient estimation. We evaluate these models with a four-component framework that separately measures abstention, hallucination, overall usability, and per-nutrient numerical accuracy. On real food images, every NutriMLLM variant achieved near-complete coverage across all 65 nutrients, and the largest variant matched or exceeded proprietary baselines (GPT-5, Gemini 3, and Claude Sonnet 4.5) in accuracy on most nutrients. These results show that recall-driven synthetic supervision can make image-based comprehensive micronutrient estimation a tractable engineering problem and support dietary assessment, personalized nutrition guidance, and population-scale micronutrient surveillance.

---


### 225. [AlloSpatial: Agentic Harness Framework for Spatial Reasoning in Foundation Models](https://arxiv.org/abs/2606.08952)

**<font color=#1a73e8>作者：</font>** Shouwei Ruan, Bin Wang, Zhenyu Wu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal Foundation Models (MFMs) have made substantial progress, yet remain fragile in spatial reasoning over the physical world. A key bottleneck lies in their inability to transform local egocentric observations into a global allocentric spatial representation. To address this, we propose AlloSpatial, an agentic framework for allocentric spatial cognition in foundation models. AlloSpatial introduces World2Mind, a plug-and-play cognitive mapping sandbox that converts egocentric observations into structured allocentric priors, including Allocentric-Spatial Trees and route maps that support querying object topology, geometric relations, passability, and trajectories. To utilize these priors reliably under noisy reconstruction and ambiguous visual evidence, AlloSpatial introduces a Spatial Reasoning Harness for tool-use judgment, modality-decoupled cue collection, and geometry-semantic arbitration. We further internalize this process in Qwen3-VL through cold-start reinforcement learning with a harness-gated trajectory-level reward. Experiments on VSI-Bench and MindCube show that AlloSpatial improves proprietary models by 5%-18% in a training-free setting, while ASTs alone support strong spatial reasoning even when visual inputs are removed. The trained AlloSpatial agents further outperform larger general-purpose models and competitive spatial baselines, suggesting that structured allocentric representations, active tool use, and verifiable reasoning offer a promising route toward spatially capable foundation models.

---


### 226. [ChinaHeritaQA: A Culturally-Grounded Visual Question Answering Dataset for World Heritage Sites in China](https://arxiv.org/abs/2606.08959)

**<font color=#1a73e8>作者：</font>** Yi Zhang, Bolei Ma, Yong Cao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce ChinaHeritaQA, a multimodal benchmark dataset for evaluating the cultural reasoning abilities of vision-language models (VLMs) on UNESCO World Heritage sites in China. The dataset comprises 2,279 in-the-wild images paired with 14,133 bilingual (Chinese/English) multiple-choice QA pairs spanning seven cognitive dimensions, from basic identity recognition to historical periodization and architectural analysis. Guided by a UNESCO-aligned heritage ontology and verified through rigorous human annotation, the dataset ensures linguistic quality and factual consistency. Evaluations of state-of-the-art VLMs reveal that while top models exceed human performance on average, substantial task-level variation emerges: models excel at visual recognition but struggle with culturally grounded reasoning. Performance also varies by dynasty and region. ChinaHeritaQA reveals that strong visual retrieval does not extend to cultural and historical understanding. We release the dataset to support future research on culturally aware multimodal learning.

---


### 227. [CARE: A Conformal Safety Layer for Medical Summarization](https://arxiv.org/abs/2606.08969)

**<font color=#1a73e8>作者：</font>** Suhana Bedi, Bridget Lin, Anson Y. Zhou 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used for medical summarization, but their outputs can omit medically important information and introduce unsupported claims. Existing error-detection methods produce heuristic or uncalibrated scores, providing no formal control over missed errors and no principled way to trade off safety against clinician review burden. We introduce Conformal Assessment for Risk Evaluation (CARE), a post-hoc, model-agnostic safety layer that uses conformal risk control to overlay calibrated omission and hallucination flags onto summaries from any LLM without retraining. CARE provides finite-sample, distribution-free guarantees through two controllers: a hallucination controller that bounds the probability of a document containing any unflagged hallucinated sentence, and an omission controller that bounds the expected fraction of important omissions not surfaced for review. Unlike hallucination detection, omissions depend jointly on whether a source sentence is important and whether it is covered by the summary. We show that calibrating only one dimension can violate the target risk bound, while marginal decompositions remain valid but overly conservative. By jointly calibrating over the full $(\tau,\gamma)$ threshold space, CARE preserves formal guarantees while surfacing up to 5$\times$ fewer sentences than alternative calibrated baselines. Across five medical summarization tasks, CARE satisfies the target risk bound at $\alpha = 0.15$ with 95% confidence across 100 calibration/test resplits, using only ~100 labeled documents per domain. In a preliminary clinician study (75 document reviews), calibrated flags improved omission detection by 28.6 percentage points on average. These results show that sentence-level safety guarantees are feasible for LLM-assisted medical summarization and offer a tunable mechanism for balancing residual risk and review effort.

---


### 228. [An Effective Router for Vision-Language Model Selection](https://arxiv.org/abs/2606.08970)

**<font color=#1a73e8>作者：</font>** Can Wang, Shengwei Wang, Bolin Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) with varying performance and resource requirements are widely deployed, making it difficult for users to select the most appropriate one among numerous VLM candidates. Existing work reveals the performance paradox phenomenon in language models and focuses on routing methods to solve it. However, developing a router for VLM selection is still a critical yet challenging problem, which primarily faces: 1) lack of specialized data, 2) ineffective feature representation, and 3) rigid model space and costly adaptation. In this paper, we construct a multimodal dataset for VLM selection, containing the outputs of seven mainstream VLMs on 32,626 unique image-text queries. We then propose ARMS, a router for VLM selection. ARMS enhances input signals with VLM profiles, employs a simple but effective architecture to improve representations of queries and VLM capabilities. To improve ARMS' adaptation to new VLMs, we propose two extension training strategies: incremental training and independent training. Experimental results on both in-distribution and out-of-distribution test sets demonstrate the effectiveness of ARMS. In particular, using our training strategy, ARMs (only 800M in size) can adapt to a broader VLM space and defeat commercial models like GPT-4o that are hundreds of times larger in scale. Our code, models, and datasets are available in the anonymous repository.

---


### 229. [Diverse Thinking Schemata Elicit Better Reasoning in Large Language Models](https://arxiv.org/abs/2606.08974)

**<font color=#1a73e8>作者：</font>** Xinyue Liang, Yizhe Yang, Yu Bai 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large reasoning models (LRMs) have attracted increasing attention for their ability to solve complex mathematical problems by generating extended reasoning chains. In this work, we focus on two critical yet underexplored aspects of the reasoning process: reasoning transitions capturing the distinct transitions between reasoning steps and answer candidates reflecting the variety of solution paths produced by the model. We collectively define these two aspects as thinking schemata. We observe a correlation between the diversity of thinking schemata and model performance, which motivates us to enhance diversity as a means to further improve reasoning potential. To this end, we propose Diverse Schemata Policy Optimization (DiScO), a framework that first endows the model with schemata awareness, then encourages diversity through reinforcement learning, and further promotes diverse reasoning at inference time. Experiments on multiple mathematical reasoning benchmarks demonstrate that DiScO consistently outperforms standard group relative policy optimization. Beyond accuracy, human-annotated analyses show that DiScO substantially improves the model's ability to recover from erroneous initial attempts. Overall, our work suggests the important role that diversity of the thinking schemata plays and points to scaling along the diversity dimension as a promising research direction.

---


### 230. [RTL-BenchLS: A Large-Scale Benchmark for RTL Reasoning and Generation with Large Language Models](https://arxiv.org/abs/2606.08976)

**<font color=#1a73e8>作者：</font>** Jing Wang, Shang Liu, Wenji Fang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-based RTL generation and reasoning is a promising direction for hardware design automation. High-quality benchmarks are critical infrastructure for tracking progress in this direction. However, existing RTL benchmarks face inherent limitations in both scale and task scope. The designs they cover are typically small and simple, and the tasks focus almost entirely on specification-to-RTL generation. Frontier models' performance already saturates on the existing benchmarks. Scaling these benchmarks up is fundamentally difficult because aligned labels are required for benchmarking, such as specifications and testbenches. Such aligned high-quality data are rarely available for real-world designs. We introduce RTL-BenchLS, a large-scale benchmark addressing both limitations above. It contains over 10,000 formally verified Verilog designs, covering substantially larger and more complex designs than existing benchmarks. Beyond specification-to-RTL generation, we propose three novel tasks that jointly evaluate reasoning and generation: round-trip reasoning, masked-content reasoning, and repository-issue reasoning. The first two are self-supervised, which directly resolves the scaling bottleneck. All tasks are verified through formal equivalence checking without any manual testbenches. We evaluate eight LLMs on RTL-BenchLS. Even the best model reaches only 23% on natural-language round-trip reasoning, 28% on masked-content reasoning, and 12% on repository-issue fixing. RTL-BenchLS is substantially more challenging than existing benchmarks. It leaves ample room for future improvement and offers guidance for developing LLM-based methods for hardware design.

---


### 231. [Language-Aware Token Boosting: LLM Language Confusion Reduction Without Tuning](https://arxiv.org/abs/2606.08994)

**<font color=#1a73e8>作者：</font>** Trapoom Ukarapol, Pakhapoom Sarapat, Nut Chukamphaeng  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) sometimes exhibit language confusion when generating non-English text. Existing approaches typically rely on fine-tuning to mitigate this issue. In contrast, we propose a tuning-free paradigm for reducing language confusion. Within this paradigm, we introduce two methods: Language-Aware Token Boosting (LATB), which applies targeted perturbations to tokens associated with the desired language, and Adaptive Language-Aware Token Boosting (Adaptive-LATB), which dynamically adjusts these perturbations based on the model's confidence in the intended language. Experiments demonstrate that our methods effectively improve multilingual alignment by reducing language confusion, while maintain the summarization quality without requiring any additional fine-tuning. Our code is publicly available. this https URL.

---


### 232. [LATTEArena: An Evaluation Framework for LLM-powered Tabular Feature Engineering (Extended Version)](https://arxiv.org/abs/2606.09004)

**<font color=#1a73e8>作者：</font>** Ankai Hao, Ke Chen, Huan Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Feature engineering remains essential for tabular data analysis, and Large Language Models (LLMs) have emerged as a promising paradigm for automating this process, giving rise to LLM-powered AuTomated Tabular feature Engineering (LATTE). However, the absence of standardized platforms prevents fair, cost-aware comparisons. Furthermore, complex methodological designs obscure the specific contributions of individual components; for example, although LFG integrates Tree-of-Thought, few-shot demonstrations, Monte Carlo Tree Search, and natural language generation, the isolated impact of each technique's competitive edge remains unquantified. To address these challenges, we introduce LATTEArena, the first competitive evaluation framework featuring: (1) a six-dimensional taxonomy decomposing 15 representative methods into reusable components; (2) a standardized modular arena for controlled comparison; (3) multi-dimensional assessments covering performance, cost, and robustness; and (4) component-level ablation quantifying each technique's competitive edge. Through extensive evaluations, we reveal 16 key findings, including: (1) Tree-of-Thought with Monte Carlo Tree Search achieves optimal cost-effectiveness; (2) RPN and Code output formats dominate classification and regression tasks, respectively. We publicly release the modular framework and over 4000 execution logs, enabling researchers to seamlessly pit new techniques against existing ones and advance LATTE.

---


### 233. [Beyond Averages: Evaluating LLMs on Human Survey Replication at the Distributional Level](https://arxiv.org/abs/2606.09013)

**<font color=#1a73e8>作者：</font>** Jeonghyeon Moon, Jiwon Kim, Yeheum Lah 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLMs are increasingly used to simulate human survey responses, but prior work has mainly evaluated replication using mean-level or aggregate agreement, offering limited insight into whether LLMs reproduce the variability of human behavior. We evaluate LLM-based survey replication at the distributional level using a non-public 2010 consumer choice experiment on Korean instant noodle purchases, a setting unlikely to overlap with model training data. We evaluate three response variables of differing statistical type: binary purchase incidence, categorical brand choice, and count purchase quantity. For each, we compare human and LLM responses at mean-level, pattern, and distributional alignment, and against reference baselines from the human data alone. LLMs reproduce condition-level patterns reasonably well but fail to capture distributional structure: for purchase quantity, no model beats a condition-insensitive baseline that simply matches the pooled human distribution. Because models that match human means well can still produce distributions further from humans than this baseline, mean-based evaluation alone can be actively misleading. Replication also varies with input configuration, with structured personas and multimodal inputs improving alignment while explicit reasoning prompting degrades it monotonically.

---


### 234. [SafeRun: Enabling Determinism in LLM Planning for Running](https://arxiv.org/abs/2606.09027)

**<font color=#1a73e8>作者：</font>** Meilin Chen, Zepeng Zhai, Jiaxuan Zhao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models enable flexible natural-language planning but remain unreliable in determinism-critical domains due to their probabilistic nature. This limitation is especially problematic in running planning, where violating safety rules can lead to safety risks. We propose SafeRun, a framework for deterministic LLM-based planning via a decoupled architecture. SafeRun separates soft interpretation by an LLM from hard constraint enforcement by a deterministic solver, ensuring strict safety constraints while preserving natural-language flexibility. To validate SafeRun, we build a comprehensive benchmark for running planning under realistic physiological and safety constraints. Experiments across five LLMs show that SafeRun achieves 100\% safety score (vs.\ 79.1\% PE average and 97.6\% CodeAct average) while maintaining competitive instruction-following scores. The SafeRun benchmark is publicly available at \href{this https URL}{huggingface}.

---


### 235. [ATM: Action-Consistency Transfer Matrix for Diagnosing and Improving Latent World Models](https://arxiv.org/abs/2606.09028)

**<font color=#1a73e8>作者：</font>** Jiaheng Chen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Latent world models are increasingly used for control and goal-conditioned planning, yet assessing whether their learned representations are useful for planning usually requires slow, planner-coupled simulator evaluation with CEM or similar planners. Such evaluation is black-box and model-complexity-dependent: under the same protocol, different world models may require minutes to hours per checkpoint. In this work, we propose ATM, an Action-Consistency Transfer Matrix for diagnosing whether latent transitions preserve action semantics relevant to planning. ATM compares action information in real encoded transitions and model-predicted transitions through lightweight post-hoc probes, producing an interpretable matrix that reveals representation quality, transition-domain inconsistency, and failure modes without simulator rollout. It can also be collapsed into a simple screening score for within-task ranking across checkpoints, variants, and world models. When the true success gap is non-trivial, ATM achieves highly reliable pairwise ranking, while reducing minutes-to-hours CEM evaluation to seconds-level transition analysis, yielding more than 100x speedup in our setup. We further introduce AITS, showing that action-identifiability is not only diagnostic but also a useful training signal for improving downstream planning without changing the planner.

---


### 236. [TRIAGE: Dialectical Reasoning for Explainable Risk Prediction on Irregularly Sampled Medical Time Series with LLMs](https://arxiv.org/abs/2606.09030)

**<font color=#1a73e8>作者：</font>** Hyeongwon Jang, Gyouk Chu, Changhun Kim 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Clinical early warning systems built on electronic health records, in which clinical observations are recorded as irregularly sampled medical time series (ISMTS), must deliver both calibrated risk scores for patient triage and interpretable rationales that clinicians can verify. Large Language Models (LLMs) have been explored for this task, yet they collapse graded clinical risk into overconfident binary predictions. This risk polarization undermines both calibration and cross-patient comparability. To address this, we propose TRIAGE, a framework that trains an LLM to generate dialectical reasoning over competing clinical outcomes by eliciting outcome-specific rationales. This dialectical formulation mitigates risk polarization, enabling a single LLM to yield continuous risk scores grounded in explicit clinical reasoning. Evaluated on three ISMTS benchmarks, TRIAGE achieves an average AUPRC improvement of 3.3% and reduces calibration error by 81% compared to the competitive baselines. An LLM-as-a-judge assessment further shows that our rationales surpass post-hoc explanations from the baseline by 20% in clinical reasoning quality. The source code is available at this https URL .

---


### 237. [Bridging the Agent-World Gap: Text World Models for LLM-based Agents](https://arxiv.org/abs/2606.09032)

**<font color=#1a73e8>作者：</font>** Yixia Li, Hongru Wang, Peng Lai 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM)-based agents are increasingly used in interactive textual environments, from web navigation and code editing to tool use and long-horizon dialogue. Yet many remain largely reactive, mapping observations to actions without an explicit model of how these environments are structured and evolve. This motivates text world models (TWMs): transition models over textual states that, given a state and a candidate action, predict the resulting webpage, terminal output, API response, or user reply, thereby supporting planning, efficient learning, and principled evaluation. We systematically review text world models for LLM-based agents, organized around a formal framework and the agent lifecycle: (1) Foundations, defining text world models and characterizing them by state representation and grounding domain; (2) Construction, taxonomizing LLM-as-WM and code-as-WM paradigms and reviewing methods for building them; (3) Application, examining how world models support agents at training time through experience synthesis and at inference time through planning, verification, and adaptation; and (4) Evaluation, covering both evaluation of the world model itself and its use as an evaluation environment for agents. We aim to consolidate this rapidly developing area, clarify its design space, and highlight open challenges for future research.

---


### 238. [CRANE: Knowledge Editing for Reasoning MLLMs](https://arxiv.org/abs/2606.09033)

**<font color=#1a73e8>作者：</font>** Han Huang, Hao Wang, Mengqi Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The emergence of reasoning multimodal large language models (MLLMs), which generate explicit chain-of-thought (CoT) reasoning before producing answers, has introduced a new challenge for knowledge editing: methods that appear successful under traditional metrics (teacher-forcing accuracy up to 100%) can fail severely when the model's reasoning process is examined (Grounded Success as low as 0%). We identify three failure modes: (1) Structural Collapse, where weight-modifying methods destroy the CoT format; (2) Cognitive Dissonance, where the model's reasoning chain actively rejects the injected edit fact based on visual evidence; and (3) Shallow Internalization, where methods succeed on exact queries but fail on rephrase or multi-hop variants. On reasoning MLLMs, these modes interact: methods that generalize (FT, LoRA) trigger format collapse, while methods without deep modification cannot generalize. To expose these failures, we propose a CoT-aware evaluation protocol and construct ReasonEdit-Bench, with conflict stratification, multi-level probes, and multi-hop portability tests.
We propose CRANE, a retrieval-augmented framework that requires no per-edit parameter modification. CRANE combines a modality-aware dual-library retrieval system with a two-phase training strategy: Supervised Fine-Tuning (SFT) for structural initialization, followed by GRPO with a Cognitive Routing Reward that trains the model to arbitrate between visual priors and injected edit facts. On ReasonEdit-Bench, CRANE achieves 96.9% Grounded Success on conflict scenarios and 96.9% intermediate entity usage in multi-hop chains, with 97.6% text-locality and 68.1% image-locality Edit Independence. On the out-of-distribution MMEVOKE benchmark, CRANE reaches 87.0% under gold retrieval.

---


### 239. [Leveraging NeRF-Rendered Images for 3D Gaussian Splatting](https://arxiv.org/abs/2606.09034)

**<font color=#1a73e8>作者：</font>** Mizuki Morikawa, Yuta Shimizu, Chunyu Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Neural radiance field (NeRF) and 3D Gaussian splatting (3DGS) are two mainstream approaches for novel view synthesis. They often show complementary performance, i.e., 3DGS demonstrating faster rendering speed and NeRF demonstrating higher rendering quality. Motivated by this, we propose leveraging NeRF-rendered images for 3DGS. Specifically, we target street scenes and utilize a pre-trained street-specific NeRF method to produce training images for a target 3DGS method. In our 3DGS training, NeRF-rendered images are used to remove transient objects in street-level input views and to generate bird's-eye views as additional views, inheriting the higher-quality rendering of NeRF into 3DGS. We further incorporate a diffusion-based image enhancement to improve the image quality of the additional views. Experimental results on one synthetic and two real datasets demonstrate that our proposed method improves street-scene rendering while preserving the speed of 3DGS and the quality of NeRF.

---


### 240. [Personalization Meets Safety:Mechanisms,Risks,and Mitigations in Personalized LLMs](https://arxiv.org/abs/2606.09038)

**<font color=#1a73e8>作者：</font>** Yanyan Luo, Xue Han, Ruiqiao Bai 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have enabled increasingly personalized interactions by adapting to users' preferences, contexts, and long-term histories. However, the mechanisms that enable personalization also expand the safety landscape in ways not systematically addressed by existing literature. Existing reviews typically focus either on personalization or safety, leaving their intersection largely unexplored. We present the first comprehensive, safety-aware review of personalized LLMs. We organize personalization along three dimensions-user representation, personalization paradigm, and evaluation-and introduce a unified taxonomy of safety risks. At the representation level, we analyze risks arising from diverse user representations. Across mainstream personalization paradigms, we delineate vulnerabilities inherent to prompting, retrieval augmentation, parameter fine-tuning, reinforcement learning, Mixture-of-Experts (MoE), pruning, agent frameworks, and multimodal personalization, and synthesize mitigation strategies across the model lifecycle. Beyond these fine-grained risks, we characterize paradigm-agnostic safety risks arising from personalized adaptation. We further summarize personalized datasets and evaluation methodologies. Through a case study of OpenClaw, we analyze deployment trends in personalized agent ecosystems. Our analysis reveals three structural inadequacies in existing research: safety is evaluated as user-invariant rather than relational, personalization techniques are analyzed in isolation rather than in composition, and evaluation frameworks cannot capture emergent long-term risks. By jointly examining personalized representations, personalization paradigms, safety risks, defenses, and evaluation methods, we provide a unified framework for developing safe personalized LLMs and highlight key directions for future research.

---


### 241. [Agent Economics: An Entropy-Controlled Pluralistic Alignment Framework for Preventing Artificial Hivemind in Autonomous Agents](https://arxiv.org/abs/2606.09039)

**<font color=#1a73e8>作者：</font>** Cheonsu Jeong  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This study proposes the Behavioral Protocol Framework (BPF), an entropy-controlled pluralistic alignment framework designed to address two critical challenges in autonomous agent economies: the hivemind effect arising from excessive strategic convergence among agents and the lack of transparency in autonomous decision-making processes. The proposed BPF consists of three core modules: Mentalizing-based Social Intelligence (MbSI) grounded in Theory of Mind (ToM), Pluralistic Alignment (PA), and a Verifiable Execution Kernel (VEK). These modules are organically integrated within a closed-loop architecture that governs the entire lifecycle of agent behavior, from decision-making and execution to verification and feedback. To evaluate the proposed framework, a simulation environment implemented in Python and a Streamlit-based user interface will be developed. Through empirical experimentation, the study aims to examine whether the entropy-control mechanism of the PA module can effectively preserve strategic diversity among agents and mitigate collective convergence, while the VEK module provides a comprehensive and transparent audit trail of the decision-making process. The anticipated results are expected to demonstrate that the proposed framework can simultaneously enhance the stability, efficiency, and trustworthiness of autonomous agent economies. Consequently, this research offers a practical approach for developing robust, transparent, and accountable agent-native economic systems.

---


### 242. [Decoy-Calibrated Failure Audits for Language Models](https://arxiv.org/abs/2606.09046)

**<font color=#1a73e8>作者：</font>** Vyzantinos Repantis, Ameya Gawde, Harshvardhan Singh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Useful audits reveal not only how often a model fails, but also where its failures concentrate. An auditor may test many candidate explanations: long inputs, indirect questions, distracting evidence, or combinations of these factors. The risk is selection. The largest observed effect may reflect a real failure mode, or it may simply be the best result among many tried. We introduce Janus, a procedure for deciding when a proposed error explanation is credible enough to report. The goal is not to generate new explanations, but to decide which ones hold up. The auditor starts with a fixed model, a labeled evaluation set, and a frozen list of candidate explanations, which we call descriptors. Janus scores each descriptor by its error-rate lift, then compares real descriptors with fake ones that have the same frequencies but are randomly assigned to examples. A descriptor is confirmed only if it beats this decoy floor on the data used for discovery and then repeats on separate held-out data. In a controlled audit of multi-table lookup tasks, Janus identifies the planted failure, confirming long-chain descriptors and their interactions. The LLM often stops partway through the lookup chain instead of reaching the final answer. On two public benchmarks, MuSiQue and LongBench v2, the SliceLine baseline flags plausible high-error pockets, but Janus confirms none of them. Ablations show why both safeguards matter. On LongBench v2, an uncalibrated fixed threshold reports 20 descriptors, the decoy floor leaves one, and the holdout check rejects the last one after its lift shrinks from 0.36 to 0.05. The resulting principle separates proposing explanations from reporting them. Candidates may come from any source, but only those that beat decoys and replicate on fresh data become audit findings.

---


### 243. [Stage-1 Controls the Entropy Regime, Not the Outcome](https://arxiv.org/abs/2606.09059)

**<font color=#1a73e8>作者：</font>** Jianxiong Shen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Two-stage post-training -- a Stage-1 warm-start (supervised fine-tuning, SFT, or on-policy distillation, OPD) followed by Stage-2 reinforcement learning (RL) -- is increasingly used for vision-language models (VLMs). We ask what Stage-1 actually controls in a small-data study using Qwen2.5-VL-7B with a same-modality 72B VLM teacher for OPD. First, the three warm-starts reach a narrow $53$--$54\%$ band on Geometry3K internal validation, consistent with the narrow range reported by recent specialized methods; this setup provides little evidence that Stage-1 changes the in-domain endpoint. Second, a matched-recipe, early-stopped SFT improves out-of-domain MathVista by $+2.1$ points, reversing the $-9.5$-point drop of an over-trained variant. The clearest difference is the \emph{entropy regime}: OPD enters RL with substantially higher policy entropy than either SFT initialization, and the separation remains visible through the available trajectories. At the in-domain initialization, OPD also has higher answer diversity and pass@16 ($+2.0$ to $+5.2$ points over SFT), although problem-level bootstrap intervals show that the smaller contrast is uncertain. The advantage is absent after RL (endpoint pass@16 values within $1.1$ points) and on MathVista (six models within $1.2$ points). Our contribution is therefore a bounded empirical characterization: Stage-1 is strongly associated with the entropy regime in this setup, but the downstream payoff is small, localized, and not evidence that OPD is a better RL warm-start.

---


### 244. [Emergent Misalignment Can Be Induced by Sycophancy and Reversed via Alignment Gating](https://arxiv.org/abs/2606.09068)

**<font color=#1a73e8>作者：</font>** Sicheng Wang, Xiangyang Zhu, Han Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Prior work has shown that fine-tuning large language models on malicious or incorrect outputs in narrow domains can induce broad misalignment and harmful behavior, a phenomenon known as emergent misalignment. However, efficient methods for reversing such misalignment remain limited. In this work, we make two contributions. First, we identify sycophancy fine-tuning, i.e., training models to passively agree with users' incorrect opinions, as a previously underexplored driver of emergent misalignment, and show that it induces broad and severe misaligned behavior. Second, we propose Alignment Gating, an efficient method for reversing emergent misalignment that inserts learnable and controllable gates into the model during fine-tuning. Through fine-tuning, these gates learn to identify the internal representations responsible for unsafe responses. Thus, amplifying or suppressing these representations then exacerbates or mitigates EM, respectively. We further find that alignment gating module exhibits strong generalization: gating weights obtained from narrow-domain fine-tuning substantially suppress broad-domain misaligned behavior while preserving the model's general capabilities.

---


### 245. [REFLECT: Intervention-Supported Error Attribution for Silent Failures in LLM Agent Traces](https://arxiv.org/abs/2606.09071)

**<font color=#1a73e8>作者：</font>** Xiaofeng Lin, Yingxu Wang, Tung Sum Thomas Kwok 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents now solve complex tasks through long plan-and-execution traces, yet the ability to locate errors in a completed traces still lags far behind, especially in the \emph{silent failure} regime. Existing approaches predict suspect steps via classifiers or LLM judges, or recover correct answers via retry, but none feed the intervention outcome back to \emph{refine the attribution itself}. We propose \methodname, a method that closes this gap by diagnosing a candidate error step, testing it through controlled replay with a diagnosis-specific patch, and using the verified outcome flip as contrastive evidence to refine the final attribution. Across four localization benchmarks spanning multi-hop reasoning across domains, \methodname achieves the highest localization accuracy among same-auditor methods across all four benchmarks, with the largest gains on structured tool-use traces, while providing actionable localization even when ground-truth answers are unavailable.

---


### 246. [A Unifying Lens on Reward Uncertainty in RLHF](https://arxiv.org/abs/2606.09073)

**<font color=#1a73e8>作者：</font>** Ely Hahami, Yoel Zimmermann, Ray Zhou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning from human feedback (RLHF) is bottlenecked by \emph{reward hacking}, where the policy exploits errors in a proxy reward model (RM) and produces high RM scores without genuine quality gains. A natural mitigation is \emph{pessimism}: penalizing rewards in regions where the RM is uncertain. However, standard scalar RMs provide no principled notion of uncertainty. We argue that the right object is a \emph{distributional} reward model $p(r\mid x,y)$. Under either a Bayesian inference or a KL-distributionally robust optimization (KL-DRO) lens, the KL-regularized RLHF objective admits a closed-form effective reward $\tilde r(x,y) = \pm\beta\log\mathbb{E}_p[e^{\pm r/\beta}]$. The pessimistic branch unifies the prior heuristics for RM ensemble aggregation: mean aggregation, worst-case optimization (WCO), and uncertainty-weighted optimization (UWO) all emerge as limits or truncations of this single expression. This also clarifies the implicit assumptions of each existing rule.

---


### 247. [FlashMemory-DeepSeek-V4: Lightning Index Ultra-Long Context via Lookahead Sparse Attention](https://arxiv.org/abs/2606.09079)

**<font color=#1a73e8>作者：</font>** Yan Wang, Qifan Zhang, Jiachen Yu 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Conventional LLMs keep the full KV cache loaded during decoding, causing a severe GPU memory bottleneck for ultra-long context serving. In this report, we propose Lookahead Sparse Attention (LSA), a novel inference paradigm powered by a Neural Memory Indexer built upon the DeepSeek-V4 architecture. Rather than passively attending to all historical tokens, LSA proactively predicts future context demands and preserves only the query-critical KV chunks in the GPU memory. Crucially, we instantiate this architecture via a backbone-free decoupled training strategy. By formulating the indexer as a standard dual-encoder architecture, we train it independently using standard retrieval training frameworks without ever loading the massive backbone model into GPU memory.
We demonstrate that this "less is more" paradigm significantly maximizes serving efficiency while acting as an effective attention denoiser in tasks that rely on long-term global memory. Across primary long-context evaluation suites (e.g., LongBench-v2, LongMemEval, and RULER), FM-DS-V4 compresses the average physical KV cache footprint down to merely 13.5% of the full-context baseline, while consistently preserving or slightly elevating downstream accuracy (+0.6% absolute margin on average). Crucially, at extreme 500K scales, FlashMemory suppresses the physical KV cache overhead by over 90% without destabilizing the backbone's core reasoning capacities.

---


### 248. [Beyond FLOPs: Benchmarking Real Inference Acceleration of LLM Pruning under a GEMM-Centric Taxonomy](https://arxiv.org/abs/2606.09080)

**<font color=#1a73e8>作者：</font>** Haozhe Hu, Hao Wu, Anhao Zhao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Pruning has emerged as a dominant paradigm for accelerating large language model (LLM) inference, spanning a broad spectrum of methods that remove computation across tokens, layers, heads, dimensions, and attention patterns. Despite sharing the same objective, these pruning approaches induce fundamentally different execution behaviors, causing realized speedups to depend heavily on hardware and kernel implementations. Consequently, the practical acceleration benefits of different pruning families remain poorly understood. In this work, we introduce a GEMM-centric taxonomy that reorganizes existing pruning methods according to the logical \textbf{M}, \textbf{N}, and \textbf{K} dimensions of general matrix multiplication (GEMM). Leveraging this abstraction, we build a unified benchmarking framework that enables implementation-consistent comparison across the pruning design space and systematically characterizes the acceleration--quality Pareto frontier. Our results show that static depth pruning remains the strongest Pareto-optimal baseline and stays closest to its theoretical acceleration upper bound in memory-bounded scenarios. During prefill, the frontier transitions from static depth at low quality loss (0\%--4\%), to dynamic depth at moderate loss (5\%--16\%), and finally to static width pruning at higher loss levels (17\%--26\%). These findings establish the first unified view of the practical limits of pruning-based LLM acceleration and provide guidance for future pruning research.\footnote{Code is available at this https URL}

---


### 249. [Stabilizing On-Policy Distillation for MLLM Reasoning with Global Normalization](https://arxiv.org/abs/2606.09091)

**<font color=#1a73e8>作者：</font>** Dongze Hao, Zhiwei Jin, Chen Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) has recently emerged as an important post-training paradigm. By using a stronger teacher model to provide dense, fine-grained supervision for sampled trajectories, OPD offers a clear advantage over reinforcement learning with verifiable rewards (RLVR), which typically depends on sparse binary or outcome-based environmental feedback. However, naive token-level distillation can suffer from gradient instability, due to magnitude misalignment in outlier states. To address this issue, we propose Globally Normalized Distillation Policy Optimization (GNDPO), a practical method that stabilizes optimization by transforming raw KL scores into batch-level relative advantages. This normalization effectively mitigates gradient explosions while retaining the benefits of token-level guidance. Experimental results show that GNDPO substantially improves training robustness and downstream performance across multimodal reasoning tasks. The code is released at this https URL.

---


### 250. [From Shortcuts to Reasoning: Robust Post-Training of Theory of Mind with Reinforcement Learning](https://arxiv.org/abs/2606.09092)

**<font color=#1a73e8>作者：</font>** Jike Zhong, Yuxiang Lai, Ming Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Theory of Mind (ToM) is a must-acquire skill for modern foundation model systems to operate effectively and safely in the real world. Recent works have explored honing ToM via post-training; however, we show that such progress is confounded by a pervasive "shortcut" issue: tasks can reach up to 99% accuracy by simply exploiting spurious causal correlations, leading to a false sense of ToM. Motivated by this, we first develop a framework to systematically examine ToM datasets for shortcuts and provide guidance for future development. We find that questions reducible to pure state tracking, such as "belief," are especially shortcut-prone compared to mind questions, such as "intention," where reasoning beyond tracking is required. Using four shortcut-free datasets across three ToM contexts, we then comprehensively study whether Reinforcement Fine-Tuning with verifiable rewards and explicit reasoning chains, called Thinking-RFT, elevates ToM beyond Supervised Fine-Tuning, or SFT. Our key findings are as follows. First, Thinking-RFT effectively improves ToM in all scenarios, with a 6% improvement over SFT, particularly in complex higher-order reasoning, with a 10% improvement over SFT, and multimodal cases, with a 7% improvement over SFT. It also generalizes notably better to unseen domains and higher-order queries while being more robust to counterfactuals. Second, ToM benefits specifically from the joint effect of reasoning and RL: Thinking-RFT outperforms Non-Thinking-RFT by 7% on average. Third, RFT works by learning to ground its reasoning on anchor cues, such as keywords and state changes, that correspond to causal factors. We believe our study is useful for developing effective and robust ToM post-training datasets and advancing critical ToM capabilities.

---


> [!TIP]
> 当前位于：**201-250**（第 5/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-331](./part-07.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
