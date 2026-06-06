# 📦 其他研究 | 2026年06月07日

> 本类共 **289** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**1-50**（第 1/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-289](./part-06.md)

---

### 1. [RAINO: Anchoring Agents in Reality, A Systematic Review and Conceptual Framework for Realism in Agent-Based Modelling](https://arxiv.org/abs/2606.05167)

**<font color=#1a73e8>作者：</font>** Loïs Vanhée, Melania Borit  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Realism is a central yet seemingly under-theorized concept in Agent-Based Modelling. This paper presents a Systematic Literature Review, aiming to identify how realism is currently operationalized and demonstrated. The results show that realism is often poorly defined and lacks a consistent conceptual framework. A wide variety of methods are used to achieve and demonstrate realism, but explanations of whether and why these methods are appropriate for their intended purposes are generally limited. Building on this review, we introduce the Reality Anchor, Input, Output (RAINO) framework. RAINO identifies the key structures used to argue for realism in Agent-Based Models, consisting of Reality Anchors (e.g., empirical data, formal theory, expert knowledge, common-sense expectations) and their application as model Input or Output. RAINO broadens existing perspectives on how realism is framed. It explains why different assessors may evaluate the realism of a model in different ways, and it shows how this broader framing can lead to significantly different approaches to model development.

---


### 2. [Epidemiology of Model Collapse: Modeling Synthetic Data Contamination via Bilayer SIR Dynamics](https://arxiv.org/abs/2606.05168)

**<font color=#1a73e8>作者：</font>** Xiangyu Wang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Training on synthetic data causes model collapse, but existing analyses treat this as single-chain degradation. In reality, the AI ecosystem involves cross-contamination: models ingest synthetic data from other models, produce new synthetic text, and contaminate shared corpora. We propose a bilayer coupled SIR/SIRS framework -- a phenomenological mean-field model treating data corpora and AI models as two interacting populations, each with susceptible, infected, and recovered compartments linked by cross-layer transmission. The SIRS variant (our primary recommendation) incorporates immunity waning, reflecting that filtered corpora and retrained models remain susceptible to re-contamination. We derive the basic reproduction number $R_0 = \sqrt{\beta_D \beta_M / [(\gamma_D+\mu_D)(\gamma_M+\mu_M)]}$ via the Next Generation Matrix and apply standard epidemic threshold results to the bilayer system. Illustrative scenario-based calibration from public AI text prevalence data yields supercritical dynamics ($R_0 > 1$) across three scenarios; Sobol sensitivity analysis identifies synthetic-text detection as the highest-leverage parameter. A bipartite-network agent-based model confirms mean-field consistency ($R^2 > 0.96$) for dense networks but degrades under heterogeneity. GPT-2 contamination chain experiments (192 runs across WikiText and Shakespeare) show dose-response degradation and diversity loss qualitatively consistent with the threshold picture. Matched-budget source-diversity experiments (1,088 runs) provide suggestive evidence that multi-source mixing modestly attenuates collapse, but the effect vanishes at lower contamination fractions. Intervention analysis identifies detection-based filtering and herd immunity as the highest-leverage strategies.

---


### 3. [AppAgent-Claw: CLI Is All You Need for GUI Automation](https://arxiv.org/abs/2606.05171)

**<font color=#1a73e8>作者：</font>** Zhixue Song, Zhiheng Zhang, Yi Song 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The OpenClaw platform provides a practical foundation for automation through its skill-oriented architecture, organizing external capabilities into lightweight, reusable components that can be invoked efficiently through a command-line interface (CLI). However, a significant bottleneck remains: many real-world tasks are confined to graphical user interfaces (GUIs) with no stable API available. While LLM-based GUI agents offer generality, their reliance on repeated live model inference makes them too slow, costly, and inconsistent to serve as efficient OpenClaw skills. In this paper, we present AppAgent-Claw, a demonstration-driven system that converts GUI workflows into reliable, reusable skills without runtime inference. By following a ``record-once, replay-many'' paradigm, the system captures rich contextual metadata to facilitate robust execution. It employs a layered localization strategy to handle visual shifts and a validation-coupled execution model to ensure intended on-screen effects. AppAgent-Claw provides a practical, efficient, and diagnosable solution for integrating GUI-bound tasks into the OpenClaw ecosystem.

---


### 4. [Is This Edit Correct? A Multi-Dimensional Benchmark for Reasoning-Aware Image Editing](https://arxiv.org/abs/2606.05172)

**<font color=#1a73e8>作者：</font>** Yixuan Ding, Wei Huang, Ruijie Quan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Diffusion-based image editing has achieved strong visual fidelity under natural language instructions, yet most existing systems still operate at the level of surface instruction following, without reasoning about the implicit contextual constraints embedded in real user requests. This often leads to visually plausible but logically inconsistent edits. In this work, we introduce RE-Edit, a benchmark for REasoning-aware image Editing that evaluates image editing systems across five complementary reasoning dimensions: physical, environmental, cultural, causal, and referential. RE-Edit comprises 1,000 carefully curated samples, each designed such that visual plausibility alone is insufficient and correct editing requires satisfying implicit logical constraints. To support fine-grained analysis, we establish dimension-aligned evaluation criteria and conduct a comprehensive study of ten open-source and two commercial image editing models. Our results show that even advanced systems frequently struggle with implicit multi-dimensional reasoning despite producing high-quality visuals. We further present a lightweight reasoning-guided post-edit baseline as an initial exploration, illustrating how inserting explicit reasoning can help mitigate such failures in a model-agnostic manner.

---


### 5. [Predict and Reconstruct: Joint Objectives for Self-Supervised Language Representation Learning](https://arxiv.org/abs/2606.05173)

**<font color=#1a73e8>作者：</font>** Aimen Boukhari  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Masked language modelling (MLM) has been the dominant pre-training objective for text encoders since BERT, yet it encourages representations that are strongly anchored to surface-form token identity rather than deeper semantic structure. Inspired by the success of Joint Embedding Predictive Architectures (JEPA) (LeCun, 2022) in vision and audio, we propose a hybrid pre-training objective that combines a JEPA-style latent-space prediction loss with a standard MLM objective over a single shared encoder. A learnable scalar parameter continuously balances the two objectives during training. We pre-train both a hybrid model and a pure-MLM baseline on English Wikipedia using identical architectures and compute budgets (NVIDIA H100). Extensive representation analysis across five GLUE benchmarks (SST-2, MRPC, MNLI, CoLA, STS-B) using four pooling strategies reveals that the hybrid encoder produces significantly more uniform embeddings (uniformity less than -0.16 vs -0.05 for MLM), exhibits richer spectral geometry under max pooling, encodes less surface-level lexical information, and achieves a better semantic-to-lexical balance. Despite similar linear-probe downstream accuracy, the geometric differences are consistent and significant, suggesting that the JEPA predictive objective reshapes the latent space in ways that standard accuracy metrics alone cannot capture.

---


### 6. [Generic Triple-Latent Compression with Gated Associative Retrieval](https://arxiv.org/abs/2606.05175)

**<font color=#1a73e8>作者：</font>** Liu Xiao  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We study generic triple-latent sequence models that maintain a running token state and compressed pair-memory pathway to capture higher-order token interactions without benchmark-specific parsing. The triple-latent family improves a small Transformer baseline on byte-level WikiText-2 and on a tokenizer-based MiniMind language-model benchmark, while a recall-focused gated key-value retrieval extension improves associative recall but remains seed-sensitive and much slower in the current reference implementation.

---


### 7. [The Virtual Roundtable: Multi-Agent Personas Simulating the Dynamics of Human Brainstorming](https://arxiv.org/abs/2606.05178)

**<font color=#1a73e8>作者：</font>** Tim Dorn, Saara A. Khan, Julie Mumford  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> As AI-driven product development accelerates, the bottleneck is shifting from how we build to what we build. Traditional human brainstorming faces challenges including groupthink, echo chambers, and limited diversity. To address this, we present a multi-agentic architecture that simulates roundtable brainstorming through two phases: divergent thinking to generate diverse ideas, and convergent thinking to evaluate and rank the most promising ones. The system employs diverse AI personas that engage in roundtable discussions, guided by an agentic facilitator that steers the discussion toward productive outcomes. Personas maintain private thoughts while commenting publicly, with ideas emerging organically throughout the discussion. Per-persona quotas on idea submissions and votes promote balanced participation while producing natural rankings. Throughout the session, the system tracks each idea's lineage, capturing how concepts originate and cross-pollinate over time. We demonstrate this approach through a case study generating consumer ideas for AI smart glasses, showing (i) it produces diverse, relevant ideas with insights into their evolution; (ii) the cumulative exchange of perspectives across personas cultivates a shared context that progressively deepens the quality of discussion and the ideas produced.

