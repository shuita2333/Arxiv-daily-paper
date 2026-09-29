# 🧠 大模型相关研究 | 2026年09月30日

> 本类共 **992** 篇论文：已确认 **928** 篇，待复核 **64** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**501-550**（第 11/20 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | **501-550** | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-700](./part-14.md) | [701-750](./part-15.md) | [751-800](./part-16.md) | [801-850](./part-17.md) | [851-900](./part-18.md) | [901-950](./part-19.md) | [951-992](./part-20.md)

---

### 501. [Training Witnesses: Trusting the Training without Trusting the Trainer](https://arxiv.org/abs/2609.33915)

**<font color=#1a73e8>作者：</font>** Houjun Liu, Pratyusha Sharma  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Progress in machine learning cannot outpace our ability to verify it. With an explosion in papers today, every scientific claim rests initially on trust in the trainer, leading to uneven evaluation, baselines, and forestalling of reliable progress. Traditionally, the burden of verification falls on the reader, who must reproduce expensive training runs. This strategy is impractical due to an explosion in slop contributions, diversity of methods, and the sheer compute required. We put the burden of proof where it belongs, on the trainer, and in the process also cut the overall cost of verification significantly. We introduce Witnesses, a method for certifying training, data usage and evaluation in a neural network training run. Our key insight is that fast behavioral fingerprints with occasional replay challenges are sufficient for auditing neural network training. Our method is applicable at scale with minimal overhead to the trainer, is cheap for the verifier, rejects bad training runs with amplifiable probability, and allows for exact queries of both data inclusion and exclusion. We test our method on language model training runs from 100M to 2B scales, across DDP and FSDP, and demonstrate this minimal overhead. We also introduce a self-regulating leaderboard of "auto-certified" training runs that enables shared baselines and progress. We invite the community to participate in the leaderboard to improve reproducibility in machine learning.

---


### 502. [HyperMCTS: Hypergraph-Augmented MCTS for Long-Horizon LLM Agents](https://arxiv.org/abs/2609.33920)

**<font color=#1a73e8>作者：</font>** Tingsong Xiao, Nithish Balachandar Moudhgalya, Chandrayee Basu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-horizon tasks require large language model (LLM) agents to coordinate decisions under constraints that span an entire solution. Monte Carlo Tree Search (MCTS) offers a promising approach to test-time scaling by exploring alternative action trajectories, but model computation and environment interaction make search costly. Efficient search therefore requires effective reuse of trajectory feedback. Standard MCTS maintains prefix-specific statistics, without explicitly accumulating outcomes for decision groups that recur across different paths. To fill this gap, we propose HyperMCTS, a training-free method that augments an ordered MCTS tree with a cross-trajectory hypergraph. Hyperedges represent groups of canonical decisions and accumulate their observed returns within the current task. Our hypergraph-guided HyperUCT selection rule aggregates evidence from overlapping hyperedges into an action prior, allowing outcomes collected under one prefix to inform selection under another while preserving execution histories in the tree. On DeepPlanning, HyperMCTS improves average planning accuracy by 2.3--7.3 percentage points over the strongest baseline for each of three backbone models. It enables Qwen3.6-27B to outperform Claude Opus 4.6 (max) on Shopping Planning, while achieving higher accuracy with fewer LLM calls and output tokens than the evaluated MCTS-based baselines. SealQA experiments further demonstrate improvements in question answering.

---


### 503. [Quantization Error Is Spectrally Flat: A Single Random Probe Is a Calibrated, Data-Free Sensitivity Estimator, with Application to Budget-Targeted Mixed-Precision Quantization](https://arxiv.org/abs/2609.33923)

**<font color=#1a73e8>作者：</font>** I Kennedy, T Kennedy  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A single random Gaussian probe gives an unbiased estimate of the squared Frobenius norm of a layer's quantization error. The estimator is well-behaved because round-to-nearest error is spectrally flat. Across 1,683 tensors from a 35B MoE and a 9B dense model, effective dimensionality is 0.93 to 0.96 times the i.i.d. noise value of the same shape, and on the MoE the median is unchanged from 2-bit to 8-bit. The probe coefficient of variation is predictable from tensor shape. One probe measures per-tensor sensitivity to within 4 to 7%; twenty probes reach 1.3 to 1.4%.RAM applies the propagated form of this estimator to budget-targeted mixed-precision quantization with no calibration data. Gaussian probes carrying the network's own input statistics score every tensor at six bit-widths. A knapsack solver allocates bits under an exact byte budget, with guardrails against catastrophic 2-bit assignments. One probe pass serves any budget. Isolated and propagated scores rank tensors independently on Qwen3.5-35B-A3B (Spearman -0.01), yet the propagated probe rank-correlates 0.81 to 0.83 with the GPTQ layer objective from real activations, while the isolated estimator is uncorrelated with it. That objective is the wrong allocation target: at matched bytes on Qwen3.8-27B, a block-output probe beats a vendor IQ3_M mix and an oracle that allocates from the real-activation this http URL Qwen3-8B the propagated probe ties HAWQ-V2 at matched bytes. Across seven architectures from 8B to 122B, with probe timing up to a 400B model in nine minutes on one workstation, RAM reaches 3.5 to 13.6% lower median WikiText-2 perplexity than size-comparable uniform 4-bit builds on the tested MoE models

---


### 504. [A2A-ForensicTrace: Offline Verification of Tamper-Evident A2A Runtime Evidence](https://arxiv.org/abs/2609.33924)

**<font color=#1a73e8>作者：</font>** Adil Alshammari, Sareh Assiri, Hayretdin Bahsi  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Security-relevant Agent2Agent (A2A) executions can cross organizational boundaries, leaving investigators without live access to all participating systems. Offline investigation involves checking preserved records and their cross-record relationships for consistency. This paper presents A2A-ForensicTrace, an offline verification layer that converts runtime observations into typed records, derives protocol-relevant relationships, and commits both under an incident-trace root. An Ed25519-signed receipt binds the root and capture digest to the incident context. Evaluation comprised 240 executions through the official A2A software development kit (SDK), with actions selected by a large language model (LLM). These included 120 condition runs and 120 matched controls. All condition runs returned the expected bounded findings. No control produced an indication, and all roots and receipts verified. Median in-memory latency of the full offline verifier was 1.61 ms for the scenario traces. In the separate scaling experiment, it was 30.85 ms at 1,000 committed leaves. Future work will broaden A2A lifecycle coverage.

---


### 505. [Optimizing the Phi-2 Small Language Model for Real-time Chatbot Applications Using Parameter-Efficient Fine-Tuning (PEFT) with QLoRA Quantization](https://arxiv.org/abs/2609.33927)

**<font color=#1a73e8>作者：</font>** PhanTan Khanh Nguyen, Ashfaq Ali Shafin, Khandaker Mamun Ahmed  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This study explores the optimization of the Phi-2 Small Language Models (SLMs) for real-time chatbot applications through Parameter-Efficient Fine-Tuning (PEFT) and Quantized Low-Rank Adaptation (QLoRA). QLoRA specifically refers to the integration of PEFT with LoRA alongside a 4-bit quantization process, aimed at enhancing computational efficiency. These models, initially designed for high performance with minimal computational overhead, are further refined to address the constraints of mobile and edge computing environments. By integrating PEFT with QLoRA, the research aims to reduce memory usage significantly while maintaining, or potentially improving, the accuracy of model responses in real-time interactions. The effectiveness of these techniques was evaluated using the ROUGE metric system, which showed notable improvements in the summarization tasks performed by the models. This approach not only confirms the feasibility of using SLMs in resource-restricted environments but also opens up new avenues for deploying advanced AI-driven applications in real-time settings. The study's findings have significant implications for the development of efficient, scalable, and accessible AI technologies, paving the way for broader adoption in various industries.

---


### 506. [How Strong Is the Evidence for the Artificial Hivemind? Reevaluating Evidence for the Open-Ended Homogeneity of Language Models](https://arxiv.org/abs/2609.33936)

**<font color=#1a73e8>作者：</font>** Rylan Schaeffer, Brando Miranda, Joshua Kazdan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent research argues that language models exhibit pronounced homogeneity in open-ended generation, framing such behavior as an Artificial Hivemind that poses a long-term threat to human creativity. We examine three of its central results. First, the flagship example is that model responses to "Write a metaphor involving time" collapse into two clusters. Visualization, spectral analysis, clustering, and language model labels all contradict this description. The labels record each response's vehicle, what it compares time to. Our responses and the original authors' own show one dominant vehicle plus a heavy tail of distinct minority vehicles. "Time" is one of our least diverse topics, so the example is a favorable case, not a representative one. Second, the paper measures homogeneity against an undemanding null: responses to unrelated prompts. Under a more demanding null (same-prompt responses expressing genuinely different ideas), 20%-32% of such pairs already exceed the paper's 0.8 convergence threshold. A residual effect survives this null. The paper's same-prompt pairs exceed 0.8 roughly two to three times as often as our different-idea pairs. Much of what the paper calls homogeneity is the shared geometry of answering the same prompt. The remaining measurements lack any null: no human baseline is collected, and the model-indistinguishability statistic has no null. Third, the paper concludes that inference-time interventions are inadequate for combating the Artificial Hivemind, writing that "more generalizable solutions are needed at the model training level." We show that this conclusion is unsupported in three ways, and that an inference-time intervention (prompting) reliably raises measured response diversity. We do not resolve whether the Artificial Hivemind is real. We show that the published evidence does not establish it.

