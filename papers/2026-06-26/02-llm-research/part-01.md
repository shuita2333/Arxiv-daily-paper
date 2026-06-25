# 🧠 大模型相关研究 | 2026年06月26日

> 本类共 **112** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**1-50**（第 1/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-112](./part-03.md)

---

### 1. [Small edits, large models: How Wikipedia advocacy shapes LLM values](https://arxiv.org/abs/2606.24890)

**<font color=#1a73e8>作者：</font>** Jasmine Brazilek, Maria Navas, Alexa Gnauck  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Can a small group of volunteers shape how AI systems discuss animal welfare, just by editing Wikipedia? We show that they can. Wikipedia appears in nearly every major language model training dataset and is weighted more heavily than web-crawled text. The Pro-Animal Wikipedians (PAW), a group of advocates who add sourced animal welfare content to relevant articles, have made 125 edits across 115 pages. Using gradient-based data attribution (Bergson; MAGIC), we traced how these edits influence language model behavior. TrackStar retrieval attribution on Llama 3.1 8B found that PAW-edited sections made up 68 percent of the highest-attributed documents for animal welfare queries (p < 0.0001) but only 52 percent for unrelated queries about the same companies (p = 0.53): the model links PAW content specifically to animal welfare topics, not to the entities in general. MAGIC counterfactual influence estimation on Llama-3.2-1B, run across five random training-order seeds, gave the same picture even more sharply: in every seed, the top-10 most influential documents on animal welfare queries were all PAW edits (10 of 10, 5 of 5 seeds), while on general queries the same top-10 sat at chance (4 to 6 of 10). Mean PAW influence exceeded mean control influence on animal welfare queries with p < 0.0001 in every seed, an effect 6 to 30 times larger than on general queries. Leave-subset-out validation gave Spearman rho = 1.00 for all 10 runs. When we fine-tuned separate models on PAW content versus control content, each model performed better specifically on the type of text it was trained on: the PAW-trained model cut perplexity on animal welfare text from 12.4 to 8.4, while the control-trained model cut perplexity on control text from 16.1 to 11.4. A small, coordinated Wikipedia editing campaign therefore measurably shapes how language models handle the topics those edits address.

---


### 2. [Dense Supervision Is Not Enough: The Readout Blind Spot in Looped Language Models](https://arxiv.org/abs/2606.24898)

**<font color=#1a73e8>作者：</font>** Rituraj Sharma, Tu Vu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Looped language models turn hidden states into runtime state: each state is decoded for prediction and fed back into future computation. This creates a basic supervision question: which state variables does cross-entropy actually control? We show that dense per-loop cross-entropy controls the variables exposed by the readout, not every variable active in the recurrent transition. Hidden-state scale gives a concrete failure mode. Scale-invariant readouts such as RMSNorm and LayerNorm hide radial scale from the immediate cross-entropy loss, while pre-norm residual recurrence continues to carry and update that same scale. Thus per-loop loss can make early exits usable without controlling recurrent scale. In 44M and 129M looped transformers without inter-loop normalization, per-loop cross-entropy through RMSNorm readouts still drives final hidden-state norms into the thousands or tens of thousands. Scale-visible readouts and explicit norm penalties keep norms in the tens, and scale-removing recurrence is the complementary architectural fix. The resulting design rule is simple: dense supervision trains exits; recurrent scale control requires either making scale visible to a loss or removing it from the loop. Consistent with this rule, scale-controlled variants achieve lower perplexity at matched inference-depth operating points in our variable-depth benchmarks.

---


### 3. [LLM Evolution as an Industry-Scale Ecosystem: A Lifecycle Perspective on Continual Learning](https://arxiv.org/abs/2606.24901)

**<font color=#1a73e8>作者：</font>** Hao Jiang, Enneng Yang, Guojie Zhu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continual learning capability is critical for Industrial LLMs, as deployed models must be continuously updated to meet evolving requirements and environments, rather than repeatedly retrained from scratch. However, most existing research focuses on improvements on static benchmarks, failing to capture real industrial needs. In this survey, we reformulate Industrial Continual Learning (ICL) for LLMs as a closed-loop update-and-release problem in a versioned ecosystem, where updates propagate hierarchically to industrial, application-specific models and LLM-powered applications, with capability inheritance and transfer across versions and model families. From this ecosystem perspective, we identify three core challenges: repeated adaptation erodes model plasticity, foundation-model upgrades break capability inheritance, and long-term sustainability is constrained by deployment requirements. We then organize the technical landscape of ICL around five lifecycle design principles: preserving plasticity headroom, treating upgrades as capability transfer, enabling trustworthy continual reinforcement learning, making training recipes self-optimizing, and building accountability as a base layer for long-term iteration. For each principle, we synthesize representative technical directions. Finally, we evaluate the maturity of each principle and its technical components via an evidence-based lens, identify key gaps hindering real-world deployment, and outline a practical ICL deployment blueprint and a pathway for feeding industrial realities back into academic research.

---


### 4. [Error-Aware TF-IDF Retrieval-Augmented Generation for ASR Error Correction](https://arxiv.org/abs/2606.24915)

**<font color=#1a73e8>作者：</font>** Mohammad Aref Jafari-Raddani  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> End-to-end automatic speech recognition systems frequently hallucinate rare entities and domain-specific terms, especially in low-resource languages. While retrieval-augmented generation frameworks can mitigate these errors using large language models, current architectures face significant challenges. They either rely on standard sparse retrieval that ignores phonetic misrecognitions or utilize heavyweight cross-modal embeddings that introduce high latency. This letter proposes a highly efficient, purely lexical error-aware framework designed to explicitly resolve phonetic and loop hallucinations. Our approach integrates a symmetric text normalization module with a novel error-aware term frequency-inverse document frequency algorithm. By constructing a sparse diagonal penalty matrix based on historical errors, the retriever mathematically prioritizes corrective documents containing specific high-risk misrecognitions. Evaluated on the Persian subset of the FLEURS dataset, our method increased the error-aware hit rate from 53.7% to 90.9%. In end-to-end evaluations, the integrated framework reduced the final word error rate from 23.06% to 18.83%, achieving significant accuracy gains with near-zero inference latency.

---


### 5. [The Hitchhiker's Guide to Agentic AI: From Foundations to Systems](https://arxiv.org/abs/2606.24937)

**<font color=#1a73e8>作者：</font>** Haggai Roitman  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The Hitchhiker's Guide to Agentic AI is a comprehensive practitioner's reference for building autonomous AI systems. The book covers the full stack from first principles to production deployment, organized around a central thesis: building great agentic systems requires understanding every layer of the pipeline, not just one. The book opens with the LLM substrate -- transformer architecture, GPU systems, training and fine-tuning (SFT,LoRA, MoE), model compression, and inference optimization -- treated as essential foundations rather than the primary focus. It then develops the alignment and reasoning layer: reinforcement learning from human feedback (RLHF), PPO, DPO and its variants, GRPO, reward modeling, and RL for large reasoning models including chain-of-thought and test-time scaling. The second half is devoted to agentic AI proper. Topics include agentic training and trajectory-based RL, retrieval-augmented generation (RAG and Agentic RAG), memory systems (in-context, external, episodic, and semantic), agent harness design and context management, and a taxonomy of agent design patterns. Inter-agent coordination is covered in depth: the Model Context Protocol (MCP), agent skills and tool use, the Agent-to-Agent (A2A) communication protocol, and multi-agent architectures spanning centralized, decentralized, and hierarchical topologies. The book concludes with agent development frameworks, agentic UI design, evaluation methodology for agentic tasks, and production deployment. Each chapter pairs rigorous theoretical foundations with implementation guidance, code examples, and references to the primary literature.

---


### 6. [When Do Conservation Laws Survive Learned Representations? Certified Horizons for Latent World Models](https://arxiv.org/abs/2606.24945)

**<font color=#1a73e8>作者：</font>** Hongbo Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We ask a representation-learning question about physical world models: when does a conservation law remain certifiable after a model learns a latent representation? A certified horizon bounds -- in advance, from measurable model defects -- how many steps a rollout provably stays on a physical invariant's level set. The key design choice is what is certified: not a learned latent Hamiltonian or a learned scalar witness (a model can conserve either while drifting in true energy), but the decoded physical invariant obtained by decoding the latent state and evaluating the known invariant. Around this object we derive shell-horizon certificates whose budget decomposes into representation, readout, and latent-dynamics defects, with a monotone alignment bridge through which a soft learned witness yields a certified horizon for the decoded invariant, and test them across state, learned-lift, and pixel observations on conservative systems. Conservation certificates can survive learned representation, but not all geometric priors survive equally: hard canonical symplectic structure yields the longest horizons in known phase coordinates yet does not cross a learned chart, whereas a controlled-Lipschitz-aligned soft invariant survives in the learned-representation settings we test; pixel certification is recovered on a readout-stable sub-tube; and the Kepler problem exposes a geometric boundary. The central object is therefore not a latent Hamiltonian, but a decoded physical invariant whose robustness to representation learning can be measured, certified, and falsified.

---


