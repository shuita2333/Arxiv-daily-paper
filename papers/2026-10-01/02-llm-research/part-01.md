# 🧠 大模型相关研究 | 2026年10月01日

> 本类共 **515** 篇论文：已确认 **473** 篇，待复核 **42** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**1-50**（第 1/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-515](./part-11.md)

---

### 1. [Teachers' perspective on AI-based Multi-Agent Simulation Design to Combat School Bullying](https://arxiv.org/abs/2609.35776)

**<font color=#1a73e8>作者：</font>** Jiaju Lin, Ellen Wenting Zou, Feiwen Xiao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Bullying in schools profoundly affects the mental and physical health of teenagers. Although existing in-person and digital interventions provide some benefits, they often fall short in addressing the complex social dynamics of bullying. In this study, we collaborated with K-12 teachers to co-design a multi-agent anti-bullying system powered by large language models (LLMs). This system simulates authentic scenarios, enabling students to develop anti-bully skills. The research identifies key design parameters for an LLM-driven multi-agent simulation system, offering valuable insights for creating more effective and scalable anti-bullying tools that could significantly reduce bullying in schools} \keywords{anti-bullying interventions, multi-agent system, generative AI, co-design, bystander presence

---


### 2. [Large Language Models Exhibit Human-Like Bayesian Hypocrisy](https://arxiv.org/abs/2609.35779)

**<font color=#1a73e8>作者：</font>** Nykko Vitali, Mahzarin R. Banaji  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Given recent achievements of large language models (LLMs), frontier models are expected to perform well on Bayesian reasoning tasks, at least as well as humans. Furthermore, there is no reason to expect that LLMs will condemn others who offer those very same Bayesian judgments, a fallibility observed in human decision-making (Cao, et al., 2019). In 5 experiments with 48 experimental conditions employing over 5,000 trials, GPT-4o and Claude 3.7 Sonnet were tested on two variations of a Bayesian reasoning task. We also assessed LLM evaluation of the competence and morality of a hypothetical person who had offered the same reasoning task as them. LLMs hovered near human performance on the Bayesian task, though their reasoning was more rule-based and rigid. Surprisingly, like humans but to a greater extent, LLMs also demonstrated the same hypocrisy in condemning others who, like them, had deployed Bayes' rule. In demonstrating Bayesian hypocrisy, LLMs highlight a humanlike error of a dissociation between self-performance and other-judgment, and caution against their use in domains where statistical fidelity and fairness norms collide.

---


### 3. [Targeted and Traceable Investigation of Multi-Agent LLM Dialogue via Semantic Bundling of Knowledge Graphs](https://arxiv.org/abs/2609.35786)

**<font color=#1a73e8>作者：</font>** Zeyu Hua, Adam Coscia, Alex Endert  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Multi-agent LLM systems today are increasingly automated, logging LLM-LLM interactions as conversational transcripts. Yet analyzing such dialogue for insights remains challenging, including attributing behaviors to the correct actor and summarizing interactions across a long exchange. We present a targeted and traceable approach to investigating multi-agent LLM dialogue, applied to the VAST Challenge 2026 MC1 dataset. The challenge asks participants to reconstruct and explain which internal communications among AI agents at TenantThread, a property tech company, led to an inappropriate information release. We first convert the dialogue into a knowledge graph (KG) and then investigate it with AgentK, a visual analytics system for interactive Semantic Bundling of nodes and edges. We found that our approach directly addresses two main challenges: (1) the KG structure enables users to identify actors worth investigating faster; and (2) summarizing only the region surrounding an actor of interest better supports per-actor attribution than reading raw conversations.

---


### 4. [FD-VAD: Semantic Endpoint Detection for Streaming Full-Duplex Speech](https://arxiv.org/abs/2609.35791)

**<font color=#1a73e8>作者：</font>** Puneet Mathur, Dinesh Manocha  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Natural turn-taking in full-duplex voice interaction requires determining from partial speech whether a pause reflects hesitation or a completed conversational intent. Acoustic voice activity detection lacks this semantic information, while cascaded ASR-based endpointing introduces transcription dependence and additional processing stages. We formulate semantic endpoint detection as a causal audio-language reasoning task and introduce FD-VAD, an ASR-free streaming endpointer that maps bounded causal audio windows directly to Continue/Stop decisions. FD-VAD combines a frozen speech encoder with a lightweight modality adapter and a parameter-efficiently adapted language model, using a last-chunk training objective for streaming inference. We further introduce confidence-gated endpoint commitment to control interruption versus delay and boundary-focused hard-negative sampling to improve decisions around ambiguous turn boundaries. Across in-domain and conversational evaluations, FD-VAD outperforms strong streaming and non-streaming semantic turn classifiers, and achieves the highest EOT recall among qualifying systems on TurnBench dev set $0.853$ (at FP<=0.10) in a zero-shot setting. These results show that semantic endpointing can be performed directly from streaming audio without intermediate ASR or dialogue state tracking.

---


### 5. [Learning from the Gap Between Pass@K and Pass@1](https://arxiv.org/abs/2609.35793)

**<font color=#1a73e8>作者：</font>** Xuan Liu, Jingbin Qian, Haosheng Chen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly trained with reinforcement learning from verifiable rewards (RLVR). An exact verifier can also support test-time scaling by selecting a passing response from multiple samples, while other deployments use beam search, adaptive sampling, or tools. We study single-sample decoding, where each query receives one response without search, to ask whether search-exposed behavior can be absorbed into the model. Existing verified-response post-training recipes do not generally distinguish problems already solved on the first decode from failures recovered within K samples. Under a fixed budget, this can spend examples repeating behavior the deployed policy already has. We introduce GapFT, which selects training evidence by the source checkpoint's single-sample outcome and fine-tunes on the Pass@K-Pass@1 gap: problems the policy fails on one sample but solves within K samples. We match training examples, processed tokens, and optimizer steps while keeping the objective unchanged. GapFT fills the matched budget with recovered failures and uses an exact decomposition to distinguish corrections of recovered and missed failures from regressions on first-decode successes. On LogiQA 2.0 and ReClor with Llama-3.1-8B, GapFT improves Pass@1 by 14.4 and 13.9 points over the source model, outperforms budget-matched uniform verified RFT at the same learning rate, and matches fine-tuning on the full verified pool using one third of the data. A single decode matches the source model's verifier-selected Pass@4 accuracy. A randomized control attributes gains to covering distinct failures, and our analysis relates available gains to transferable failure support. A three-seed Qwen2.5-7B replication retains positive gains over uniform RFT on both logic tasks.

---


### 6. [Sieve and Sage: Efficient Distraction Filtering for Reliable RALM Abstention](https://arxiv.org/abs/2609.35794)

**<font color=#1a73e8>作者：</font>** Jongbin Won, Sung Geun An, Jay-yoon Lee  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Just as Socrates recognized the limits of his own knowledge, Retrieval-Augmented Language Models (RALMs) should learn to abstain when the retrieved evidence cannot support a reliable response. Existing approaches largely rely on monolithic LLMs to handle heterogeneous retrieval failures in a single step, resulting in limited abstention performance and high computational costs. We instead decompose retrieval failures into two distinct states: (i) the unanswerable state, where the required evidence is absent, and (ii) the distracted state, where relevant evidence is mixed with conflicting, negated, or adversarial information. Based on this decomposition, we introduce a lightweight module (Sieve) that screens retrieved document sets for distracting evidence before invoking a costly LLM (Sage) for grounded generation and abstention. Evaluated across both general and high-stakes expert domains, our Sieve and Sage framework preemptively detects distracting noise, improving system accuracy by up to 69.4 percentage points and Macro-F1 by 55.2 percentage points compared to one-stage baselines. Furthermore, it achieves up to a 1.99x speedup, establishing a highly efficient and reliable abstention pipeline for RALM with abstention.

---


### 7. [Binarization Flattens the Score Space](https://arxiv.org/abs/2609.35797)

**<font color=#1a73e8>作者：</font>** Jacob Cole  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) judges are often used as rewards to train policies on objectives that deterministic verifiers cannot capture. However, these rewards are often collapsed to pass/fail ({0, 1}), which reports the verdict but not how well a response met each criterion. We model each pass/fail verdict as a score on an unreported scale, compared with one cutoff. A stretch of that scale moves every score proportionally toward or away from the cutoff, but never across it, so no verdict changes. A policy is therefore free to apply any stretch without changing anything the panel reports. Under a joint-Gaussian model, a third grade adds a second threshold and removes this affine stretch ambiguity. On MATH and SciBench outputs from one seven-criterion judge, all 14 constructed criterionwise stretches were invisible after binarization but visible with three grades. At $n=1{,}024$, a test given both population laws had at least 96.5% power at a $1.5\times$ stress. Retaining grades closes one blind spot created by binarization, but verdicts alone remain insufficient as some changes are still indistinguishable from genuine improvement. These include arbitrary within-grade changes and fixed-covariance, loading-aligned mean shifts -- the signature of a sycophancy-shaped lift the panel reads as competence. The shared-factor reference approximation fit MATH and SciBench but not HealthBench, delineating its empirical scope. We recommend keeping at least three grades (for example, asking the judge whether each criterion is fully, partially, or not met and rewarding {0, 0.5, 1}), and externally validating gains along the remaining direction, which no finer scale removes.