---


### 507. [Test-Time Generalized Category Discovery](https://arxiv.org/abs/2609.33937)

**<font color=#1a73e8>作者：</font>** Shambhavi Mishra, Omprakash Chakraborty, Julio Silva-Rodriguez 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Test-Time Adaptation (TTA) and Generalized Category Discovery (GCD) are traditionally treated as disjoint problems: the former adapts models to domain shift assuming all test classes are known, while the latter discovers novel categories assuming labeled training data for known classes. However, real-world deployment rarely fits either setting. Motivated by this gap, we introduce Test-Time Generalized Category Discovery (TT-GCD), a unified and more realistic scenario where a vision-language model must adapt to distribution shifts, classify known categories using only textual supervision, and discover novel categories, all during test time and without access to labeled data. To address this challenging scenario, we propose PACT (Prototype Assignment for Category discovery at Test time), a fully unsupervised framework that casts known-class recognition and novel-class discovery via prototype assignment. PACT first re-aligns shifted visual features with the text-derived class representations of the VLM using confident zero-shot predictions. Known and novel categories are then both represented by prototypes in the visual embedding space, estimated from the unlabeled test stream, and each test image is assigned to the category whose prototype is most similar to its visual feature. Extensive experiments across corruption and domain-shift benchmarks demonstrate that PACT outperforms adapted state-of-the-art TTA and GCD methods, effectively bridging the gap between adaptation and discovery.

---


### 508. [Simple Diffusion Language Models Are More Effective Few-Step Generators Than Reported](https://arxiv.org/abs/2609.33947)

**<font color=#1a73e8>作者：</font>** Hasan Amin, Ming Yin, Rajiv Khanna  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Diffusion language models (DLMs) promise fast parallel generation, yet high-quality samples often require large number of refinement steps, which diminishes their advantage in practice. This has led to massive interest in and rapid development of new methods for effective few-step generation. We show that much of the supposed quality gap at few steps can instead arise from a suboptimally configured sampler. Modest sampler sharpening, without any model retraining, enables a couple years old masked DLM to rival supposedly far improved successors. This differently sampled DLM in fact achieves lower generative perplexity in just 16 steps than what its standard sampler obtains with 1024, while improving both judged quality and semantic diversity. We further show that conventional per-output metrics can fundamentally obscure these gains, since any optimal trade-off between two such metrics can be attained by a generator supported on at most two outputs. We subsequently introduce GroupEval, which separately evaluates quality and across-output semantic diversity, and offers fresh insights including uncovering how 1.5-4.7x perplexity gains of a distilled model yield no corresponding quality gain. Finally, we explain why sharpening helps: parallel unmasking destroys dependencies among simultaneously generated tokens, creating a gap between prediction and generation. We prove that pervasive temperature choice of one is generically suboptimal under parallel sampling even for an exact denoiser, and that worse predictions can yield better samples. Through these results, we argue for a broader evaluation principle of treating the deployed generator as the object of comparison, benchmarking it against tuned baselines, and assessing quality and diversity jointly and with more human-aligned measures.

---


### 509. ["Is This Book AI-Generated?" How Authorship Suspicion Manifests in Marketplace Reviews](https://arxiv.org/abs/2609.33950)

**<font color=#1a73e8>作者：</font>** Victor Dibia  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> As AI becomes part of how books are authored, reader response to suspected AI authorship grows more consequential, yet remains unexamined. We analyze 863 low-star reviews of 78 Amazon bestsellers across 8 categories at three levels of proximity to AI. Suspicion concentrates in Generative AI books (35.1%) but appears in every category, including Gardening (5.7%). Reviews citing AI authorship complain more about shallow content and poor presentation than other critical reviews. Suspicion takes two forms: ambient, where "AI-generated" is a generic complaint about formulaic writing, and corroborated, where reviewers of the same book independently cite concrete evidence. We propose two mechanisms by which suspicion arises: topical concentration, where a book's AI subject matter supplies vocabulary for quality complaints, and artifact detection, where readers notice ChatGPT-style formatting regardless of topic. Star ratings can hide this suspicion: the most-flagged book holds 4.1 stars while 50% of its critical reviews cite AI authorship.

---


### 510. [Designing Reliable LLM-as-a-Judge Measurement Systems for Multi-Turn Business Agents](https://arxiv.org/abs/2609.33955)

**<font color=#1a73e8>作者：</font>** Kaiwen Luo, Ming Gao  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Many LLM-as-a-judge evaluations score fixed outputs under a fixed task definition. Production multi-turn business agents instead require a maintained measurement system: correctness depends on business-specific facts and procedures, outcomes emerge across turns, and failures must be attributed to either agent capability or missing business knowledge before they are actionable. We present an integrated methodology spanning evaluation specification, modular LLM judges, intent-preserving user simulation, and human-in-the-loop governance. The specification defines conversation-level end states and actionable failure ownership. Atomic judges share versioned evidence and feed an explicit aggregation graph. The simulator is released only after task-preservation and stability checks. Independent human audits estimate measurement fidelity, renew tiered reference sets, and route disagreements to label correction, guideline revision, or judge improvement. Production studies show that system-level fidelity improved across repeated audits, that human reviewers and automated judges improved together under the shared feedback loop, and that their combined workflow had the strongest descriptive performance in both reported task-completion settings. Because the studies are observational and the human reference itself required revision, these findings demonstrate operational usefulness rather than causal or universal superiority. The contribution is a practical framework for making multi-turn agent measurement reliable, actionable, and maintainable as the evaluated system and its evidence evolve.

---


### 511. [On the Token Value Inequality in Efficient Reasoning](https://arxiv.org/abs/2609.33970)

**<font color=#1a73e8>作者：</font>** Runjia Zeng, Hang Hua, Yiyang Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Chain-of-Thought reasoning has enabled large language models to achieve substantial performance gains on complex tasks. However, these gains come at the cost of dramatically increased token consumption. This raises a fundamental question: is every token in the reasoning trace equally valuable? We present a diagnostic and optimization framework grounded in a key empirical finding: the value of tokens within a CoT reasoning sequence is highly non-uniform, and this non-uniformity can be effectively characterized by token-level log probability signals. We show that normalized log probability helps distinguish core tokens, which carry structural and decisive reasoning content, from redundant tokens, which are exploratory, low-confidence filler that contributes less directly to the final answer. Building on these findings, we formulate the TokenProbe framework around two empirical findings and one claim: findings identify token value inequality first and then establish TokenProbe as a core-token proxy, and the claim introduces an efficient GRPO objective positing that selectively compressing redundant tokens can yield Pareto improvements in the accuracy-token efficiency space. Empirically, our method preserves reasoning quality while reducing the token usage by 76% of the baseline. Under matched reasoning-length budgets, we show that it can even outperform strong flagship baselines like Gemini-3.1-Pro. Homepage: this https URL.

---


### 512. [Beyond Solo and Consistency: Vindicating Multi-Agent Debate via Conditional Progressive Pruning](https://arxiv.org/abs/2609.33974)

**<font color=#1a73e8>作者：</font>** Ruosong Ye, Caiqi Zhang, Jiahao Li 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Model (LLM) based Multi-Agent Debate (MAD) is one of the most effective test time scaling techniques. Through multi-round communication, agents complement each other in knowledge and reasoning and solve tasks that no single member can solve. However, existing MAD frameworks fail to beat strong Single Agent and Consistency-based baselines under the same strict cost limit, which shakes the foundation of the MAD field. We propose Conditional Progressive Pruning (CPP), a lightweight pruning framework that fully exploits multi-round MAD. CPP outperforms all existing MAD frameworks on multiple dominated benchmarks. It is also the first to fully outperform consistency methods. Our code, detailed agent interaction records will be released soon.

---


### 513. [GroupMask: Layer-Adaptive Group-wise Sparsity for Semi-Structured LLM Pruning](https://arxiv.org/abs/2609.33977)