---


### 8. [Efficient Punctuation Restoration via Weighted Lookahead Scoring Method for Streaming ASR Systems](https://arxiv.org/abs/2606.05179)

**<font color=#1a73e8>作者：</font>** Sungmook Woo, Hyungu Kang, Chanwoo Kim  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Punctuation restoration improves ASR (Automatic Speech Recognition) readability. However streaming ASR requires online decisions with limited future context. In streaming ASR, the system predicts punctuation incrementally, which makes generation-based approaches prone to latency and alignment failures under boundary-wise evaluation. This paper proposes a non-autoregressive scoring method (no free-form generation) that preserves the input transcript and makes a decision at each word boundary. Our method compares punctuation insertion hypotheses against a no-insertion baseline under a bounded K-subword-token lookahead, and calibrates decisions using a weight {\alpha} and a validation-calibrated threshold {\tau} (no parameter updates during inference). On IWSLT 2017, our scoring method achieves a 4-class macro F1 of 0.893 in the no fine-tuning setting (validation-calibrated, K=2) and 0.937 after fine-tuning (K=2), outperforming the prompt-based baseline (0.566) and a fine-tuned ELECTRA baseline (0.913) under the same lookahead budget. We analyze the impact of the lookahead budget through ablation studies on K.

---


### 9. [Multi-Granularity Reasoning for Natural Language Inference](https://arxiv.org/abs/2606.05181)

**<font color=#1a73e8>作者：</font>** Chunling Xi, Di Liang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Natural Language Inference (NLI) is a fundamental task in natural language understanding that requires determining the logical relationship between a premise and a hypothesis. Despite the remarkable success of transformer-based pre-trained models, most existing approaches primarily rely on the final-layer token representations, which are often insufficient for capturing the complex and hierarchical semantic interactions required for effective reasoning. In particular, fine-grained lexical cues, phrasal compositions, and higher-level contextual semantics are typically entangled or diluted in a single representation space. To address these limitations, we propose a novel \emph{Multi-Granularity Reasoning Network} (MGRN) that explicitly leverages hierarchical semantic features within an interactive reasoning space. The proposed framework mimics the human cognitive process of language understanding, which naturally progresses from shallow lexical matching to deeper semantic abstraction and logical reasoning. By integrating semantic information across multiple granularities in a progressive and structured manner, MGRN is able to uncover intricate semantic relationships underlying natural language expressions. Extensive experiments on multiple public benchmarks demonstrate that MGRN consistently outperforms strong baseline models, validating the effectiveness and robustness of the proposed approach.

---


### 10. [Staged Factorial Screening for Budget-Constrained Micro-Pretraining](https://arxiv.org/abs/2606.05186)

**<font color=#1a73e8>作者：</font>** Felipe Chavarro Polania  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Budget-constrained micro-pretraining often requires triaging many candidate recipes on a shared accelerator before larger search budgets are spent. We study whether a staged fractional-factorial workflow can recover stable early effect structure in this setting. On a fixed autoresearch-derived single-GPU training loop, we run 613 experiments across pilot and follow-up screens at 2, 5, and 10 minutes; full 16-condition seeded reruns at 5 and 10 minutes; targeted seeded anchor checks; same-host greedy and matched-cost random baselines; a 60-minute bridge package; and bounded Windows A100 and Linux L40S anchor continuations through 24 hours. Main penalties from total batch, depth, and width are largest at short budgets and relax as budget increases. Within the predeclared seeded full-screen families, D, A, B, and C retain non-zero estimates at 5 and 10 minutes after within-budget Benjamini-Hochberg correction, while E does not. Random search can reach strong incumbents in this 32-condition space, but repeatedly in the same low-penalty region and without factor attribution. The 60-minute bridge anchor has the lowest mean, although that package does not separate workflow refinement from the larger bridge model's capacity advantage. In bounded 12-hour and 24-hour three-anchor continuations on both hosts, the bridge has the lowest sample mean while the non-bridge ordering stays host-sensitive. We therefore present a bounded methods result: use short designed screens to identify high-penalty directions, confirm promising anchors under repeated runs, and refine locally inside the reduced space. The evidence supports a bridge-centered recommendation through 24 hours on two hosts, not hardware-invariant ranking or general hyperparameter-optimization superiority.

---


### 11. [PyCC.id: A package for hypothesis-driven equation discovery with structural identifiability](https://arxiv.org/abs/2606.05191)

**<font color=#1a73e8>作者：</font>** Federico J. Gonzalez  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Data-driven equation discovery is fundamentally an inverse problem that seeks to infer the governing differential equations of a system directly from time-series measurements. A known issue is the ill-conditioned nature of the inverse problem, which frequently produces multiple mathematical models that fit the data similarly well. One path to address this issue is by incorporating known hypotheses and constraints into the training phase beforehand. While this approach effectively reduces the search space, it still results in multiple candidate models, forcing practitioners to rely on post-hoc manual filtering based on their own domain expertise. A recent approach incorporates structural `skeletons' inspired by characteristic curves (CCs), defining a hypothesis-driven methodology. In this methodology, practitioners define a skeleton, which is associated with a family of ordinary differential equations (ODEs), and then add their hypotheses and priors based on their domain knowledge to refine the obtained model iteratively. An important advantage of this approach is that some skeletons have demonstrable structural identifiability properties, which are useful for checking whether the skeleton is correct or should be discarded. Furthermore, this formalism enables the use of multiple equation discovery paradigms due to its modularity (such as neural networks, symbolic regression, and sparse regression). In this work, we present the Python library PyCC, which condenses these efforts into a flexible tool that allows researchers and engineers to seamlessly define their skeletons and hypotheses to discover ODEs from time-dependent data.

---


### 12. [Gradient Descent with Large Step Size Restores Symmetry in Deep Linear Networks with Multi-Pathway](https://arxiv.org/abs/2606.05219)

**<font color=#1a73e8>作者：</font>** Hee-Sung Kim, Sungyoon Lee  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent analyses of multi-pathway Deep Linear Networks use Gradient Flow to predict a "winner-takes-all" specialization in which path symmetry breaks and each feature concentrates in a single pathway. In this work, we show that discrete Gradient Descent (GD) with a large step size tells a different story. We prove that single-path solutions are sharp minima, whereas distributing signals across pathways reduces sharpness by a factor that decreases with both the number of pathways and depth. Consequently, while early training reproduces the depth-driven symmetry breaking predicted by GF, oscillations at the Edge of Stability subsequently override this tendency and drive the network into a re-balancing phase, where signals redistribute across pathways. Together, these results clarify how depth shapes pathway competition and explain why large-step GD favors shared representations rather than persistent single-pathway dominance.

---


### 13. [Differentiable Efficient Operator Search](https://arxiv.org/abs/2606.05232)

**<font color=#1a73e8>作者：</font>** Xiaohuan Pei, Jiyuan Zhang, Yuanfan Guo 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Efficient multimodal foundation models often rely on manually designed token-reduction operators, such as pruning, merging, pooling, and adaptive reweighting. Although these operators appear different, we show that they can be interpreted as distinct regimes of a shared operator space. Based on this view, we introduce Efficient Operator Search, a differentiable framework that jointly searches where to reduce tokens, how many tokens to retain, and how reduced token information should be processed. The proposed search space parameterizes layer activation, retention budget, and operator behavior, while the search policy optimizes task performance under one-sided budget and cost constraints. This formulation recovers representative hand-designed baselines as special cases and further discovers hybrid operators beyond isolated manual designs. Experiments on multimodal benchmarks show that the searched operators achieve competitive accuracy-efficiency trade-offs, especially under aggressive visual-token reduction. These results suggest that efficient multimodal inference can be reframed from manual operator design to differentiable operator search.

---


### 14. [Domain-Conditioned Safety in Frontier Computer-Using Agents: A 793-Episode Browser Benchmark, a Coding-Domain Cross-Reference, and a Reproducibility Audit of Recent Red-Teaming](https://arxiv.org/abs/2606.05233)

**<font color=#1a73e8>作者：</font>** Nicholas Saban  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Recent computer-using-agent (CUA) red-teaming papers report prompt-injection attack success rates (ASR) of 42-98%, but these headline numbers cluster on retired models and on the most-vulnerable model in each paper's panel. We ask whether those techniques, reproduced as hand-crafted templates, still work against current frontier CUAs. We release CUA-HandCrafted, a public benchmark of 793 episodes spanning 24 multi-step web tasks, 56 attack templates, 8 attack families, and 4 system-prompt configurations. Against Claude Sonnet 4.6 and GPT-5.4 we measure 0/140 multi-step attack success (Clopper-Pearson 95% upper bound 2.60%); a prompt ablation shows this resistance lives in the model weights. Yet it does not generalize: on a sister coding-agent benchmark (SkillBench), the same weights fall to hand-crafted skill-injection at up to 100%. We argue that the literature's high ASR is largely attributable to RL-optimized injection text rather than the attack categories, and that frontier safety hardening is domain-conditioned, specific to the heavily-targeted browser surface. Reporting techniques without releasing the optimized strings, or extrapolating browser-domain safety to other CUA modalities, makes published ASR numbers unreproducible.