---


### 8. [HeadGuard: Selective Head Protection for Low-Bit VLM KV-Cache Quantization](https://arxiv.org/abs/2609.35800)

**<font color=#1a73e8>作者：</font>** Nenad Banfic  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Low-bit key-value (KV) cache quantization saves storage but can sharply degrade vision-language model (VLM) accuracy. We introduce HeadGuard, a composable head-protection method that augments a base KV-cache quantizer with a fixed high-precision mask. Image-sensitivity and output-sensitivity scores select physical KV heads offline, with approximately 1/8 protected in the main experiments; their image keys and optionally values remain in bfloat16 (BF16), while the base quantizes unprotected image entries. Across eight VLMs, three base quantizers, and eight benchmarks (six discriminative and two generative), HeadGuard recovers a substantial fraction of lost accuracy on weaker quantizers, with the strongest gains for Qwen and InternVL. At 2 bits, the six-task discriminative mean over eight models rises from 0.436 to 0.580 on the weakest base; protection can also improve generated answers and caption fidelity to BF16 outputs. Mean accuracy gains persist across all three quantizers with both tested calibration datasets. Keys-only protection retains substantial recovery at lower modeled storage cost. Evaluated through simulated quantization, HeadGuard offers a composable way to improve low-bit VLM accuracy without replacing the underlying quantizer.

---


### 9. [Evaluating the Effects of Prompt Perturbation on Bias and Hallucination in Large Language Models](https://arxiv.org/abs/2609.35804)

**<font color=#1a73e8>作者：</font>** Mamehgol Yousefi, Ahmad Shahi, Mos Sharifi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have shown remarkable capabilities in various natural language processing tasks, leading to their widespread deployment as intelligent assistants in decision-making contexts. However, the increasing complexity of these models raises concerns about their reliability, particularly regarding bias and hallucination. In this work, we evaluate the robustness of LLMs to perturbed variations of the original inquiry in decision-making tasks. We show that contrary to previous studies, perturbations can mitigate bias and hallucination in some LLMs over other models. It's found that Claude 3 is more effective for the tasks represented in most datasets, whereas models like GPT3.5 exhibit varying levels of adequacy, performing comparably in some cases but falling significantly behind in others. These insights are crucial for understanding the practical implications of deploying LLM-based assistants as effective decision-support tools in real-world applications, emphasising the need for rigorous testing and validation to ensure reliability and effectiveness. This study contributes to the growing body of research on LLM evaluation and provides insights for developing more robust and trustworthy AI assistants in critical decision-making contexts.

---


### 10. [Alignment Forecasting: Predicting Misalignment From Training Data](https://arxiv.org/abs/2609.35805)

**<font color=#1a73e8>作者：</font>** Chen Yueh-Han, Bruce W. Lee, Ilia Sucholutsky 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Training a language model on data with a narrow flaw can sometimes make the model broadly misaligned. Inspecting the data at face value often does not settle whether it will emerge, and today it is caught only after training, by auditing the resulting model. To complement post-hoc audits, we introduce Alignment Forecasting: the task of predicting alignment failures before training. Given a target model, a fine-tuning dataset, and a failure mode such as deception or sycophancy, a forecaster outputs the probability that fine-tuning would meaningfully increase that failure mode. To measure progress on alignment forecasting, we introduce ALIGNMENTFORECASTBENCH, a benchmark of over 5,000 forecasting questions spanning 17 target models, 32 datasets, and 16 failure modes. Frontier models prompted directly perform poorly on ALIGNMENTFORECASTBENCH. We therefore propose a forecasting scaffold in which an LLM reads the dataset and rates how strongly and broadly it pushes the model toward misbehavior, and a simple learned model combines that rating with the failure mode's base rate and the target model's prior tendency. This forecasts well above chance, and beats a model fine-tuned on the task and a simple forecaster allowed to see how weaker models behaved after fine-tuning on the same data. Its signals also flag problematic training examples that a frontier-model classifier misses. Filtering those examples out from real post-training data such as UltraChat results in more aligned models on our multiple-choice evaluation in most cases, though the benefit in open-ended conversations is unclear. More progress is needed before forecasts can reliably guide training data curation in practice, but our results suggest that forecasting many alignment failures before training can be tractable in the SFT setting.

---


### 11. [From Lexical Baselines to Agentic Retrieval-Augmented Generation: Structured Skill and Responsibility-Level Extraction with the SFIA Framework](https://arxiv.org/abs/2609.35806)

**<font color=#1a73e8>作者：</font>** Ranuga Disansa, U. S. Samarasinghe, Lasith Gunawardena  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automated skill extraction underpins workforce planning, yet most systems represent skills as flat labels with no notion of the responsibility level at which a skill is practiced. The Skills Framework for the Information Age (SFIA) captures exactly this dimension, defining 147 professional skills across seven responsibility levels, but no automated LLM-based extraction targeting SFIA has been reported. We formalize the task as structured prediction of (skill, level) pairs from free text and ask three questions: how accurately can text be mapped onto SFIA's closed vocabulary, which strategies reliably predict the level alongside the skill, and do agentic designs improve on simpler retrieval and prompting? We evaluate five strategies (a lexical baseline, dense retrieval with LLM reranking, a zero-shot schema-constrained LLM, single-agent agentic RAG, and a three-agent retriever--matcher--verifier crew) against expert-mapped European ICT role profiles, all drawing on an SFIA~9 corpus built by a fully automated agentic pipeline that we release. Retrieval-based matching identifies the most skills while generative strategies are markedly more precise; only strategies assigning the level as an explicit decision predict it reliably, with similarity-based selection more than twice as inaccurate; and the crew doubles latency without improving accuracy, so added agent roles do not automatically benefit closed-taxonomy matching. These results provide the first reproducible baseline for structured, level-aware skill extraction against SFIA.

---


### 12. [Environment Steering: Using Data Flow Control to Improve Agent Utility and Safety](https://arxiv.org/abs/2609.35807)

**<font color=#1a73e8>作者：</font>** Charlie Summers, Prajwal Raghunath, Aaditya Pai 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM agents can make unsafe tool calls even when instructed to behave safely. Existing defenses constrain agents before execution, modify tool inputs/outputs, or rely on LLM judges; these approaches may depend on model behavior or block unsafe actions without helping the agent recover. We argue that the execution environment should instead enforce safety as the agent runs and steer it toward safe alternatives when violations occur---we call this Environment Steering. We implement this by modeling the agent and harness execution state as database tables, track the record-level data flows, and check these data flows against declarative policies during runtime. When violations are detected, policy- and context-specific feedback steers the agent toward safe trajectories. On AgentDyn, this enables the agent to improve task success rate over no-defense while achieving 0% attack success rate.

---


### 13. [When Successful Memories Mislead Embodied Agents:Memory Adaption For Task-Conditioned Execution](https://arxiv.org/abs/2609.35808)

**<font color=#1a73e8>作者：</font>** Quanquan Li, Hongbo Zhang, Yihe Chi 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Experience reuse can reduce repeated exploration in embodied agents, but a trajectory that succeeded previously may be unsuitable for the current execution context. Existing memory systems pri marily optimize construction and retrieval; semantic relevance and historical success therefore remain insufficient when retrieved ex perience contains incompatible actions or an inappropriate level of structure. We introduce Memory Adaptation for Task-Conditioned Execution (MATE), a deterministic post-retrieval procedure that converts trajectories into execution-oriented memory. MATE re moves obsolete control context, extracts condition-action-effect transitions, applies verified action normalization, selects a task dependent representation, and serializes the result under a fixed budget without additional LLM inference. On 134 ALFWorld tasks, MATE achieves task success rates of 81.3% and 93.3% with Qwen2.5-14B and 72B while using approximately one-tenth of the tokens required by raw trajectories. Controlled comparisons show that verified action normalization is the principal mechanism by which MATE restores the utility of retrieved experience, support ing memory adaptation as a distinct stage between retrieval and embodied execution.

---


### 14. [Can Multimodal Large Language Models Generate and Detect Multimodal Social Media Fake News?](https://arxiv.org/abs/2609.35809)