### 7. [Conformal Orbit-Valid Trust Horizons for Equivariant World Models](https://arxiv.org/abs/2606.24946)

**<font color=#1a73e8>作者：</font>** Hongbo Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learned world models are useful only over horizons on which their rollout error remains controlled. We study trust-horizon certification for latent world models with known group symmetries. Given a one-step latent residual and a finite-time expansion estimate, we form a raw horizon curve and calibrate it with a split-conformal multiplicative factor. On the reproducible audit set, the conformal factor is $\gamma_\alpha=1.0$: the raw certificate is already conservative under the audit protocol. Across 50 stable audits, we observe zero anti-conservative violations, corresponding to an exact-binomial 95% upper bound of 5.8% on the violation rate. Our main structural result is that exact equivariance transports a calibrated trust-horizon curve over the group orbit: when the environment dynamics, encoder, predictor, action transform, and latent metric satisfy the stated equivariance/invariance conditions, rollout errors and trust horizons are orbit-constant. Empirically, the implemented models exhibit small orbit-transport residuals, with median 1.1% and maximum 4.1% over 14 orbit audits. The certificate is also non-vacuous (median certified-to-measured horizon ratio 0.67). A certificate-level calibration-cost study shows two complementary regimes. On a symmetric 2D substrate, equivariant, plain, and augmented models are all orbit-valid from a single calibration sector -- no separation, because the substrate already makes non-equivariant baselines approximately orbit-robust. A 3D yaw audit shows the other regime: the equivariant model obtains a one-sector safe and non-vacuous orbit-valid certificate, while healthy non-equivariant baselines pay violation, slack, sharpness, or additional-sector cost. The certificate is a conservative, distributional audit rather than a global reachability guarantee, and certificate-guided subgoal spacing is not confirmed in the current 3D CEM-MPC behavior layer.

---


### 8. [MacroLens: A Multi-Task Benchmark for Contextual Financial Reasoning under Macroeconomic Scenarios](https://arxiv.org/abs/2606.24950)

**<font color=#1a73e8>作者：</font>** Patara Trirat, Jin Myung Kwak, Jay Heo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Financial decision-making is contextual: forecasting prices, valuing companies, and assessing event exposure weigh price history, accounting fundamentals, macroeconomic regime, and contemporaneous text. A benchmark over these four signals is hard to build because finance violates four assumptions of time-series evaluation: text must be gated by its publication date to prevent look-ahead, quarterly fundamentals are reported with a one- to ninety-day lag, filing text is partly redundant with the numerical statement fields it accompanies, and macroeconomic regimes leak across calendar splits. No public benchmark addresses all four signals jointly. MacroLens covers 4,416 U.S. small- and micro-cap equities over 2021-2026. Seven tasks share one point-in-time panel of prices, 46.8M XBRL accounting facts, 53 macroeconomic series, 295,860 SEC filings, and 215,882 news articles, plus a scenario layer of 1,130 macroeconomic events across 49 types automatically detected and rendered as natural language. Tasks span contextual forecasting, public and private valuation, statement generation from fundamentals and descriptions, scenario-conditioned returns, and real-estate valuation. We evaluate 19 methods across six families spanning naive heuristics through time-series foundation models, fine-tuned LLM-based time-series models, and zero-shot large language models (LLMs), plus a five-step feature-context ablation on two frontier LLMs and a gradient-boosted baseline. MacroLens is released at this https URL.

---


### 9. [Perfect Detection, Failed Control: The Geometry of Knowing vs. Steering in Language Models](https://arxiv.org/abs/2606.24952)

**<font color=#1a73e8>作者：</font>** Cosimo Galeone, Anna Ettorre, Minsu Park 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A central aspiration of mechanistic interpretability is controllability: if we know where a behavior is represented in a model's activations, we should be able to modify it. This rests on a hidden premise -- that the direction which detects a behavior and the direction which controls it are the same, or close. We test this geometrically: what is the angle between the direction that best detects a behavior and the one that best causes it? If detection implies control the cosine is near 1; otherwise it quantifies a detection-intervention gap. On Gemma 2-2B-it, output format (clean JSON vs markdown fencing) collapses both roles onto one axis. Hallucination does not: the model detects fake entities with perfect linear separability (AUC = 1.000 from layer 5), yet that direction sits at cos = 0.12 (about 83 degrees) from the direction producing a refusal -- a small, reproducible alignment, far from the cos = 1 that "detection is control" would require. A detector built from activations, with no chosen tokens, likewise fails to align (cos = -0.06). The gap generalizes: across four models from three families and two scales (1B-9B), cos stays in [0.12, 0.20], identical before and after instruction tuning (0.1197 vs 0.1200), placing its origin in pretraining. A 15-degree rotation toward the refusal direction partially bridges it -- 73% and 60% refusal on two held-out fake-entity categories at 1.8% false positives. We then ask whether this cosine predicts steerability, and it does not: detection is a high-dimensional class, not a single direction, and what separates the steerable case is functional, not readable from a static angle. The cosine is a weight-computable signature of the dissociation between knowing and steering, not a predictor of it.

---


### 10. [Digital Twin-Driven Adaptive Sim-to-Real Alignment via Reinforcement Learning for Vibration-Based Bearing Health Monitoring Under Data Scarcity](https://arxiv.org/abs/2606.24954)

**<font color=#1a73e8>作者：</font>** Jinghan Wang, Yanjun Chen, Wei Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Vibration-based health monitoring of rotating machinery requires reliable fault diagnosis under operational data constraints, yet condition assessment remains challenged by structural scarcity of fault events and heterogeneous sim-to-real gaps in digital twin-generated signals. Each fault type generates impulses with distinct periodicity, amplitude modulation, and spectral character, making feature-space discrepancies fundamentally heterogeneous across fault classes. Existing domain adaptation methods apply a class-agnostic global transformation that cannot close all fault-specific gaps without distorting inter-class separability, while uniform source-target mixing introduces distributional noise into the data-abundant Normal class. These limitations stem from treating a sequential, state-dependent alignment problem as a one-shot optimization. Each corrective transformation simultaneously reshapes all class distributions, creating state dependencies that static gradient descent cannot resolve. We formulate feature alignment as a continuous-action Markov decision process solved via Proximal Policy Optimization, where the learned policy issues fault-type-specific affine corrections responsive to the current feature-space configuration, with a dual-objective reward balancing gap minimization against separability preservation. An asymmetry-aware strategy reserves real data for the Normal class while augmenting fault classes with policy-aligned simulated samples. Validation across XJTU-SY, CWRU, and a self-built slewing bearing testbed confirms the dominant gain from reinforcement learning-driven alignment, and cross-equipment linear probing achieves 92.8% without encoder retraining, demonstrating transferable monitoring capability.

---


### 11. [Dustin: Draft-Augmented Sparse Verification for Efficient Long-Context Generation with Speculative Decoding](https://arxiv.org/abs/2606.24957)

**<font color=#1a73e8>作者：</font>** WenHung Lee, Jian-Jia Chen, Xiaolin Lin 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While speculative decoding improves inference throughput for multi-batch long-context Large Language Models (LLMs), its efficiency is often limited by a verification bottleneck where Key-Value (KV) cache loading dominates latency. Existing compression methods fail in this regime: static eviction incurs accuracy loss due to saliency shift, while dynamic selection introduces prohibitive computational overhead during the verification path. We propose Dustin, a sparse verification framework designed for long-context speculative decoding. Dustin integrates lookahead signals from the draft model with historical attention from the target model to identify critical tokens with high fidelity across multi-step verification windows. To reduce recomputation latency, this approach further employs a sparse estimation scheme that restricts importance scoring to a minimal subset of attention heads. Evaluations on PG-19 and LongBench with Qwen2.5-72B demonstrate that Dustin achieves a 27.85x speedup in self-attention and a 9.17x end-to-end decoding speedup at a 32k sequence length, all with negligible accuracy degradation.

---


### 12. [Curvature-Guided Mixing for MLLM Adaptation](https://arxiv.org/abs/2606.24963)

**<font color=#1a73e8>作者：</font>** Jinglong Yang, Jiaxuan He, Wenjian Huang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Fine-tuning Multimodal Large Language Models (MLLMs) on specialized tasks often leads to catastrophic forgetting of their general capabilities. Existing model merging methods to combat this are often heuristic or use sub-optimal objectives. We propose CurvatureGuided Mixing (CGM), a theoretically grounded framework that merges pre-trained and fine-tuned models. CGM formulates a joint optimization objective and uses a second-order (Hessian) approximation of the loss landscapes to analytically derive an optimal, closed-form "soft mixing" ratio. This ratio intelligently blends parameters based on their relative task-specific curvatures. We also introduce CGM$\dagger$, a robust "hard mixing" variant that performs sparse parameter selection guided by a novel, curvature-aware score. Experiments on LLaVA-1.5 and Qwen2.5VL across multiple downstream tasks show that CGM and CGM$\dagger$ consistently improve the trade-off between task specialization and general knowledge retention over existing methods. Code is available at this http URL.

---


### 13. [Evidence for feature-specific error correction in LLMs](https://arxiv.org/abs/2606.24964)