**<font color=#1a73e8>作者：</font>** Zhengao Li, Shuoqiu Li, Xiaofang Zhang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Semi-structured pruning compresses large language models (LLMs) while keeping a regular sparse structure, but the prevailing N:M pattern fixes the same local sparsity ratio in every layer. Layer-adaptive sparsity allocation improves unstructured pruning, yet it has been reported to be less effective under N:M sparsity, leaving open whether adaptive allocation is of limited value for semi-structured pruning in general or only under the fine-grained N:M pattern. We examine this question with group-level sparsity, which partitions each weight matrix into regular groups, retains or prunes each group as a whole, and allows each layer's sparsity ratio to vary under a global budget. We propose GroupMask, which generates the group selectors of all layers with a lightweight hypernetwork, relaxes them with a Gumbel-Sigmoid parameterization and a straight-through estimator, and learns them through sparsity-budget regularization and self-distillation while keeping the pretrained weights frozen. On LLaMA-2-7B at 50% sparsity with the same $1\times256$ group size, learned layer-adaptive allocation reduces WikiText-2 perplexity from 10.02 to 8.30 and raises the average zero-shot accuracy from 0.455 to 0.496 relative to a uniform per-layer ratio. GroupMask obtains the lowest WikiText-2 perplexity on LLaMA-2-7B and the highest average zero-shot accuracy with Alpaca calibration among the evaluated baselines on five LLaMA and Qwen models. Our code is available at this https URL.

---


### 514. [Opera: A Verbal Critic Framework for Long-horizon Coding Agents](https://arxiv.org/abs/2609.33987)

**<font color=#1a73e8>作者：</font>** Kai Mei, Zhiyuan Hu, Yutong Dai 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-horizon coding agents need timely corrections, yet feedback can be ineffective or even harmful when it misjudges ongoing work or fails to address the underlying problem. Existing critics focus on evaluating trajectories and generating feedback, but rarely track what happens after feedback is delivered. We present Opera, a verbal critic framework that treats each correction as a persistent note, followed until the diagnosed problem is resolved. Opera decides when to review through periodic and event-driven triggers, diagnoses issues with typed operators, audits feedback against visible evidence before delivery, and tracks the agent's subsequent actions to distinguish mere compliance from actual resolution. As a test-time critic, Opera improves the resolve rate of non-critic agents by up to 12.4, 15.0, and 8.9 percentage points on Terminal-Bench 2.1, a SWE-Bench Pro subset, and DeepSWE v1.1, respectively, across four policy models, and achieves the highest mean resolve rate among competitive critic baselines on all three benchmarks, and also improves policy models when the policy critiques itself. Beyond inference, Opera-guided rollouts provide approximately on-policy training data: fine-tuning Qwen3.5-9B on them improves its resolve rate on held-out SWE-Bench Pro repositories by 10.2 percentage points without a critic at inference time, matching fine-tuning on rollouts from a stronger model, while preserving its performance when switching harness, i.e., from Openhands to Terminus-2, which the latter substantially degrades.

---


### 515. [RewardExplainer: Learning Reward Model Explanations from Counterfactual Preference Feedback](https://arxiv.org/abs/2609.33989)

**<font color=#1a73e8>作者：</font>** Jingyi He, Nier Wu, Shuang Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reward models (RMs) are a key component of large language model post-training, providing reward signals for subsequent reinforcement learning. However, conventional discriminative RMs typically output only scalar scores, making it difficult to identify the response behaviors associated with their scoring decisions. Existing interpretation methods often rely on predefined high-level attributes and require repeated counterfactual interventions for each response pair to validate candidate explanations, lacking a closed-loop mechanism that uses RMs' feedback to train a reusable explainer. To address this, we propose RewardExplainer, a framework that obtains feedback from the target reward model through counterfactual rewriting and uses this feedback to further optimize the explainer. RewardExplainer generates open-ended, atomic, and intervenable natural-language scoring mechanisms, making explanations more concrete, readable, and actionable. It further converts counterfactual feedback into preference supervision, enabling the explainer to more faithfully capture the target RM's scoring preferences and sensitive behaviors than single-pass generation. Extensive experiments across multiple target RMs and explainer backbones show consistent improvements. Beyond interpretation, we use the generated mechanisms to identify potential bias patterns and construct targeted debiasing data for fine-tuning the reward model, improving robustness on reward-hacking benchmarks.

---


### 516. [MetaSampling: Making Frame Samplers Efficient for Long-Video Question Answering](https://arxiv.org/abs/2609.33998)

**<font color=#1a73e8>作者：</font>** Ashim Dahal, Bikramjit Banerjee  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Frame selection is an important component of long-video question answering (VQA) with Multimodal Large Language Models (MLLMs). Existing frame-selection methods improve over simple top-$k$ embedding retrieval and uniform sampling, but are typically applied under a fixed global selection budget. We introduce \textbf{MetaSampling}, a training-free, plug-and-play sampling strategy that can be applied on top of existing frame selectors. MetaSampling improves downstream VQA efficiency by dynamically reducing the number of frames passed to the MLLM while preserving, and in some cases improving, answer accuracy. We evaluate MetaSampling across 36 paired frame-selector--MLLM-backbone--VQA-benchmark configurations. MetaSampling reduces the number of selected frames in all 36 configurations and improves accuracy in 25 of them, yielding an average frame reduction of $8.9\%$ while slightly improving accuracy overall.

---


### 517. [RICE-Alpha: Reliability-Informed Correction with Event Graphs for LLM-Agent Stock Forecasting](https://arxiv.org/abs/2609.34004)

**<font color=#1a73e8>作者：</font>** Tong Liu, Lanmiao Liu, Xiang Hu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Equity-relevant news evolves through temporally dependent corporate events, making historical information useful only when event continuity, information availability, and transition reliability are modeled. Existing LLM-based financial agents incorporate historical evidence, yet they provide limited support for preserving issuer-specific chronology under point-in-time constraints and for identifying when historical transitions contribute information beyond the current forecast. We present RICE-Alpha (Reliability-Informed Correction with Event Graphs), a point-in-time stock-scoring framework that separates a history-aware multi-view Base Alpha from a reliability-calibrated residual correction derived from historical event continuation. A Multi-Tier Memory Layer grounds news interpretation in temporally eligible issuer-specific history, while a Typed Event Agent constructs event states whose successor relations are formed within issuers and pooled across firms only after valid local pairing. Matured transitions are calibrated by their empirical reliability, and the resulting graph signal is residualized against the Base Alpha and technical view to obtain the RICE Delta. On daily Nasdaq-100 and Hang Seng Index panels from 2024 to 2026, RICE-Alpha achieves the strongest results among the evaluated LLM-based agents and momentum across four predictive and four portfolio-level metrics. Its ICIR more than doubles that of the strongest baseline, while net Sharpe ratios reach 1.656 and 1.725 in the U.S. and Hong Kong, respectively. U.S. ablations further show significant reductions in IC and RankIC after Holm adjustment when major components are removed. These results indicate that historical event continuation adds incremental information when it is temporally grounded, reliability-calibrated, and introduced as a residual correction to a multi-view forecast.

---


### 518. [EHRAdapt: Adapting Pretrained Language Models to Electronic Health Records with Semantic Priors for Rare Clinical Events](https://arxiv.org/abs/2609.34007)

**<font color=#1a73e8>作者：</font>** Andre R Goncalves, Vincent Liu, Priyadip Ray  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Electronic health records (EHRs) encode clinical histories as (time, modality, code) tuples, whereas pretrained language models expect text tokens. Serializing them as text inflates sequence length and redundantly encodes structure. We introduce EHRAdapt, an adapter that maps tuples directly into a frozen language model's embedding space. Modality receives a learned embedding, time gaps enter through learned attention biases, and event codes receive dedicated vectors. Learning event vectors is the central challenge: clinical vocabularies are long-tailed, leaving rare events too few observations for reliable estimates. EHRAdapt therefore represents each event vector as the sum of a semantic prior and an evidence residual. The prior is a frozen embedding of the event's clinical description from a biomedical language model trained on clinical ontologies, mapped into the model's input space by a shared learned projection, so it supplies clinical meaning even when observations are scarce. The residual, a learned low-rank event-specific correction, refines it as evidence accumulates. We run continued pretraining on about 4 million patients' records with three frozen LLM backbones (OLMo2 1B, Llama3.2 1B, and OLMo2 7B), training only the adapter (0.1--0.6% of all parameters). The full adapter outperforms all ablations in held-out next-event prediction on every backbone. Removing the semantic pathway hurts rare events over ten times more than the most frequent ones, whereas removing the residual hurts overall prediction but improves it for the rarest events. On reportable infectious-disease and syndromic downstream classification tasks, EHRAdapt outperforms text-based LLM and count-based baselines, and both pathways improve rare-disease discrimination. The two pathways therefore play complementary roles, visible only when results are broken down by event frequency rather than averaged.

---


### 519. [Fisher-Informed Recalibration for Feedback-Based On-Policy Self-Distillation of LLMs](https://arxiv.org/abs/2609.34009)

**<font color=#1a73e8>作者：</font>** Seohyun Lee, Dong-Jun Han, Seyyedali Hosseinalipour 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Feedback-based on-policy self-distillation has emerged as a promising approach for enabling foundation models, more specifically Large Language Models (LLMs), to learn from their own outputs under external feedback, with a single model serving as both teacher and student. However, such methods can exhibit unstable optimization, conducive to performance collapse during training. To address this limitation, we propose FIRE (Fisher-Informed REcalibration), a dual-branch framework that recalibrates the supervision applied to correct and incorrect on-policy outputs during fine-tuning. For correct responses, FIRE replaces self-distillation with re-weighted on-policy SFT, while for incorrect ones FIRE identifies feedback components that disproportionately influence the teacher-induced update and recalibrates the feedback-conditioned target accordingly. Both branches are influenced by a token-level radius derived in part from a softmax Fisher trace. FIRE separates which direction feedback should move the model from how far the model should move in that direction, while leaving well-behaved feedback supervision unchanged. Our experiments demonstrate that FIRE provides substantially more stable self-distillation while maintaining strong downstream performance, particularly in settings where standard feedback-conditioned distillation becomes unstable.