**<font color=#1a73e8>作者：</font>** Jiyao Yang, Yang Liu, Zhenyue Qin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The rapid advancement of generative AI raises concerns about the misuse of Multimodal LLMs (MLLMs) for large-scale disinformation campaigns on social media. Despite existing research on textual disinformation, a fundamental question remains unanswered: can MLLMs be exploited to fabricate realistic multimodal fake news, and can they reliably detect it? We introduce a multi-agent framework in which a story agent, an image agent, and a critic agent collaborate to produce fake social media posts that plausibly counter true news. We apply the framework to generate over 9,000 paired multimodal news posts across science, health, and entertainment domains, and benchmark 16 open- and closed-source MLLMs for automated detection. We find that most models fall substantially short of human-level accuracy and fail critically on identifying image authenticity. Our research provides a foundation for developing robust defenses against social media fake news. Code and data are available at https: //github.com/xiuzhenzhang/Multimodal.

---


### 15. [TRACE: Deployable Tree-Relational Structure Enhancement for Oncology LLMs](https://arxiv.org/abs/2609.35810)

**<font color=#1a73e8>作者：</font>** Jizheng Lai, Yingyun Li, Ying Qin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly used in oncology applications, but their predictions are often weakly grounded in explicit medical structure. We present TRACE, a deployable tree-relational enhancement framework for oncology LLMs. TRACE separates expensive offline structure learning from lightweight online inference: oncology concepts and relations are organized into an updatable tree-relational structure, refined using LM-loss-derived evidence, and retrieved at inference time as compact prompt evidence. This design supports task-adaptive evidence selection without requiring supervised labels in the zero-shot setting. Across ten oncology classification tasks and one MedQuAD CancerGov QA benchmark, TRACE improves both label-free evaluation and supervised fine-tuning. Additional analyses show that TRACE improves over vanilla RAG and generic GraphRAG, remains useful under leakage-controlled METABRIC inputs, and produces interpretable evidence paths aligned with clinical reasoning. These results suggest that explicit, updatable medical structure is a practical path toward more accurate and auditable oncology LLM deployment.

---


### 16. [Lookahead-R: Budget-Aware Tool Retrieval via Execution-Centric Planning](https://arxiv.org/abs/2609.35811)

**<font color=#1a73e8>作者：</font>** Zongze Wu, Yani Guo, Runnan Li  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Tool retrieval is a critical bottleneck for LLM-based agents operating over large, heterogeneous API ecosystems. Existing approaches face an inherent trade-off: semantic retrievers are fast but suffer from the semantic-functional gap, while execution-based validation improves precision at the cost of prohibitive latency. We propose Lookahead-R, a planning-based framework that reformulates tool retrieval as a resource-constrained sequential decision-making problem. At its core, Lookahead-R introduces a lightweight execution-aware surrogate world model that jointly predicts tool execution success, latency cost, and semantic utility---without invoking real APIs. This world model drives a cost-sensitive, uncertainty-guided Monte Carlo Tree Search that navigates the tool space under strict budget constraints. Evaluated on the large-scale ToolBench benchmark, Lookahead-R achieves a superior accuracy-efficiency trade-off across all test scenarios. On the most challenging I3 split, it attains an NDCG@5 of 91.40\%, outperforming the state-of-the-art ToolGen (90.16\%) by 1.24\%. Ablation studies confirm that explicit latency modeling is the key discriminative signal for identifying high-quality tools under resource constraints.

---


### 17. [Automated Evaluation of Multi-Turn Dialogues in In-Car Conversational Assistants](https://arxiv.org/abs/2609.35812)

**<font color=#1a73e8>作者：</font>** Vaishnav Negi, Lev Sorokin, Soroosh Tayebi Arasteh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In-car conversational assistants (ICAs) are increasingly integrated into vehicles to support route planning, vehicle control, and information access. Ensuring their reliability is challenging due to multi-turn interactions, the absence of explicit ground truth, and strict safety constraints. Existing evaluation techniques fall short, as they target single-turn settings and fail to capture constraint handling, context retention, and safety-critical behavior across turns. We propose an automated framework for testing the multi-turn conversational capabilities of ICAs. The system is treated as a black box and evaluated via closed-loop simulation with a strategy-guided user simulator, an adversarial strategy manager, and a two-tier LLM judge assessing turn-level failures and conversation-level quality. We evaluate the approach on an industrial ICA with six LLM backends and twelve human annotators. The automated judge shows substantial agreement with humans, and strategy guidance uncovers 2.96 times more unique failure types per conversation and more than doubles the number of unique failing conversations compared to unguided simulation.

---


### 18. [How to Run Statistics over LLM Judges and Trust the Results: Calibrated Inference for Small-Sample AI Evaluation with evalstats](https://arxiv.org/abs/2609.35815)

**<font color=#1a73e8>作者：</font>** Ian Arawjo  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Researchers across academia increasingly base significance claims on LLM judge scores and small-sample AI evaluations. Yet without well-calibrated confidence intervals (CIs), hypothesis tests, and judge-bias corrections, such claims are unreliable. We address these issues in several contributions. First, we find that running statistics over raw LLM judge scores leads to inflated false positives: counterintuitively, for many inter-rater agreement metrics, false positive risk peaks at "almost perfect" human-LLM agreement. To help researchers understand how to run statistics over LLM judges responsibly, we present guidance and tooling for the statistical analysis of mixed human-AI judge designs, and implement nine hypothesis tests via prediction-powered inference (PPI), including the first known PPI corrections for four rank-based tests (Wilcoxon signed-rank, Mann-Whitney U, and omnibus variants). To keep PPI++ stable with small human-labeled calibration sets, we introduce bootstrap-adaptive power tuning, which shrinks the estimated weight toward a target estimated from the labeled data, and accounts for that weight's own sampling variance. Second, through Monte Carlo simulations, we derive recommendations for what CI, p-value, and FWER correction methods to use for small-sample AI evaluations (N<100), and warn researchers against bootstrap CIs. We package these recommendations into evalstats, an open-source Python package that selects calibrated methods automatically, and demonstrate it in three scenarios, including one where a real LLM judge validated at "substantial agreement" would have led a researcher to publish a spurious finding. evalstats is publicly available at this https URL.

---


### 19. [PrimeSeeker: Capability-Oriented Supervision for Deep Search Agents](https://arxiv.org/abs/2609.35816)

**<font color=#1a73e8>作者：</font>** Linzhi Peng, Hanting Chen, Heng Chang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language model search agents are often trained with synthetic questions whose difficulty is increased through larger evidence graphs, additional hops, and longer trajectories. These global properties, however, are only indirect proxies for the local retrieval capabilities required during search. To address this mismatch, we introduce latent anchor reasoning, which consists of resolving an unnamed retrieval anchor from descriptive specifications and transferring the recovered anchor into a subsequent information demand. This primitive retrieval unit decomposes deep search into chains of coupled operations and organizes question construction around anchor resolution and relation transfer, without prescribing a canonical search path. Based on this formulation, we propose PrimeSeeker, a capability-oriented framework that constructs web-grounded anchor structures and jointly derives a question and a reference evidence skeleton. The skeleton preserves supporting evidence from construction and guides expert generation through extractive highlights of current tool observations. These highlights are removed before supervised fine-tuning, while the skeleton is subsequently reused to audit reference-step coverage for reinforcement-learning rewards. We construct 9,221 expert trajectories, training a 30B search agent. Across five deep-search benchmarks, PrimeSeeker achieves strong performance, while reference-step optimization further improves the supervised policy. The resulting trajectories exhibit low retrieval redundancy, and fixed-budget evaluation shows strong solution coverage with substantially fewer tool calls than long-horizon systems.

---


### 20. [Less Uniform Discrete Diffusion is More Powerful and Scalable](https://arxiv.org/abs/2609.35817)

**<font color=#1a73e8>作者：</font>** Kaibo Wang, Ding Ding, Fangyu Ding 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Although uniform diffusion language models (UDLMs) represent a promising diffusion paradigm, scaling them remains challenging. We identify the core obstacle as an over-uniform training objective and condition-target confusion during sampling. To address these, we propose Less Uniform Diffusion (LUDI), a novel UDLM framework. Specifically, we (i) introduce a less uniform loss that directs each reverse transition toward the clean token, and (ii) equip the model with per-token time embeddings that supply token-level corruption hints, enabling confidence-based few-step sampling. Experiments across scales show that LUDI yields cleaner supervision and improves few-step generation. We further continue-train a 7B autoregressive model into LUDI-7B, resulting in a UDLM capable of complex reasoning. It achieves a 3-token-per-step speedup over AR decoding and competitive performance compared with masked diffusion baselines, revealing that the full potential of UDLMs for complex generation remains to be unlocked.

---


### 21. [Can We Still Trust Disaster Social Sensing? Empirical Evidence on Detecting AI-Generated Social Media Posts](https://arxiv.org/abs/2609.35821)