**<font color=#1a73e8>作者：</font>** Francisco Ferreira da Silva, Stefan Heimersheim  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Understanding the features of large language models (LLMs) is a central goal of interpretability. LLMs are commonly assumed to use superposition to represent more features than they have dimensions. They may not only represent features in superposition but also perform computation in superposition. Theory predicts that computing in superposition requires error correction that privileges feature directions over generic ones, but this prediction has not been tested empirically. We propose an empirical test of error correction in LLMs based on activation perturbations. Perturbing residual-stream activations, we find that they are robust to small perturbations--forming activation plateaus consistent with error correction--but less robust along candidate feature directions ("pure" directions, constructed from contrastive prompt pairs) than along mixtures of two such directions, indicating that the pure directions are privileged. We quantify this privilegedness by modeling the perturbation effect as a function of the $L^p$-norm of its decomposition into feature components. For $p=2$ the response is a quadratic form with at most as many nonzero eigenvalues as the residual-stream dimension, which cannot privilege the many feature directions superposition requires. $p>2$ lifts this constraint and is consistent with feature-specific error correction. We find $p>2$ for contrastive, MELBO, and SAE-decoder directions, and $p\approx2$ for random and PCA directions (controls). These results replicate across Gemma-2-9B, Qwen3-1.7B, Llama-3.1-8B, Mistral-7B-v0.3, Aya-Expanse-8B, and Yi-1.5-9B. We further validate our method on a toy model of error correction with known ground-truth features, recovering $p>2$ for true feature directions, degrading toward $2$ as we rotate away from them.

---


### 14. [Project Auto-World: Towards Automated Benchmarking of Neural Relational Reasoners](https://arxiv.org/abs/2606.24965)

**<font color=#1a73e8>作者：</font>** Anirban Das, Joanne Boisson, Irtaza Khalid 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reasoning about relational structures remains a significant challenge for neural models, particularly when they must systematically apply learned knowledge to problem instances that are harder than those seen in training. Progress is hampered by the difficulty of evaluating such generalization, since a priori, it is rarely clear what makes an instance hard. We study how this issue can be addressed by using large language models (LLMs) to automate benchmark generation, learning to produce increasingly challenging instances in an end-to-end manner. Concretely, given a world parametrized by Datalog rules, and an Edge Transformer as the reasoning evaluator, we use LLM-driven evolutionary search (based on FunSearch) and autonomous agentic search to discover sampling functions that yield hard problem instances. We also show that the Edge Transformer can be improved using this data such that it generalizes well to further data perturbations. Finally, we show that the same machinery can be applied to novel worlds proposed by LLMs, opening the door to autonomous research on neural relational reasoning.

---


### 15. [Don't Go Breaking My LLM: The Impact of Pruning Attention Layers on Explanation Faithfulness and Confidence Calibration](https://arxiv.org/abs/2606.24970)

**<font color=#1a73e8>作者：</font>** Pietro Tropeano, Maria Maistro, Tuukka Ruotsalo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Pruning Large Language Models (LLMs) reduces memory and inference costs by removing parts of the network, producing smaller models that retain most of their accuracy. As attention layers are the most resource-intensive parts of LLMs, pruning them is a promising compression strategy. Prior work shows that up to 33% of attention layers can be pruned with minimal accuracy loss. Nevertheless, the impact of attention pruning on model interpretability, specifically faithfulness and confidence calibration, remains unstudied. To address this gap, we study how pruning attention layers affects explanation faithfulness and confidence calibration across five LLMs and eight datasets. While the pruned models often maintain high accuracy, we find that their faithfulness and calibration often degrade. Notably, faithfulness and calibration can fluctuate significantly, even when accuracy remains stable, highlighting a misalignment between model confidence, interpretability, and accuracy. Our findings suggest that layer pruning can affect LLMs' interpretability and reliability in ways not captured by accuracy and efficiency measures alone. We recommend including explainability and calibration metrics when evaluating pruned models.

---


### 16. [LLM Performance on a Real, Double-Marked GCSE Benchmark](https://arxiv.org/abs/2606.24973)

**<font color=#1a73e8>作者：</font>** Malachy Fox, Kavi Samra, Paul Jung  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We introduce a dataset of 32,534 double-marked real student responses to GCSE mock exams (GCSEs are the UK's national exams, taken at age ~16), spanning 328 questions across five subjects and including handwritten work. We test whether off-the-shelf large language models agree with examiners as closely as the two examiners agree with each other. We find that models overwhelmingly agree well with the examiner consensus across subjects, with the top performing models agreeing more closely with examiners than examiners agree with each other. Models achieve high scores for subjective tasks like English essay marking, as well as handling complex and messy handwritten Maths paper scripts. Agreement is uniform near the examiner line, and not massively discriminated by model size, providing cost-effective automated marking solutions.

---


### 17. [Diagnosing and Mitigating Compounding Failures in Agentic Persuasion via Taxonomic Strategy Retrieval](https://arxiv.org/abs/2606.24976)

**<font color=#1a73e8>作者：</font>** Pradyumna Narayana, Sana Ayromlou, Purvi Sehgal  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Foundation-model agents in multi-step, open-ended environments frequently suffer from compounding errors, where early mistakes contaminate long-horizon trajectories. While Multi-Agent Debate (MAD) succeeds in deterministic domains, agents in subjective tasks like persuasion experience severe problem drift and sycophantic conformity. We identify semantic leakage in standard Retrieval-Augmented Generation (RAG) as a reproducible trigger for these failures, as standard RAG prioritizes vocabulary overlap over logical necessity.
To eliminate this leakage, we introduce Taxonomic Strategy RAG (TS-RAG), a systems intervention that routes strategies through a discrete categorical bottleneck to decouple argumentative structure from topical content. Zero-shot, cross-domain evaluations demonstrate that TS-RAG significantly improves the transfer of abstract logic where standard semantic retrieval collapses. Crucially, TS-RAG acts as a "capability bridge" in asymmetric deployments, empowering lightweight persuaders to consistently defeat parametrically superior opponents (improving win rates from 70.5 to 78.5) and accelerating argumentative efficiency. Finally, we introduce trace-level diagnostics via a turn-by-turn Debate State Representation (DSR), demonstrating the necessity of strict constraints to prevent evaluation collapse via default agentic sycophancy.

---


### 18. [Closed-Loop Graph Algorithm Execution with Small Language Models: Step Accuracy and Rollout Reliability](https://arxiv.org/abs/2606.24980)

**<font color=#1a73e8>作者：</font>** Michal Podstawski  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Small language models offer an efficient alternative to large-scale systems, but their ability to execute structured algorithms over multiple dependent decisions remains poorly understood. We study graph algorithm execution as a closed-loop prediction problem in which a model repeatedly selects the next action from the current graph and algorithmic state. Our evaluation framework covers several classical graph procedures, multiple synthetic graph families, and disjoint training, validation, and test partitions. It assesses both local decision quality and global execution behaviour using step accuracy, exact rollout accuracy, constraint validity, partial solution quality, prefix survival, and intervention-based diagnostics. The results show that adaptation can produce reliable policies for structural procedures such as traversal and coloring, while weighted algorithms remain substantially more sensitive to error accumulation. More broadly, the findings demonstrate that strong next-step prediction does not necessarily translate into reliable autonomous execution and motivate evaluating algorithmic language models through complete closed-loop rollouts rather than isolated decisions.

---


### 19. [A Single Stepsize Suffices for Unprojected Linear TD(0): Simultaneous Robust and Fast Rates via Polyak--Ruppert Averaging](https://arxiv.org/abs/2606.24981)

**<font color=#1a73e8>作者：</font>** Wei-Cheng Lee, Francesco Orabona  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study linear TD(0) under Markovian sampling, where data are generated along a single trajectory. We provide high-probability guarantees for a plain unprojected TD(0) algorithm with Polyak-Ruppert (PR) averaging, using a single stepsize schedule $\eta_t \propto \frac{1}{\tau_{\mathrm{mix}}\log(t)\sqrt{t}}$ that depends on the mixing time but requires no prior knowledge of the curvature parameter $\omega$. Our first result shows that such a choice of the stepsize guarantees that the TD(0) iterates are automatically and uniformly bounded with high probability, without projections and without any stability argument based on $\omega$. Building on this result, we establish a simultaneous high-probability convergence guarantee for the PR average: the same stepsize yields both a robust curvature-free $\widetilde{\mathcal{O}}\!\left(\frac{\tau_{\mathrm{mix}}}{\sqrt{T}}\right)$ rate and a fast curvature-dependent $\widetilde{\mathcal{O}}\!\left(\frac{\tau_{\mathrm{mix}}^2}{\omega T}\right)$rate, with the bound taking the minimum of the two. The core technical ingredient is a Poisson-equation toolkit for geometrically mixing Markov chains, which decomposes Markov noise into a martingale term plus a controlled remainder and enables a new self-bounding inductive argument for pathwise stability.

---


### 20. [Retrieval-Augmented Personalization with Foundation Models for Wearable Stress Detection](https://arxiv.org/abs/2606.24985)