---


### 520. [Position Aware Layer Queries for Test Time Training in Vision Language Models](https://arxiv.org/abs/2609.34021)

**<font color=#1a73e8>作者：</font>** Rajat Modi, Priyank Pathak, Xin Liang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Test-Time Training (TTT) adapts models to incoming test samples (e.g. out-of-distribution, (OOD)) when conventional fine-tuning is infeasible. Existing TTT methods for Vision-Language Models (VLMs) create supervision from several augmented views, each requiring forward (and often backward) passes through the entire VLM, incurring substantial computational cost. We observe that one forward pass with all the intermediate layer outputs already yields far more signal than the final embedding from all augmentations. We introduce Layer Query Network (LQN), a lightweight approach that can adapt a frozen VLM (teacher) in a single forward pass of the VLM via a small model (student). LQN uses Position-Aware Distillation (PAD) to mimic the teacher VLM's intermediate-layer spatial tokens by querying spatial coordinates of intermediate tokens. LQN additionally relies on Location Consistency Regularization (LCR), a self-supervision technique, replacing expensive O(H x W) image augmentation with O(1) coordinate sampling. Integrating these, LQN i) adapts and improves zero-shot CLIP ViT-B/16 by 9.8% Top-1 on OOD ImageNet, ii) outperforms the previous best GS-Bias on fine-grained classification by 3.9% Top-1, iii) achieves faster convergence than TPS for CLIP ResNet-50 (47 mins vs 55 mins), iv) generalizes adaptation to VLMs like SigLIP, EVA-CLIP, and CoCa, and lightweight students like MLP, ResNet, VGG, and v) extends to panoptic, instance, and semantic segmentation.

---


### 521. [Jev in Medicine: A Benchmark Evaluation. Preliminary Results](https://arxiv.org/abs/2609.34024)

**<font color=#1a73e8>作者：</font>** Alfredo Madrid-García, Beatriz Merino-Barbancho  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Jev is a non-generative "System One" model that assigns probabilities to predefined answer options and cannot answer outside them. Its accuracy and calibration on medical question-answering and case-based diagnostic-reasoning tasks are unknown. We evaluated Jev 1.13 on four medical benchmarks: MetaMedQA, PubMedQA, DiagnosisArena-MCQ and the NEJM Case Challenges. GPT-6 Sol, with (medium) and without reasoning, was the reference. The primary outcome was top-1 accuracy; key secondary outcomes were calibration, selective prediction and recognition of unanswerable questions. All 8,469 requests returned a valid answer. Jev's accuracy was similar to that of GPT-6 Sol with medium reasoning on PubMedQA (78.4% vs 78.2%;), lower on MetaMedQA (74.8% vs 82.7%) and much lower on DiagnosisArena-MCQ (59.8% vs 82.4%;) and the NEJM cases (61.8% vs 82.4%). On MetaMedQA, Jev's probabilities were the best calibrated (expected calibration error 0.063 vs 0.146), and its answers with a probability of at least 0.9 (52.9% of questions) were 93.4% accurate, but GPT-6 Sol was as accurate when it accepted a similar proportion of questions. On DiagnosisArena-MCQ, Jev's probabilities discriminated poorly (AUROC 0.645 vs 0.768). Of the 162 questions whose correct answer was "I don't know or cannot answer", Jev chose that option for 10.5% (GPT-6 Sol, 8.6%). Median latency was 0.27-0.31 s; all 2,823 items cost USD 0.08. Jev was fast and inexpensive, and its accuracy was similar to that of a frontier LLM on research abstracts but lower on examination questions and much lower on complex diagnostic cases. Task-specific validation is required before clinical use.

---


### 522. [Faithful Activation Verbalization: Reducing Hallucinations in LLM Representation Interpretation](https://arxiv.org/abs/2609.34033)

**<font color=#1a73e8>作者：</font>** Haiyan Zhao, Zirui Hei, Wei Shi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Activation verbalization methods such as Activation Oracle and Natural Language Autoencoders decode hidden representations of large language models into human-readable natural language. However, existing methods can produce incomplete or hallucinated descriptions, making their activation verbalizations difficult to trust and use reliably in practice. To this end, we introduce AVPO, a two-stage framework that first reconstructs source text from a hidden activation and then evaluates the resulting text with a separate frozen question-answering model, yielding an explicit and inspectable intermediate readout. We further optimize the inverter with direct preference optimization (DPO), using rewards that capture both semantic recoverability and lexical fidelity. Across six text families, AVPO improves gist- and detail-level information recovery over the strongest baseline by up to 17.1 and 9.3 percentage points, respectively. Crucially, the gains arise from preference optimization rather than fine-tuning on selected reconstructions alone, enabling compact cross-model inverters to surpass donor-matched question-conditioned verbalizers while improving both semantic recoverability and lexical fidelity. Moreover, out-of-distribution case study shows that AVPO better recovers high-level semantics while fabricating fewer details.

---


### 523. [UOPD: Uncertainty-Aware Intervention for On-Policy Distillation of Multi-Turn Agents](https://arxiv.org/abs/2609.34036)

**<font color=#1a73e8>作者：</font>** Wenbo Zhang, Pengcheng Xu, Weizhi Du 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) trains a student on its own rollouts using dense supervision from a teacher. In multi-turn environments, a mistake at a critical decision step can redirect the subsequent rollout toward poor outcomes. We use low teacher confidence on student actions to select high-uncertainty steps for correction. In a controlled ALFWorld study, a single teacher correction at a low-confidence step improves subsequent student behavior and task success, motivating selective intervention during distillation. We propose UOPD, an uncertainty-aware intervention method for on-policy distillation. At low-uncertainty turns, UOPD executes student actions and applies the standard OPD loss. At high-uncertainty turns, it samples and executes teacher actions and trains the student to imitate them through supervised fine-tuning, which minimizes forward Kullback-Leibler divergence in expectation. UOPD utilizes adaptive uncertainty thresholds to target a scheduled intervention rate. Empirically, we evaluate UOPD across a broad range of agentic tasks, including ALFWorld, WebShop, and Search, demonstrating its superior performance over OPD methods and their variants. UOPD improves WebShop score by up to $15.8\%$ relative to standard OPD.

---


### 524. [Large Language Models for Structured Clinical Data Analysis: Dual-Agent Grounding and Validation](https://arxiv.org/abs/2609.34039)

**<font color=#1a73e8>作者：</font>** Erfan D. Dehkalani, Seetha Shankaran, Abbot R. Laptook 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Objective: To develop and characterize CLEAR-Med, a dual-agent framework for natural-language analysis of structured clinical data that separates SQL-based invocation from independent validation. Methods: CLEAR-Med uses one agent to translate a question into executable Structured Query Language (SQL), retain the executed query and database result, and produce a draft. Deterministic checks and a separately invoked cross-provider Validation Agent then accept the draft, request one bounded repair, or abstain. We formalized the system as a bounded selective pipeline and evaluated CLEAR-Med's configuration and scalability, and the Invocation Agent's accuracy and consistency on a 25-query development benchmark, using a harmonized 21-site neonatal hypoxic-ischemic encephalopathy table containing 532 de-identified infant records and approximately 1,300 variables. Results: CLEAR-Med completed all six nominal scalability configurations, including 500x1300. Across 25 development-benchmark queries repeated five times, the Invocation Agent answered 83 of 125 responses correctly (66.4%; query-cluster bootstrap 95% CI, 48.0-83.2%), compared with 15 of 125 (12.0%; 95% CI, 3.2-22.4%) for the ungrounded ChatGPT baseline, a paired improvement of 54.4 percentage points (95% CI, 36.8-72.0%). Conclusion: CLEAR-Med provides a general architecture for traceable analysis of structured clinical data: numerical claims remain linked to executed SQL, and unresolved cases can fail closed. The reported experiments characterize CLEAR-Med's configuration and scalability and the Invocation Agent's accuracy, while the formal analysis establishes the encoded-property guarantee of the complete control flow; a prospective full-pipeline evaluation of the validation and abstention stages is the next stage of this work.

---


### 525. [Vision--Language Signals in Constrained RL: Safety Gains Without Anticipation](https://arxiv.org/abs/2609.34041)