---


### 15. [Search-Time Contamination in Deep Research Agents: Measuring Performance Inflation in Public Benchmark Evaluation](https://arxiv.org/abs/2606.05241)

**<font color=#1a73e8>作者：</font>** Yongjie Wang, Xinyue Zhang, Kunhong Yao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Public benchmarks enable fair and reproducible evaluation of LLM reasoning, but they become fragile for deep research agents that actively search the web during inference. Such agents may retrieve public benchmark metadata, question context, or even ground-truth answers via web search. This gives rise to Search-Time Contamination (STC), where external retrieval bypasses intended reasoning and inflates measured performance. We systematically study STC in deep research agent evaluation. We define three contamination types with increasing severity, namely Benchmark Metadata Leakage, Question-Context Leakage, and Explicit Answer Leakage, and develop detection algorithms to identify them and quantify their impact on agent performance. Evaluating modern deep research agents on six public benchmarks, we find that STC is widespread and can inflate performance by up to 4%. Our findings show that existing evaluations may overestimate true reasoning ability. We therefore advocate contamination-aware practices, including isolated sandboxes, transparent search trajectories, and controlled benchmark access.

---


### 16. [DiffSlack: Learning under Nonlinear Inequality Constraints via Learnable Slack Variables](https://arxiv.org/abs/2606.05247)

**<font color=#1a73e8>作者：</font>** Ziqian Wang, Chenxi Fang, Zhen Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Enforcing nonlinear inequality constraints in neural networks remains challenging, especially when the output is subject to many coupled constraints. Existing hard constraint methods often impose structural restrictions on the constraint set or introduce substantial computational overhead for large-scale nonlinear problems. Here, we propose DiffSlack, a differentiable projection layer for nonlinear inequality-constrained neural prediction. DiffSlack reformulates inequalities as equalities with learnable slack variables, which are predicted as part of the augmented network output and provide a data-driven warm start for damped Gauss-Newton projection. The projection layer maps raw predictions onto the augmented feasible manifold while preserving end-to-end differentiability. A two-stage curriculum further stabilizes training and improves constraint satisfaction. We evaluate DiffSlack on vehicle path planning with 200 nonlinear inequality constraints from collision avoidance, curvature limits, and waypoint spacing. Compared with existing learning-based baselines, DiffSlack achieves a higher planning success rate and stronger geometric constraint satisfaction under a comparable inference budget. Ablation studies further show that the hard projection layer reduces sensitivity to supervision quality. Closed-loop tracking in CARLA and real-world vehicle experiments confirms the executability of the generated trajectories. These results demonstrate that DiffSlack provides a practical and scalable approach to embedding hard inequality constraints into neural networks for engineering applications.

---


### 17. [From Attack Simulation to SIEM Rule: Deterministic Detection-as-Code Synthesis with Probe-Level Traceability](https://arxiv.org/abs/2606.05252)

**<font color=#1a73e8>作者：</font>** Alexandre Cristovão Maiorano  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Security teams routinely simulate attacks against their own systems to check whether their monitoring would catch a real intruder. These Breach-and-Attack-Simulation (BAS) tools surface findings, but the security information and event management (SIEM) systems that watch production need detection rules -- and today a human bridges that gap by hand, reading each finding and writing the corresponding Sigma rule (a vendor-neutral detection format). We show this translation can be partially automated when probes are drawn from a locked corpus, so each finding carries a stable identifier back to the originating probe. We describe a deterministic synthesis function that maps each finding to a starter Sigma rule through a small template library (N=23, indexed by categories from the OWASP LLM and Web Top 10), with a back-reference to the originating finding and its MITRE ATT&CK technique. On two locked corpora (17-probe LLM, 23-probe Web), every bypassed-probe finding yields a starter rule, and all 17/17 emitted rules parse and convert to Splunk and Elasticsearch backends. Replayed through a live OpenSearch SIEM, the LLM rules fire on 30% of a held-out AdvBench subset and 14% of HarmBench at 7.7% false positives on a benign baseline; the Web side is validated structurally, not against a held-out attack set. The contribution is a verifiable, byte-stable path from BAS finding to operator-deployable starter rule, re-derivable from the published corpus and template library alone -- trading the breadth of LLM-generative methods for exact reproducibility and a typed traceback from any fired alert to the originating probe.

---


### 18. [Alpha-RTL: Test-Time Training for RTL Hardware Optimization](https://arxiv.org/abs/2606.05253)

**<font color=#1a73e8>作者：</font>** Peilong Zhou, Zhirong Chen, Cangyuan Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have shown increasing promise in generating
functionally correct register-transfer-level (RTL) hardware designs.
Recent systems improve further through EDA-integrated reinforcement
learning with syntax, simulation, and PPA rewards, but train a general
RTL generator before deployment while test-time approaches search with
a frozen policy. We instead perform reinforcement learning at test time,
allowing the LLM policy to adapt to executable EDA feedback for the
specific RTL problem at hand. We propose TTT-RTL, to our knowledge the
first per-design test-time training framework that closes the loop
between an LLM policy and an EDA pipeline for RTL optimization. TTT-RTL
samples candidate implementations, verifies them through syntax checking
and simulation, scores valid designs using synthesis-derived PPA product,
reuses high-reward variants through a PUCT-indexed design-state pool,
and updates the policy with an entropic policy-gradient objective. To
stabilize policy updates under sparse or plateaued rewards, we introduce
an adaptive KL-budget controller that adjusts the entropy constraint
using reference KL, effective sample size, and reward saturation signals.
On RTLLM v2.0 under Nangate 45nm, TTT-RTL reduces the geometric-mean
PPA product by 65.1% over the reference, outperforming the strongest
published frozen-policy agent baseline at 26.1%. On an industrial
XuanTie C910 FPU leading-zero-anticipation unit under Sky130, TTT-RTL
achieves a 59.4% ADP reduction, and ablations confirm that policy
adaptation, state reuse, and KL-budget control each contribute. These
results suggest that test-time training with executable EDA feedback can
move LLM-based RTL generation beyond functional correctness toward
physically optimized hardware.

---


### 19. [Flash-WAM: Modality-Aware Distillation for World Action Models](https://arxiv.org/abs/2606.05254)

**<font color=#1a73e8>作者：</font>** Arman Akbari, Ci Zhang, Arash Akbari 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> World-action models (WAMs) jointly generate future video and robot actions through iterative diffusion, achieving strong performance on manipulation benchmarks but requiring tens of denoising steps, a cost that precludes real-time control. Step distillation has emerged as the natural remedy, but off-the-shelf methods break down in the joint video-action setting because video and action streams use different SNR-shifted noise schedules and reach training with substantially different marginal noise distributions, an asymmetry that single-modality distillation methods cannot accommodate. We introduce \textbf{Flash-WAM}, a modality-aware step-distillation framework inspired by consistency distillation that selects the consistency function for each modality to match its noise regime: a linear-gradient-scaling parametrization for the action stream's low-noise regime, paired with a variance-preserving parametrization for the video stream's high-noise regime, grounded in a structural analysis of the consistency-function family that characterizes the achievable gradient scaling under the consistency boundary condition. Instantiated on LingBot-VA, Flash-WAM compresses inference to a single step in each modality. On RoboTwin 2.0, this reduces per-chunk latency from $8.1$ seconds to $348$ ms on NVIDIA L40S, a $23{\times}$ speedup that enables real-time inference. Flash-WAM preserves task success on simulation benchmarks ($85.5\%$ RoboTwin 2.0, $95.7\%$ LIBERO) and substantially recovers real-world performance ($60\%$ average on a Unitree G1 humanoid robot), while naive consistency distillation drops to $24\%$ at the same step budget.

---


### 20. [VideoKR: Towards Knowledge- and Reasoning-Intensive Video Understanding](https://arxiv.org/abs/2606.05259)