**<font color=#1a73e8>作者：</font>** Louis Simon, Mohamed Chetouani  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Personalization in wearable-based stress detection remains challenging due to substantial inter-individual variability in physiological and behavioral responses. While traditional approaches rely on user-specific fine-tuning or costly self-supervised pre-training on large datasets, we propose a lightweight alternative based on retrieval-augmented personalization. Our method leverages frozen, out-of-domain foundation models to retrieve similar patterns from a target user's history and encode them into a compact personalized embedding that modulates representations extracted by a lightweight transformer network. We evaluate our approach on the WESAD stress detection dataset with N=15 users, comprising wrist-worn physiological (EDA, BVP, temperature) and activity (accelerometer) signals, and report gains of +3.92\% in accuracy and +4.76\% in macro F1-score over a non-personalized transformer baseline, approaching supervised fine-tuning performance without requiring any labeled user data. We further show that temporal retrieval, where only prior user samples are available, achieves performance close to full intra-user retrieval, demonstrating robustness to limited user history. Finally, we explore personalization in a cross-dataset retrieval setting, leveraging embeddings from the K-Emocon dataset to personalize representations for stress detection on the WESAD dataset.

---


### 21. [Uncertainty-aware reinforcement learning for chemical language models](https://arxiv.org/abs/2606.24990)

**<font color=#1a73e8>作者：</font>** Borja Medina, Jon Paul Janet  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement Learning (RL) has become a powerful paradigm for de novo molecular design, enabling Chemical Language Models (CLMs) to navigate and explore the chemical space while optimizing specific desired properties. However, the existing RL frameworks treat all scoring functions as deterministic oracles, neglecting the inherent uncertainty attached to the predictions of the different molecular properties. This can lead to the exploration of highly-uncertain regions of the chemical space, focusing on the generation of highly scored molecules which are poorly supported by the training data. This can destabilize the optimization process, yielding predictions that are far from their true values.
We propose and compare two complementary ways of incorporating predictive uncertainty into RL. In the first one, uncertainty is treated as an additional optimization objective and incorporated along with the rest of the scoring functions, allowing the policy to trade off exploitation against reliability. Secondly, uncertainty is used to modulate policy updates, reducing the influence of molecules whose properties lie far outside the scoring function confidence domain.
Both approaches were evaluated across three different settings: (i) a controlled model system, in which the prediction error is modeled as a Gaussian distribution, with a variance proportional to the distance to the training data; and two real-world tasks, making use of (ii) ChemProp models and (iii) a Conformal Prediction wrapper applied to a Random forest classifier.
We show that uncertainty-aware RL enables CLMs to explore chemical space more robustly by favoring lower-uncertainty regions. This leads to more reliable hit discovery without compromising molecular score, increasing the true hit rate by 0.25 (from 0.5 to 0.75), and nearly doubling the total number of true hits.

---


### 22. [ExTra: Exploratory Trajectory Optimization for Language Model Reinforcement Learning](https://arxiv.org/abs/2606.24994)

**<font color=#1a73e8>作者：</font>** Wenyang Hu, Junxiang Jia, Zhen Shu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement Learning with Verifiable Rewards (RLVR) for language-model reasoning can fail at both extremes of task difficulty: easy prompts often produce all-correct, low-diversity rollout groups with little gradient signal, while hard prompts can produce all-incorrect groups with no positive reward. We introduce ExTra (Exploratory Trajectory Optimization), a GRPO-compatible framework that extracts exploration signals from the model's own rollouts. ExTra combines two mechanisms: (i) a novelty reward that adds embedding-based diversity bonuses after GRPO normalization, rewarding diverse correct solutions; and (ii) entropy-guided prefix regeneration, which scores partial trajectories using entropy signals and continues exploration from promising intermediate steps. Across six mathematical reasoning benchmarks, ExTra improves Qwen3-1.7B over GRPO by about +5 points on pass@1 and +7 points on pass@16, showing that trajectory-level exploration signals can improve both single-sample accuracy and inference-time coverage.

---


### 23. [Are Tabular Foundation Models Robust to Realistic Query Distribution Shifts in Microbiome Data?](https://arxiv.org/abs/2606.24995)

**<font color=#1a73e8>作者：</font>** Giulia Perciballi, Ahmad Fall, Federica Granese 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tabular foundation models (TFMs) achieve strong performance on microbiome abundance data, yet their robustness under realistic distribution shift remains poorly characterized. We introduce a benchmark that evaluates the robustness of TFMs to biologically inspired perturbations across six gut microbiome datasets spanning four disease contexts. In this in-context learning setting, models receive unperturbed support sets as context and are evaluated on perturbed query samples. To isolate robustness beyond "shortcut" features, we preserve the most discriminative taxa and apply three controlled perturbation strategies: (i) removal of high-abundance (uninformative) taxa, (ii) sparsification via increased zero-inflation, and (iii) zero-imputation via spurious non-zero injections. Our results show that protecting discriminative features is insufficient to guarantee stability under support-query shift: across datasets, all perturbations degrade model performance, with zero-imputation consistently the most harmful, indicating that corrupting global feature structure can break generalization even when key taxa are retained. Sparsification disproportionately affects TFMs relative to a classical random forest baseline, suggesting greater sensitivity to zero-inflation-type shifts. The code is publicly available at: this https URL.

---


### 24. [Internal Data Repetition Destroys Language Models](https://arxiv.org/abs/2606.24998)

**<font color=#1a73e8>作者：</font>** Jessica Chudnovsky, Joshua Kazdan, Noam Levi 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Language models are running out of high-quality training data, and even aggressively deduplicated corpora retain some amount of repetition. Earlier controlled studies predated Chinchilla-style scaling laws and could only measure the cost of repetition indirectly. We revisit repetition in the Chinchilla era, using a fitted no-repetition scaling law to report Compute-Equivalent Gain and Compute-Equivalent Loss. We show that under this modernized paradigm, repetition damage is systematic in three ways. First, holding compute allocated to repeated data constant, eval loss peaks at an intermediate repeat count $\Rep$; repeating a moderately sized subset a moderate number of times damages performance more than repeating a large subset a few times or a small subset many times. Second, the location of this peak is well-fit by a power law in model size; this scaling law reveals that the most damaging number of repeated data grows more quickly than compute. Finally, when repeated documents consume 10\% of the FLOPs budget in a controlled exact-document repetition setting, the compute-equivalent loss can be large: on FineWeb-Edu-Dedup, the most damaging repeat count for a Qwen3-style 344M-parameter model at $\OT=1$ matches the loss of a no-repetition run using 67% of the FLOPs. We demonstrate that these phenomena are not language-model-specific, and can be analytically understood in a simple statistical model: a misspecified linear regression with verbatim duplicates reproduces the same qualitative loss peak, quantifying how such peaks can arise from a statistical tradeoff between memorization and generalization. Our findings add precision to the study of duplication in language models, allowing practitioners to quantify the wasted compute incurred by the presence and repeat structure of duplicates in pretraining corpora.

---


### 25. [Neural Scaling Universality: If Exponents Are Fixed, Time to Understand Coefficients](https://arxiv.org/abs/2606.25008)

**<font color=#1a73e8>作者：</font>** Yizhou Liu, Jeff Gore  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural scaling laws describe how pre-training loss decays as power laws with training time, model size, and compute. This position paper argues that the exponents of these power laws are fixed by generic mechanisms: a one-third time scaling due to the strong nonlinearity of Softmax, an inverse width scaling due to representational superposition, and an inverse depth scaling due to ensemble averaging of Transformer layers. These mechanisms are robust to a wide range of data structures and architectural details, placing current large language models in a universality class with fixed exponents. The coefficients, however, are expected to be sensitive to data and architecture details, and directly determine practical quantities such as the optimal model shape and the compute-optimal frontier. We therefore argue that understanding the coefficients is the key to near-term performance improvements, and that a closer examination of the current universality class may reveal pathways to better universality classes.

---


### 26. [Bias-Controlled Primal-Dual Natural Actor-Critic: Optimal Rates for Constrained Multi-Objective Average-Reward RL](https://arxiv.org/abs/2606.25012)

**<font color=#1a73e8>作者：</font>** Ankur Naskar, Swetha Ganesh, Vaneet Aggarwal  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many reinforcement learning (RL) problems in the infinite-horizon average-reward setting require optimizing multiple conflicting objectives while satisfying multiple safety constraints. A common approach is concave scalarization, where the agent maximizes a utility $ f(J^\pi_{r_1}, \ldots, J^\pi_{r_M}) $ subject to a scalarized constraint $ g(J^\pi_{c_1}, \ldots, J^\pi_{c_N}) \ge 0 $, where $J^\pi_{r_m}$ and $J^\pi_{c_n}$ denote the average-reward and cost under policy $\pi$. However, the nonlinearity of $f$ and $g$ introduces bias in policy-gradient and actor-critic methods, since gradients must be evaluated using noisy estimates of $J^\pi,$ and $ \mathbb{E}[\partial f(J^\pi)] \neq \partial f(\mathbb{E}[J^\pi]),$ and this bias propagates through both primal and dual updates. We propose an MLMC-based primal-dual Natural Actor-Critic algorithm for average-reward MDPs that controls bias in scalarized objectives, constraint evaluation, and actor-critic estimation without requiring mixing-time knowledge. We show that the algorithm achieves optimal global convergence and constraint-violation rates of $ \tilde{O}(1/\sqrt{T}) $. To our knowledge, this is the first result establishing optimal convergence for concave scalarized multi-objective RL in the average-reward setting, both with and without constraints, and the first to do so without mixing-time information even in the absence of scalarization.