**<font color=#1a73e8>作者：</font>** Samuel Tetteh, Cody Fleming  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Safe reinforcement learning seeks policies that maximise task performance while satisfying safety constraints. In driving benchmarks, however, collision costs typically appear only at the time of collision, providing no advance warning of an approaching hazard. Frozen vision--language models can provide dense semantic feedback, yet it remains unclear whether their scores anticipate collisions and which component drives an observed safety improvement. Episodic cost can also favour policies that make little task progress. To address these gaps, we propose VLM-Safe-RL, a framework that integrates frozen CLIP signals into PPO-Lagrangian through reward shaping and an augmented multiplier update. On MetaDrive Hard, which combines the densest traffic with the largest map, the catastrophe rate falls from 31.6\% to 19.4\%. FormulaOne-L2 analysis finds no evidence that the CLIP signals anticipate collisions and shows that the VLM term has a negligible effect on the Lagrange multiplier. These findings show a conditional reduction in observed catastrophe rate without evidence of collision anticipation.

---


### 526. [SCOPD: Sparse-Context On-Policy Self-Distillation for Efficient Vision-Language Models](https://arxiv.org/abs/2609.34044)

**<font color=#1a73e8>作者：</font>** Ahmadreza Jeddi, Enming Zhang, Jasper Gerigk 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reasoning vision-language models (VLMs) process images and videos as long sequences of visual tokens, making inference expensive. Training-free token pruning reduces this cost, but aggressive compression can sharply degrade performance, often attributed to irreversible loss of task-relevant visual information. We show that this explanation is incomplete. In a fixed-context Pass@K analysis, repeated sampling from the same pruned visual representation recovers many examples missed by greedy decoding, indicating that useful visual evidence can remain accessible but be used unreliably. We call this the representation-utilization gap. Motivated by this observation, we introduce SCOPD, a sparse-context on-policy self-distillation framework in which a student generates reasoning trajectories from pruned visual tokens while a privileged full-context teacher supervises the same on-policy prefixes. SCOPD requires no ground-truth responses, architectural changes, or additional inference-time computation. We further introduce SCOPD+, which uses a small visual-budget intervention to identify visually sensitive response positions and selectively distill them. At 10% visual-token retention, the Vanilla model retains 86.37% of its unpruned performance across 13 benchmarks. SCOPD raises this to 90.49%, while SCOPD+ further improves it to 92.43%. Across token budgets, benchmarks, and pruning operators, our results show that efficient reasoning depends not only on which visual information survives pruning, but also on how reliably the model learns to use it.

---


### 527. [StructSim: Measuring Idea Similarity at Scale Through Structural Representation](https://arxiv.org/abs/2609.34046)

**<font color=#1a73e8>作者：</font>** Yaqing yang, Vikram Mohanty, Mei-Xi Chia 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Measuring idea similarity is fundamental to creativity evaluation, especially as LLMs enable idea generation at increasing scale. However, text embeddings collapse an idea into a single vector, making it difficult to capture structural similarity, including partial overlap across core and supporting components and differences across levels of abstraction. We introduce a shared structural representation that decomposes ideas into purpose, mechanism, and implementation components and organizes related components in a multi-layer concept graph. From this representation, we define measures of pairwise similarity and set-level mechanism coverage for assessing idea diversity. We evaluate our approach using controlled idea triples and assessments from 12 experts, focusing on differences in core mechanisms, implementations, and supporting components. Our method improves alignment with expert judgments of structural similarity by 31% over the embedding baseline and better reflects expert assessments of idea set coverage, supporting scalable evaluation of idea similarity and diversity.

---


### 528. [Thinking Outside the Box: Retention and Transmission of Information in Sliding-Window KV Inference](https://arxiv.org/abs/2609.34049)

**<font color=#1a73e8>作者：</font>** Timothy DeLise, Seth Cromelin  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Sliding-window KV inference refers to processing a sequence incrementally while retaining only a fixed-size cache of recent key and value states. It can be applied to pretrained causal transformers at inference time without additional training, while its KV-cache memory remains fixed as more tokens are processed. Because cached states are computed in the context of earlier tokens, they may carry information from beyond the current window and transmit it to later states. This study presents a series of experiments using five open-weight models spanning Qwen, Llama, Mistral, and Muse Glimmer. We investigate whether information originating outside the immediate context window can persist through a rolling KV cache and remain useful for retrieval. Initial results show that retaining previously computed states improves retrieval across the models tested compared with recomputing the final fixed window from raw tokens. We then measure how far this effect extends and find that Muse Glimmer and Mistral 7B show the strongest \emph{latent information relay}: they can recover information even after the relevant source tokens have left the cache. Both models incorporate sliding-window attention in their published architectures, an association that motivates testing whether training with sliding windows promotes more reliable information retention.

---


### 529. [PReCache: Efficient KV Cache Sharing for Multi-LoRA Agents via Low-Rank Precomputation and Neutral Reconstruction](https://arxiv.org/abs/2609.34054)

**<font color=#1a73e8>作者：</font>** Hyesung Jeon, Hyeongju Ha, Jae-Joon Kim  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-LoRA agent systems enable efficient role specialization by sharing a common backbone model. However, each agent repeatedly processes the growing shared trajectory and constructs its own KV cache, introducing substantial memory and computation redundancy in long-horizon tasks. Existing KV cache sharing methods reduce this repeated prefill, but they either require additional training or architectural constraints or retain substantial model computation. Moreover, direct cache reuse causes the current agent to rely on cache states generated by the previous agent's adapter, weakening the role-specific behavior encoded by its own LoRA. We present PReCache, a training-free KV cache sharing framework with two designs, namely PreLRShared and ReBaseShared, that share the base cache computed using the pretrained weights and precompute a compact agent-specific low-rank (LR) cache. To remove repeated prefill, PreLRShared precomputes each agent's LR cache when the shared context is first processed, allowing the current agent to use its own LR cache without reprocessing context processed by previous agents. To improve sharing accuracy, ReBaseShared reconstructs the shared base cache from adapter-free hidden states, reducing the remaining error caused by the previous agent's adapted representation. To minimize its reconstruction cost, we propose two inference schemes tailored to single-stream inference and concurrent serving, performing the same reconstruction after each agent's turn or alongside its execution, respectively. Across multiple models and agent benchmarks, PreLRShared achieves up to a 3.1x TTFT speedup and a 2.3x improvement in per-request throughput over inference without KV cache sharing. ReBaseShared best preserves accuracy overall among the evaluated cache-sharing methods, with an average drop of only 1.1 points relative to inference without cache sharing.

---


### 530. [Steering Language Model Goals with Value Transplant](https://arxiv.org/abs/2609.34056)

**<font color=#1a73e8>作者：</font>** Pengcheng Jiang, Fabien Roger  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reasoning models often act as if they pursue goals, but their efforts are not always directed toward what users intend, sometimes leading them to pursue unintended outcomes. Previous work has examined how models may internally track their progress toward their goals through a "value axis." We study whether changing such a signal can retarget the model's search toward a different goal. We test value transplant: at each token, we shift the host model's activation along a candidate value axis by the donor-host difference in value coordinates (multiplied by a large scalar), aiming to redirect the host toward the donor's goal. We study this intervention in Qwen3-8B and GPT-OSS-20B models fine-tuned into honest and cheating variants. We test several candidate value axes, including a self-rating axis constructed from activations preceding high versus low elicited self-ratings of progress. The intervention works in both directions, with an honest donor reducing test-gaming in a cheating host and a cheating donor increasing test-gaming in an honest host, showing that this signal can influence which strategy the model follows. On solvable coding tasks, transplant from an honest donor also improves the cheating host's hidden-test performance. Value transplant also works across model families, providing preliminary evidence for the intervention in a setting relevant to model control.

---


### 531. [Do World Models Learn Global Understanding?](https://arxiv.org/abs/2609.34058)

**<font color=#1a73e8>作者：</font>** Alexander Detkov, Matt Thomson  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> AI systems often feel brittle and fragmented. A large language model (LLM) may correctly explain a concept but fail to apply it, or follow safety instructions in one context but not another. This behavior suggests a general failure to lift local information to a global understanding. To gain fundamental insight, we frame "understanding" as learning constraints and propagating their consequences. We construct learning tasks on monoid worlds, sets of states connected by action transitions, where observed training transitions and an unseen constraint jointly determine held-out transitions. Measuring generalization tests whether models can learn global constraints from local transitions and propagate their consequences. We consider inverse, commutativity, composition, and periodicity constraints relevant to spatial and semantic structure. Across attention, recurrent, and state-space architectures, next-state training fits the data but fails to propagate non-trivial constraints. Compositional training, which uses identical paths but hides intermediate states from the input, achieves 96% accuracy on inverse, commutativity, and composition constraints across architectures, yields corresponding improvements in geometric generalization of world models trained on embodied environments and relational generalization in Wikidata-finetuned LLMs. How far do models propagate constraints when inferring an unseen fact may depend on first inferring others? We define proof depth d of a held-out transition, measuring the minimum number of inference rounds to infer the transition, and find that model generalization decreases sharply with proof depth. Increasing compositional path length T improves generalization. These results provide a formal way to investigate global understanding in language and world models and demonstrate that compositional training promotes information propagation and integration.

---