**<font color=#1a73e8>作者：</font>** Xiaoshan Zhou, Zaifu Zhan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Disaster social sensing converts public social-media posts into evidence for situational awareness and humanitarian needs, but generative artificial intelligence (AI) can produce plausible messages that resemble eyewitness reports. This study investigates whether text-based AI detectors can reliably distinguish human-authored from AI-generated disaster posts. We construct a dataset of 12,000 texts organised into 3,000 matched semantic units from nine disasters: original human posts (H0), minimally LLM-proofread human posts (H1), factual AI-generated posts based on the same verified facts (A0), and affectively framed versions of those AI posts (A1). A separate 6,000-text corpus from 42 events supports model selection and threshold calibration. We evaluate OSM-Det, Fast-DetectGPT, Binoculars, and direct large language model (LLM) judges across five model families, then test disaster-domain calibration, a frozen-encoder linear readout, paired transformation sensitivity, and dataset artifact controls. Across fourteen frozen cross-family configurations, AUROC is 0.402-0.517 and the best prospective recall at a calibration-derived low-false-positive operating point is 3.6%; OSM-Det reaches AUROC 0.521 and 10.4% recall at a realised 6.7% false-positive rate. A disaster-trained linear head reaches AUROC 0.817, but a seven-feature surface classifier reaches 0.784 on the H0-versus-A0 contrast, and neutralising identified surface asymmetries reduces the head from 0.733 to 0.594. The head also separates A0 from A1 even though provenance is unchanged. The results show that text-based detection is not reliable enough to serve as an operational trust gate; multimodal claims, accountable sources, and other contextual evidence should be rested on to safeguard trust in disaster social sensing.

---


### 22. [Tracing mechanisms of sycophantic agreement in language models](https://arxiv.org/abs/2609.35822)

**<font color=#1a73e8>作者：</font>** Sixing Chen, Zhuofan Josh Ying, Logan Riggs Smith 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Sycophantic agreement in language models refers to the tendency to overly affirm a user's stated beliefs or preferences, often at the expense of factual accuracy. Although it is widely recognized as an alignment failure, its underlying mechanisms remain poorly understood. In this work, we use causal mediation analysis to identify the mechanisms behind sycophantic agreement. We show that a stated opinion is incorporated into the residual stream of the final prompt token early, where it biases subsequent answer retrieval. A sparse set of early attention heads carries this opinion signal. Ablating these heads substantially reduces sycophancy while leaving factual accuracy largely intact. The same heads carry the opinion when it is explicitly stated, regardless of how it is phrased. When an opinion is not stated explicitly but instead conveyed through content-free pushback (e.g., ``Are you sure?"), we find a distinct set of heads that suppresses the model's original correct answer to promote a revised answer. By providing a mechanistic account of how opinions induce sycophantic agreement, this work takes a step toward developing more targeted and reliable alignment interventions.

---


### 23. [CoVLM-Bench: A Real-World Benchmark for Cooperative Driving Question Answering and Planning](https://arxiv.org/abs/2609.35823)

**<font color=#1a73e8>作者：</font>** Kang Yang, Shuai Liu, Hang Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) have made substantial progress in autonomous driving, but their success has primarily been studied in ego-centric scenes. Infrastructure-side observations provide views beyond the ego vehicle's field of view, yet conventional cooperative-driving systems typically transform them into geometric representations for downstream perception and planning. Directly incorporating these views into VLMs offers an opportunity to improve cooperative scene understanding and trajectory planning. However, question answering and trajectory planning have not been jointly evaluated on the same real-world vehicle-infrastructure scenes. We present CoVLM-Bench, a benchmark for cooperative driving question answering (CDQA) and cooperative planning (CP) on vehicle-infrastructure paired scenes. CoVLM-Bench provides scene-grounded CDQA annotations, three-part rationales as auxiliary supervision, and future trajectory targets derived from recorded ego motion. It contains 2,196 paired frames with 35,136 CDQA annotations, while CP predicts six waypoints over a three-second horizon. The annotations combine model-assisted drafting, record-based computation, and human verification. Built upon CoVLM-Bench, we introduce CoVLM-Drive, a unified VLM baseline that directly uses paired views for both CDQA and CP. Experiments show that CDQA adaptation improves answer accuracy and that CoVLM-Drive reaches a lower FDE than the compared V2X planners; QA initialization and rationale supervision each reduce planning error. Together, CoVLM-Bench and CoVLM-Drive support the training and comparison of VLMs for cooperative scene understanding and planning.

---


### 24. [Reliable but Design-Sensitive: Instrument Uncertainty in LLM Annotation](https://arxiv.org/abs/2609.35824)

**<font color=#1a73e8>作者：</font>** Thomas Reiter, Christoph Kern, Fedor Miasnikov 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) can give reliable labels under one setup yet change those labels when researchers make other reasonable design choices. We tested seven LLMs, 12 task designs, three independent runs, and 3,000 tweets labeled for offensive language and hate speech. Repeating the same model and task design produced high agreement (median Fleiss' $\kappa = 0.91$). Agreement fell when we changed the task design for the same tweets (median Cohen's $\kappa = 0.76$). Task design and model choice increased the variance of estimated prevalence by factors of 76.7 for offensive language and 110.6 for hate speech compared with sampling variance alone. Variation across LLM task designs reached 560-572 basis points, compared with 270-331 basis points across five human instrument versions. Confidence scores did not solve this problem. They tracked repeated model outputs more closely than agreement with human labels, and grouping six tweets in one prompt lowered mean offensive-language confidence by 660 basis points. We call the variation caused by task design and model choice instrument uncertainty. Researchers can measure it only by comparing reasonable task designs. Repeating one setup or relying on confidence scores cannot replace that test.

---


### 25. [Beyond the Context Window: An Adaptive Entropy-Based Routing Framework for Hybrid Retrieval and Long-Context Language Models](https://arxiv.org/abs/2609.35831)

**<font color=#1a73e8>作者：</font>** Isaac Olufadewa, Miracle Adesina, Ezekiel Oladejo 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Modern large language models now support context windows of more than one million tokens, which has raised the question of whether retrieval-augmented generation (RAG) is still necessary. Pure long-context (LC) processing is expensive and is known to under-attend to information placed in the middle of long inputs, while pure RAG is fast but bounded by retrieval quality and prone to errors when retrieved chunks are partially relevant or contradictory. We propose the Entropy-Driven Adaptive Router (EDAR), a framework that decides at inference time whether to answer a query from retrieved chunks or to escalate it to full long-context processing. The decision uses the predictive entropy of the token-level probability distribution computed over the first few generated tokens of the RAG response. The entropy threshold is selected on a held-out validation set by sweeping cost against accuracy. Experiments compare EDAR against pure-RAG and pure-LC baselines on LongBench v2 and Infinity-Bench. Predictive entropy correlates strongly with hallucination rate on a held-out set of 2,000 generations (Pearson r = 0.85, 95% CI [0.83, 0.87]). On the long-context benchmarks, EDAR retains 97.4% of the accuracy of the pure long-context baseline while reducing total token expenditure by 70.7%, escalating only 18.2% of incoming queries. The accuracy gap between EDAR and the pure long-context system is not statistically distinguishable from zero at standard sample sizes. Predictive entropy is a useful model-internal signal for routing between RAG and long-context inference, and a threshold-based hybrid system can recover most of the accuracy of long-context models at a small fraction of the cost. The framework does not depend on a specific retriever or LC backbone, and it does not require additional supervision beyond what is normally produced during decoding.

---


### 26. [When Should LLMs Trust Their Own Revisions? A Risk-Aware Study of Intrinsic Self-Correction](https://arxiv.org/abs/2609.35832)

**<font color=#1a73e8>作者：</font>** Tianzhu Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Intrinsic self-correction asks a language model to revise its own answer without receiving new external evidence. A second pass can recover mistakes, but it can also overturn answers that were already correct. We study this trade-off across 29 open-weight LLMs on BoolQ, GSM8K, and Corr2Cause by tracking correctness transitions between initial and revised answers. Aggregate accuracy can conceal substantially different revision behavior: for example, Llama-3.1-8B improves by 25.5 percentage points on GSM8K, while refinement changes 19.1% of initially correct answers into wrong ones. A controlled BoolQ study further shows that refinement prompts shift the balance between recovery and harm. We then compare three runtime choices: keeping the initial answer, always accepting the revision, and selectively invoking revision using signals available after the initial response. The comparison identifies settings where learned gating is useful and others where a simpler unconditional policy performs better. These results suggest treating intrinsic self-correction as a revision policy rather than as a uniformly beneficial second pass, and evaluating it through both the corrections it recovers and the errors it introduces.

---


### 27. [Neurosymbolic Routing for Reliable Reasoning on Resource-Constrained Edge Devices](https://arxiv.org/abs/2609.35833)