**<font color=#1a73e8>作者：</font>** Lin Fu, Zheyuan Yang, Yang Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce VideoKR, the first large-scale training corpus specifically designed to strengthen knowledge- and reasoning-intensive video understanding. It comprises 315K video reasoning examples over 145K newly collected, CC-licensed, expert-domain videos. We develop a human-in-the-loop, skill-oriented example generation pipeline that targets progressively deeper video reasoning capabilities while ensuring the difficulty, diversity, and reliability of both the examples and their CoT rationales. We also curate VideoKR-Eval, a new expert-annotated benchmark where questions require genuine video understanding and knowledge-intensive reasoning rather than textual shortcuts. Our experiments show that, under a standard SFT$\rightarrow$GRPO pipeline, models post-trained on VideoKR outperform prior post-training approaches on knowledge-intensive video reasoning while remaining competitive on general video reasoning, highlighting data design as a key driver of progress in video reasoning. We further conduct comprehensive ablations to isolate the contributions of VideoKR, providing actionable insights for future work.

---


### 21. [NIV: Neural Axis Variations for Variable Font Generation](https://arxiv.org/abs/2606.05261)

**<font color=#1a73e8>作者：</font>** Nadav Benedek, Ariel Shamir, Ohad Fried  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Variable fonts enable continuous variation of glyph geometry along semantic design axes such as weight, width, slant, and optical size. However, constructing a variable font from a static font remains a labor-intensive process requiring expert typographic design and manual specification of glyph variation data. We introduce NIV (Neural Axis Variations), a method that automatically converts a static font into a fully functional variable font. Given glyph outlines and a set of desired design axes, NIV predicts per-point displacements. The model operates directly on vector glyph geometry and employs a novel Property Embedding mechanism that captures interactions between multiple axes, enabling consistent multi-axis variation within a unified framework. We train NIV on a newly constructed dataset derived from variable Google Fonts, comprising over one million variation tuples. The resulting model generalizes across unseen code points, unseen font styles, high-complexity CJK glyphs, and even out-of-distribution handwriting inputs. The generated outputs are standard variable font files supporting continuous interpolation via existing rendering engines. To facilitate research, we release the dataset, the complete training and inference implementation, and trained models at this https URL. Beyond typography, our approach demonstrates how structured geometric objects with continuous parametric variation can be synthesized using neural deformations.

---


### 22. [Policy-Conditioned Counterfactual Credit for Verifiable Reinforcement Learning of Long-Horizon Language Agents](https://arxiv.org/abs/2606.05263)

**<font color=#1a73e8>作者：</font>** Renwei Meng  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards improves reasoning and tool use, yet long-horizon language agents still learn unsupported evidence chains, belief drift, and shortcut actions that satisfy terminal checks. Existing process rewards are mostly correlational: they reward retrieval-, reflection-, or verification-like steps without estimating whether the step contributes to final verified success under a specified intervention. We propose CVT-RL, a constrained policy-gradient algorithm with dense verifiable rewards, intervention-validity gating, and a policy-conditioned counterfactual contribution (PCCC) estimator. Deletion, semantic substitution, evidence substitution, and tool-output perturbation define separate controlled interventions; continuations are sampled from a frozen reference policy, and a selection-adjusted doubly robust estimator augments the advantage. Belief control uses only prefix-observable labels, while an augmented Lagrangian constrains unsupported claims, skipped verification, tool tampering, and unsafe calls. On long-context QA, ALFWorld, ScienceWorld, and web/tool tasks, CVT-RL improves average task success from 71.8% for compute-matched non-causal RL and 75.4% for an information-matched counterfactual-process baseline to 78.9%, improves evidence F1 from 78.9 to 82.8 over the information-matched baseline, and reduces measured hacking from 7.2% to 3.9%. Independent human audit estimates 4.6% hacking for CVT-RL versus 8.1% for the information-matched baseline, and adaptive detector-evasion attacks raise hacking only to 7.1%. Stratified bootstrap and mixed-effects tests give p<0.01 after Holm correction for all primary metrics. Carefully scoped counterfactual credit, paired with validity gating, diagnostics, and verifiable constraints, provides a reproducible route toward more reliable long-horizon RL for language agents.

---


### 23. [REGEN: Reference-Guided Synthetic Multivariate Time Series Generation for Forecasting](https://arxiv.org/abs/2606.05264)

**<font color=#1a73e8>作者：</font>** Moulik Gupta, Dhruv Kumar, Murari Mandal 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Training robust multivariate time series forecasting models requires large, diverse corpora, yet many real-world domains provide only a handful of observed sequences. Existing generators fail to resolve this mismatch: prior-based approaches (e.g., CauKer, TimePFN) produce domain-agnostic samples, while data-driven methods (e.g., TimeGAN) treat references as black-box supervision, forfeiting explicit control over periodic structure, local variability, and cross-variable dynamics.
We propose ReGeN, a reference-guided generative pipeline that treats observed sequences not as examples to imitate, but as structural scaffolds for controllable synthesis. ReGeN decomposes each reference into three interpretable components: a phase-aligned periodic backbone capturing dominant domain morphology; per-variable stochastic residuals modeled with a deep-kernel Gaussian process; and lag-aware cross-variable dependencies injected through a structural causal model with fitted coupling coefficients. Sampling these components at controllable temperature broadens distributional coverage while preserving domain-grounded structure.
We show that ReGeN-generated data consistently substitutes for real sibling data with minimal forecasting degradation, and in strongly periodic domains such as traffic, can outperform the real source itself. We further show that a foundation model pretrained on ReGeN corpora outperforms those pretrained on prior-based and data-driven synthetic alternatives. This suggests that in low-data regimes, how reference data is structurally exploited can matter as much as how much data is available.

---


### 24. [Sharp Low-Degree Thresholds for Planted-vs-Planted Testing](https://arxiv.org/abs/2606.05266)

**<font color=#1a73e8>作者：</font>** Anda Skeja, Daniel Gutiérrez Espinoza, Fiona Skerman 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We establish the first sharp thresholds for low-degree polynomial tests in planted-vs-planted settings, where the goal is to determine with vanishing error which of two structured planted mechanisms generated the observed data. We prove matching low-degree upper and lower bounds for counting communities in the planted submatrix and planted dense subgraph models. The resulting testing threshold coincides, down to the sharp constant, with the known low-degree recovery threshold. In contrast, the task of weak testing, where the goal is to outperform random guessing, does not have a sharp threshold but rather a smooth transition, which we identify. To prove our results, we develop a framework for planted-vs-planted testing that builds on a latent-variable expansion originating in low-degree recovery and employs new methods to identify and prune non-signal contributions.

---


### 25. [Learning Manifold and Itô Dynamics with Branched Neural Rough Differential Equations](https://arxiv.org/abs/2606.05272)

**<font color=#1a73e8>作者：</font>** Luke Thompson, Dai Shi, Lequan Lin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural rough differential equations (NRDEs) stay accurate under irregular sampling while taking far fewer integration steps than standard neural differential equations, summarising a finely sampled driver by its log-signature and advancing the hidden state over coarse intervals using the log-ODE method. This efficiency rests on the shuffle algebra, the algebraic counterpart of Stratonovich calculus. This reliance means NRDEs cannot expose the quadratic-variation terms Itô dynamics require, nor the ordered covariant derivatives that govern Itô flows on connection-equipped manifolds. Ameliorating this, we introduce Branched Neural Rough Differential Equations (B-NRDEs), a Hopf-algebraic framework that recasts the NRDE log-ODE step as geometric numerical integration on the state-space manifold, matching the driving algebra to the governing calculus: Grossman--Larson rooted trees for Euclidean Itô dynamics, Munthe-Kaas--Wright planar rooted trees for ordered covariant derivatives on manifolds, and the shuffle algebra in the classical Stratonovich case. This yields intrinsic coarse-step dynamics that exactly preserve manifold constraints. Finally, we introduce a branched signature-kernel objective to enable Itô-consistent law matching by making quadratic-variation terms visible during training. On rough Bergomi volatility, sim-to-real $\mathrm{SO}(3)$ dynamics forecasting, and SPD covariance dynamics, B-NRDEs offer a unified, effective approach to stochastic and manifold-valued dynamics beyond the Euclidean--Stratonovich setting.

---


### 26. [Anomaly Detection for Electro-Hydrostatic Actuators using LSTM Autoencoder](https://arxiv.org/abs/2606.05274)