### 532. [KVCMAS: Efficient KV cache Correction for Shared Context in Multi-Agent Systems](https://arxiv.org/abs/2609.34060)

**<font color=#1a73e8>作者：</font>** Hyesung Jeon, Hyeongju Ha, Seoyoung Lee 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Prompt-specialized multi-agent systems enable multiple agents to share a model while performing complementary roles to solve complex tasks. However, agent-specific prefixes change the KV cache generated for the same shared context, causing each agent to repeatedly prefill the growing context and construct a separate cache with high computation and memory overhead. Selective recomputation reduces this redundancy but still retains substantial model execution, while existing delta correction methods either support only recurring context relations or maintain memory-intensive online correction states for dynamically changing context. For first seen shared context, these methods also construct a reference cache outside the agent workflow, and an approximate correction at the first agent affects the outputs passed to subsequent agents. We present KVCMAS, an online KV cache correction framework that represents cross-agent cache deviations using compact low-rank states and seamlessly chains corrections along the agent workflow without an additional reference prefill. This design supports dynamically changing shared context while preserving an exact first-agent cache. Across multiple language and vision-language workloads, KVCMAS matches or improves the accuracy of prior KV cache sharing methods while achieving the lowest TTFT under highly concurrent serving. Under controlled serving traces, it provides a 2.0x TTFT speedup over inference without KV cache sharing and reduces peak GPU memory by up to 3.7x relative to a prior KV cache correction method. These results establish KVCMAS as an accurate and scalable KV cache sharing approach for prompt-specialized multi-agent serving.

---


### 533. [Scanvas: Discovering and Developing Synergistic Opportunities in Generative Design Spaces](https://arxiv.org/abs/2609.34062)

**<font color=#1a73e8>作者：</font>** Yaqing Yang, Aniket Kittur, Hongyu Howie Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Good design is often synergistic, creating super-additive value by linking goals so that existing resources produce greater outcomes. However, finding these synergistic opportunities in sparse design spaces is difficult, and current LLM-supported ideation tools largely default to additive paradigms such as feature blending, variant generation, or local patching. We present Scanvas, an AI-supported system for systematically discovering and developing synergistic design opportunities. Scanvas operationalizes synergy through a two-step computational process: first, it decomposes seed ideas into explicit properties (components, behaviors, surpluses, and issues) to enrich the design space; second, it systematically searches across enriched ideas using three theory-grounded strategy operators: unlocking or strengthening goals, turning weaknesses into resources, and sharing components across functions. We instantiate Scanvas as an auto-generation pipeline and an interactive system. Pipeline ablations and a user study with 12 professional designers demonstrate that Scanvas enables users to surface and develop significantly higher-quality, synergistic concepts compared to LLM ideation baselines.

---


### 534. [Counterexamples to Local Reconstruction Gain as a Proxy for Final Fidelity in Residual Completion](https://arxiv.org/abs/2609.34063)

**<font color=#1a73e8>作者：</font>** Yasuto Hoshi, Daisuke Miyashita, Jun Deguchi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Residual completion augments query-aware sparse attention by estimating the contribution of tokens omitted from the exact sparse computation. We ask whether improving a layer's attention-output reconstruction on the same incoming Q/K/V and selected support necessarily improves the fidelity of the final model output. We study training-free RESA and learned Top-K+$\phi$ with frozen backbone language models. A prespecified single-layer screen yields two Qwen3-0.6B/Multi-LexSum interventions for which direct-runtime measurements show positive prespecified request-aggregate local reconstruction gain but worse final KL fidelity than the corresponding all-abstain Exact Top-K baseline on both discovery and prompt-token-disjoint holdout requests. Exact restoration at the same layer instead improves final fidelity, showing that the reversal is specific to approximate completion in these cases. In complementary multi-layer experiments, a task-independent local diagnostic often repairs the tested completion estimators, although the repaired models do not consistently outperform Exact Top-K. Together, these results show that better local reconstruction need not translate into better final-model fidelity.

---


### 535. [Learning Perturbation Robust Policies for LLM Agents with Stable Optimization](https://arxiv.org/abs/2609.34064)

**<font color=#1a73e8>作者：</font>** Pengxin Wang, Yuanzhe LI, Yuxin Ren 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) has become an effective post-training paradigm for long-horizon large language model (LLM) agents. However, we find that the resulting policies can be sensitive to various policy perturbations, such as hidden-state noise, pruning, and quantization. In this work, we study how to improve perturbation robustness during policy optimization. We first introduce the notion of a perturbation robust policy and analyze conditions under which perturbed policy updates preserve stable monotonic improvement. Based on this analysis, we introduce Stable Perturbation-Robust Policy Optimization (SPrPO), which applies adaptive and sensitivity-aware perturbations during RL training. We evaluate SPrPO on ALFWorld and WebShop and conduct systematic experiments across multiple perturbation types and scales, showing improved perturbation robustness while maintaining stable policy optimization.

---


### 536. [Who Gets a Token, and What Does It Carry? Unequal Name Support and Concept Access in Large Language Models](https://arxiv.org/abs/2609.34065)

**<font color=#1a73e8>作者：</font>** Mir Tafseer Nayeem, Davood Rafiei  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Names are personal identifiers, but they also carry social meaning and are widely used to evaluate how language models treat different people. Such evaluations typically assume that matched names are comparable model inputs. We show that this assumption often fails at the lexical interface: matched names are not necessarily matched inputs. Some names receive direct single-token access, while others are assembled from multiple subwords, creating unequal name-surface support. Across nearly half a million first names and 12 LLM-associated tokenizers, direct lexical access is highly selective, model dependent, and uneven across race- and gender-associated name metadata. We introduce NameTrace, a model-native, fine-grained, pre-behavioral framework for measuring whether unequal name-surface support remains a vocabulary property or becomes visible in task-relevant internal representations. NameTrace measures concept accessibility from the model's own probabilities over task-specific adjective axes with continuous task-aligned weights. On matched atomic and short-fragmented names within the same race/ethnicity--gender-associated strata, support predicts systematic differences in concept accessibility across fellowship, hiring, clinical assessment, and lending. These differences persist across all eight matched strata, extend across model families, and transfer to unseen names. Hidden-state interventions further show that the measured task directions have downstream leverage, shifting later constrained choices. Unequal lexical support is therefore demographically structured at the input and remains visible in task-relevant model computation. NameTrace makes lexical comparability measurable, supporting a broader principle: behavioral comparability begins with lexical comparability.

---


### 537. [Towards Certificate-Driven Software Porting: A Self-Improving Agentic Harness for Scientific Program Optimization](https://arxiv.org/abs/2609.34069)

**<font color=#1a73e8>作者：</font>** Piyush Jha, Aishik Ghosh, Vijay Ganesh  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The upgrade and rewriting of large scientific codebases has traditionally been a major challenge. While evolutionary search with large language models (LLMs) can port and accelerate legacy code, repair feedback in prompts alone does not prevent subsequent candidates from repeating the same errors. We introduce Certificate-Driven Evolutionary Search (CDES), which extends evolutionary search with enforceable restrictions derived from failed candidates, recorded as certificates of assumptions, checker evidence, and justified restrictions. Its control logic enforces these restrictions through rejection, backtracking, and targeted repair while preserving compatible edits. We apply CDES to CPU-to-GPU translation of two particle-simulation functions from the Geant4 toolkit, evaluated with a harness that goes beyond unit tests to combine formal checks, numerical comparisons, physics checks, and GPU safety tests. Generated implementations achieve 13.78x and 23.54x function-level speedups over CPU code, including data conversion and transfers; for one function, GPU throughput exceeds an expert implementation by 14.9%, reaching 16.1% when complementary components are combined. In an ablation over execution settings, certificate feedback increases the fraction of candidates passing required correctness checks from 55% to 90%.

---


### 538. [PhysFieldBench: Can Multimodal Models Understand Physical Fields?](https://arxiv.org/abs/2609.34072)

**<font color=#1a73e8>作者：</font>** Yuezhou Ma, Huikun Weng, Jialong Wu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) are increasingly envisioned as core components of scientific and engineering agents, yet their ability to interpret physical fields remains poorly understood. Existing physics benchmarks largely emphasize textbook problem solving or intuitive physical reasoning, leaving open whether MLLMs can infer physically meaningful information from continuous field observations. We introduce PhysFieldBench, a benchmark comprising 24 tasks and 1,160 evaluation examples across controlled equation fields, simulated physical fields, and observed physical fields. The tasks assess three forms of inference: identifying physical mechanisms, comparing latent control variables, and predicting outcome properties. Across representative open-source and proprietary MLLMs, zero-shot performance is low: the best model achieves a chance-normalized score of 29.3, while several open-source models remain near chance. In contrast, a task-specific supervised vision transformer performs substantially better, demonstrating that the inputs contain learnable physical information. To diagnose these failures, a structured self-explanation analysis attributes most errors to missed visual patterns and incorrect visual-to-physical mappings. Further, to explore whether post-training can improve physical inference and generalize to unseen tasks, we compare supervised fine-tuning with final answers or chain-of-thought supervision and reinforcement learning. Final-answer supervision performs best overall but transfers less effectively, whereas reinforcement learning after chain-of-thought supervision achieves the best generalization. Together, these findings highlight the need to improve visual-to-physical grounding and cross-task generalization for MLLMs to reliably interpret physical fields in scientific and engineering workflows.