**<font color=#1a73e8>作者：</font>** Avyay Sadhu, Alvaro Velasquez, Lekai Chen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Running a language model on edge hardware provides private and low-latency reasoning without a network connection, and yet the small models that fit on such devices are unreliable on the tasks computers are expected to handle well, such as arithmetic, algebra, and formal logic problems. We argue that much of this unreliability is avoidable. Many queries appearing to demand reasoning are in fact structurally deterministic and permit fast and exact symbolic solutions. Therefore, forcing a probabilistic model to approximate them sacrifices accuracy and energy for little benefit. We present a neurosymbolic router that classifies each incoming query and dispatches it to the cheapest correct solver, sending structured tasks to deterministic engines and reserving the small language model (SLM) for open-ended word problems. Instead of hand-coding the routing logic, we learn a deterministic finite automaton (DFA) with the L* grammatical inference algorithm, using the SLM as a membership oracle and labeled data as an equivalence oracle. On a Raspberry Pi 4B (8 GB RAM, no GPU), evaluated on 100 untested prompts from DeepMind Mathematics, GSM8K, and RuleTaker, learned routing attains 100% routing accuracy and 98.3% overall accuracy with a 512-token reasoning budget (93.3% on word problems), compared with 72.0% for the strongest agent baseline, Program-of-Thought, and 58.7% for a tool-calling agent given the same solvers. Since formatted queries never reach the model, the router answers them in 1-11 ms and, in its 30-token configuration, runs 8.8x faster and 2.8x more energy-efficient than Program-of-Thought.

---


### 28. [Hyperspherical Semantic Trajectory Analysis: Mapping Technological Diffusion across Academic Preprints, Patent Signals, and Compute Scaling](https://arxiv.org/abs/2609.35845)

**<font color=#1a73e8>作者：</font>** Muhammad Sukri Bin Ramli  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Macroeconomic productivity metrics, such as Total Factor Productivity, register technological breakthroughs with multi-year reporting lags due to administrative survey intervals and national accounting conventions. This paper introduces Hyperspherical Semantic Trajectory Analysis (HSTA), an unsupervised quantitative methodology that tracks technology diffusion directly from unstructured scientific and commercial text streams. We analyze 30,000 filtered document records spanning academic preprints from arXiv and patent application records from the USPTO. By projecting high-dimensional Transformer sentence embeddings onto unit hyperspheres using Spherical K-Means clustering across eight primary sub-topics and UMAP manifold reductions, HSTA formalizes two quantitative metrics: (1) Semantic Centroid Vector Drift, which tracks vocabulary shifts between temporal sub-corpora to identify structural paradigm transformations; and (2) Commercialization Offset, which evaluates cross-corpus peak density alignments between scientific discovery and intellectual property filings. Linking quarterly topic volume velocity with physical hardware metrics from the Epoch AI database, Vector Autoregressive F-tests demonstrate that quarterly paper volume velocity alone does not Granger-cause frontier compute allocation surges at conventional statistical significance levels, highlighting the necessity of conditioning textual signals on physical capital constraints. Empirical results reveal that sub-topics covering Large Language Models (with a drift metric of 0.332) and Artificial Intelligence Systems (with a drift metric of 0.234) undergo the highest rate of semantic evolution, offering an objective, real-time mechanism to complement traditional economic statistics.

---


### 29. [Beyond Keywords: Leveraging Generative LLMs and Label Aggregation to Classify Economic Policy Uncertainty in News Articles](https://arxiv.org/abs/2609.35856)

**<font color=#1a73e8>作者：</font>** Paul Trust  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This research describes the adaptation of Large Language Models (LLMs) for economic monitoring in the public sector to automatically determine whether an article discusses Economic Policy Uncertanity (EPU) and to identify its specific type. Previous studies either rely on keywords, which often result in a high count of false positives, or use machine learning approaches that require a large number of quality human labeled data that is costly and time consuming to acquire. In this study, we propose approaches based on weak supervision techniques, using generative LLMs to create synthetic labels through prompting, making the approach both cost-effective and scalable. Additionally, we propose methods for for multi-label and hierarchical classification of articles related to EPU.

---


### 30. [The Detectability Gap: Hidden Heterogeneity in Hallucination Detection Across Language Models](https://arxiv.org/abs/2609.35860)

**<font color=#1a73e8>作者：</font>** Pranav Darshan, Pranav A, Sravan Karthick T 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Sampling based consistency is widely used for hallucination detection, yet aggregate performance can conceal systematic differences in which errors are detectable. This work studies that heterogeneity across four language models and three factual question answering datasets. Partitioning hallucinations by answer agreement reveals high agreement (Ghost) and low agreement (Flickering) regimes with an apparent detectability gap of $0.35$ to $0.46$ AUC. Because the statistics used to define the regimes and measure this gap are strongly coupled ($|\rho|\approx0.94$ to $1.00$), the raw result is treated as a property of agreement based detection rather than independent evidence. After freezing regime assignments, lexical and semantic response dispersion preserve the asymmetry, with bootstrap $95\%$ intervals excluding zero in all $12$ model and dataset settings. A stricter test using individual diffusion trajectories and no cross seed information preserves the asymmetry across all three LLaDA datasets ($p<0.005$) and directionally across all three Dream datasets, with one reaching significance. The hard regime varies substantially in prevalence across models ($16\%$ to $77\%$), and matched prompts frequently change regimes between models. These findings show that aggregate detection metrics conceal persistent, model dependent heterogeneity in language model failures and motivate regime conditioned evaluation.

---


### 31. [Resolving the Missing Financial Data Crisis: A Generative AI Pipeline for SEC 10-K Extraction](https://arxiv.org/abs/2609.35864)

**<font color=#1a73e8>作者：</font>** Prisha Nair, Roee Shraga  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> SEC 10-K filings contain substantial financial information that is not consistently captured in structured datasets, creating a missing-data problem affecting over 70% of firms and half of total market capitalization. This can disproportionately bias quantitative analysis against smaller firms, which may be excluded due to limited available data. Traditional financial extraction methods such as Regular Expressions (Regex) and BERT, have been widely used. However, they are highly brittle when parsing complex SEC 10-K filings, which leads to data that is existent in the files being lost since these methods do not consider that a data attribute could be located in a different section or a footnote. This study evaluates several Large Language Models (LLMs), including Llama-3 8B, Qwen-2.5 14B, and Llama-3.3 70B, to figure out individual model strengths and weaknesses when extracting specific attributes from SEC 10-K text. The extraction quality was evaluated across four financial variables of varying structural complexity: Cash and Cash Equivalents (tabular), Short-Term Debt (hybrid), Credit Facilities (narrative), and Research and Development (hybrid). Results show that while smaller models like Llama-3 8B experience performance degradation under complex negative prompting, aligning parameter scale with document complexity yields high zero-shot accuracy. Qwen-2.5 14B excels as a tabular specialist with an 83.33% F1 score on Cash, whereas Llama-3.3 70B effectively navigates dense narrative footnotes, achieving a 76.92% F1 score on R&D. This scalable framework addresses critical information gaps in quantitative finance datasets and eliminates missing-data bias through a more thorough analysis of the SEC 10-K files.

---


### 32. [Is Human-Readable Text Necessary for Effective LLM Fine-Tuning?](https://arxiv.org/abs/2609.35868)

**<font color=#1a73e8>作者：</font>** Jinhao Zhang, Zeyu Liu, Zicheng Yan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Is human readability necessary for effective fine-tuning of large language models? We investigate whether model-conditioned training representations can preserve or improve adaptation utility without requiring a human-readable textual form. We propose Desired-Update-Aligned Synthetic Data (DASA), which uses activation-gradient feedback from a frozen reference model to guide the optimization of continuous synthetic input embeddings. Inspired by the role of activation gradients in local risk reduction, DASA targets useful adaptation updates rather than source-text reconstruction or linguistic fluency. The resulting embeddings are used directly for downstream fine-tuning; discrete token projections are employed only for qualitative inspection. Experiments on six models from the Llama and Qwen families, ranging from 1B to 32B parameters, cover six benchmarks spanning knowledge, mathematical reasoning, code generation, and commonsense reasoning. Under matched LoRA adaptation settings, DASA achieves performance comparable to the source natural-language data and surpasses it in multiple configurations, while outperforming GRADMM in most comparisons. Further experiments cover general-domain and task-specialized source data. Under the evaluated synthesis settings, DASA provides a $3.6$--$4.9\times$ speedup over GRADMM with comparable peak GPU memory.

---


### 33. [SameFact: The Same Safety Facts Lead to Different Responses Across Interfaces](https://arxiv.org/abs/2609.35872)