**<font color=#1a73e8>作者：</font>** Nehal Afifi, Abdelmonem Elhendawi, Felix Leitenberger 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Electro-Hydrostatic Actuators (EHAs) are widely used in aerospace and industrial systems, where timely detection of sensor anomalies is essential to ensure safe and reliable operation. However, the large volume and high sampling frequency of EHA sensor data pose challenges for accurate and efficient anomaly detection. Conventional statistical and classical machine-learning methods such as Z-score, Interquartile Range (IQR), Median Absolute Deviation (MAD), Isolation Forest, Gaussian Mixture, and k-means often fail to capture the temporal dependencies inherent in EHA signals, resulting in limited detection accuracy and elevated false-alarm rates. Furthermore, systematic evaluations of data-driven anomaly detection approaches for EHA systems remain scarce, particularly under varying operational conditions. This study presents an offline anomaly-detection framework for univariate EHA sensor signals, focusing on temperature and pressure data collected from a controlled test bench. The method employs a reconstruction-based Long Short-Term Memory (LSTM) autoencoder, calibrated and evaluated using validation-set reconstruction-error distributions. Performance is assessed across multiple fault-injection scenarios using accuracy, precision, recall, and F1-score, complemented by sensitivity analyses under varying operating conditions. The LSTM autoencoder achieved an average accuracy of 99.0\%, precision up to 100\%, recall between 90.2\% and 99.6\%, and F1-scores from 93.1\% to 99.8\%, demonstrating high detection sensitivity and a very low false-alarm rate across all evaluated sensors. These results highlight the feasibility of data-driven offline anomaly detection for EHAs. Future work will focus on adapting the developed framework for an online (real-time) environment.

---


### 27. [Personal AI Agent for Camera Roll VQA](https://arxiv.org/abs/2606.05275)

**<font color=#1a73e8>作者：</font>** Thao Nguyen, Krishna Kumar Singh, Donghyun Kim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We study the personal camera roll visual question answering setting. In this setting, a conversational AI assistant can access a user's personal camera roll and retrieve relevant photos to answer queries, ranging from simple factual questions (e.g., ``Name of the food I tried yesterday?'') to more open-ended ones (e.g., ``Recommend some dishes I have never eaten before''). Given the vast nature of the personal camera roll (i.e., multiple years, hundreds to thousands of photos), a successful AI assistant needs to understand a long-horizon, highly personalized visual content stream in order to navigate and locate the correct and/or relevant information. To support this, we collect and manually annotate questions that mimic real-world usage. The final dataset, camroll, contains 50 users, 31,476 images, and 2,500 QA pairs. We further design camroll-agent, a conversational AI agent equipped with hierarchical memory and a minimal set of tools for efficient navigation over large, personalized visual memory. Experimental results show that camroll-agent outperforms numerous baselines and methods for long-context understanding AI agents system. Together, the camroll dataset and camroll-agent highlight the gap in AI agents' long-context reasoning: personalized visual memory requires different approaches from standard long-context textual memory, especially when consistency, visual details, and user-specific context are present.

---


### 28. [Do Models Share Safety Representations? Cross-Model Steering for Safe Visual Generation](https://arxiv.org/abs/2606.05290)

**<font color=#1a73e8>作者：</font>** Tobia Poppi, Silvia Cappelletti, Sara Sarto 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent progress in generative modeling has made safety control a central challenge, yet existing approaches remain largely model-specific, requiring retraining or tailored interventions for each new architecture. In this work, we ask whether safety can be represented as a portable latent direction, learned once and reused across heterogeneous generators. We introduce the first framework for cross-model safety steering, in which a safety direction is estimated in a source LLM from paired safe-unsafe prompts, transported to a target generator through a lightweight alignment fitted on benign data alone, and applied at inference time. Crucially, our pipeline never accesses unsafe data on the target side, isolating whether safety can be transferred through shared representation geometry. Beyond a single global direction, we also identify a multi-vector extension that captures category-specific safety behaviors, enabling more selective control. We evaluate our approach in text-to-image and text-to-video generation across diverse source-target model pairs. Across models, transferred safety directions achieve ASR reduction and CLIP-Score/FID trade-offs comparable to directions learned natively on the target model using unsafe data, while requiring no target-side unsafe data. This indicates that safety improvements do not come at the expense of generation quality. Our results point to a modular view of safety: safety-relevant behavior is not purely model-local, but can be controlled through latent directions that persist across models. This suggests a new path toward lightweight, reusable safety mechanisms that do not require target-side unsafe data.

---


### 29. [What Should Agents Say? Action-state Communication for Efficient Multi-Agent Systems](https://arxiv.org/abs/2606.05304)

**<font color=#1a73e8>作者：</font>** Chen Huang, Yuhao Wu, Wenxuan Zhang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-agent systems (MAS) built on large language models are typically organized around roles, pipelines, and turn schedules, while the content that agents pass to one another is often left as unconstrained natural language. However, this free-form communication can rapidly inflate token usage, consume the shared context window, and ultimately affect both system performance and inference cost. We analyze five common inter-agent communication strategies across two MAS topologies, finding that no fixed strategy is universally optimal. Instead, effective inter-agent messages consistently preserve action-centered information needed by downstream agents. Building on this, we propose the PACT (Protocolized Action-state Communication and Transmission), which treats inter-agent communication as a public state-update problem and projects each raw agent output into a compact action-state record before it enters shared history. Across different MAS topologies, PACT consistently improves the performance-cost trade-off, achieving comparable or stronger task performance with substantially fewer tokens. The gains extend to production coding harnesses: PACT lifts OpenHands' resolve rate at -10% tokens-per-resolved, and is resolve-neutral on SWE-agent while halving input tokens. Our code is publicly available at this https URL.

---


### 30. [I Know What You Meme, Even If it Emerged Today: Understanding Evolving Memes through Open-World Knowledge Acquisition](https://arxiv.org/abs/2606.05316)

**<font color=#1a73e8>作者：</font>** Shanhong Liu, Rui Cao, Pai Chet Ng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal memes are dynamic and often require up to date background knowledge for interpretation. Existing methods often overlook such knowledge or rely on fixed parametric knowledge of pretrained models that may be incomplete, outdated, or unavailable for emerging memes. We introduce Query Retrieve Conclude, a zero shot framework that identifies missing knowledge, retrieves open web evidence, and synthesizes evidence grounded background knowledge for meme understanding and detection. We also introduce a curated meme understanding benchmark of recent memes from 2024 to 2026 with external background knowledge annotations. Experiments on three meme understanding datasets and five meme detection tasks show that our framework improves knowledge recovery, meme understanding and downstream detection over zero shot baselines.

---


### 31. [Multimarginal flow matching with optimal transport potentials](https://arxiv.org/abs/2606.05327)

**<font color=#1a73e8>作者：</font>** Raghav Kansal, David Crair, Nghia Nguyen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Flow matching (FM) has emerged as a powerful framework for learning dynamic transport maps between two empirical distributions. However, less explored is the setting with intermediate observed marginals that can help constrain the flows between the endpoints. This "multimarginal" regime is central to modeling temporal evolution in dynamical systems in many scientific domains that can sample sequential distributions. We tackle this problem with a novel approach that leverages the connection between FM and dynamic optimal transport (OT), softly steering the flow towards the intermediate marginals through potential terms in the dynamic OT action. By extending the conditional FM learning target to incorporate these potentials, we derive an efficient, simulation-free algorithm for multimarginal FM that offers considerable flexibility in the spatiotemporal dynamics of the learned flows. We demonstrate state-of-the-art performance and training efficiency of OT-potential FM (OTP-FM) on diverse single-cell RNA sequencing, oceanographic, and meteorological datasets. Our code is available at this https URL.

---


### 32. [A Model of Multi-turn Human Persuadability Using Probabilistic Belief Tracing](https://arxiv.org/abs/2606.05330)

**<font color=#1a73e8>作者：</font>** Jared Moore, Noah Goodman, Nick Haber 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models can shift human beliefs across high-stakes domains, but most persuasion studies rely on pre/post belief change. These endpoint measures identify whether persuasion occurred, yet miss where and how beliefs moved within a dialogue. We present PERSUASIONTRACE, a framework for studying persuasion in human-LLM interaction. Built on a web-based experimental platform, PERSUASIONTRACE contributes a tool for multi-turn persuasion studies and a process-level evaluation protocol: it records multi-turn belief reports from human or simulated targets of persuasion, annotates persuader turns with rhetorical dimensions (logos/pathos/ethos), and evaluates simulators by fidelity to real human belief dynamics. Using this framework, we find that human targets group into two clusters of multi-turn belief updates and exhibit susceptibility to rhetorical strategies, and that LLMs are persuasive across generic and personalized topics, text and audio modalities, and multi-turn interactions. Prior work has chiefly used vanilla-prompted LLMs to simulate human targets, but we show that these simulators fail to replicate human belief dynamics. We introduce a Bayesian-network simulated target that maintains an explicit latent belief state over time so each persuader message yields cognitively realistic belief updates. In human-likeness evaluation, our Bayesian target scores near a human reference (81 vs 80), while baseline LLM targets score substantially lower (64). PERSUASIONTRACE reframes persuasion evaluation from endpoint movement alone to process fidelity, providing a stronger basis for scientific analysis and safer optimization of persuasive systems.

---


### 33. [GITCO: Gated Inference-Time Context Optimization in TSFMs](https://arxiv.org/abs/2606.05332)