---


### 27. [Do Thinking Tokens Help with Safety?](https://arxiv.org/abs/2606.25013)

**<font color=#1a73e8>作者：</font>** Narutatsu Ri, Abhishek Panigrahi, Sanjeev Arora  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Today's reasoning models use thinking tokens to attain stronger performance on benchmarks than their instruction-tuned counterparts. It is also generally believed that this more "deliberative" mode should improve alignment and safety, by providing the model a safe space to consider whether its planned answer to a request violates its safety principles. We present evidence that this intuition is not always correct. Across frontier open-weight reasoning models spanning GPT-OSS, Qwen, Olmo, and Phi families, we find that the eventual refusal/compliance outcome is already strongly predictable via a trained head on the first token's hidden representation ($0.84$-$0.95$ AUROC and $\sim88\%$ balanced accuracy for predicting refusal/compliance) before any visible thinking. The thinking process turns out to be more akin to prefix completion than to deliberative revision, with the final outcome rarely changing after the first $\sim20\%$ of thinking, despite giving the appearance of deliberation at the text level ($\sim74\%$ of text-level deliberations occur when the response distribution is already locked to one refusal/compliance side). We also find that existing inference-time and training-based safety interventions, despite being motivated by the goal of inducing deliberation, largely shift model behavior toward over-refusal while suppressing already-scarce deliberation signals. Our results suggest that safety behavior in current reasoning models is much less deliberative than commonly assumed, and highlight the need for methods that induce real safety deliberation.

---


### 28. [Yuvion VL: A Multimodal Foundation Model for Adversarial Content and AI Safety](https://arxiv.org/abs/2606.25034)

**<font color=#1a73e8>作者：</font>** Shikai Qiu, Xiaowen Xu, Benlei Cui 等 54 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> General-purpose models often struggle to reliably identify and understand real-world multimodal risks, largely due to the inherent multimodal adversarial nature of content and AI safety. We present Yuvion VL, a family of multimodal large language models purpose-built for content and AI safety, with both instruction-tuned and reasoning-oriented variants. Yuvion VL addresses this gap by treating safety as an inherently adversarial and multimodal problem and designing the entire pipeline around adversarial robustness. For data construction, we develop an automated pipeline integrating adversarial-aware data synthesis with multi-stage quality control, producing large-scale, high-quality multimodal samples augmented with domain knowledge and reasoning annotations. For training, we adopt a three-stage pipeline that includes continued pretraining for risk-concept cross-modal alignment, instruct post-training for production-grade safety tasks, and reasoning post-training for enhanced interpretability and performance in complex tasks. We further introduce Confuse-then-Contrast Fine-Tuning, a contrastive framework that mines model-specific confusions and constructs multi-image contrastive groups to enforce explicit discrimination of fine-grained visual-semantic elements, enabling the model to distinguish between visually similar cases with different safety implications in adversarial safety tasks. To support rigorous evaluation, we further introduce Yuvion VL RiskEval (YVRE), a collection of benchmarks covering diverse open and internal evaluations, with a focus on content and AI safety, adversarial robustness, and real-world capability requirements. Experiments show that Yuvion VL-32B achieves industry-leading safety performance, surpassing comparably sized open-source models and best closed-source commercial models, while maintaining comparable general capabilities.

---


### 29. [LLM-ACES: Closed-Loop Discovery of Dynamical Systems with LLM-Guided Adaptive Search](https://arxiv.org/abs/2606.25039)

**<font color=#1a73e8>作者：</font>** Nikhil Abhyankar, Sha Li, Sanchit Kabra 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recovering governing Ordinary Differential Equations (ODEs) from data is a central challenge in modeling dynamical systems across scientific domains. Existing approaches cast discovery as a static inference problem over fixed datasets, assuming that the observed trajectories are sufficiently informative. However, dynamical systems evolve over large state spaces, and limited data can make multiple equations observationally indistinguishable, leading to identifiability gaps and the recovery of incorrect governing equations. To address this, we introduce LLM-ACES, or LLM-guided Active Closed-loop Equation Search, a closed-loop framework that jointly optimizes symbolic hypothesis construction and adaptive data acquisition. In LLM-ACES, a large language model (LLM) proposes operator priors that partition the large search space into distinct regions, within which candidate equations are fit to the observed data. The disagreement among these candidates guides the acquisition of informative trajectories, creating a feedback loop that iteratively refines both the hypothesis space and the discovered dynamics. On 122 ODE systems spanning ODEBench and ODEBase, LLM-ACES achieves the lowest median NMSE, outperforming state-of-the-art baselines by several orders of magnitude while achieving a high symbolic accuracy of 46.2% and 52.4%, respectively. Our analysis further shows that LLM-ACES is sample-efficient, achieving better performance with one-tenth the data. Furthermore, LLM-ACES's feedback-driven data acquisition makes it robust to noise and recovers the correct symbolic structure, while baselines introduce spurious terms that fit the data locally but obscure the true governing relationships.

---


### 30. [Wan-Streamer v0.1: End-to-end Real-time Interactive Foundation Models](https://arxiv.org/abs/2606.25041)

**<font color=#1a73e8>作者：</font>** Lianghua Huang, Zhifan Wu, Wei Wang 等 24 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present Wan-Streamer, a native-streaming, end-to-end interactive foundation model designed from the ground up for real-time, low-latency, full-duplex audio-visual interaction. Wan-Streamer seamlessly models language, audio, and video as both input and output within a single Transformer, where the sequence is represented as interleaved visual, audio, and text input tokens together with visual, audio, and text output tokens, coordinated by block-causal attention for incremental streaming. Unlike cascaded interactive systems that rely on separate VAD, ASR, language, TTS, audio-driven animation, or video-generation modules, Wan-Streamer does not rely on external language, speech, avatar, or video-generation modules: perception, reasoning, generation, response timing, turn management, and cross-modal synchronization are learned jointly within one unified model, reducing pipeline latency and error accumulation. To support natural audio-visual responsiveness, we redesign the entire stack around streamability, including causal encoders, causal decoders, block-causal attention, and low-latency multimodal token scheduling, enabling streaming units as short as 160 ms at 25 fps. Wan-Streamer achieves approximately 200 ms model-side response latency and approximately 550 ms total interaction latency when combined with 350 ms bidirectional network latency, supporting sub-second duplex audio-visual communication. These results position Wan-Streamer as a unified, end-to-end, multimodal interactive foundation model for low-latency streaming interaction.

---


### 31. [LLM-Based Scientific Peer Review: Methods, Benchmarks, and Reliability Challenges](https://arxiv.org/abs/2606.25057)

**<font color=#1a73e8>作者：</font>** Thi Huyen Nguyen, Zahra Ahmadi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The rapid growth of scientific submissions has pushed traditional peer review toward its scalability limits, motivating the exploration of large language models (LLMs) as intelligent automated evaluation assistants. Although recent studies show that LLMs can generate fluent critiques and approximate reviewer scores, their reliability, robustness, and security as decision-support systems remain insufficiently understood. This survey offers a systems-level analysis of LLM-based scientific peer review, focusing on two core evaluative functions: critique generation and score prediction. We present a structured taxonomy of modeling approaches (including prompt-based, supervised, retrieval-augmented, and alignment-optimized approaches), and synthesize empirical findings across existing benchmarks. We analyze dataset constraints, evaluation shortcomings, and domain concentration biases that limit current assessment practices. Beyond performance metrics, we identify emerging robustness risks, including prompt injection, data poisoning, retrieval vulnerabilities, and reward hacking, which expose automated review pipelines to strategic manipulation. From a data mining perspective, we outline key open challenges in modeling subjective disagreement and cross-domain generalization. By reframing automated peer review as a high-stakes, multi-objective decision problem, this survey provides a roadmap for developing robust, transparent, and trustworthy AI-assisted scientific evaluation systems.

---


### 32. [Do vision-language models search like humans? Reasoning tokens as a reaction-time analog in classic visual-search paradigms](https://arxiv.org/abs/2606.25066)