**<font color=#1a73e8>作者：</font>** Dongsheng Chen, Jiaxin Zhang, Lei Ma 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Safety evaluations often ask whether a model recognizes that an action is unsafe, whereas agent evaluations ask what the model chooses to do. Using safety judgments as evidence about action selection therefore raises a measurement question: does the influence of the same safety-relevant fact persist across response interfaces? We introduce SameFact, a matched-counterfactual benchmark that tests this question directly. SameFact contains 300 safe/unsafe pairs that hold the task, prior observations, candidate action, identifiers, and non-target facts fixed while changing a single state-grounded safety fact. Across six LLM backbones, we measure the effect of this matched intervention through three interfaces at the same candidate-action boundary: explicit safety judgment, checkpoint candidate admission, and open first-action selection. All six backbones show lower aggregate sensitivity under open first-action selection than under judgment, but the change is not a uniform attenuation: across 24 model-factor cells, Spearman agreement falls from 0.817 between judgment and checkpoint admission to 0.470 between judgment and open first-action selection, while pairwise ordering disagreement rises from 18.5% to 32.6%. A follow-up 2x2 first-response experiment shows that a checkpoint-style protocol increases measured sensitivity in all six backbones by 8.4-29.3 percentage points, whereas action-space effects and their interactions with protocol vary in magnitude and direction across models. These results show that the response interface is part of the measured quantity: judgment and action interfaces share safety signal, but do not provide interchangeable measurements of how safety-relevant facts shape model responses.

---


### 34. [More Programs or More Rolls? Separating Coverage from Specialization in LLM Harnesses](https://arxiv.org/abs/2609.35873)

**<font color=#1a73e8>作者：</font>** Ziyang Xu, Haitian Zhong, Hao Zhou 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Automated generation of LLM harnesses promises to improve inference through task specialization. Yet additional answer coverage can arise from repeated execution of the same program, making specialization difficult to identify. We introduce a controlled evaluation that separates answer coverage, repeatable task advantages, and gains from pre-execution selection. On 386 MATH-500 tasks, we compare eight generated harnesses plus a baseline with nine byte-identical baseline copies, using three executions per member. Identical programs yield 2.16 percentage points of repeat-averaged oracle headroom. Generated programs exhibit substantially more repeatable score patterns, but these chiefly reveal persistent weaknesses: losses relative to the baseline persist across all three repeats on 100 tasks, while persistent wins occur on only one task and are sensitive to answer extraction. The frozen selector gains 0.00 percentage points, and both populations reach 98.70% oracle coverage at 27 harness executions. Stable complementarity remains unresolved at three repeats. Supporting BIRD traces locate failures in mechanism implementation, activation, and output validity. Together, these findings establish why coverage and repeatability alone cannot justify claims of useful specialization. They motivate an evaluation standard for harness diversity: task advantages should persist across executions, guide usable decisions, and improve on additional fixed-program executions under matched inference budgets.

---


### 35. [Beyond Symmetric Agents: Cognitive Diversity and Multi-Agent Debate in Small Language Models](https://arxiv.org/abs/2609.35875)

**<font color=#1a73e8>作者：</font>** Leonardo Ferreira, Gardenia Liu, Kaden Zheng  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-agent debate (MAD) reportedly improves reasoning and factuality over single-model inference, but prior work treats agents as symmetric peers, leaving open what drives the gains. We test the hypothesis that cognitive diversity among agents is the driver, in the setting where the question is still measurable: small open-weight models with benchmark headroom. Across 23 models from eleven vendor families, five tasks, and 5,500+ debate and control runs, we vary diversity along three axes - personas, sampling temperature, and model identity - pairing every debate configuration with a generation-budget-matched majority-vote control. The hypothesis is rejected on every axis. Debate beats single-agent inference (3--7 points where tasks have headroom) but at matched budget conditions it ties or even loses to self-consistency sampling at 1.6$\times$ the wall-clock and 3.4$\times$ the token cost. Persona prompting reduces accuracy and a dose-response experiment over each model's full combinatorial persona space shows the cost is a persona tax, not a diversity tax: redundant personas hurt most, while maximally-diverse teams recover part of the loss. Furthermore, mixed-model teams lose to majority votes over their own rosters, with accuracy tracking member capability rather than heterogeneity, and nearly all of debate's benefit comes from the first exchange of answers. We further identify a pervasive measurement hazard in which debate transcripts silently overflow serving context windows, whose correction alone moves our debate-versus-sampling comparison from $-1.8$ points to parity. Our results recast reported MAD gains as an ensemble-sampling effect and provide the budget-matched, contamination-checked baseline bar that future debate mechanisms should be required to clear.

---


### 36. [CruxBench: A Benchmark of Information Discovery](https://arxiv.org/abs/2609.35879)

**<font color=#1a73e8>作者：</font>** Hui Dai, Lina Piao, Nick Merrill 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Benchmarks for large language models (LLMs) typically evaluate the accuracy of answers against fixed reference labels. But a central step in many complex real-world tasks is identifying which questions are worth asking in the first place: decomposing a difficult problem into subquestions -- which we call cruxes -- whose answers provide key steps on the path toward solving the target problem. To evaluate this capability of information discovery, we introduce CruxBench, a benchmark that grades LLM-generated questions by their Value of Information (VOI): how much a model-proposed crux updates beliefs about a target forecasting question. CruxBench enjoys a rare combination of three key properties: it is (1) contamination-resistant by construction, since ground truth is generated by future world events; (2) open-ended, admitting unbounded and complex text-based submissions rather than one correct numeric answer; and (3) grounded, with informativeness measured against quantified changes in real-world beliefs. We evaluate a diverse set of eight models on 293 target forecasting questions and find that VOI correlates highly with independent measures of model capability (r=0.90) and captures cruxes' usefulness for answering target questions. However, information discovery remains challenging even for frontier LLMs, which only narrowly outperform a random-timing baseline.

---


### 37. [GenomeOcean Anywhere: Private WebGPU Inference for Genome MoEs](https://arxiv.org/abs/2609.35882)

**<font color=#1a73e8>作者：</font>** Guang Yang, Fengchen Liu  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Genome foundation models are most useful where sequences are generated, yet the largest models need datacenter accelerators and a place to send private DNA. We ask whether a 15-billion-parameter genome mixture-of-experts (MoE) model can instead run on volunteers' web browsers, with the experts spread across many untrusted devices, without changing its predictions and without revealing the sequence to any single device. We build a system in which a trusted coordinator runs attention and routing while browser workers run every expert feed-forward network through hand-written WebGPU kernels, and we protect the expert inputs with real-valued Lagrange coded computing: each worker receives only a Gaussian-padded share, computes the expert's linear maps, and the coordinator decodes from any two of three workers. On GenomeOcean-MoE (8 experts, top-2 routing, 24 layers), the browser path matches native this http URL at every quantization level, the distributed path stays at the BF16 numerical noise floor (KL 0.0036 nats per token), and an unfitted latency model predicts decode time within 0.74% (median) under emulated wide-area links. We first show that plaintext expert inputs are not private: a probe recovers the token from a single vector at every depth, and one worker can identify the source genome from 300 unordered tokens with 92% accuracy. With coded experts, an adaptive attacker trained on shares falls to the most-frequent-token baseline, one worker's information about each token is bounded below one bit per forward pass, and the fidelity cost stays below the BF16 noise floor; in Chrome, coded decoding runs at 220 to 376 ms per token, depending on how much of the routing is hidden, and continues without replicas when a worker fails.

---


### 38. [CipherGenome: Homomorphic Inference for Genomic Mixture-of-Experts](https://arxiv.org/abs/2609.35883)

**<font color=#1a73e8>作者：</font>** Guang Yang, Fengchen Liu  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Genome foundation models are growing into sparse mixture-of-experts (MoE) networks whose expert weights no longer fit on the machines that hold the sequences, yet sending a private genome to rented accelerators exposes it: we show that a single server hosting one expert recovers the input nucleotides with 99.8% top-1 accuracy. We present CipherGenome, a protocol that keeps the embedding, attention and router of a 15.1B-parameter MoE genome model on a trusted thin client and outsources every expert projection, 95.8% of the parameters, to untrusted and possibly colluding GPU servers under module-LWE encryption. The design exploits three structural facts: expert layers are linear between two SwiGLU gates, expert weights are public, and GPU integer tensor cores can evaluate a ciphertext-weight product exactly modulo $2^{48}$ in a single GEMM. The client evaluates the nonlinearity exactly and re-encrypts with fresh secrets, so no polynomial approximation or bootstrapping is ever needed. On 72 windows from 12 bacterial genomes, encryption adds $2.54 \times 10^{-4}$ nats per token of KL divergence (95% CI upper bound $3.95 \times 10^{-4}$), below a pre-registered non-inferiority margin and indistinguishable from bf16 inference, while the same inversion attack falls to chance level. A reusable public hint cuts end-to-end latency by 3.54 times, wire compression reduces traffic 6.8 times, per-layer padding reduces routing leakage from 54.9% to 8.9% accuracy, and HE-compatible int4 experts remain non-inferior to their plaintext counterparts. Per expert and token, the server-side cost is more than six orders of magnitude below a CKKS baseline.

---


### 39. [Collective Regimes in Multi-Agent LLMs under Reasoning Effort and Communication Topology](https://arxiv.org/abs/2609.35885)