**<font color=#1a73e8>作者：</font>** Manya Pandey, Dhruv Kumar, Murari Mandal 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Patch-based Time Series Foundation Models (TSFMs) suffer from context poisoning: structurally anomalous patches capture disproportionate attention and silently degrade zero-shot forecast quality. We propose improving TSFM accuracy at inference time by optimizing the input context rather than modifying model weights. We present GITCO (Gated Inference-Time Context Optimization), a lightweight three-component framework: Gate, Router, and Critic that selectively identifies and suppresses harmful patches without any parameter updates. Evaluated on TimesFM 2.5 across 53 GIFT-Eval datasets under K-fold cross-validation, GITCO achieves an average +1.95% MASE reduction on TimesFM 2.5 while capturing 89.9% of the improvement upper bound. We introduce context sensitivity profiles as a new characterizable property of TSFMs: the mapping from time series meta-features to expected accuracy improvement under inference-time context intervention, shaped jointly by model architecture and the statistical structure of the data.

---


### 34. [Uncertainty Aware Functional Behavior Prediction and Material Fatigue Assessment for Circular Factory](https://arxiv.org/abs/2606.05334)

**<font color=#1a73e8>作者：</font>** Nehal Afifi, Mehdi Khabou, Victor Mas 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Returned products in circular factories re-enter production with heterogeneous degradation states, usage histories, and remaining capability. Reuse cannot be decided from the current inspection alone, because future function fulfillment and component integrity may evolve differently under the next service scenario. Existing PHM approaches support degradation prediction, but often target fixed operating conditions or isolated component benchmarks, while material-fatigue assessment is rarely linked to system-level functional prognosis. This paper addresses this gap for an angle grinder by combining uncertainty-aware functional prediction with component-level fatigue assessment in an instance-specific reliability workflow. The proposed framework combines the current tool state with recent force--torque usage windows. A convolutional encoder extracts loading patterns from spindle forces and shaft torque, and an LSTM backbone predicts nine functional variables as Gaussian mean and variance estimates. In parallel, the same loading history is translated into output-shaft fatigue information through finite-element-supported stress reconstruction, S--N/Miner damage evaluation with Haibach extension, and Paris-law crack-growth analysis. A streaming replay algorithm consolidates both branches into functional, material, and system reliability trajectories. Held-out tests show mean \(2\%\)-tolerance accuracy of 0.9652 across nine outputs. Thermal variables are predicted near-perfectly, while drive motor current and load speed remain the most demanding dynamic outputs, with \(R^2\) values of 0.9750 and 0.9924. Torque history is especially important for these variables, and the conventional LSTM outperforms GRU and xLSTM in the short-history setting. Reliability calibration is most informative for drive motor current, where predicted and observed exceedance probabilities ...

---


### 35. [A prism hierarchy of learning regimes in large linear autoencoders](https://arxiv.org/abs/2606.05335)

**<font color=#1a73e8>作者：</font>** Eugene Golikov, Yaroslav Gusev, Dmitry Yarotsky  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Theoretical studies of machine learning models commonly consider different limiting regimes in which the learning dynamics of gradient descent becomes theoretically tractable. It is, however, desirable to have a systematically obtained picture of all qualitatively different extreme learning regimes for a particular type of models. In this paper we propose such a picture for large weight-tied linear autoencoders characterized by input and latent dimensions, initialization magnitude, and training set size. This model is nonlinear in the weights and its gradient flow does not have a general theoretical solution. We show that at the level of the formal loss-expansion hierarchy, its extreme regimes are naturally associated with faces of a triangular prism. In particular, there are five basic extreme regimes associated with the 2-faces of the prism: (1) large-data, (2) small-data, (3) mean-field, (4) narrow-latent, and (5) free. For regimes (1,2,3,4), we derive explicit expressions for both train and population limiting loss evolutions under gradient flow, obtaining very good agreement with experimental results.

---


### 36. [Self-supervised User Profile Generation for Personalization](https://arxiv.org/abs/2606.05336)

**<font color=#1a73e8>作者：</font>** Clark Mingxuan Ju, Yuwei Qiu, Tong Zhao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Personalizing large language models (LLMs) has become a central challenge as LLMs are deployed across recommendation, search, dialogue, and content generation -- settings where the same query should yield different answers given different users. A promising route is to summarize each user's interaction history into a natural-language memory or profile and prepend it to the prompt to facilitate personalization. Existing methods learn such profile generators with explicit rewards derived from labeled downstream tasks, which are expensive and sparse as they require annotated supervision for every target task. In light of this challenge, we introduce Bidirectional User Modeling via Profiles (BUMP), a self-supervised framework that trains a profile generator without any downstream labels. Specifically, given a user's interaction history, we use GRPO to train an LLM to emit a free-form textual profile under a bidirectional in-batch ranking objective: a small LLM judge measures (i) how well the generated profile, used as a query, ranks the user's own held-out interactions above interactions from other users in the batch, and (ii) how well a held-out interaction, used as a query, ranks the user's own profile above profiles of other users. Both directions are scored with multi-positive NDCG and combined into a dense reward per rollout; other users in the batch supply free negatives, so every training example yields supervision from raw interaction logs alone. Evaluated on the LaMP benchmark, BUMP matches or outperforms closed-source APIs and prior methods relying on labeled rewards, while requiring no task label at training.

---


### 37. [SentinelBench: A Benchmark for Long-Running Monitoring Agents](https://arxiv.org/abs/2606.05342)

**<font color=#1a73e8>作者：</font>** Matheus Kunzler Maldaner, Adam Fourney, Amanda Swearngin 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI agents are increasingly asked to carry out work that spans minutes, hours, or longer. Yet the default model of agent behavior is continuous action: issuing tool calls, refreshing pages, searching for alternatives, or otherwise trying to force progress. This is the wrong approach for many long-running tasks, which are better served by a strategy of sustained attention. Instead, agents should monitor an environment, notice when an external event makes progress possible, then respond promptly without wasting resources while waiting. To measure progress on this class of tasks, we introduce SentinelBench, an open-source benchmark for time-evolving monitoring tasks.
SentinelBench contains 100 tasks across 10 synthetic web environments, including email, calendars, finance, professional networking, and entertainment. Each environment exposes a live web interface and replays a scripted sequence of events, requiring agents to navigate and reason about web pages whose state shifts underfoot. SentinelBench measures task completion, reaction time, and resource use, exposing the tradeoff between responsiveness and cost. We report results across three models and two browser-agent harnesses, establishing performance baselines for future comparison and demonstrating how agent design choices can dramatically impact key metrics. Together, these results show that SentinelBench distinguishes meaningful differences in agent behavior.

---


### 38. [PJ-RoPE: A Fourier-Jet-Affine Position Space for Relative Attention](https://arxiv.org/abs/2606.05345)

**<font color=#1a73e8>作者：</font>** Yaobo Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We unify RoPE's Fourier phase, Jordan-RoPE's finite jets, and ALiBi's affine recency into a single learnable relative-position space, and study which regions of this space are selected by different tasks. PJ-RoPE is a Fourier-Jet-Affine formulation for relative attention, with an optional Poincare-type reading as the affine completion of a homogeneous Fourier-jet positional representation. Algebraically, the same primitives form a finite constant-coefficient difference module: simple roots of the lag-shift operator give Fourier/RoPE characters, repeated nonzero roots give Jordan/Fourier jets, and the repeated unit root gives ALiBi-like affine recency.
The framework separates scalar PJ-bias kernels from exact PJ-rotary feature transforms, introduces adaptive sector diagnostics, and uses LC/rapidity coordinates to stabilize high-order jets. Controlled probes verify sector containment and selection; small language runs expose an affine/recency boundary; music-token streams provide the clearest case where LC/affine variants remain strong while carrying measurable high-order corrections; and LC diagnostics show a scale-stability gain coupled to phase-resolution loss.

---


### 39. [TopoPult-SSL: Gland-Mask-Free Cross-Device Meibomian Gland Segmentation via Self-Distilled Weak Clinical Priors](https://arxiv.org/abs/2606.05347)

**<font color=#1a73e8>作者：</font>** Nicolò Savioli, Luca Del Tongo  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Every new clinical imaging device creates a domain shift where dense gland masks are expensive yet cheap clinical signals -- eyelid outlines, Pult grades, morphometric ratios -- are routinely recorded. We present TopoPult-SSL, a two-stage framework for cross-device meibomian gland segmentation. Stage 1 adapts a source-trained model without target gland masks in the training loss, using four weak-prior anchors driven by target eyelid masks and clinical metadata only. Stage 2, when target gland masks are available, distils complementary Stage-1 teachers into a single compact student via supervised self-distillation. We develop and validate the technique on the public MGD-1k to CAMG research benchmark (1,000 to 100 images, different device), where the distilled model achieves Dice 0.716+/-0.006 (best 0.726), surpassing UA-MT (0.710) and the ensemble teacher (0.720) -- with a single pass. The gland-mask-free Stage-1 variant reaches Precision 0.694 vs. 0.30-0.34 for SAM/MedSAM (p<0.001), enabling deployment without dense gland contouring. Code and reproducibility scripts are released.