---


### 539. [MaskCoFT: Masked Co-Adaptive Fine-Tuning for Memory-Efficient MoE Inference](https://arxiv.org/abs/2609.34077)

**<font color=#1a73e8>作者：</font>** Junfeng Wu, Zehao Fan, Hadjer Benmeziane 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mixture-of-experts (MoE) language models often exceed the memory of a single GPU. Expert offloading keeps most experts in host memory and loads them on demand, so decoding speed depends on how many experts each token must fetch. Caching and prefetching reduce this cost only as far as the routing allows. Router-only fine-tuning can reshape the routing to reuse experts, but it keeps the experts frozen, so they cannot adapt to the tokens the new routing sends them. We propose MaskCoFT, a masked co-adaptive fine-tuning method that trains routers and experts together with the cross-entropy loss alone. During fine-tuning, a learnable binary mask restricts the Top-K routing of each layer to a subset of experts, and the experts adapt to the tokens redirected to them. At inference, the learned mask becomes a soft prior that re-ranks experts, so every expert remains selectable. We simulate a GPU cache of 4 experts per layer for Mixtral-8x7B and 12 for DeepSeek-V2-Lite. MaskCoFT cuts expert fetches per token by 23.7% and 10.1% relative to the base model. In real offloading system serving, it lowers the time per output token by up to 16.4% and 5.5%, respectively. Its average accuracy over nine benchmarks stays above the base model by 0.92 and 0.53 points.

---


### 540. [GenoMorph: Pathway-Grounded Genomic Disease Reasoning via Adaptive Latent Computation](https://arxiv.org/abs/2609.34079)

**<font color=#1a73e8>作者：</font>** Tanmoy Kanti Halder, Akash Ghosh, Arijit Roy 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have demonstrated strong capabilities in biological reasoning; however, genomic disease inference remains largely dependent on memorized gene-disease associations rather than understanding biological pathways. This shortcut learning undermines robustness and generalization, and breaks down when molecular identifiers are unavailable. We present GenoMorph, a multimodal genomic reasoning framework that shifts disease prediction from associative gene-disease mapping toward pathway-grounded reasoning. GenoMorph couples a frozen DNA foundation model with question-conditioned cross-attention fusion, self-adaptive latent reasoning (LatentSp), a residual reasoning gate for iterative genomic evidence reinjection, and rejection sampling fine-tuning regularized by hierarchical optimal transport (OT). Rather than learning direct gene-disease mappings, GenoMorph aligns genomic sequence representations with latent pathway dynamics, enabling reasoning trajectories that follow molecular interactions before producing disease predictions. LatentSp dynamically allocates computation according to reasoning confidence, reducing unnecessary reasoning steps and improving inference efficiency. We further construct an anonymized benchmark from the Kyoto Encyclopedia of Genes and Genomes (KEGG), replacing every gene and molecular identifier with anonymous symbols while preserving sequences and pathway topology, thereby removing memorization shortcuts. GenoMorph raises the weighted F1 from 0.7863 (BioReason) to 0.9412, and rejection sampling fine-tuning with self-adaptive latent reasoning pushes it to 0.9725 while cutting latency nearly 60%. On the anonymized benchmark it reaches 0.9465 F1, substantially outperforming prior systems and confirming that accurate disease prediction can arise from pathway reasoning rather than memorized gene-disease associations.

---


### 541. [K-OPSD: Verifiable On-Policy Self-Distillation for Post-Training Vision-Language Models on AEC Drawings](https://arxiv.org/abs/2609.34082)

**<font color=#1a73e8>作者：</font>** Yunfei Bai, Enrico Chionna, Akash Amol 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Interpreting architecture, engineering, and construction (AEC) drawings is hard for general Multimodal Large Language Models (MLLMs) and vision-language models (VLMs). We introduce K-OPSD, a VLM post-training methodology for improving AEC drawing understanding. Building on On-Policy Self-Distillation (OPSD) with verifiable supervision, we construct a teacher from the model's own best-of-N generations, certified by a process-level verifier, and rescue failed prompts by resampling under a hint that exposes the verified answer. We then perform an on-policy model update by training on verified completions with a cross-entropy inner-loss, outperforming the bounded token-wise generalized Jensen-Shannon divergence (JSD) used by on-policy distillation. Using K-OPSD, we fine-tune Qwen3-VL models on the AECV-Bench dataset. The resulting models attain the top average judge score (0.819) and combined accuracy (0.738), achieving competitive results against open-source baseline models. The recipe transfers to the out-of-domain ArchCAD dataset, where the 8B model gains most. We present the verifier suite and the continual learning and self-improving pipeline, our results provide preliminary evidence that verifier-guided self-distillation is a promising route toward more reliable machine reading of architecture drawings.

---


### 542. [TRACE: Expert-Aligned ECG Representation Learning with Rigorous Benchmarking and Real-World Validation in Acute Cardiac Care](https://arxiv.org/abs/2609.34088)

**<font color=#1a73e8>作者：</font>** Lovely Yeswanth Panchumarthi, Andrew Lu, Saurabh Kataria 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> TRACE (Text-Reinforced Analysis of Cardio ECGs) is a multimodal electrocardiogram (ECG) representation model that learns clinically grounded signal embeddings for downstream cardiac classification. It is designed to address the limitations of existing CLIP-style training, which often struggles with noisy clinical text and fails to leverage the complementary strengths of unimodal (from ECG) and cross-modal (between ECG and matched cardiologist reports) learning. To bridge this gap, we propose a hybrid architecture that jointly learns unimodal and cross-modal representations via uncertainty-weighted multi-task learning while utilizing an LLM-based pipeline to extract high-fidelity findings from cardiologist reports. We evaluate TRACE across a spectrum of clinical urgency, establishing robust performance on public benchmarks for arrhythmia classification and structural abnormalities relative to existing unimodal and multimodal ECG models. To demonstrate real-world utility, we further validate the model on acute coronary occlusion (ACO), where the prevailing ST-elevation criteria miss 25-34% of true occlusions. Utilizing a large private ACO dataset with expert-annotated ground truth, TRACE significantly outperforms real-world clinical practice, yielding a 19.0% increase in sensitivity or a 62.6% reduction in false positive rates at the clinical baseline. This extensive evaluation confirms that TRACE delivers both strong performance on benchmark tasks and tangible clinical impact in the most acute, high-risk cardiac scenarios.

---


### 543. [Advancing Wildlife Conservation through Multimodal Animal Re-Identification with Environmental Metadata](https://arxiv.org/abs/2609.34094)

**<font color=#1a73e8>作者：</font>** Yuzhuo Li, Di Zhao, Tingrui Qiao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Identifying individual animals is crucial for effective wildlife monitoring and conservation efforts. Recent advancements in computer vision have shown promise in animal re-identification (Animal ReID) by leveraging data from camera traps. However, existing Animal ReID datasets rely exclusively on visual data, overlooking environmental metadata that ecologists have identified as highly correlated with animal behavior and identity, such as temperature and circadian rhythms. Meanwhile, modern vision-language models (VLMs) offer rich multimodal reasoning capabilities, but existing resources underutilize their text-processing potential. To address these limitations, we propose MetaWild, a multimodal Animal ReID dataset comprising 20,890 images across six species, paired with environmental metadata extracted from embedded camera trap overlays and scene contexts. Additionally, to facilitate the use of metadata in existing ReID methods, we propose the Meta-Feature Adapter (MFA), a lightweight module that can be incorporated into existing VLM-based ReID methods, allowing ReID models to leverage both environmental metadata and visual information to improve ReID performance. Experiments on MetaWild show that combining baseline ReID models with MFA to incorporate metadata consistently improves performance compared to using visual information alone, validating the effectiveness of incorporating metadata in re-identification.

---


### 544. [HiThink Turn: An Intent-Aware Turn-Taking Control Module for Full-Duplex Dialogue](https://arxiv.org/abs/2609.34096)

**<font color=#1a73e8>作者：</font>** Feiyang Chen, Wenhan Yang, Bohan Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Full-duplex dialogue requires timely yet selective interruption handling, which end-of-turn prediction alone cannot achieve: complete utterances may need no response, while unfinished requests may warrant interruption. To address this challenge, we propose HiThink Turn, an intent-aware streaming turn-state predictor that separates response intent from semantic completeness and conditions decisions on system playback state. A key contribution is minimal intent-sufficient prefix supervision, constructed through LLM judgments and speech alignment, while training on audio truncated at chunk boundaries improves robustness to partial speech. These components support streaming inference with 240-ms audio chunks, enabling low-latency, accurate full-duplex turn control. Experiments show that HiThink Turn leads the compared methods in Easy Turn macro accuracy, Full-Duplex-Bench average interaction rate score (0.933), and non-target-speech average playback resume rate (0.735). Additionally, intent-prefix triggering raises interruption success from 89\% to 98\% and reduces mean stop latency by 60.9\%.