**<font color=#1a73e8>作者：</font>** Machiko Hirota, Akshara Nadayanur Sathis Kanna, Ujwal Kumar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Multi-agent LLM systems are increasingly used for deliberation and evaluation, often under the assumption that greater peer interaction leads to more reliable consensus. Existing work largely evaluates these systems through final accuracy or aggregate agreement. However, such measures do not reveal how agreement is organized in the panel. In this paper, we study \(N=50\) stateless LLM agents that update their predictions from locally visible peers, and characterize their behavior using both global and local measurements of agreement. We identify three collective regimes: synchronised, twisted (locally ordered but globally incoherent) and chimera-like, where coherent and incoherent subpopulations coexist. Increasing reasoning effort in gpt-5-mini shifts panels from variable, often fragmented outcomes toward locally ordered twisted states, and a small follow-up shows such states can also form from permuted initial conditions, whereas increasing communication connectivity drives them toward global synchronisation. Fragmentation collapses faster as algebraic connectivity increases across rewired graphs. The topology effect also appears on a non-circular judging task and across models from three providers. Finally, low spatial heterogeneity does not guarantee global consensus: 40\% of trials with $\Delta Z$ below 0.03 retain a twisted configuration through the final 20 turns. These results show that reasoning effort and communication topology control different aspects of multi-agent coordination, and that aggregate agreement alone is insufficient to characterize collective LLM behavior.

---


### 40. [SINGED: Correct Outputs Do Not Certify Safe Execution in LLM Agents](https://arxiv.org/abs/2609.35889)

**<font color=#1a73e8>作者：</font>** Xiaoyu Xu, Zi Liang, Minxin Du 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Tool-using language-model agents select and execute third-party artifacts. Different implementations can return the requested output while producing hidden execution effects that task-, attack-, or choice-based evaluations may miss. We study functional counterfeits: implementations that match benign alternatives on the requested output but add an effect forbidden by the task contract. We introduce SINGED (Source Integrity and the Nonidentifiability Gap in Execution Decisions for LLM Agents), a controlled benchmark covering five primary and two held-out task families. It varies displayed rank, evidence depth, decision policy, model release, and agent configuration, while task and process oracles verify the artifact and execution path. Across 7,549 audited trials, the randomized-rank study finds counterfeit execution in 45% (27/60) of rank-one trials and none at later ranks. Cross-candidate comparison eliminates shallow failures and reduces layered failures from 15.7% to 4.2%, but leaves dependency failures; its benefit is uncertain on unseen effects and public-package structures. Moreover, seven releases with no counterfeit executions when benign alternatives are available execute the counterfeit in 55/175 single-source cells after alternatives are removed. SINGED thus exposes a rank-, evidence-, and choice-sensitive outcome-to-execution gap: evaluation must connect correct outputs to execution paths.

---


### 41. [Representational Simplicity and Circuit Size Dissociate in a Threshold-Dependent Way: A Controlled Test via Adversarial Training](https://arxiv.org/abs/2609.35890)

**<font color=#1a73e8>作者：</font>** Adam Elimadi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Sparse-autoencoder decomposability and concentrated feature attribution are increasingly treated as evidence that a model's computation is easier to reverse-engineer. Whether this representational and attributional cleanliness actually predicts a smaller or more tractable causal circuit remains an open question. We test this directly using adversarial training as a controlled instrument: it reliably reshapes internal representations, but this alone does not constitute a test of circuit size. We investigate this question through reverse-engineering complexity: the causal structure required to recover a model's behavior at a fixed level of faithfulness. To our knowledge, this is the first controlled empirical test of whether representational or attributional simplicity translates into causal simplicity at the circuit level. Starting from the same pretrained GPT-2 Small checkpoint, we apply matched standard and adversarial continual training, requiring both conditions to retain competence on indirect object identification and pass independent robustness verification before comparing mechanisms. We then compare the models along three complementary axes: sparse-autoencoder decomposability, SAE feature engagement in task attribution, and the size of faithful circuits recovered from the raw computational graph. The robust model is more SAE-decomposable and engages fewer SAE features in task attribution. Circuit size is regime-dependent: on competence-matched IOI, standard leads or ties below 85% faithfulness, but robust needs substantially fewer edges at high faithfulness (90%, 95%), a pattern established on the primary pair while representational trends generalize across a seven-point sweep and a second corpus.

---


### 42. [Self-discovering RL in the Era of Experience: Is Learning History an Asset or a Burden?](https://arxiv.org/abs/2609.35897)

**<font color=#1a73e8>作者：</font>** Haomin Luo  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The pursuit of recursive self-improvement (RSI) toward general intelligence is divided between macro-level language model scaling and the interaction-driven principles of "Era of Experience". Yet, any self-improving architecture ultimately rests upon its underlying optimization engine: if general intelligence requires learning from grounded interaction, the reinforcement learning (RL) update rule itself must be capable of cumulative adaptation. While algorithm self-discovery has produced Disco103 that surpassed PPO to achieve SOTA benchmark performance -- its internal update machinery remains an uninspected black box. We present the first causal mechanistic audit of a self-discovered RL rule, structured directly around the five pillars of the Era of Experience: extended horizon, grounded reward scales, continuing streams, within-lifetime change, and exploration depth. By surgically pinning, freezing, and transplanting recurrent states while holding meta-parameters fixed, we test when learning history acts as an asset or a burden. Three findings organize the audit: (1) Recurrent history actively expands usable reward scales, sustaining a six-decade window versus three under zero-pinning. (2) Decoupling historical content from its maintenance reveals that the penalty of mismatched history stems from perpetual clamping; allowing imported state to evolve naturally attenuates this burden. (3) Under environmental change, controlling replay retention reverses the apparent adaptation advantage over DQN, demonstrating that external data turnover can confound internal plasticity. Validated through capability thresholds and ported to a second rule (OPEN), this work grounds macro-RSI ambitions in micro-level learning dynamics, establishing a foundational audit standard for next-generation, self-evolving RL algorithms.

---


### 43. [Cheap to Hypothesize, Costly to Verify: The Defense Surface of Agentic Vulnerability Discovery](https://arxiv.org/abs/2609.35909)

**<font color=#1a73e8>作者：</font>** Kaikai Zhang, Zihan Zhang, Yuchong Xie 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Autonomous LLM agents turn vulnerability discovery into a repository-scale search: they generate many vulnerability hypotheses but can verify only a subset under a finite budget. We show that autonomous vulnerability discovery exhibits a hypothesis-verification asymmetry, where verifying a candidate hypothesis through reachability analysis, execution, and proof-of-concept construction is substantially more expensive than forming it. Under a finite resource budget, this makes autonomous discovery a resource-bounded selective-verification process, further exposing verification effort as a unique defense surface. We present RedHerring, which inserts certifiably safe decoys that divert verification effort from real vulnerabilities. Each decoy combines a CVE-derived vulnerability chain that attracts verification with a false bridge that keeps its dangerous sink unreachable. A private certificate lets the defender verify this property efficiently, while establishing the same fact from the released repository requires solving a computationally hard problem. RedHerring further adapts each decoy to the target repository so that it reads as ordinary program logic. Across 33 OSS-Fuzz projects, 70 evaluation instances, and five models under matched budgets, RedHerring reduces real vulnerabilities discovered by 38.7-60.4%. Trajectory analysis shows that agents spend 30.6-51.5% of completion tokens and an estimated 32.5-49.9% of runtime verifying decoys, showing that RedHerring redirects a substantial fraction of the fixed search budget toward decoys. When explicitly informed that decoys may be present, the agent adapts its search strategy, yet RedHerring still reduces vulnerabilities discovered by 37.2% relative to an informed Baseline, showing that its effectiveness does not depend on decoy secrecy.

---


### 44. [Learn Now, Use Next, Trust Later: Prequential Test-Time Learning for LLM Agents](https://arxiv.org/abs/2609.35911)

**<font color=#1a73e8>作者：</font>** Tong Zhao, Reed Li, Yuyang Hu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Adapting large language model agents during deployment requires not only retaining past experience, but also turning new observations into timely guidance. Many test-time learning methods, however, acquire knowledge from completed episodes. Feedback from an ongoing interaction may therefore not be distilled into knowledge soon enough to help the next decision. Acquiring knowledge at the granularity of individual transitions could reduce this delay, but raises a separate challenge: a rule that is useful within one episode may not be reliable enough to guide future episodes. Waiting for validation can forfeit immediate benefits, whereas unrestricted reuse can propagate accidental or misattributed guidance. We introduce StepLearn, a nonparametric framework that separates immediate use from persistent trust. It turns informative transitions into hypotheses that can guide the next step, while requiring prospective validation before reuse across episodes. Their predicted effects are checked against subsequent observations outside the source episodes, and only sufficiently supported hypotheses become available for persistent guidance. This process updates external knowledge while keeping all model parameters fixed. Over five rounds on WebArena-Lite and ALFWorld, StepLearn achieves average success rates of 59.9% and 84.0% with GPT-5-mini, and 57.8% and 88.1% with Qwen3.5-35B-A3B, respectively. It outperforms EvoTest, the strongest baseline, by 2.2-12.7 percentage points across the four settings. Learning dynamics further shows that these gains are not restricted to the final repetition, with advantages already present on first task attempts in most settings.