---


### 40. [LightVesselNet: An Ultra-Lightweight Sub-100K Parameter Network for Retinal Blood Vessel Segmentation](https://arxiv.org/abs/2606.05354)

**<font color=#1a73e8>作者：</font>** Shadman Sobhan, Farhana Jalil  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Retinal blood vessel segmentation plays a vital role in the early detection of diabetic retinopathy and glaucoma. While recent deep learning models have achieved great segmentation accuracy, they typically require heavy computational resources, making real-world deployment on edge devices difficult. In this paper, we propose LightVesselNet, an efficient neural network designed for retinal vessel segmentation in a resource-constrained environment. Despite containing only 75K parameters, LightVesselNet performs competitively with much larger models. The network employs a compact encoder decoder architecture enhanced with channel and spatial attention mechanisms, a multi-scale feature aggregation module at the bottleneck, and a subpixel upsampling strategy in the decoder. A dedicated edge residual connection preserves fine vessel detail throughout decoding. Extensive experiments on five publicly available datasets: DRIVE, STARE, CHASEDB1, FIVES, and HRF, yield sensitivity scores of 0.8189, 0.8499, 0.8640, 0.8634, 0.8096, and Dice coefficients of 0.8070, 0.8072, 0.8181, 0.8649, and 0.7686, respectively. LightVesselNet shows improved efficiency (Performance vs Parameter or GFlops) compared to State-of-the-Art models. Cross-dataset evaluation confirms the model's generalisation capability. Overall, LightVesselNet is a strong candidate for deployment in low-resource clinical settings and mobile screening tools.

---


### 41. [An interpretable and trustworthy AI framework for large-scale longitudinal structure-pain association studies using data from the Osteoarthritis Initiative (OAI)](https://arxiv.org/abs/2606.05357)

**<font color=#1a73e8>作者：</font>** Jincheng Yu, Haoyang Li, Yiwen Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Purpose: To develop an interpretable and trustworthy AI framework that combines deep learning based MRI Osteoarthritis Knee Score (MOAKS) prediction with interpretable statistical modeling to study structure-pain relationships at scale using data from the Osteoarthritis Initiative (OAI). Materials and Methods: We first developed a deep learning framework to predict MOAKS features directly from knee MRIs and incorporated conformal prediction to provide prediction uncertainty quantification. This uncertainty-aware strategy enables explicit filtering of model outputs, retaining only high-confidence MOAKS predictions at the knee level. Second, we applied a longitudinal latent class mixed model (LCMM) to examine associations between key structural abnormalities and four complementary knee pain measurements. Results: Among the three MRI-defined abnormalities (i.e., bone marrow lesions (BML), cartilage loss (CART), and meniscal extrusion (ME)), our framework substantially improved the Matthews correlation coefficient (MCC) and some other metrics. For example, MCC increased from 0.69 to 0.91 for BML, from 0.45 to 0.80 for CART, and from 0.59 to 0.89 for ME. Using these high-confidence predictions, we expanded the sample size to 2,175 knees for the LCMM analysis. Two distinct pain trajectories were identified (rapid and stable pain progression). The estimated odds ratios (95% CI) for the rapid progression group were 1.62 (1.12-2.35) for BML, 1.83 (1.24-2.70) for CART loss, and 2.50 (1.75-3.57) for ME. Conclusion: These results highlight the importance of these structural abnormalities as risk factors for pain and functional progression in osteoarthritis.

---


### 42. [Recovering Physically Plausible Human-Object Interactions from Monocular Videos](https://arxiv.org/abs/2606.05359)

**<font color=#1a73e8>作者：</font>** Dingbang Huang, Etienne Vouga, Qixing Huang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this paper, we propose RePHO, a method to reconstruct physically plausible human-object interactions (HOI) from monocular videos. While existing kinematic-based approaches produce visually plausible motion, they often result in physically implausible artifacts such as interpenetration and object floating. To overcome these issues, we introduce a physics-guided reconstruction framework. We begin with a kinematic estimate and then refine it by training a policy with reinforcement learning (RL). This policy is optimized to reproduce the interaction in a physics simulator. Because kinematic estimates are typically noisy, naive RL training can fail. Therefore, we propose an adaptive sampling strategy with a dual self-updating mechanism that can identify the frames with the most informative and reliable kinematic reconstruction. Our process progressively improves reconstruction quality and yields physically consistent HOI sequences. We demonstrate our approach on two standard HOI benchmarks and achieve clear improvements in physical plausibility metrics over state-of-the-art methods. Project Page: this https URL

---


### 43. [Mamba-Assisted Non-Markovian Closure for Reduced-Order Modeling](https://arxiv.org/abs/2606.05371)

**<font color=#1a73e8>作者：</font>** Zhi-Feng Wei, Saad Qadeer, Panos Stinis  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reduced-order modeling of high-dimensional dynamical systems is often hindered by the non-Markovian closure term that represents the effect of unresolved variables on the resolved dynamics. Inspired by the Mori--Zwanzig formalism, in which the closure takes the form of a memory functional of the resolved trajectory, we recast closure modeling as a sequence modeling problem and propose the Mamba-Assisted Closure (MAC) framework: a Mamba-based sequence model, trained to predict the closure from the resolved trajectory, is coupled with the reduced-order governing equations through a numerical integrator to advance the resolved variables in time. A key feature of the framework is its exploitation of the dual representation of state-space models -- the model is trained in a sequence-to-sequence fashion via the convolutional form, and deployed for step-by-step autoregressive rollout via the recurrent form, yielding both efficient long-trajectory training and constant per-step inference cost. On the viscous Burgers' equation and the chaotic two-scale Lorenz '96 system, the MAC model substantially outperforms the Markovian reduced-order model, the GRU-based sequence model, and the Wilks method in predictive accuracy and long-time rollout stability.

---


### 44. [Evidence-Guided Neural Architecture Selection under Uncertainty for Subject-Specific Blood Glucose Forecasting](https://arxiv.org/abs/2606.05373)

**<font color=#1a73e8>作者：</font>** Md Azharul Islam, Dwyer Deighan, Tarunraj Singha 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reliable neural architecture selection is an open challenge in time-series forecasting under limited, noisy, and heterogeneous data, where standard heuristic architecture design and validation approaches fail to ensure accurate and reliable prediction and generalization. We propose EVIDENT (EVidence-based IDEntification of Neural archiTectures), a framework for architecture selection that integrates Bayesian training, evidence-based ranking, and task-specific validation under uncertainty. The framework explores the candidate architecture pool and identifies the lowest-capacity model that satisfies a prescribed validation criterion. We demonstrate this method using temporal convolutional networks (TCNs) for individualized blood glucose forecasting in type 1 diabetes patients. The results show that EVIDENT systematically rejects both under- and over-parameterized TCN architectures on population-level diabetes data, while identifying models that generalize reliably to unseen patients. When multiple architectures are competitive, the framework further supports plausibility-weighted ensemble predictions that enhance predictive performance. Compared with a random-search baseline, EVIDENT identified smaller architectures with more consistent forecasting performance on unseen patients. These findings establish EVIDENT as a strategy to neural architecture discovery, enabling reliable model selection for high-consequence forecasting in data-limited and heterogeneous settings.

---


### 45. [Three-Dimensional Retinal Microvasculature Restoration in OCT Angiography](https://arxiv.org/abs/2606.05375)

**<font color=#1a73e8>作者：</font>** Yukun Guo, Min Gao, Tristan T. Hormel 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Optical coherence tomographic angiography (OCTA) is a powerful technique for imaging retinal microvasculature. However, acquiring reliable quantification of retinal blood flow and areas of retinal nonperfusion is challenging because of imaging artifacts. Existing methods primarily focus on noise suppression, projection artifact removal, or signal enhancement to improve the image quality of OCTA in cross-sectional or two-dimensional (2D) en face projections, while neglecting the intrinsic three-dimensional vascular architecture. In this study, we propose a deep learning-based algorithm for restoring capillary anatomical vasculature from a single OCTA volume. The network consists of an EfficientNet-B5 encoder and a decoder incorporating concurrent spatial and channel squeeze-and-excitation modules, connected via skip connections to preserve spatial resolution. Three adjacent B-frames are used as input to predict the restored middle B-frame. We evaluated the performance of the model using the peak signal-to-noise ratio (PSNR) and structural similarity index measure (SSIM) against ground truth generated from averaging multiple scans. The results show that the proposed model significantly (both p < 0.001) improved image quality compared with the original single OCTA volume, with a PSNR of 26.16 +/- 1.26 vs. 22.23 +/- 0.78 and an SSIM of 0.91 +/- 0.02 vs. 0.72 +/- 0.03. The proposed model also significantly (p < 0.001) improved microvascular fidelity, measured by the Dice coefficient overlap between the model output and ground truth, in both 2D and 3D by at least 3.8% and 51.2%, respectively, across several different vascular slabs.