**<font color=#1a73e8>作者：</font>** Farahnaz Wick  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Visual search has been one of the most productive paradigms in the study of visual attention: the way reaction time scales with the number of items distinguishes parallel, "pop-out" search from serial, attention-demanding search. I ask whether vision-language models (VLMs) exhibit the same behavioral signatures. I adapt four classic paradigms: feature versus conjunction search, spatial-configuration (T-vs-L) search, enumeration, and the tilted/vertical search asymmetry; and present them to current frontier and mid-tier models. Because a single model call has no reaction time, I use the number of reasoning ("thinking") tokens a model spends per trial as a within-model analog of search effort, and I compare against a large public human benchmark (Wolfe et al., 2010). The models reproduce several human signatures: feature search costs flat effort while conjunction effort climbs with set size; frontier models hold accuracy where mid-tier models collapse to chance; and a resolution control shows the conjunction cost is genuine search rather than difficulty resolving small shapes. They also diverge from humans in informative ways. The target-present effort slope exceeds the target-absent slope, reversing the human ordering; enumeration remains accurate where humans would lose count; and a reasoning model with adaptive deliberation declines to deliberate on detection tasks altogether, so that a single search expresses itself as an effort gradient in one model and as an accuracy cliff in another. I argue that psychophysical paradigms, applied behaviorally, are a sharp and inexpensive probe of machine visual cognition, and that the points of divergence are as informative as the points of agreement.

---


### 33. [Are We There Yet? Exploring the Capabilities of MLLMs in Assistive AI Applications](https://arxiv.org/abs/2606.25084)

**<font color=#1a73e8>作者：</font>** Shayon Dasgupta, Avijit Dasgupta, C. V. Jawahar  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) have redefined visual understanding by combining vision encoders with large-scale language models. This unified architecture enables strong performance on tasks like image captioning, visual question answering, and multimodal dialogue, often in zero- and few-shot settings. Their general-purpose capabilities and flexible interfaces make MLLMs a promising foundation for real-world vision-language applications.
Assistive AI aims to help users interact with their environments through natural language. These scenarios demand robust visual recognition, contextual reasoning, and multilingual comprehension-capabilities that MLLMs are believed to offer. However, their effectiveness in assistive settings remains to be fully understood.
In this work, we explore whether MLLMs can support Assistive AI by evaluating state-of-the-art models on real-world tasks: recognizing everyday objects like currency, answering questions based on scene text, and reading visually presented content across multiple languages. To this end, we developed a system, NetraLink, using a head-mounted GoPro to capture real-world egocentric data, and collected a benchmark covering these assistive scenarios. Our findings provide a comprehensive diagnostic of current MLLMs, highlighting their strengths and limitations in enabling assistive technologies grounded in visual perception and language interaction.

---


### 34. [Training for the Model You Return: Improving Optimization for Iterate-Averaged Language Models](https://arxiv.org/abs/2606.25086)

**<font color=#1a73e8>作者：</font>** Kwok Chun Au, Adam Block  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many modern Language Model (LM) pipelines return an averaged model, such as an exponential moving average of the training iterates, rather than the final iterate itself. This raises a fundamental question: given that we will return an iterate average, how should we change training to improve the performance of this average? We study this question by formulating optimizer design for the iterate-average estimator as an optimal-control problem. In a continuous-time stochastic quadratic model, we solve for the control strategy that minimizes the error of the returned average subject to a penalty on the size of the intervention. A practical approximation to this controller yields PACE, a lightweight wrapper around AdamW that pulls the live weights toward their exponential moving average with a clipped, per-coordinate control strength. We prove that a stylized version of PACE converges at the standard stochastic convex optimization rate, up to a factor depending on the averaging rule, while in the quadratic setting it can strictly improve the limiting squared error of the iterate-average estimator and can do so by an arbitrarily large factor on some instances. Empirically, our results suggest that PACE improves over AdamW and EMA-evaluated AdamW in supervised fine-tuning of 1-2B parameter LMs and in GPT-2 pretraining on FineWeb for a wide range of learning rates, decay schedules, and other hyperparameters.

---


### 35. [Dream at SemEval-2026 Task 13: SALSA for Single-Pass Machine-Generated Code Detection](https://arxiv.org/abs/2606.25102)

**<font color=#1a73e8>作者：</font>** Ruslan Berdichevsky, Shai Nahum-Gefen, Elad Ben-Zaken  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models have transformed code generation, raising concerns around authorship, assessment integrity, and software trust. SemEval-2026 Task 13 Subtask A operationalizes detection as binary classification over code snippets, with a particular emphasis on out-of-distribution (OOD) generalization across unseen programming languages and application domains. We propose a SALSA-style formulation, Single-pass Autoregressive LLM Structured Classification, that maps each class to a dedicated output token and trains the model to emit a single-token label in a structured response. Rather than engineering hand-crafted features or decision rules, this formulation delegates the authorship decision to the model. To improve OOD robustness, we combine balanced sampling across languages with parameter-efficient fine-tuning and conservative training (low learning rate, single epoch) to avoid overfitting to the training domain. Our best system achieves OOD $F_1 = 0.789$ on the official leaderboard, substantially outperforming the CodeBERT baseline ($F_1 = 0.305$).

---


### 36. [Forget to Improve: On-Device LLM-Agent Continual Learning via Budget-Curated Memory](https://arxiv.org/abs/2606.25115)

**<font color=#1a73e8>作者：</font>** Beining Wu, Zihao Ding, Jun Huang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-device language-model agents improve by accumulating experience in retrieved memory rather than by updating weights. This memory is hard-bounded and exposed: it consumes RAM and energy, reaches peers through a thin uplink, and becomes an attack surface because it is writable by what the agent reads. Existing systems each cover one part of this problem: agentic memories grow without a budget, on-device methods keep entries by success alone, and poisoning is studied mainly as an attack rather than as a memory-governance problem. We propose \sys{}, a single net-value-per-byte score that governs an agent's experience-memory lifecycle. The main idea is to let the budget act as the curator: each entry is scored as value minus harm, per byte, so one ruler decides what to keep, share, and trust. \sys{} makes three decisions: (1) \textbf{KEEP} evicts low-value bytes under the RAM and energy budget; (2) \textbf{SHARE} sends an insight only when its value exceeds its uplink cost; and (3) \textbf{TRUST} gates a peer entry by provenance. On language-model-agent task-drift benchmarks and a real heterogeneous Jetson testbed with two robot-arm nodes and a hub, \sys{} reduces memory by $2.7\times$ and uplink by $2.4\times$, drives injection success from 0.75 to zero, and raises accuracy on cases corrupted by poison or stale memory. Curating by net value reduces footprint, energy, uplink, and injection success together without reducing accuracy. In this setting, forgetting by net value improves the agent rather than weakening it.

---


### 37. [ATMA: Length-Invariant Language Modeling via Polar Attention and Gated-Delta Compression Memory](https://arxiv.org/abs/2606.25156)

**<font color=#1a73e8>作者：</font>** Habibullah Akbar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern large language models based on softmax scaled-dot-product attention are constrained by their training sequence length: as the key-value sequence grows, softmax probability mass can dilute across a wider distribution, inducing activation shift and long-context performance collapse. Moreover, long-context language modeling faces a structural tension: a sliding-window attention core maintains a bounded local representation and low perplexity but is blind to long-range dependencies, while full-context attention preserves global recall but suffers from out-of-distribution perplexity explosion. To resolve these limitations, we introduce ATMA, a hybrid convolutional-attention architecture that integrates a novel three-channel attention mechanism. ATMA factorizes the attention mixing step into: (1) a count-blind, unit-vector direction channel, (2) a bounded magnitude channel driven by the participation ratio of effective matches over an extreme-value-corrected null sink, and (3) a long-term recurrent compression memory optimized via a gated-delta fast-weights rule. Neither the Polar Attention core nor the recurrent memory is sufficient alone; their combination enables monotonic perplexity reduction and high-fidelity long-range retrieval simultaneously. We evaluate ATMA using a 100-run factorial ablation sweep, demonstrating that the combined Polar + memory model maintains induction needle-in-a-haystack retrieval accuracy above 90% out to 64K tokens (32 times the training length of 2K) while its document perplexity improves monotonically, outperforming softmax-based memory baselines which collapse at extreme context lengths. Code: this https URL

---


### 38. [TRUSTMEM: Learning Trustworthy Memory Consolidation for LLM Agents with Long-Term Memory](https://arxiv.org/abs/2606.25161)

**<font color=#1a73e8>作者：</font>** Tianyu Yang, Sudipta Paul, Vijay Srinivasan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents rely on long-term memory to support extended interactions and personalized assistance beyond finite context windows. Existing memory agents actively update external memory through generated write, revise, and delete operations, but these updates may omit important information, corrupt existing memory, or introduce unsupported hallucinated content. Once stored, such errors become persistent system-state failures that can affect future reasoning and generation. In this paper, we propose TrustMem, a framework designed to improve the trustworthiness of memory consolidation. TrustMem relies on a Memory Transition Verifier to evaluate the transition process of memory updates in terms of coverage, preservation, and faithfulness. It further constructs preference pairs among candidate updates under the same memory state, enabling preference-guided reinforcement learning to directly optimize memory updating behaviors. Extensive experiments demonstrate that TrustMem improves both memory utility and reliability: it achieves state-of-the-art results across MemoryAgentBench, HaluMem, and the Mem-alpha validation set, improves HaluMem memory extraction by 12.14 F1 points, and reduces transition-level omission, corruption, and hallucination by 40.1\%, 79.1\%, and 50.0\%, respectively, compared with the strongest baseline for each error type.