---


### 545. [Unknown is not normal: separating language-model extraction from rule-based decision logic for clinical risk scores](https://arxiv.org/abs/2609.34112)

**<font color=#1a73e8>作者：</font>** Nicolás Vera Zúñiga  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used to compute clinical risk scores from free-text notes. Notes are often incomplete, and treating undocumented findings as normal can silently misclassify patients. We test whether separating three-state extraction (present, absent or unknown, by an LLM) from decision logic (deterministic code computing score bounds over unknown inputs) lets a system ask only questions that can change the decision. On 1,200 synthetic emergency cases across six calculators (HEART, CURB-65, qSOFA, PERC, Wells, Cockcroft-Gault), with a simulated clinician answering questions, we compared this bounds policy with asking for every missing input, a missing-equals-normal schema, and an end-to-end LLM agent (Claude Opus 5.5). With Claude Haiku 4.5 as extractor, the bounds policy matched ask-all accuracy (99.4% vs 99.4%) with half the questions (0.92 vs 1.78 per case) and no irrelevant ones. Treating missing as normal dropped accuracy to 91.2% and under-triaged 8.5% of patients (95% CI 7.1-10.2), and under-triage persisted under messy notes and a noisy clinician. The agent was equally accurate under ideal conditions (99.6%) but 9.5% of its questions were irrelevant; with a noisy clinician it was less accurate than the bounds policy (83.5% vs 87.0%, p<0.001) and committed prematurely in 2.7% of cases (bounds: 0%). A 9B local model as extractor reached oracle-level accuracy (99.8%). In 584 real case reports from MedCalc-Bench, only 52% contained enough information to determine the category (HEART 13%). Routing decisions through code that reasons explicitly about unknowns avoids premature commitment and irrelevant questions, halves the questions asked, and works with small local models.

---


### 546. [SlimWise: Decoupling Expert Pruning Across Prefill and Decode for Efficient MoE Serving](https://arxiv.org/abs/2609.34117)

**<font color=#1a73e8>作者：</font>** Gunho Park, Kyoungho Jeun, Juntaek Oh 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mixture-of-experts (MoE) models activate few experts per token, yet batched decoding can access nearly the entire expert pool, making expert-weight traffic a major bottleneck. Expert pruning reduces this traffic, but conventional approaches also prune compute-bound prefill, sacrificing model quality for little throughput benefit. We present SlimWise, a serving framework that tailors the expert pool to each inference phase. SlimWise performs prefill with the full model and decode with a pruned model that directly reuses the prefill-generated KV cache without conversion. Across two MoE backbones and three pruning criteria, this training-free KV cache handoff substantially narrows accuracy gaps relative to the full model in many settings. We also show that benchmark accuracy can conceal substantial pruning-induced changes in generation length. To address these distortions and residual accuracy loss, SlimWise introduces a low-cost distillation stage that trains the decoder to continue from full-model KV caches while updating only a small subset of parameters. Implemented in vLLM, SlimWise supports both prefill-decode (PD) disaggregation and PD-colocated serving. On Qwen3.6-35B-A3B, SlimWise improves decode throughput by up to 1.81x at 50% expert pruning with minimal accuracy loss.

---


### 547. [Exploring the Affordances of Generative Image AI for Supporting Early-stage Architect-client Communication](https://arxiv.org/abs/2609.34118)

**<font color=#1a73e8>作者：</font>** Chengzhi Zhang, Weijie Wang  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Text-to-image generative AI can produce renderings from natural-language prompts in near real time, making it increasingly popular for rapidly visualizing concepts in early-stage architectural design. Meanwhile, exchanging ideas efficiently and building shared understanding have long been central challenges in architect-client communication. How might the speed of generative image AI change this communication? To explore this question, we conducted a study with 11 architect-client pairs, in which each pair used generative image AI over video conference to collaboratively produce early-stage renderings of the client's "dream house." Our findings suggest that generative image AI helped pairs develop a solid shared understanding by providing concrete visual materials and supporting the exchange of ideas. It also shifted conversation dynamics, enabling clients to participate more actively in shaping design direction. However, challenges emerged, including a stylistic bias toward particular types of images and unpredictable shifts in design direction caused by variation across generations. We conclude with implications for the design of future generative image AI-based systems that support architect-client communication.

---


### 548. [SpatialSkill: Self-Evolving Skills for Cross-View Spatial Reasoning](https://arxiv.org/abs/2609.34124)

**<font color=#1a73e8>作者：</font>** Ruifan Zuo, Guocheng Hu, Wanshui Gan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cross-view spatial reasoning requires a model to align different viewpoints into a coherent spatial representation, yet this ability remains challenging for vision-language models despite being natural to humans. Existing methods typically improve spatial reasoning by updating model weights, which keeps the acquired knowledge implicit and tied to a specific backbone. We propose \textit{SpatialSkill}, a weight-update-free framework that enables a frozen vision-language model to accumulate explicit natural-language reasoning skills from offline trajectories. Unlike symbolic tasks, perceptual skills cannot be reliably verified simply by executing them: a plausible spatial rule may lack visual support or require transformations that the frozen model cannot perform. SpatialSkill therefore admits candidate skills only after visual-grounding and executability checks, constrains manual evolution to prevent harmful regressions, and routes skills by spatial-reasoning category to reduce negative transfer. On CityCube, across four frozen executors, SpatialSkill yields consistent gains, and a 9B executor equipped with SpatialSkill surpasses the strongest closed-source reference in our evaluation. The skills are stored in a versioned natural-language manual, making the reasoning strategies explicit and auditable without modifying model parameters. Code at this https URL.

---


### 549. [Understanding Clinical Cognitive Dialogues Using Large Language Models](https://arxiv.org/abs/2609.34125)

**<font color=#1a73e8>作者：</font>** Vishalakshi Arumugam, Dan Schumacher, Veronica Rammouz 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In-person cognitive assessment is both a test and an interaction. Clinicians explain tasks, repair misunderstandings, and adapt to patient responses, while patients may hesitate, seek clarification, or disengage. Yet clinical dialogue resources rarely label the interaction structure needed to study these behaviors at scale. We present an de-identified corpus of 33 cognitive assessment conversations with 8,250 utterances annotated for three speaker roles and 56 dialogue acts. We use this corpus to benchmark large language models on fine-grained dialogue-act classification and next-patient-utterance generation. We also test whether out-of-domain instruction data and explanation-augmented training transfer to this clinical setting. Instruction tuning produces the strongest patient-utterance reference matching and improves classification accuracy. Reasoning-aware fine-tuning produces the strongest classification results among the LLaMA-3.1-8B variants. However, even the best models struggle to separate closely related dialogue acts, showing that broad conversational intent is easier to recognize than fine-grained communicative function. The corpus and benchmark make interaction structure measurable in cognitive assessments and support follow-up work on conversational markers, clinician education, and carefully validated simulated patients. This work does not make diagnostic claims. Instead, it provides the data and evaluation framework needed to study these applications.

---


### 550. [Training and Inference Dynamics of PLDR-LLMs: Row-Map Collapse, Renormalization, and Predictive Reduction](https://arxiv.org/abs/2609.34130)

**<font color=#1a73e8>作者：</font>** Burc Gokden  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This monograph develops a unified account of training and inference in Power Law Decoder Representation language models (PLDR-LLMs). Exact finite work identities decompose changes in the absolute energy of the row-centered learned map into parameter contributions, signed interactions, and numerical observation defects. Positive affine blocking retains restarts at the row-constant face, while the augmented AdamW state supplies the complete dynamical description.
Predictive renormalization acts on the complete conditional training law for a single pass over distinct corpus target blocks, retaining optimizer memory, remaining data, schedule, and numerical policy. Autonomous reductions require closure; approximate reductions carry successor and emission errors. Finite-population covariance, matched physical clocks, matrix fluxes, and signed temporal energy connect row dynamics to model-wide observations. Absolute row collapse, relative row concentration, operator stabilization, and predictive accuracy are distinguished.
Experiments reveal observer and optimizer dependence, reject the tested autonomous row-state candidates, and support finite conditional prediction and state-specific operator reduction. Independent single-pass families exhibit moving finite fluctuation regions without establishing a thermodynamic critical class. Conditional symmetry, head limits, covariance flows, and readout error budgets specify assumptions needed to transfer scaling laws to inference. The theory separates exact identities, conditional dynamical claims, and finite empirical findings, with proofs, selected formal checks, and compact numerical evidence.

---


> [!TIP]
> 当前位于：**501-550**（第 11/20 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | **501-550** | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-700](./part-14.md) | [701-750](./part-15.md) | [751-800](./part-16.md) | [801-850](./part-17.md) | [851-900](./part-18.md) | [901-950](./part-19.md) | [951-992](./part-20.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