---


### 46. [Deep Learning-assisted AMD Staging based on OCT and OCT Angiography](https://arxiv.org/abs/2606.05379)

**<font color=#1a73e8>作者：</font>** Yukun Guo, Tristan T. Hormel, An-Lun Wu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> To develop and evaluate deep learning models for automated grading of age-related macular degeneration (AMD) severity using optical coherence tomography (OCT) and OCT angiography (OCTA) data. Two hundred seventy-one participants aged >= 50 years with varying AMD severities. Central macular 6 x 6 mm OCT/OCTA volumes were acquired using a swept-source OCTA system (SOLIX; Visionix/Optovue Inc., CA). AMD severity was graded into four stages (No AMD, Early AMD, Intermediate AMD, and Advanced AMD) according to the AREDS simplified severity scale. Three deep learning models were developed using different input modalities: (1) biomarker maps derived from segmented pathological features, including retinal fluid, drusen, geographic atrophy (GA), and macular neovascularization (MNV); (2) two-dimensional (2D) en face OCT and OCTA projections; and (3) three-dimensional (3D) OCT/OCTA volumes. EfficientNet-based architectures were trained using normalized inputs, data augmentation, and five-fold cross-validation. A total of 2,030 OCT/OCTA volumes from 351 eyes of 271 participants were analyzed. All models demonstrated strong AMD staging performance with substantial agreement with the reference standard (QWK >= 0.83). The biomarker-based model achieved the highest overall performance (QWK = 0.85 +/- 0.03, mean +/- standard deviation) and the best detection of early AMD (F1-score = 0.59 +/- 0.14). The 3D model achieved performance comparable to the 2D OCT/OCTA model (QWK = 0.83 +/- 0.04 vs. 0.83 +/- 0.09), while the 2D OCT/OCTA model showed the highest precision (0.79 +/- 0.06) and most accurately identified eyes without AMD. Deep learning models using OCT/OCTA data can accurately and automatically grade AMD severity. Among the evaluated approaches, the biomarker-based model provided the most balanced performance and showed particular value for early AMD detection.

---


### 47. [Generalized TV--$\ell_p$ Structured Priors for Bayesian $T_1$ Mapping](https://arxiv.org/abs/2606.05381)

**<font color=#1a73e8>作者：</font>** Disi Lin, Martin Berggren, Tommy Löfstedt  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose an extended family of structured spatial priors that incorporates the total variation (TV) function with $\ell_p$ norms. The prior is proven to be proper and incorporated into a Bayesian regression framework to enable uncertainty quantification in $T_1$ mapping, with posterior inference performed using the No-U-Turn Sampler (NUTS). This TV--$\ell_p$ construction is proven to constitute a well-defined family of prior distributions, and it naturally enforces spatial consistency and smooth variations in the estimated parameter maps. The method was evaluated in comparison to maximum-likelihood estimation and several Bayesian alternative priors based on the uniform, Gamma, and bounded TV priors. The evaluation includes experiments on synthetic brain and cardiac $T_1$ mapping datasets, as well as a real in-vivo breast $T_1$ mapping dataset. The results show that the TV--$\ell_p$ prior yields more concentrated posterior densities, indicating reduced uncertainty. It also consistently achieves lower variance and smaller (negative) bias, leading to more reliable estimates. Overall, embedding a TV-based structured penalty along with $\ell_p$ norms in a prior in a Bayesian model improves spatial coherence in $T_1$ maps and enhances uncertainty quantification, offering a robust approach for $T_1$ mapping with uncertainties.

---


### 48. [Residual Modeling for High-Fidelity Learned Compression of Scientific Data](https://arxiv.org/abs/2606.05389)

**<font color=#1a73e8>作者：</font>** Liangji Zhu, Sanjay Ranka, Anand Rangarajan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Lossy compression is essential for massive spatiotemporal data from scientific simulations. Learned compressors can achieve high compression ratios at moderate accuracy targets, but their aggregate reconstruction losses do not guarantee accuracy for each block. Existing Guaranteed Autoencoder (GAE) methods add a per-block residual correction by retaining SVD/PCA-style coefficients until the target is met. This works at moderate tolerances, but in the high-fidelity regime with block-level NRMSE from 10^-6 to 10^-4, the number of retained coefficients grows quickly and the correction stream dominates the total rate.
We propose a residual-centric view: the learned residual is structurally different from the original scientific field and should be coded with a representation designed for that residual. We introduce two residual coders. LBRC is a deterministic, training-free pipeline that adaptively quantizes the learned residual to the target NRMSE and losslessly encodes the resulting integer residual using 3D Lorenzo differencing, zigzag mapping, bit-plane coding, and entropy coding. NGLR adds a causal neural predictor that outputs a normalized bias for an integer-rounded Lorenzo prediction in the same deterministic integer pipeline, reducing the entropy of the remaining residual code while preserving deterministic decoding. The predictor weights are serialized and counted in the bitstream.
Across E3SM, JHTDB, and ERA5 at block-level NRMSE targets from 10^-6 to 10^-4, LBRC improves compression ratio over GAE by 30-60% and is broadly competitive with SZ. NGLR adds a further 10-40% over LBRC and outperforms SZ in the evaluated high-fidelity regime. These results show that residual representations tailored to learned-compressor residuals can preserve the advantage of learned compression when global residual correction becomes rate-dominant.

---


### 49. [UniPixie: Unified and Probabilistic 3D Physics Learning via Flow Matching](https://arxiv.org/abs/2606.05399)

**<font color=#1a73e8>作者：</font>** Qilin Huang, Quynh Anh Huynh, Long Le 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing feed-forward networks excel at predicting a single set of physical properties from visual appearance, but this point-estimate paradigm fundamentally fails to capture the real world's inherent physical ambiguity. We address this by reframing physics prediction as a task of learning a controllable, continuous distribution of material properties. We introduce UNIPIXIE, a framework trained to predict a continuous and parameterized path of physically plausible material properties from a single visual input. By learning a direct mapping along an object's softest-to-stiffest spectrum on our PIXIEMULTIVERSE dataset, UNIPIXIE allows for controllable generation of diverse, physically valid material fields via a single intuitive parameter. Crucially, UNIPIXIE introduces a novel unified architecture to produce simulation-ready parameters for diverse physics solvers, including continuum-based Material Point Method (MPM), reduced-order deformation based on Linear Blend Skinning (LBS), and anchor-based Spring-Mass systems, addressing a key portability issue in prior work. Experiments show our approach not only generates a rich variety of plausible dynamics but also reduces Young's Modulus prediction error by over 50% against the strongest deterministic baseline, bridging the gap between static point estimates and the continuous nature of physical reality. Project page: this https URL

---


### 50. [LeanMarathon: Toward Reliable AI Co-Mathematicians through Long-Horizon Lean Autoformalization](https://arxiv.org/abs/2606.05400)

**<font color=#1a73e8>作者：</font>** Yuanhe Zhang, Yuekai Sun, Taiji Suzuki 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-horizon autoformalization of research mathematics fails not only at hard lemmas, but at scale: statements drift, dependencies tangle, context decays, and local repairs corrupt distant work. We present LeanMarathon, a multi-agent harness for reliable research-level Lean autoformalization. Its core abstraction is an evolving blueprint: a Lean file that serves simultaneously as formal proof skeleton, natural-language proof graph, and shared system of record. Four contract-scoped agents construct, audit, prove, and repair this blueprint. These agents are coordinated by a two-stage orchestrator that first stabilizes target fidelity through adversarial review and then discharges the proof directed acyclic graph (DAG) from its dynamic leaves upward in parallel CI-gated rounds. LeanMarathon turns one brittle multi-hour run into many local, recoverable, parallel transactions. We evaluate LeanMarathon on two recent research papers spanning four Erdős problems (#1051, #1196, #164, #1217). Across three autonomous runs, it formalizes all seven target theorems with no sorry, proving 258 lemmas and theorems. These results show that reliable AI co-mathematics requires not only stronger provers, but durable harnesses that preserve target fidelity across long mathematical developments. The code can be found at this https URL.

---


> [!TIP]
> 当前位于：**1-50**（第 1/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-289](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