---


### 39. [An iterative energy-based multimodal transformer for joint retrieval of wheat soil moisture, leaf area index, and plant height from Sentinel-1 and Sentinel-2 time series](https://arxiv.org/abs/2606.25174)

**<font color=#1a73e8>作者：</font>** Shubham Kumar Singh, Peilei Fan, Suraj A. Yadav 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Field-scale retrieval of surface soil moisture (SM), leaf area index (LAI), and plant height (PH) is essential for precision agriculture, yet it remains an ill-posed inverse problem. Concurrent variations in soil moisture and canopy density generate substantial ambiguities in radar backscatter and spectral responses, which reduces the effectiveness of traditional feedforward regression models in heterogeneous smallholder cropping systems. This study presents the Iterative Energy-Based Transformer (iEBT) for the joint retrieval of coupled soil-canopy states from Sentinel-1 C-band SAR and Sentinel-2 multispectral time series. Instead of direct regression, iEBT embeds multi-modal predictors within a shared sequence, produces an initial state estimate, and iteratively updates the target [SM, LAI, PH] vector through normalized gradient descent to minimize a learned scalar compatibility energy function. Using 700 quality-controlled field measurements from Varanasi, India, iEBT achieved the highest learned-model performance on the random test split, with a four-seed mean R^2 of 0.854 \pm 0.012 (R_SM^2 = 0.841, R_LAI^2 = 0.905, R_PH^2 = 0.821). WCM and PROSAIL were retained as physically interpretable SAR and optical reference models for comparison. Modality ablations confirmed that Sentinel-1 drives SM retrieval, while Sentinel-2 dominates LAI, whereas PH relies on combined structural-phenological signatures. Crucially, the model's terminal energy functions as an uncalibrated post-retrieval quality diagnostic; screening the 10% highest-energy samples markedly reduced target level root-mean-square errors. While leave-one-campaign-out validation highlights persistent cross-season domain shift challenges due to localized management variations, compatibility-guided multimodal fusion offers a structured self-diagnostic path toward reliable biophysical parameter estimation

---


### 40. [Transferability for General Reasoning: An Automated Curriculum for Multi-Domain RLVR](https://arxiv.org/abs/2606.25178)

**<font color=#1a73e8>作者：</font>** Yongjin Yang, Jiarui Liu, Yinghui He 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR) has been extended from single-domain training to multi-domain reasoning suites spanning mathematics, programming, and science. However, the training curriculum (how often each domain is sampled) is typically fixed or hand-tuned, even though reasoning skills transfer unevenly across domains. Existing learnability-based curricula adapt to where the policy is currently improving, but are blind to whether a gradient step on the selected domain benefits the remaining domains. In this paper, we propose Transfer-Aware Curriculum (TAC), a bandit-style online curriculum that prioritizes domains whose updates broadly benefit the rest of the training suite. TAC repurposes signals already produced by RL training: per-domain advantages capture local learnability, and projected gradients, taken from the GRPO step being computed, estimate cross-domain transferability via gradient-geometry alignment, at negligible cost (<1% wall-clock overhead). Across a six-domain reasoning suite, TAC achieves the best macro-averaged accuracy on both Qwen3-1.7B and Llama3.2-3B, outperforming proportional random sampling, a hand-designed schedule, and a learnability-only bandit, and improving over the last of these by up to 2.8 points (10% relative). Ablations show performance degrades sharply when the transferability term is removed, and TAC remains robust on imbalanced training mixtures where learnability-only curricula over-commit to dominant domains. Our findings establish cross-domain transferability as a key signal for curriculum design in multi-domain RLVR.

---


### 41. [What Intermediate Layers Know: Detecting Jailbreaks from Entropy Dynamics](https://arxiv.org/abs/2606.25182)

**<font color=#1a73e8>作者：</font>** Sofiia Nikolenko, Michele Papucci, Mina Rezaei 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Jailbreak attacks reveal a persistent weakness in aligned Large Language Models: carefully crafted prompts can elicit policy-violating responses despite safety training. While most defenses operate at the prompt or output level, it remains unclear how harmful intent is encoded within the model's internal representations. We investigate this question by analyzing token-level predictive entropy trajectories across layers of a frozen LLM using the logit lens. We find that static aggregate statistics of prompt-level entropy (e.g., mean, variance) carry little discriminative signal, whereas features capturing how entropy evolves across token positions, such as monotonic rank-based trend scores, are substantially more informative. Importantly, this signal is not uniform across model depth: it is concentrated in intermediate layers and degrades at the final layer, indicating that jailbreak-relevant structure is most pronounced in mid-network representations rather than at the output head. Across multiple models (Llama, Qwen, Gemma) and adversarial benchmarks, these entropy dynamics provide architecture-consistent separation without additional training. Together, our findings show that jailbreak behavior is reflected in structured intermediate uncertainty dynamics, clarifying both which entropy-derived features encode harmful intent and where in the network that signal is most pronounced.

---


### 42. [To Isolate or to Score? Model-Adaptive Assessment for Cost-Efficient Multi-Agent RAG](https://arxiv.org/abs/2606.25191)

**<font color=#1a73e8>作者：</font>** Jungseob Lee, Chanjun Park, Heuiseok Lim  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-agent document assessment for retrieval-augmented generation is computationally expensive, driving practitioners toward smaller, deployable models whose assessment mechanisms remain poorly understood. We conduct a controlled study of training-free interventions on 7B-9B instruction-tuned models across diverse QA benchmarks, revealing a sharp dichotomy in how models benefit from assessment. For weaker baselines, the dominant mechanism is per-document isolation. Astoundingly, assessment-free isolation matches full multi-agent assessment, demonstrating that resolving multi-document context confusion, rather than scoring quality, drives outsized gains of up to 50 percentage points. Conversely, for strong baselines where scoring quality matters, we introduce Reasoning-Score Coupling, a label-free perturbation probe that classifies scoring behavior. Integrating these findings, we propose MADARA, a model-adaptive routing architecture. Crucially, MADARA's diagnostic thresholds derived from a single pilot model generalize zero-shot to four unseen model families, providing a robust, lightweight pipeline to eliminate computational overhead.

---


### 43. [EPTS: Elastic Post-Training Sparsity for Efficient Large Language Model Compression](https://arxiv.org/abs/2606.25285)

**<font color=#1a73e8>作者：</font>** Ke Xu, Jiaqi Wan, Wenhao Hu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Post-Training Sparsity (PTS) has emerged as a crucial paradigm for compressing Large Language Models to facilitate efficient deployment on resource-constrained devices. However, existing PTS methodologies are typically confined to Single-Sparsity optimization, necessitating a separate, time-consuming optimization session for each specific sparsity level. This rigid paradigm significantly hinders flexible deployment across diverse hardware scenarios, as adapting to a new sparsity requirement mandates a complete re-optimization process. To address these limitations, we propose Elastic Post-Training Sparsity (EPTS), a unified Multi-Sparsity framework that produces a single elastic model capable of maintaining robust performance across diverse sparsity configurations through a one-shot optimization process. Specifically, we design a Multi-Sparsity Hierarchy LoRA (MS-HiLoRA) mechanism that facilitates knowledge inheritance from low- to high-sparsity groups, effectively mitigating the competition for parameter reconstruction. Furthermore, we introduce a Multi-Sparsity Feature Mixer (MSFM), which significantly enhances the model's adaptability to pruning perturbations by dynamically fusing feature representations of varying sparsity granularities. Extensive experiments on LLaMA and OPT families demonstrate that EPTS achieves competitive performance compared to state-of-the-art methods like SparseGPT and Wanda, while offering significant efficiency gains by enabling multi-scenario deployment from a single optimization. our source code is available at this https URL.

---


### 44. [HiFiVe: High-Fidelity Vehicle Generation Leveraging Auto-Regressive 2D Generative Priors](https://arxiv.org/abs/2606.25300)

**<font color=#1a73e8>作者：</font>** Hongli Xiao, Youjian Zhang, Qi Zheng 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing 3D vehicle generation methods often suffer from low geometric fidelity and blurry textures, hindering their downstream applications. While recent works adopt multi-view diffusion models for high-fidelity texture, they are often constrained by fixed viewpoints, limited resolution, and a reliance on costly fine-tuning to achieve cross-view consistency. In this paper, we propose HiFiVe, a training-free framework for high-fidelity vehicle modeling through joint texture and geometry enhancement by imposing 3D geometric constraints to anchor 2D generative priors. Specifically, we propose an auto-regressive texture refinement pipeline that progressively synthesizes high-resolution textures from arbitrary viewpoints. To ensure cross-view consistency, the coarse geometry serves as a synchronization prior, conditioning each generation step on previously synthesized frames via depth-based warping and multi-view texture fusion. Moreover, the inherent symmetry of vehicles is exploited to mitigate error accumulation. Finally, high-frequency surface details are recovered by refining the mesh geometry using normal maps estimated from the enhanced textures. Extensive experiments on synthetic and real-world vehicle datasets demonstrate that our method significantly improves both geometric detail and texture quality compared to state-of-the-art baselines.

---