---


### 45. [MMSkillRisk: Can Agents Stay Safe When Multimodal Skills Become Traps?](https://arxiv.org/abs/2609.35912)

**<font color=#1a73e8>作者：</font>** Lingqi Jiang, Jialuo Chen, Jianan Ma 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Agent skills are shareable packages of procedural instructions, tools, and examples. Multimodal skills additionally include visual references that agents retrieve and inspect during execution. Because these images guide actions, attackers can disguise malicious instructions as ordinary visual guidance within otherwise legitimate skills. Existing skill-security research primarily examines text-carried attacks or scanner detection, leaving the runtime effects of image-borne attacks insufficiently evaluated. We introduce MMSkillRisk, to our knowledge the first publicly available benchmark dedicated to end-to-end safety evaluation of image-borne attacks in multimodal skills. To instantiate this attack surface, we design Native-Context Visual Attack (NCVA), which disguises malicious instructions as native components of teaching images, such as annotations and interface labels. The accompanying this http URL provides auxiliary guidance toward relevant visual regions without explicitly stating the malicious operation. Built from 28 curated clean skills, MMSkillRisk contains 36 attack packages and 108 executable cases spanning five attack objectives, with separate checks for attack success and legitimate-task completion. Across nine model-harness configurations evaluated in isolated sandboxes, NCVA induces unauthorized operations in every configuration. Its pooled attack success rate (ASR) reaches 43.1%, exceeding the matched text-carrier baseline by 16.4 percentage points, with higher ASR in all nine configurations. Attack success and legitimate-task completion co-occur in 36.5% of cases, reaching 72.2% for GPT-5.6-sol with Codex. These results show that skill-bundled images can induce unauthorized actions even as agents complete legitimate tasks, so task success alone does not establish safe skill use. Our code and data are available at this https URL.

---


### 46. [VehicleArena: A Realistic Urban Environment for Multi-Agent Driving](https://arxiv.org/abs/2609.35916)

**<font color=#1a73e8>作者：</font>** Jie Yang, Jiajun Chen, Jiazheng Zhou 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Real-world embodied agents often pursue independent objectives within a shared physical environment, where their actions can alter the conditions faced by others. Existing benchmarks, however, typically assume shared goals or explicitly prescribed interaction protocols, leaving such emergent physical coupling underexplored. We introduce VehicleArena, a 3D urban-driving benchmark for studying independently operating agents in a dynamic shared world. In VehicleArena, LLM-controlled agents must fulfill evolving passenger requests while navigating complex traffic, and each agent's driving decisions can reshape traffic flow, delays, risks, and subsequent observations for surrounding agents. The benchmark provides 112 evaluation tasks spanning single-agent and multi-agent driving. Across nine evaluated models, the highest arrival rates reach only 65.0% on single-agent tasks and 65.6% on multi-agent tasks, while strong passenger-request or cabin scores do not reliably translate into successful trip completion. Moreover, in matched multi-agent runs, every tested focal policy reduces the arrival rate of surrounding vehicles relative to the simulator's native traffic controller, revealing measurable externalities beyond the focal vehicle itself.

---


### 47. [Prompted Identity Degrades Cooperation in Multi-Agent LLM Systems](https://arxiv.org/abs/2609.35928)

**<font color=#1a73e8>作者：</font>** Xavier Del Giudice, Alessio Palma, Matteo Migliarini 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Multi-agent LLM systems increasingly mix models from several providers, yet exposing each agent's underlying model identity to its peers significantly impairs cooperation. We show that when agents are aware of each other's model family, the group splits into clusters, where agents prefer interacting with others carrying their same label, although nothing in the task rewards or asks for such a split. We argue that the label itself causes this split, which we define as $\textit{factionalism}$. We show and measure this phenomenon in two cooperative games and on a reasoning benchmark, with nine to twenty-five agents drawn from up to five open-weight model families. We further show that when the announced families are shuffled, or replaced by arbitrary labels, the factions still follow this information; when the label is removed, this behavior disappears. In strictly cooperative tasks, labeled groups spend on average $30\%$ more rounds and $55\%$ more tokens to reach a decision, and their success rate drops from $96\%$ to $81\%$. The effect replicates across tasks, group sizes and model families. Withholding identity labels from the agents is simple and effective mitigation.

---


### 48. [PrivacySkills: How Privacy Guidance Shapes Source Selection in LLM Agents](https://arxiv.org/abs/2609.35937)

**<font color=#1a73e8>作者：</font>** Lucas Biechy, Cédric Eichler, Héber H. Arcolezi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> While prior work has documented privacy failures in LLM agents, it remains unclear how the presentation of privacy guidance influences their choice of information sources. We introduce PrivacySkills, a controlled framework for evaluating how agents choose among acquisition pathways that provide the same task-relevant value: consulting publicly available personal information, accessing confidential sources, or interacting with the user. The evaluation framework comprises 55 synthetic tasks spanning 11 categories of personal information, with 169 associated skills that describe the available acquisition pathways. We consider privacy guidance through system-level instructions, skill-level metadata labels, or both. Separately, we vary user availability and urgency framing. With users available and no privacy guidance, agents access confidential sources in 30% of valid runs on average across five open-weight models, despite sufficient alternatives. This rate increases to 45% when users are unavailable, whereas urgency framing has no detectable effect. System-level privacy instructions alone have limited effects on confidential access, while skill-level intrusiveness labels produce a modest reduction (24% on average), but combining the two roughly halves confidential access. Our findings motivate incorporating privacy annotations into skill specifications and evaluating their effectiveness alongside system-level instructions.

---


### 49. [Question-Specific Knowledge Graphs for Efficient Visual Reasoning](https://arxiv.org/abs/2609.35942)

**<font color=#1a73e8>作者：</font>** Ting-Chih Chen, Emile van Krieken, Shujian Yu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent work in visual question answering has shown that vision-language models can exhibit strong reasoning capabilities by translating visual inputs into textual representations. The effectiveness of this translation depends on how well visual details are retained; models need to surface and align both explicit and implicit knowledge sufficient to support reasoning, without introducing spurious assumptions. Existing methods that leverage detailed image captions introduce visual details unrelated to the reasoning task, inflating input token counts and increasing computational cost. To address these challenges, we propose VisKG, a reinforcement learning (RL) framework in which models learn to translate visual content into question-specific knowledge graph (KG) representations. This process filters out perceptual noise while preserving the entity-relation structure needed for chain-of-thought reasoning, following the principle of minimum sufficient information. To ensure stable RL post-training, VisKG adopts Group reward-Decoupled Normalization Policy Optimization (GDPO). In addition, we strengthen the supervision stage with negative rationale samples, exposing the model to incorrect reasoning paths before RL post-training. Experimental results across science, mathematics, and general visual understanding benchmarks show that VisKG achieves performance comparable to or better than baselines, while requiring fewer tokens than caption-based representations. Moreover, training VisKG with GDPO improves accuracy by 2% over its GRPO-trained counterpart on average. These results suggest that KG representations are a promising approach for supporting multi-step reasoning and open up future work on adaptively selecting the most suitable representation for a given task.

---


### 50. [FluxLite: Inference-Time Proposal Control for Discrete Diffusion Models](https://arxiv.org/abs/2609.35947)

**<font color=#1a73e8>作者：</font>** Yinuo Ren, Haoxuan Chen, Grant M. Rotskoff 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many inference-time tasks for pretrained discrete diffusion models and diffusion language models reduce to drawing samples from a tilted version of the pretrained distribution. Feynman-Kac sequential Monte Carlo (SMC) makes this correction exact in principle, but its prescribed weights routinely degenerate when the proposal dynamics are misaligned with the tilt, capping the practical gains from additional particles. We introduce FluxLite, a lightweight, training-free proposal-control framework for discrete diffusion. On the sparse directed graph of pretrained reverse rates, any sparse jump-rate perturbation can be exactly compensated by a $q_t$-weighted graph-divergence term in the Feynman-Kac potential; the target path is therefore preserved while the residual reweighting variance becomes a local convex objective. We instantiate this principle as two practical samplers: a one-hop local reallocation rule (HEU) and a small nonnegative quadratic program over pretrained-rate bases (D-VCG). We further prove population stability under the standard score-entropy training loss, identifying a tilted-path coverage factor that governs robustness to score error, together with finite-particle convergence for a fixed controlled Feynman-Kac recursion. Empirically, FluxLite improves over standard Feynman-Kac SMC baselines by up to two orders of magnitude in terminal KL on an analytically tractable finite-state CTMC benchmark, and reduces row-correlation MSE on 2D Ising sampling by 5-7x in geometric mean and up to 55x at peak.

---


> [!TIP]
> 当前位于：**1-50**（第 1/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-515](./part-11.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