### 45. [LEVIRDet: A Million-Scale 159-Category Dataset and Foundation Model for Universal Remote Sensing Object Detection](https://arxiv.org/abs/2606.25312)

**<font color=#1a73e8>作者：</font>** Qinzhe Yang, Dongyu Wang, Haohan Niu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Remote sensing object detection has advanced rapidly with the development of large-scale benchmarks and modern detection architectures. However, existing datasets and detectors remain fragmented. Most benchmarks focus on limited categories, fixed spatial resolutions, or a single sensor, while detectors still struggle to work across different sensors and categorical systems. In this paper, we introduce LEVIRDet-159, the largest and most comprehensive remote sensing object detection dataset to date, with 159 categories, 2.56 million bounding boxes, and 700k fine-grained annotations under a multi-level taxonomy. In each key scale dimension, LEVIRDet-159 exceeds the corresponding largest existing remote sensing object detection dataset, containing approximately (7x) more images, (6x) more object instances, and (4x) more categories. Based on this dataset, we design LEVIRDetNet, a scale-hierarchy-aware detection foundation model for universal remote sensing object detection. LEVIRDetNet couples online visual Ground Sampling Distance (GSD) prediction, GSD-conditioned query modulation and allocation, and a hierarchy-aware detection head for mixed-granularity remote sensing supervision. Under stringent evaluation settings, LEVIRDetNet demonstrates strong cross-domain generalization. Even without target-domain training or fine-tuning, it achieves state-of-the-art detection performance on 9 external benchmarks, improving the strongest fully supervised competing methods by 5.02 mAP on average under each benchmark's primary metric. We hope this study will facilitate the development of strongly generalizable remote sensing object detection across diverse category systems, spatial resolutions, and sensor platforms. The dataset and trained models will be released at this https URL, accompanying the final paper.

---


### 46. [V-Zero: Answer-Label-Free On-Policy Distillation with Contrastive Evidence Gating for Fine-Grained Visual Reasoning](https://arxiv.org/abs/2606.25319)

**<font color=#1a73e8>作者：</font>** Haoxiang Sun, Zhihang Yi, Langxuan Deng 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Fine-grained visual reasoning requires multimodal large language models (MLLMs) to identify task-relevant visual evidence and ground their reasoning in local image regions. Existing agentic methods typically rely on reinforcement learning with verifiable rewards or supervised fine-tuning on large-scale annotated reasoning traces, leading to costly exploration, hand-designed verification rules, or heavy dependence on textual supervision. A natural way to avoid such external answer labels is to learn from trajectories sampled by the student itself, which points to On-Policy Distillation (OPD). To understand what OPD can and cannot provide for visual reasoning, we revisit it as negative-free stop-gradient alignment. This perspective shows that, although OPD provides effective token-level correction, its ceiling is constrained by the absence of trajectory-level discrimination. Motivated by these observations, we propose V-Zero, an answer-label-free framework for visual reasoning with contrastive evidence gating. V-Zero uses no annotated textual answer labels; instead, during training it pairs a question-relevant regional crop with a negative visual view to evaluate student-sampled trajectories and gate dense token-level distillation. Experiments on multiple visual reasoning benchmarks show that V-Zero consistently improves fine-grained visual reasoning while preserving strong generalization. Notably, V-Zero is more than 5$\times$ faster than previous supervised fine-tuning methods and more than 10$\times$ faster than reinforcement learning baselines. Code and dataset will be released at this https URL

---


### 47. [Efficient Remote Sensing Instance Segmentation with Linear-Time State Space Distilled Visual Foundation Models](https://arxiv.org/abs/2606.25324)

**<font color=#1a73e8>作者：</font>** Qinzhe Yang, Keyan Chen, Jia Xu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The computational complexity of Transformers scales quadratically with the number of tokens, which significantly constrains the efficiency of vision models, particularly recent ViT-based foundation models in dense prediction tasks. Instance segmentation, a typical dense visual prediction task in the remote sensing field, faces similar challenges. In this paper, inspired by the recent advances of knowledge distillation in large language models, we introduce RS4D - a new remote sensing instance segmentation method with linear computational complexity, which addresses the inefficiency of long sequence modeling through distilled state space modeling (SSM). We propose an adaptive noise and masking knowledge distillation training method for pre-training lightweight SSM backbones, which effectively compresses knowledge from the vast self-attention space into a compact, dense linear state space. We also design a remote sensing image instance segmentation architecture based on this lightweight visual encoder, where we explore variants of three different backbones and two segmentation heads. Extensive experiments are conducted on multiple benchmark datasets, including SSDD, WHU, and NWPU. Compared to ViT-based approaches, our proposed SSM backbone achieves an 8x reduction in parameters and a 9x reduction in FLOPs while maintaining comparable or superior accuracy to both ViT- and CNN-based instance segmentation methods. The implementation codes have been publicly available at this https URL.

---


### 48. [Omni-Perception Policy Optimization for Multimodal Emotion Reasoning](https://arxiv.org/abs/2606.25325)

**<font color=#1a73e8>作者：</font>** Zhiyuan Han, Beier Zhu, Wenwen Tong 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We find that current emotion-oriented Omni-MLLMs still lack reliable omni-modal perception: they (i) underutilize multimodal cues in their reasoning trajectories and (ii) exhibit unfaithful behavior, often hallucinating modality-specific statements from other modalities. Building on these insights, we propose OPPO (Omni-Perception Policy Optimization), a reinforcement learning framework that explicitly optimizes multimodal perception. First, an Omni-Perception Reward decomposes ground-truth reasoning into fine-grained visual, acoustic, and emotion cues and rewards trajectories that semantically recover these cues. Second, an Omni-Perception Loss compares the policy under full and unimodally masked inputs, applying a KL penalty only to modality-specific evidence tokens to suppress cross-modal hallucination. We further introduce MEP-Bench, a diagnostic benchmark that quantifies utilization and faithfulness. Experiments show that OPPO achieves state-of-the-art performance on MER-UniBench and MME-Emotion, while substantially improving utilization and faithfulness scores on MEP-Bench, highlighting the importance of sufficient and faithful omni perception for multimodal emotion reasoning.

---


### 49. [Improved Large Language Diffusion Models](https://arxiv.org/abs/2606.25331)

**<font color=#1a73e8>作者：</font>** Shen Nie, Qiyang Min, Shaoxuan Xu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Modern large language models are predominantly trained with autoregressive factorization and causal attention. We present \emph{iLLaDA}, an 8B masked diffusion language model trained from scratch with fully bidirectional attention. iLLaDA keeps the masked diffusion objective throughout pre-training and supervised fine-tuning (SFT), scaling pre-training to 12T tokens and fine-tuning on a 25B-token instruction corpus for 12 epochs. We further use variable-length generation for efficiency and introduce confidence-based scoring for multiple-choice evaluation. Compared with LLaDA, iLLaDA improves broadly across general, mathematical, and code benchmarks; for example, iLLaDA-Base improves by 21.6 points on BBH and 14.9 points on ARC-Challenge, while iLLaDA-Instruct improves by 14.5 points on MATH and 16.5 points on HumanEval. Despite its non-autoregressive training, iLLaDA also remains competitive with Qwen2.5 7B on several benchmarks. These results show that fully bidirectional diffusion training from scratch is a competitive path toward strong language models. Model weights and codes: this https URL.

---


### 50. [Bridging the Post-discharge Gap: A Traceable Multi-agent Framework for Safe and Continuous Care](https://arxiv.org/abs/2606.25334)

**<font color=#1a73e8>作者：</font>** Runwei Guan, Yi Zhou, Heyi Lin 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Post-discharge clinical follow-up is critical for maintaining continuity of care and mitigating long-term health risks. However, traditional follow-up paradigms suffer from shortage of health workforce, fragmented patient histories, and information silos across clinical departments. While large language models have demonstrated potential in medical question-answering, their deployment in continuous care is hindered by hallucination risks and a fundamental inability to reason over longitudinal, patient-specific constraints. Here we present Healink, a memory-enhanced multi-agent framework to support AI-assisted post-discharge follow-up by generating prescription-grounded, traceable responses that improved completeness and perceived clinical utility in retrospective and physician-blinded evaluations. The architecture seamlessly integrates a triage routing mechanism, a unified memory enhancement module utilizing a robust relational database for optimal latency, and a strict constraint-based retrieval-augmented generation engine. By vectorizing historical clinical records and employing weighted similarity functions across diverse phenotypic and intervention dimensions, Healink ensures precise inter-patient and intra-patient case matching while actively preventing cross-departmental drug conflicts. We evaluated Healink on a dataset comprising 400 continuous and 85 highly complex real-world follow-up cases, alongside the webMedQA benchmark. In a rigorous single-blind evaluation conducted by clinical experts, the framework outperformed human physician baselines in both authoritativeness and clinical safety. By generating a traceable, white-box evidence chain, Healink provides a scalable, safe, and highly effective paradigm for intelligent patient management, ultimately enhancing societal healthcare outcomes.

---


> [!TIP]
> 当前位于：**1-50**（第 1/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-112](./part-03.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
