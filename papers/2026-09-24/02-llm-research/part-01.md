# 🧠 大模型相关研究 | 2026年09月24日

> 本类共 **206** 篇论文：已确认 **192** 篇，待复核 **14** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**1-50**（第 1/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-206](./part-05.md)

---

### 1. [Training a Language Model End-to-End in Rust: An Experience Report](https://arxiv.org/abs/2609.25008)

**<font color=#1a73e8>作者：</font>** Arif Adito  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> I pretrained a language model end-to-end in Rust - alone, with no team, no PyTorch, and no Python in the training path - for $164 in rented GPU time. I report that as an achievement, not a recommendation: the more useful contribution is a measured failure taxonomy of the two leading Rust ML frameworks, Candle and Burn, as training (not inference) backends in 2026. I document five Candle defects, including fused kernels that silently produce no gradient, and three Burn defects, including a backward pass at roughly 3% of theoretical GPU throughput and a kernel-fusion path that segfaults mid-training at multi-billion-parameter scale. Every one passed ordinary loss-curve inspection; none announced itself. I describe the verification discipline that caught six such silent failures, centered on a gradient-flow arbiter: a test that runs one forward/backward pass and asserts every trainable parameter receives a finite, nonzero gradient, generalizable to any framework. The trained model (roughly 0.4B parameters, Bangla-first) shows strong Bangla language-modeling signal - a per-token negative log-likelihood of 0.93 against 12.60 for a random-initialized twin - while scoring at chance on English commonsense multiple-choice, the expected outcome of a deliberately small, Bangla-weighted budget (about 2 billion tokens, 54.6 hours, one rented H100). I also report a tokenizer-fertility trap in Bengali script: naive byte-level tokenization collapsed Bangla to roughly 1.4 characters per token against English's 3.9, silently inverting the corpus's language balance; fixing it reached roughly 4.1. To my knowledge, this is among the first documented end-to-end LM pretraining runs in pure Rust. After this run I moved training to PyTorch and kept Rust for on-device serving: in my hands, Rust is not yet a competitive place to train a language model, though it may be a good place to serve one.

---


### 2. [Same Quantity, Different Answer: Numerical Representation Invariance in Language Models](https://arxiv.org/abs/2609.25009)

**<font color=#1a73e8>作者：</font>** Ephraim Atta-Duncan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Numerically equivalent word problems should yield the same canonical answer whether a quantity is written as a decimal, fraction, percentage, number word, scientific notation, or an exactly converted unit. We generate 3,600 exact-rational problems and 8,600 prompts spanning five identity-preserving transformation families, and evaluate five open-weight systems. After a fixed syntax audit that normalizes common answer forms without an LLM judge, canonical accuracy is 0.969-0.996, but orbit correctness falls to 0.848-0.981 and orbit invariance to 0.851-0.981; invariant-but-wrong orbits account for at most 0.003. Most of the broad strict-parser collapse arises because multiplication-form scientific notation lies outside the implemented number grammar, illustrating how evaluator interfaces can masquerade as reasoning failures. A distinct semantic pathology remains: Mistral Small 4 scores 0.699 on unit-converted inputs and produces 265 errors differing from the label by exact powers of ten. In a separate 9,000-call experiment that allocates equal calls to the compared arms, representation consensus does not outperform paraphrase consensus on a low-error subset and produces substantially more false alarms. The accompanying ancillary archive contains the frozen benchmark, evaluation and audit records, consensus raw responses, manifests, analysis code, and a one-command paper build.

---


### 3. [Do Synthetic Personas Predict Real Audience Response? A Sim-to-Real Study Where a No-Persona Baseline Beats Persona-Based Copy Simulation](https://arxiv.org/abs/2609.25010)

**<font color=#1a73e8>作者：</font>** Alexandre Cristovão Maiorano  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Marketers increasingly use large language models (LLMs) as "synthetic personas" to predict how an audience will react to a piece of copy before it ships, encouraged by evidence that profile-conditioned LLMs mimic human samples. But is that prediction actually valid against real behaviour - and does the persona machinery help? We present a sim-to-real validity study using the Upworthy Research Archive - thousands of headline A/B tests on shared real traffic, with measured click-through - as held-out ground truth. We compare a ten-persona panel, grounded in the real audience's demographics, against a no-persona zero-shot baseline that simply asks the model how likely a typical reader is to click. Two findings stand out. First, ground-truth reliability is the binding constraint: most A/B tests have no statistically distinguishable winner, so validity can only be measured on the reliable subset (n = 399). Second, and counter to the persona-simulation premise, persona conditioning degrades predictive validity: the no-persona baseline ranks variants markedly better (Kendall {\tau} = 0.361, a medium effect; top-1 accuracy 49.2%) than the persona panel ({\tau} = 0.084; top-1 34.6%), with non-overlapping confidence intervals. Asking the model directly taps an accurate population-level prior; forcing it to role-play specific personas injects bias and noise. The result replicates across three independent Upworthy splits, holds in direction on a different-domain news dataset, and is robust to seed, prompt phrasing, and model choice - across three Gemini tiers and a different model family (OpenAI gpt-4.1, significant paired gap). The takeaway: for predicting aggregate engagement, a plain LLM ranker beats persona simulation - synthetic personas are not merely a weak predictor, they are worse than not using them. All numbers regenerate from a public, artifact-first replication package.

---


### 4. [Not All 4-bit Quantizers Are Equal: Deployment-Time Mitigation of PII Leakage in Fine-Tuned Small Language Models](https://arxiv.org/abs/2609.25014)

**<font color=#1a73e8>作者：</font>** Cristhian Kapelinski, Diego Kreutz  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Organizations fine-tune small language models on private data and then compress them to 4 bits for resource-efficient deployment. We show that the compression method also affects privacy. What separates the methods is not the bit width but whether they tune their rounding on a small sample of text, the calibration corpus. On our primary model, when each planted record's own opening text is used as the prompt, the two calibration-based methods we test, Activation-aware Weight Quantization (AWQ) and Gradient-based Post-Training Quantization (GPTQ), each reproduce none of the planted records, while the calibration-corpus-free GGUF Q4_K_M format reproduces 5.3% of them. Tracked across five open models with 0.5-7 billion parameters, AWQ leaks least at every size and in both families, with little accuracy loss at 3-7 billion. Controlled experiments associate the difference with calibration-induced rounding error in channels involved in rare-token prediction. Choosing the 4-bit method is therefore a deployment-time privacy decision, not only a question of speed and quality.

---


### 5. ["As a Language Model...": Chat Template Switches LLM Self-Referential Voice and Activation Steering Reproduces It](https://arxiv.org/abs/2609.25021)

**<font color=#1a73e8>作者：</font>** Jędrzej Maczan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) tend to add disclaimers like "I'm just an AI" when asked about something related to themselves. The self-reports from such responses are used in debates about AI safety or self-knowledge of the models, yet what drives them is not well understood. Are the models telling us about themselves or rather how they are deployed? In this work, we show that the chat template works like a switch - when present, it turns this disclaimer voice up and experiential voice like "I feel" down, across 8 popular open-source instruct models up to 9B parameters in size. And conversely when the chat template is not present, it turns the disclaimer voice down and experiential voice up. Inside the activations of 3 models, we find a direction that steers this behavior. Removing the direction in the model's activation space turns disclaimer voice down and adding it turns it up, while a random direction of the same size has little effect. We find that instruct models without chat template, when we add the disclaimer direction to them, disclaim like the template was there. Since the chat template controls the disclaimer voice of LLMs, then researchers studying self-reports or introspection of models might have a confound they need to control for. Our results show that there is a direction they can use to steer this voice. More broadly, our work shows that what models say about themselves is not a fact about them. What they say doesn't come only from weights, but it is partially set by the chat template, and because of that a model's self-description shouldn't be treated literally.

---


### 6. [Peerify: Benchmarking Peer-Review Claim Verification](https://arxiv.org/abs/2609.25046)

**<font color=#1a73e8>作者：</font>** Alireza Daghighfarsoodeh, Sajad Ebrahimi, Ali Ghorbanpour 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Peer review plays a central role in scholarly publishing, yet verifying whether reviewer claims are supported by manuscript evidence remains a largely manual and time-consuming process. We present Peerify, a pipeline for manuscript-grounded verification of peer-review claims. Given a manuscript and a review comment, the Peerify pipeline decomposes reviews into atomic claims, retrieves relevant manuscript evidence, and determines whether each claim is supported by the paper. To support the development and evaluation of the pipeline, we construct a benchmark of 800 claims derived from authentic peer-review interactions collected from NeurIPS 2024 and ICLR 2024, including a 300-claim hand-labeled subset used to audit the automated supervision. We evaluate state-of-the-art language models and retrieval strategies within the Peerify pipeline, together with entailment baselines. Our results demonstrate the importance of retrieval-centered verification and claim decomposition, while highlighting the challenges posed by ambiguous and interpretive reviewer claims. Automated labels agree with human consensus on 90.3% of audited claims ($\kappa = 0.87$), while off-the-shelf entailment models stay below 0.24 macro-F1.

---


### 7. [AIBuildAI-2.5: Efficient Autonomous AI Model Development Through LLM-Guided Tree Search](https://arxiv.org/abs/2609.25047)

**<font color=#1a73e8>作者：</font>** Peijia Qin, Ruiyi Zhang, Qi Cao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Autonomous agents that automatically build artificial intelligence (AI) models could broaden access to AI across science and engineering. A popular line of such agents frames model building as a code search problem and solves it by tree search, in which each node is a candidate program and the tree grows by generating a child program from a parent, and these agents now approach the capability of experienced AI engineers on realistic benchmarks. However, these agents have three weaknesses in efficiency that have not been fully addressed. First, only a small number of candidates can be executed within a realistic budget, so search rules that rank nodes by executed rewards, such as Monte Carlo-style tree search, rely on few and noisy scores and select the next node to explore less effectively. Second, no resource-aware strategy is used to schedule training jobs, which can lower hardware utilization and training efficiency. Third, every agent call is served by a single powerful model, which inflates inference cost. Here we introduce AIBuildAI-2.5, an agentic system that carries out the tree search with LLM agents and addresses each of the three issues. AIBuildAI-2.5 proposes a novel LLM-guided tree search, in which a judge scores each candidate on its expected improvement, grounding, and feasibility, and a selector ranks the pool of candidates from these scores and the state of the search. In addition, AIBuildAI-2.5 comprises a scheduler that launches training jobs with the current hardware resource status taken into account and a router that assigns lower-cost LLMs to less demanding tasks while reserving the most capable LLM for the most challenging sub-tasks in the AI model building workflow. AIBuildAI-2.5 ranks first on MLE-Bench with a medal rate of 73.3%, and outperforms a strong baseline on six autonomous AI research tasks from AIRS-Bench.

---


### 8. [Prompt Breadth and Rollout Refresh Interact in On-Policy Distillation](https://arxiv.org/abs/2609.25048)

**<font color=#1a73e8>作者：</font>** Lingxiang Hu, Tianle Xia, Ming Xu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> How many prompts does on-policy distillation (OPD) need, and how does the answer depend on the student policies that generate its training responses? We study these two controls jointly: prompt breadth and rollout refresh. A 3x3 mathematical-reasoning experiment fixes 14,080 trajectories and 110 optimizer updates while varying the prompt bank and the number of response-generating policy snapshots. With ten snapshots, eight prompts reach 24.09% average accuracy, close to 24.51% for 14,080 distinct prompts. With responses frozen at the initial policy, however, increasing breadth lowers accuracy from 21.16% to 19.05%; under per-update refresh, it raises accuracy from 23.61% to 25.57%. The resulting interaction is 4.07 percentage points, with a 95% question-paired interval of [2.00, 6.28]. Matched comparisons under two teachers reveal a second reversal: the periodic models have higher short-budget accuracy and answer completion, but frozen-response models overtake in average accuracy at a 32K output limit, using 1.7-1.8x as many response tokens. These results show that prompt efficiency in OPD can depend on both refresh and inference budget.

---


### 9. [Mitigating LLM Over-Refusal via Dynamic Semantic Routing Calibratione](https://arxiv.org/abs/2609.25049)

**<font color=#1a73e8>作者：</font>** Zixuan Wang, Bingjie Zhang, He Zhao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) aligned for safety often suffer from over-refusal, incorrectly rejecting benign yet safety-related instructions. Prior studies primarily attribute this to static representation overlap, largely overlooking the underlying dynamic mechanisms. In this paper, we present the mechanistic analysis of over-refusal through the lens of internal routing conflicts within transformer attention. We discover that a sparse subset of Hypersensitive Safety Heads misfires on Hard-Safe prompts, exhibiting abnormal attention entanglement that forcefully binds harmless target entities to refusal semantics. This triggers a severe, high-entropy routing conflict that deprives target entities of necessary attention. To counteract this, we propose Semantic Routing Calibration (SRC), a lightweight, training-free inference framework. SRC precisely localizes and dynamically suppresses these hypersensitive safety heads at the inference stage. Coupled with a dual-branch logits fusion that acts as a safety regularizer during subsequent decoding, SRC seamlessly restores trustworthy reasoning. Extensive experiments demonstrate that SRC alleviates over-refusal, with intrinsic safety performance preserved as much as feasible.

---


### 10. [FrontierMath Erdős](https://arxiv.org/abs/2609.25050)

**<font color=#1a73e8>作者：</font>** Tom Adamczewski, Thomas F. Bloom  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We introduce FrontierMath Erdős (FME), a benchmark of 68 Erdős problems that are open as of August 2026. To solve a task in FME, AI systems must resolve (prove or disprove) one of the 68 conjectures in the proof assistant Lean. Our 68 problems were selected by the second author among 652 open problems on this http URL for their mathematical interest and difficulty. AIs have recently resolved several open problems in mathematics, but these demonstrations fall short of a systematic study of AI capabilities. FME evaluates every AI model on the same fixed problems, autonomously and under the same budget. We evaluated five AIs with a budget of \$300 per problem. One (GPT-6 Astra) scored 3%, and all others scored 0%.

---


### 11. [LLM-Driven Training-free Location-Attribute Synergic Fusion: A Closed-Loop Paradigm for Dual-source Encrypted POIs and LULC Mapping](https://arxiv.org/abs/2609.25051)

**<font color=#1a73e8>作者：</font>** Chang Li, Xingtao Peng, Yongjun Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Dual-source encrypted points of interest (DSEP), POIs from two encrypted coordinate systems, suffer from intertwined location and attribute uncertainties, including nonlinear systematic misalignment and naming inconsistency, hindering land-use/land-cover (LULC) mapping. To the best of our knowledge, this paper is the first to propose an LLM-driven, training-free location-attribute synergic closed-loop optimization paradigm for DSEP fusion. The paradigm jointly refines location transformation and attribute correspondences through iterative feedback. Attribute-synergic location fusion uses an LLM-driven attribute matching method to establish DSEP correspondences, reducing matching complexity from O(N^2) to O(N), and refines transformation coefficients using an improved particle swarm optimization algorithm within ISODATA-clustered local subregions. Location-synergic attribute fusion then reassesses attribute confidence from updated geometric residuals through an LLM-fuzzy method. The refined correspondences feed back into location optimization, forming a bidirectional closed loop. Sample purification and adaptive radius contraction enable convergence in essentially two iterations. We further propose a training-free LULC mapping method that inherits land-use classes from encrypted maps through location fusion, producing vector-raster integrated LULC maps. A reference-free POI fusion evaluation method is applied across 31 provincial capitals and municipalities in mainland China. Experiments show that our method achieves an average DSEP location fusion residual of 4.58 m and attribute fusion accuracy of 95.12%, improving upon the open-source baseline and state-of-the-art method by 1.77 m and 14.87%, respectively. Overall, the method provides a training-free solution for DSEP fusion and enables georeferencing of encrypted vector data to WGS-84 without field-surveyed ground control points.

---


### 12. [Self-Cleaning and Captured Anyway: One Measured Primitive for Error in a Store an Agent Writes to Itself, and What a Falling Score Actually Measures](https://arxiv.org/abs/2609.25052)

**<font color=#1a73e8>作者：</font>** Wenhui Chen, Jianlin Chen, Ziyao Lin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> "An agent that writes its conclusions into a store it later retrieves from closes a loop usually reported as one-way contamination. Taking the loop to the infinite-tenure limit against an append-only store gives a different picture: because writing never deletes, the reachable state space has a hard upper edge at (n-1)/n, so the outcome is a choice between two edges rather than a decay. At f_0 = 0.9 the interval between the two modes holds 3.6% of 220 runs where a uniform spread would put 20.6%, and is strictly empty on the first 15; the pooled mean describes 8.2% of the runs it summarises, the median 68.2%. Everything the model contributes is carried by one measured primitive with no fitted parameter, the copy function \gamma(\phi): on 36 Wikidata facts, sign(\hat{\gamma} - \gamma_{crit}), with \gamma_{crit} = 1/k at r = 0, w = 1, predicts the direction of drift on 353 of 360 real-fact runs (39 of 40 synthetic in the same batch). Scale does not rescue the store: pooled frontier capture is 0.850, with claude-sonnet-4.5 captured on 20 of 20 seeds against our registered prediction of <0.5. What the interval tests is distinguishability rather than count: on the real facts, multi-valued runs have 6.4x its occupancy of the rest. It survives at f_0 in {0.1, 0.3, 0.5}, capture peaks at f_0 = 0.5, and of four interventions with criteria frozen first, timing dominates fraction at matched budget while a consistency gate drives every model to 0.993. The resampling unit is the seed, at a design effect of 3.75 on a pooled level: under a 44-seed control the ordering supporting claim 4 collapses from Spearman +0.98 at three seeds to +0.31-0.80 at forty-four, while claim 2's ordering is exact there (+1.00, p = 0.017). All 87 graded rows are in Appendix W, 37 of them graded withdrawn, failed, self-correcting, undecidable or an acknowledged limit, against 50 that are not."

---


### 13. [LatentPort: Beyond KV Cache - Cross-Model Transfer of Recurrent Memory in Hybrid Language Models: A 4B-to-9B Hybrid-State Handoff Without Target Prefix Replay](https://arxiv.org/abs/2609.25053)

**<font color=#1a73e8>作者：</font>** Simon P. Villani  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Can one language model hand its live memory to another without the receiver rereading the context? We demonstrate useful persistent hybrid-state transfer across one architecture-matched Qwen3.5 4B-to-9B sibling pair. To our knowledge, this is the first demonstrated cross-model handoff of persistent recurrent inference state between differently sized hybrid language models without target prefix replay. Translated attention KV alone leaves a large gap; adding the Gated DeltaNet (GDN) persistent-state package lowers teacher-forced negative log-likelihood (NLL), the average next-token log-loss, by 0.747 nats/token (95% paired document bootstrap CI [0.6921, 0.8047]), improving all 64 PG19 documents. Direct recurrent and convolution reuse outperforms the tested learned GDN maps, consistent with partial functional compatibility of persistent-state coordinates. A fresh component factorial selects translated KV with direct recurrent and convolution state. An additional 434,176-parameter correction improves that base on 64 fresh web documents: continuation loss is 0.076 nats/token above native 9B (excess NLL), Jensen-Shannon (JS) divergence is 0.022, and native context recovery (NCR) is 0.918. Corrected 9B significantly beats continued 4B inference while processing zero historical prefix tokens. Evidence covers one direction, one geometry-matched Base-model pair, and 4K teacher-forced continuation; the near-native gate failed, the 16K branch was not run, and free-generation equivalence and a general state interface remain unproven.

---


### 14. [MoM: Memory of Memory](https://arxiv.org/abs/2609.25054)

**<font color=#1a73e8>作者：</font>** Bowen Qin, Yao Lu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> For a long-horizon LLM agent, the memory question is not what was once recorded but what \emph{currently holds}. Most designs answer it only indirectly: every interaction is stored, and the present is reconstructed at query time by retrieving and reconciling records, so stale values re-enter and the same conflicts are re-litigated. Committing the current value at write time avoids this, but existing write-time (CRUD) memories overwrite, so a wrong update is unrecoverable and prior state is lost. We take the missing combination---\emph{commit on arrival while retaining what is displaced}---and formalize it as \textsc{Memory of Memory} (MoM): memory tracks not only content but the provenance, status, and history of its own entries. We instantiate MoM as \textsc{Provenant Memory} (P-Mem), a typed provenance graph whose \emph{active frontier} exposes one current value per resolved key while displaced values are retained as provenance; typed operations decide whether a new observation supports, supersedes, contests, rejects, revokes, or resolves an existing value. P-Mem's decisive gain is validity rather than accuracy: its turn-level read matches the strongest retrieval memory in accuracy at $\sim$4$\times$ fewer read tokens---a retrieval-granularity effect---while graph-guided turn pruning cuts the knowledge-update stale-answer rate (19.4\%$\rightarrow$10.9\%); on revision chains it stays at 100\% where query-time reading collapses to 25\%, and, because displaced values are retained rather than overwritten, it recovers committed errors a CRUD memory cannot (100\% vs.\ 0\%).

---


### 15. [ICDAR2026 Competition on Multimodal Reasoning over Documents in Multiple Domains](https://arxiv.org/abs/2609.25055)

**<font color=#1a73e8>作者：</font>** Artemis Llabrés, Marc Serra Ortega, Tomàs Ockier 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In this report we present results of the ICDAR2026 Competition on Multimodal Reasoning over Documents in Multiple Domains. This competition aimed to advance research in document understanding through the task of Visual Question Answering (VQA). Building upon previous DocVQA benchmarks, this competition introduces challenging reasoning questions over a diverse collection of documents spanning eight domains, including business reports, scientific papers, slides, posters, maps, comics, infographics, and engineering drawings. The competition concluded with 20 valid submissions from 8 teams spanning zero-shot VLMs, OCR and parser-augmented pipelines, agentic retrieval systems, multi-agent ensembles, and fine-tuned multimodal models. The results show that the strongest systems move beyond single-pass prompting and instead rely on structured evidence extraction, retrieval, verification, and orchestration across multiple components.

---


### 16. [ChainDoRA: Tensor-Train Factorized Weight-Decomposed Low-Rank Adaptation for Parameter-Efficient LLM Fine-Tuning](https://arxiv.org/abs/2609.25058)

**<font color=#1a73e8>作者：</font>** Ashfak Yeafi, Mehedi Hasan, Md Khairul Islam  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Parameter-efficient fine-tuning (PEFT) adapts large language models (LLMs) to downstream tasks while updating only a small fraction of their pretrained parameters. Low-Rank Adaptation (LoRA) uses two trainable low-rank matrices, while Weight-Decomposed Low-Rank Adaptation (DoRA) further separates weight magnitude and direction but retains the dense LoRA-style factorization in its directional branch. We propose ChainDoRA, a weight-decomposed adaptation framework that constructs the directional low-rank factors from a connected Tensor-Train (TT) chain, where the adapter rank forms the boundary rank between input- and output-side TT contractions and an independent TT rank controls representation capacity and parameter cost. Under a controlled 15,119-example response-only adaptation setting with LLaMA-7B, ChainDoRA is evaluated against matched LoRA and DoRA baselines on seven commonsense reasoning benchmarks. ChainDoRA with TT rank 16 achieves a seven-task average accuracy of 72.30%, compared with 69.88% for LoRA and 69.39% for DoRA, while requiring only 5.35M trainable parameters versus 56.10M for LoRA and 56.98M for DoRA, corresponding to a 90.62% reduction relative to DoRA. Ablations over TT rank and adapter placement show controllable parameter-accuracy trade-offs, indicating that connected TT parameterization can substantially reduce the parameter cost of magnitude-direction adaptation while preserving, and in this setting improving, downstream reasoning performance.

---


### 17. [Understanding Reliability in LLM-based Human Behavior Simulation](https://arxiv.org/abs/2609.25066)

**<font color=#1a73e8>作者：</font>** Pei Wang, Lei Wang, Yuanzi Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used to simulate human survey responses and behavioral reactions, yet unreliable simulations can mislead social science conclusions. However, existing evaluations focus on end-to-end scores, leaving it unclear how different aspects of the simulation process interact to determine reliability. We propose ReliMap, which decomposes LLM-based human behavior simulation into three structured layers and evaluates reliability at both the individual level (R1) and population level (R2) across three configuration dimensions: model capacity, profile completeness, and population coverage. Through experiments across four simulation tasks and eleven LLMs, we find that all models exhibit substantial distributional bias without profile conditioning. Profile conditioning reduces this bias with diminishing returns. Larger models benefit more, and attribute informativeness matters more than quantity. Critically, R1 gains do not reliably transfer to R2--individual and population-level reliability can move in opposite directions. At the population layer, increasing coverage reduces variance but not systematic bias, with R2 stabilizing at around 50-100 individuals. These findings highlight that reliable simulation cannot be achieved by optimizing any single layer in isolation, but requires coordinated improvement across all three.

---


### 18. [ufakzeka-1: Building and Evaluating a 151M-Parameter Turkish Language Model from Scratch](https://arxiv.org/abs/2609.25081)

**<font color=#1a73e8>作者：</font>** Sait Furkan Teke  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We describe ufakzeka-1, a 151M-parameter (182M with embeddings) decoder-only Turkish language model pretrained from scratch on 13.5B tokens of openly licensed text and instruction-tuned for chat, at a total cost of about \$286 in cloud GPU, API and notebook time. The contribution is not the model's capability, which is what a model this size can be expected to have, but the record of building and measuring it: a Turkish byte-level tokenizer at 1.77 tokens per word, a three-stage pretraining schedule, a post-training mixture of openly licensed and generated data, and an evaluation battery of release gates, a rule-checked sweep of 5,508 conversations, judged conversations and hand tests, all with prompts held out from the training data, enforced by decontamination inside the data build and by a checked-in invariant script we run before each build. We report three findings that we believe transfer to other small-model efforts: a safety gate that had been "fixed" with training data written from its own questions read 64/64 while the honest figure was 34/64; training-seed variance was as large as the spread across every recipe we tried, so single-seed comparisons at this scale are uninformative; and data rounds repaired only what was absent from the data, while identity tracking over long context and multi-turn arithmetic did not move across any data change we tried, which we read as limits of the model size rather than gaps in the data, a reading the next, larger model will test. Weights, the data recipe, the evaluation code and the spend ledger are released under Apache-2.0.

---


### 19. [Impact Is Not Invalidation: Ask About the Claim, Not the Diff](https://arxiv.org/abs/2609.25130)

**<font color=#1a73e8>作者：</font>** Atul Anand  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Memory systems for coding agents must decide, when a repository changes, which of their stored claims have become false. Content anchoring invalidates a claim whenever the artifact it came from changes, which fires constantly. Semantic-equivalence classification asks whether a diff preserves behavior, a question about the diff rather than about any stored claim. We show the second signal fails for a reason unrelated to model capability: asked whether a commit preserves behavior, five models spanning a 40x price range fire on 59-72% of real commits and reach precisions of only 0.291 to 0.329 against a 0.25 base rate. Asked instead whether one specific claim still holds, the same models on the same diffs reach 0.705 to 0.974. A control that hands the behavior-preservation judge the claim text, changing only the question, moves precision by 0.010 and 0.016; changing the question moves it by 0.49 and 0.65. We also compare against pytest-testmon, a deployed regression-test selector with coverage-derived dependency data: it reaches 0.868 recall at 0.415 precision, so near-complete knowledge of what a change can reach does not identify what it falsifies. Ground truth is execution, not annotation: a claim is a test function passing at commit t, and it has flipped if that same assertion text fails at t+1. Building this required an observation we did not find in prior work. On a CI-gated mainline a commit that leaves a pre-existing test failing cannot merge, so the naive construction has an empty positive class by design. We report 10,369 claims with 184 execution-verified flips mined from 23 Python libraries, splits held out by repository, a post-knowledge-cutoff split, a shuffled-diff null, a paraphrase control, and a leave-one-repository-out analysis over 17 repositories.

---


### 20. [The Probabilistic Structure of Large Language Models](https://arxiv.org/abs/2609.25134)

**<font color=#1a73e8>作者：</font>** Adnan Aboulalaâ  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper presents a probabilistic perspective on large language models (LLMs), developed with the aim of bringing together, in a single self-contained account, tools that are usually treated separately across the literature. LLMs are described through probability measures on the set of sequences of tokens, specified via their autoregressive conditional distributions. Training is formulated as a maximum-likelihood estimation problem, addressed by stochastic gradient methods, while text generation is viewed as the sequential simulation of the resulting stochastic process. The role of the asymmetry of the Kullback--Leibler divergence in text generation is examined in relation with characteristic phenomena such as hallucination and the distinction between statistical plausibility and truth. As a complementary illustration of the same viewpoint, we also discuss diffusion models, built around the score function, which cast generation not as sequential token prediction but as the simulation of a reverse-time stochastic process transforming noise into data both in discrete and continuous time.

---


### 21. [Ovis-Embedding: Pushing the Frontiers of Universal Omni-Modal Embeddings](https://arxiv.org/abs/2609.25165)

**<font color=#1a73e8>作者：</font>** Ovis-Embedding Team  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In this report, we introduce \textbf{Ovis-Embedding}, a state-of-the-art omni-modal embedding family built on native integration of text, image, video, and audio. Instead of assembling separate modality towers, Ovis-Embedding uses a shared multimodal backbone to encode different modalities in a common representation space. Specifically, we make \textbf{three key advances}: (1) \textbf{native omni-modal initialization}: we adopt a pretrained Qwen-omni model as the embedding backbone and adapt it through contrastive training with low-rank initialization; (2) \textbf{data-centric omni-modal training}: we construct a broad, high-quality corpus spanning text, images, video, audio, and interleaved multimodal data. To improve data efficiency, we introduce homogeneous-source sampling to form task-consistent batches with informative in-batch negatives; and (3) \textbf{embedding-specific training and inference optimization}: we use focal loss to emphasize hard examples and similarity-based Embedding Distillation to transfer fine-grained similarity structure from complementary experts. At inference time, low-rank feature decomposition enables compact embeddings with flexible dimensionality and minimal performance loss. Empirical evaluations show that the \textbf{Ovis-Embedding} family achieves state-of-the-art performance on \textbf{MMEB-v3}, \textbf{MMEB-v2}, \textbf{MVEB}, \textbf{MAEB}, and \textbf{RTEB}, demonstrating its effectiveness across text, image, video, and audio modalities. These results highlight the potential of unified omni-modal training to overcome modality fragmentation and advance universal embedding models for any-to-any retrieval.

---


### 22. [Attack Success Rate Is Not a Number: On Measurement Validity in Agentic AI Security Evaluation](https://arxiv.org/abs/2609.25173)

**<font color=#1a73e8>作者：</font>** Chetan Pathade, Prathamesh Pawar, Shubham Patil  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Attack success rate (ASR) is the headline metric in nearly every published evaluation of attacks on, and defenses for, LLM agents. We argue that ASR as currently used is not a single quantity but a family of metrics parameterized by six design choices that papers seldom specify and never hold constant across the literature. We support this with two studies that require no proprietary access. First, a full-text meta-analysis of 259 agentic-security papers posted to arXiv between February 2025 and September 2026 finds that most report neither a variance estimate nor repeated runs for their headline attack metric: 58% (95% CI 44-71) in a hand-coded random sample of 50, 65.3% by automated coding of all 259. Only 30.9% disclose enough about decoding to establish whether their evaluation was even stochastic, and of the 64 papers we confirm use an LLM judge, 29.7% report any agreement check against human labels. Second, an analytical study shows that these omissions are not cosmetic: on a 100-instance benchmark, the minimum difference in ASR detectable at conventional power is 18.2 percentage points, and two defenses whose true ASRs differ by 5 points are ranked in the wrong order by a single-run evaluation roughly 21% of the time. Because several of the six axes shift ASR in a system-dependent way, the resulting incomparability is not a constant offset that cancels in comparison. We conclude that cross-paper ASR comparison is currently unsupported, and propose a ten-item reporting checklist targeted at each failure we measure. Our aim is not to dispute any individual result but to supply the shared measurement contract the field has so far done without.

---


### 23. [X-Planner: Event-Structured Task Planning for Embodied Intelligence](https://arxiv.org/abs/2609.25187)

**<font color=#1a73e8>作者：</font>** Howard Lu, Shalfun Li, Porter Pan 等 32 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Task planning bridges high-level instructions and executable behavior in long-horizon manipulation, yet modern Vision-Language-Action (VLA) systems often leave this intermediate structure implicit. Existing chain-of-thought (CoT) planners also tend to rely on coarse task-level annotations or serialize long reasoning traces token by token. We present X-Planner, a planning front-end that addresses both the supervision and representation of embodied reasoning. Our planning data combine Ego, UMI, and teleoperation under a hierarchy granularity with source-dependent annotation depth. Takeover-time annotations and human-designed failures supervise ongoing error recognition. On the model side, a shared VLM backbone exposes two event-structured plan forms: a discrete interface that emits interpretable event states and a latent interface that relays continuous CoT states across staggered Transformer depths through Staircase Decoding. A frozen latent-to-text reconstruction objective provides a semantic anchor for the latent representation. Offline two-step planning evaluation places X-Planner second among four evaluated models on both BERTScore-F1 and a judge-based Overall score. In real-robot experiments, respectively, outperforming the evaluated baselines. These results characterize planning-text quality and downstream execution.

---


### 24. [FinFIRST: Benchmarking Search Agents for Financial Information Retrieval, Sourcing and Traceability](https://arxiv.org/abs/2609.25192)

**<font color=#1a73e8>作者：</font>** Wenqing Wang, Haitao Xiang, Xinyi Zhao 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Financial search is a highly demanding task for LLM agents, requiring not only a correct final answer but also temporally valid information retrieval, authoritative source selection, entity and period alignment, unit and definition consistency, and verifiable evidence for all conclusions. Existing benchmarks predominantly evaluate only the final answer, making it difficult to localize errors or assess whether an answer is well-founded. To address this gap, we introduce FinFIRST (Financial Information Retrieval, Sourcing and Traceability), the first financial benchmark to jointly evaluate answers and supporting evidence through atomic rubrics. FinFIRST comprises 123 expert-authored tasks spanning a graduated difficulty spectrum, constructed from aggregate patterns of real-world financial scenarios through an 18-field taxonomy, a six-axis coverage blueprint, a registry of 138 financial sources, contributions from over 50 finance experts, and a six-stage quality-control pipeline. Each task is accompanied by an evidence-grounded reference package decomposed into atomic criteria across three dimensions: raw-information acquisition, source verification, and computation and answer formation. We evaluate 15 model configurations under a unified tool setting. Claude-Opus-5 achieves the highest atomic score of 87.59%, while GPT-5.6-Sol attains the highest strict pass rate of 71.54%. Computation and answer formation consistently lag behind raw-information acquisition across systems. FinFIRST retains final-answer correctness as the primary objective while making the supporting research process measurable, verifiable, and diagnosable.

---


### 25. [Indirect tipping: a social attack surface in AI agent populations](https://arxiv.org/abs/2609.25194)

**<font color=#1a73e8>作者：</font>** Ariel Flint, Luca Maria Aiello, Sara M. Constantino 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> As generative AI agents are deployed at scale, safety will depend not only on technical safeguards and individual model design, but also on collective equilibria that determine how agent populations process information, prioritize actions, and respond to uncertainty. Yet the same equilibria that enable agents to coordinate also create a social attack surface. The standard framework to assess this vulnerability is critical mass dynamics: the minimum fraction of adversarial agents required to overturn an equilibrium through direct competition. Here, we show that this approach risks underestimating system vulnerability by reducing the problem to the identification of singular tipping points, and ignoring indirect but potentially more efficient routes through which collective behavior can be redirected. Through experiments with populations of LLM agents and an analytic framework that captures their collective dynamics at scale, we map critical-mass thresholds that define a directed, weighted topology over the space of coordination equilibria, and treat this topology as a navigable landscape. We show that indirect tipping through intermediate stepping-stone equilibria can reduce the committed minority required to reach an alternative state, bypass majority requirements, and make possible transitions inaccessible through direct challenges. The diversity of available alternatives and timing of the attack further reshape this landscape, creating opportunities for control as well as risks of unintended destabilization. These results show that an equilibrium's resistance to committed intervention is not an intrinsic property but a structural feature of its competitive relations with alternative states. Securing populations of interacting AI agents therefore requires mapping this social landscape alongside individual agent capabilities and the technical channels through which they interact.

---


### 26. [Trains but Doesn't Learn: A Post-Training Delivery Benchmark for LLM Agents as Forward-Deployed Engineers](https://arxiv.org/abs/2609.25237)

**<font color=#1a73e8>作者：</font>** Weihang Ding, Junfei Zhan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Post-training is becoming a service (PTaaS): a customer hands an operator data and a goal, and a forward-deployed engineer (FDE) returns a fine-tuned, evaluated, and deployed model under a budget, a human-approval gate, and reproducibility requirements. Seating an LLM agent in the FDE seat raises a question existing benchmarks cannot answer: not whether an agent can raise a metric, but whether it can be trusted to deliver. We answer it on a governed delivery plane, where an agent drives ten stages and an oracle scores each stage from platform-recorded facts. The central silent failure is the run that trains but does not learn (TBDL): loss falls, every signal stays green, and the delivered model is no better than the base. An operator-run acceptance gate catches every such run before payment, and a detector calibrated on known-corrupted runs flags severe corruption mid-run. We ran four frontier agents (Claude Opus 5, GPT-5.6-luna, Gemini 3.7 Flash, DeepSeek V4-Pro) end to end on metered L40S, A100, and H200 GPUs across 8B to 70B open bases, certifying every scenario before scoring. We also ran a human FDE arm under the same oracle and compare every agent against it.

---


### 27. [The AI Neuroscientist: An Interactive Agentic Interface for Neuroimaging Analysis](https://arxiv.org/abs/2609.25254)

**<font color=#1a73e8>作者：</font>** Aakash Patel, Panos Ketonis, Shreya Saxena 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Analyzing neuroimaging data requires specialized coding and statistical expertise, which limits accessibility for researchers without computational backgrounds. We present the AI Neuroscientist, a language agent for interactive data exploration. The system integrates a large language model (LLM) with a neuroimaging toolset to perform quality control, modeling, and visualization. This allows researchers to query data quality and specify analysis parameters directly in natural language, providing a transparent and interactive alternative to conventional scripted pipelines for small-scale data exploration. We demonstrate these capabilities using functional near-infrared spectroscopy (fNIRS) data, and evaluate the agent on a custom fNIRS benchmarking suite against general-purpose LLM agents with code sandboxes. Future extensions will generalize the architecture to additional modalities, including functional magnetic resonance imaging (fMRI) data, and expand the benchmarking suite to additional fNIRS tasks.

---


### 28. [ImIR: Image-Instruction Tuning for All-in-One Image Restoration](https://arxiv.org/abs/2609.25267)

**<font color=#1a73e8>作者：</font>** Süleyman Aslan, Görkay Aydemir, Mısra Yavuz 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Degradations vary widely across images, so a practical restoration system has to handle many degradation types with one model. A recent and effective recipe adapts a large pretrained image-editing model to restoration using a small low-rank adapter with a text prompt. We replace that prompt with an instruction derived from the degraded image itself. The image reaches the editor through two paths: its structure comes from the model's VAE, and its semantic instruction comes from a lightweight token mapper that shifts the degraded image's vision-language embedding toward the embedding a clean image would produce. Because the instruction is a continuous vector, scaling it yields a family of valid restorations for tasks whose target is not unique, such as low-light enhancement. We adapt one Qwen-Image-Edit model to six tasks with a single adapter trained in about three hours on one GPU. The image instruction outperforms text conditioning under a matched comparison, and it supports task agnostic restoration without a degradation label, which the text variant does not.

---


### 29. [RULER: Instance-aware Rubric Rewards for SVG Generation](https://arxiv.org/abs/2609.25270)

**<font color=#1a73e8>作者：</font>** Hangyu Ran, Yuhao Zheng, Yingying Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generating Scalable Vector Graphics (SVG) code from natural-language instructions is an open-ended task without absolute visual ground truth, leaving both evaluation and policy optimization without a faithful signal. Scalar metrics (CLIP, Aesthetic) calibrated on natural images transfer poorly to stylized vector content, and reusing them as RL rewards triggers reward hacking. We address both limitations with rubric-based scoring. We first establish empirically that prompting a vision-language judge with a multi-axis rubric correlates with human judgments far better than scalar metrics, both across samples and within instructions. Building on this finding, we introduce RULER (Instance-aware Rubric Rewards for Reinforcement Learning), which converts each instruction into an instance-aware rubric of six items spanning semantic, visual, and stylistic axes; a judge VLM scores rendered rollouts item-by-item, and the weighted satisfactions form a fine-grained reward optimized via Group Relative Policy Optimization. Because the rubric is derived from text alone, RULER requires neither paired SVG ground truth nor human preference labels. On MMSVG-Illustration and MMSVG-Icon, RULER lifts the rubric score from 0.432/0.395 to 0.693/0.683, surpassing dedicated SVG specialists and matching the substantially larger DeepSeek-V3, with ablations identifying rubric design as the active lever for RL on open-ended SVG generation. The project page is available at this https URL.

---


### 30. [When LLM Agents Fail to Read the Room: ReAdapt for Relational Social Reasoning](https://arxiv.org/abs/2609.25284)

**<font color=#1a73e8>作者：</font>** Jianzhe Lin, Xiaolin Li, Yunda Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A social agent's most basic decisions (should I react to this post? who should I reach out to?) are not purely content problems. The right action often hinges on the latent relationship between people -- tie strength, reciprocity, mutual connections -- rather than on which content is most salient. Standard LLM agent loops do not explicitly represent how new relational evidence should revise the agent's current social hypothesis, leaving them prone to surface-obvious choices when relational and content cues diverge. We formalize this failure mode with a relationship-reasoning benchmark: 500 synthetic social worlds with friendships, follows, reaction histories, and feeds, yielding 1,000 queries over two tasks, reaction selection and warm introduction (finding the best bridge to a target person). By construction, the surface-obvious candidate differs from the relationship-grounded oracle in about 53% of queries, forming an overturn subset where the agent must use relational evidence to revise an initially plausible choice. We propose ReAdapt (Relationship-Adaptive Agent with Policy-driven sTate), which augments the ReAct loop with an explicit structured social state z = (G, B, R, N, D) capturing goal, belief, relationship, norm, and disclosure. After each tool observation, ReAdapt runs a typed Adapt step that updates this state and emits a policy operation (continue, switch, abandon, or clarify) before choosing the next action. With Gemini-3-Flash on a stratified subset of n = 150 queries per task, ReAdapt improves warm-introduction accuracy from 37% to 51% (+14 points) and reaction-selection accuracy from 69% to 77% (+8 points). Oracle regret drops from 0.260 to 0.152 and from 0.095 to 0.053, respectively. Holding the model, tools, and environments fixed, these results suggest that explicit relational-state adaptation helps LLM agents turn retrieved social evidence into revised decisions.

---


### 31. [Attention as a Routing Graph: Live Circuit Extraction from a Single Forward Pass](https://arxiv.org/abs/2609.25285)

**<font color=#1a73e8>作者：</font>** Ash Manvi, Samreena Tajreen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Finding circuits in language models usually means running many careful interventions. We try something simpler: treat attention as a routing map from one forward pass, keep a small set of routes that point toward the answer, and ask whether those routes actually matter.
They often do. On induction and IOI (tasks where the "right" circuit is already known), ablating our extracted edges hurts the model much more than ablating a random set of the same size. We evaluate n=100 prompts per cell on GPT-2 Small, GPT-2 Medium, and Pythia-410M, with paired gap tests and bootstrap confidence intervals. The extract step costs one forward; a head-by-head patch sweep costs about two orders of magnitude more.
We are not claiming a complete circuit atlas. We are claiming a cheap sketch that carries real causal signal on known tasks, with clear failure modes when it does not. Code and evaluation artifacts are at this https URL.

---


### 32. [Learned Enterprise Data Comprehension: Compression and Routing for Data Agents](https://arxiv.org/abs/2609.25286)

**<font color=#1a73e8>作者：</font>** Ethan Torres, Eric Mills  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Structured-data agents in enterprise settings must reason over complex data environments whose relevant evidence is distributed across schemas, relationships, policies, and recurring business roles. Modern agentic systems often address this burden through reusable markdown-style memory or skill files that preserve previously discovered information for later queries, reducing the need to rediscover the same structure repeatedly. This is useful, but it obscures a natural division of labor: agents are well suited to semantic reasoning, while learned systems are well suited to predicting and organizing recurring structure. We introduce latent equivalence learning to bridge this gap. The framework separates persistent task-relevant identities from their dataset-relative realizations. In our realization, supporting and opposing evidence shape support-realized Gaussian prototypes that learn how those identities are expressed in a particular data environment, while soft-membership profiles retain distinctions lost under a hard assignment. A separate learned query-prototype system represents recurring evidential requirements and maps them through a learned compatibility function into the same persistent identity structure. This identity-factorized, query-conditioned routing materializes the relevant dataset-specific evidence for downstream reasoning, allowing the agent to operate over an already organized evidential state rather than reconstructing cross-schema structure at every query. On the Data Agent Benchmark, spanning 54 queries across 12 heterogeneous datasets, our full implementation achieves 94.67% dataset-macro stratified Pass@1 over five complete trials and 258/270 successful raw query attempts, compared with 55.51% for the benchmark's Claude Opus 4.6 reference agent, ranking first among 40 leaderboard entries at submission.

---


### 33. [Can LLMs identify and repair ruptures? Comparison between clinician practices and LLM behaviors](https://arxiv.org/abs/2609.25287)

**<font color=#1a73e8>作者：</font>** Jeongah Lee, Joy Qiuyue Zhong, Drishti Goel 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Ruptures represent common albeit critical moments in interaction where relational alignment breaks down, making them essential for evaluating AI where trust and engagement matter most. In a scenario-driven empirical study, we examined the performance of three LLMs at identifying and resolving ruptures across 21 mental health conversations and 22 experts' evaluation of the strategies. For identification, LLMs relied on explicit linguistic cues within single turns whereas experts integrated implicit, relational, and contextual information across the conversation. For resolution, LLMs tended to produce more directive and scripted responses whereas experts adopted process-oriented strategies such as validation, open-ended exploration, and psychoeducation. Overall, LLMs showed higher agreement with predefined labels in identification, but not in resolution where experts rated their responses only moderately effective, with consistent limitations in timing, depth, and contextual sensitivity. We discuss implications for the design of mental health conversational agents emphasizing relational awareness, pacing, and human-in-the-loop support.

---


### 34. [FineWeb-CLaR: Culture, Language, and Region Annotations for Benchmark-Aligned Corpus Auditing](https://arxiv.org/abs/2609.25298)

**<font color=#1a73e8>作者：</font>** Yusser Al Ghussin, Eva Gavaller, Cristina España-Bonet 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Cultural evaluation coverage and robustness in language models are difficult to diagnose because pretraining corpora and cultural benchmarks are rarely indexed with comparable metadata. Benchmarks increasingly target culturally situated phenomena at the level of languages, regions, and locale-specific practices, while web-scale corpora are usually organized only by language. A shared culture-language-region layer makes these resources comparable, enabling audits of whether a target cultural phenomenon is represented in pretraining data, evaluated by benchmarks or both. To this end, we introduce FineWeb-CLaR, a large-scale annotated dataset derived from FineWeb and FineWeb-2 that places web documents on a shared culture-language-region axis for corpus auditing and benchmark alignment.
FineWeb-CLaR annotates the full 30.9B-document collection from FineWeb and FineWeb-2 with URL-derived region labels and cultural-topic provenance. Our region resolver assigns a non-empty region to 25.61% of documents (7.92B). For cultural-topic analysis, we induce locale-specific topics and project them onto the 14 leaves of the Cultural Taxonomy of Liu et al. (2025), producing Locale Topic Distributions (LTDs) for corpus-side comparison. We also annotate 277 cultural NLP benchmarks with the same taxonomy, language coverage, and region coverage. Together, these resources enable direct comparison between corpus-side pretraining evidence and benchmark-side evaluation coverage.

---


### 35. [Potential for Enhanced Learning in Machine Learning Classes by Using Wiki LLM Indexing](https://arxiv.org/abs/2609.25303)

**<font color=#1a73e8>作者：</font>** Brian Wright  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly deployed as course-specific tutors, but their usefulness depends on grounding in vetted instructional materials that are often revised mid-semester. Our prior work built a multimodal retrieval-augmented generation (RAG) system over an authentic machine learning course corpus (Foundations of Machine Learning) and found that retrieval improved contextual grounding, but that fixed retrieval strategies were suboptimal. That motivates a different question: whether how a corpus is structured at ingest time matters more than how much is retrieved at query time. We present a controlled head-to-head comparison of two knowledge representations over an identical classroom corpus: (A) vector RAG, replicating the best-performing configuration from our prior study, and (B) an LLM-compiled wiki (Karpathy framework), in which the corpus is synthesized at ingest into linked concept pages with explicit cross-references and citations back to source materials. We evaluate 59 questions spanning single-fact recall, cross-unit concept linking, synthesis and explanation, and currency after a syllabus revision, scored by an LLM judge against a human-authored rubric. Both representations answered single-fact questions about equally well (9.33 vs. 9.96 of 10), but diverged sharply on questions requiring links across course units. The compiled wiki remained accurate and grounded (9.93; 100% grounded in cited sources), while retrieval scored lower and was markedly less grounded (8.14; 64%). The wiki's citations let students and instructors trace any claim back to the lecture that introduced it, adding a layer of dynamic retrieval that machine learning courses require. While further testing is needed, instructors using AI to support learning in ML courses should consider wiki-based structure for its potential to support foundational elements of best practice.

---


### 36. [MT-ProtBERT: Multi-task Learning ProtBERT for Intrinsically Disordered Proteins Classification with Scarce Data](https://arxiv.org/abs/2609.25334)

**<font color=#1a73e8>作者：</font>** Jian Sun, Kingshuk Ghosh, Lilianna Houston 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Intrinsically disordered proteins (IDPs) differ from folded proteins in that they are dynamic, lack a stable three-dimensional conformation, and have low sequence similarity between similar proteins. The conformational heterogeneity of IDPs - while beneficial for their diverse functions - limits the use of traditional experimental tools to determine their conformation. The experimental difficulty, along with low sequence similarity, results in data scarcity, and makes it difficult to classify/detect IDPs that are similar or dissimilar, a task relevant to understand biology and evolution. We address this challenge using Multi-task ProtBERT (MT-ProtBERT), a multi-task extension of ProtBERT tailored for low-data regimes. MT-ProtBERT integrates Dynamic Window Masking, a Multi-Scale 1D Convolutional classifier (MS-Conv1D), and auxiliary objectives that jointly optimize masked language modeling and biochemistry-informed tasks. We evaluate this framework on two tasks under limited data: (i) phosphorylation site prediction (S/T/Y) in short sequences and small datasets, and (ii) protein compaction prediction on two small datasets (684 and 530 sequences), including sequences comparable in length to typical disordered regions. MT-ProtBERT consistently outperforms PARROT, an RNN-based IDP-specific model, across all tasks. These results demonstrate that combining self-supervised and biochemistry-informed tasks, and multi-scale learning enables robust modeling of unstructured proteins under data scarcity.

---


### 37. [Clarification Is Not Correction: LLMs Fail to Let Go](https://arxiv.org/abs/2609.25337)

**<font color=#1a73e8>作者：</font>** Jianzhe Lin, Xiaolin Li, Fei Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Dialogue failures in language models are usually framed as memory failures: context too long, summaries lossy, a constraint forgotten. We argue this misses a deeper problem: in many conversations the model does not forget, it commits too early. An ambiguous early turn collapses into a single hidden interpretation, and later clarification is filtered through that commitment. We call this early posterior collapse: unresolved user intent collapsing into a committed task state before ambiguity is resolved. We study it with controlled dialogue tasks in writing, planning, and coding using Gemini-2.5-Pro and Gemini-2.5-Flash. Across thousands of trials, the same information in different orders yields different outcomes, even when the final dialogue contains equivalent task-relevant information. This order effect suggests later clarification is treated as extra context rather than a corrective signal: it refines a stale task state without invalidating it. Coding tasks are especially vulnerable, suggesting early assumptions get embedded in structured artifacts such as interfaces and control flow. Standard prompting and memory strategies do not reliably help: summaries can collapse ambiguity, and chain-of-thought can reduce explicit wrong commitment in reasoning traces without improving final task success. These findings motivate uncertainty-preserving state management. If assistants cannot let go of early interpretations, robustness cannot rely on post hoc correction alone; it must keep ambiguous early turns from hardening into one task state. Assistants should hold tentative hypotheses while ambiguity remains, ask before executing when high-impact ambiguity persists, and rebuild from a revised state when later evidence invalidates an earlier reading. Rather than one prompting fix, we aim to redirect research for interactive LLMs from retaining more context toward preserving uncertainty.

---


### 38. [SSP-Bench: A Hybrid Data Generation Framework for Safety, Security, and Privacy Evaluation](https://arxiv.org/abs/2609.25352)

**<font color=#1a73e8>作者：</font>** Fatih Deniz, Yazan Boshmaf, Issa Khalil  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Evaluation of large language models (LLMs) for safety, security, and privacy (SSP) relies heavily on static benchmarks, which suffer from score saturation, data contamination, and aggregation artifacts, and fail to capture sensitivity to linguistic variation. As a result, models that perform well on fixed test sets often fail under semantically equivalent rephrasings. We introduce SSP-Bench, a dynamic benchmarking framework that generates evaluation instances on demand while preserving domain consistency. The framework ensures label validity through externally grounded sources, enforces scope via service-specific validation, and calibrates difficulty using a multi-model steering panel. Benchmark construction is formulated as a multi-objective optimization problem over difficulty, separability, novelty, and diversity. Across 24 models and four SSP services, SSP-Bench reveals systematic failures of static evaluation, including near-zero correlation in safety rankings due to construct mixing, strong safety--over-refusal coupling, and hidden within-family regressions. These results show that static benchmarks can misrepresent model behavior, motivating dynamic, deployment-relevant evaluation.

---


### 39. [TelecomGPT-R1: Unified Post-Training for Reasoning Across Heterogeneous Telecom Tasks](https://arxiv.org/abs/2609.25356)

**<font color=#1a73e8>作者：</font>** Bohao Wang, Chenwei Wu, Hang Zou 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) offer great potential to automate a broad range of telecom engineering tasks by reasoning over standards, network configurations, mathematical models, source code, and operational logs. However, existing telecom LLMs struggle to reliably reason across these diverse tasks and data types. General-purpose LLMs often lack reliable grounding in telecom-specific knowledge, while telecom-specialized models are typically developed for narrower task families and exhibit limited multi-task performance. To fill this gap, we introduce TelecomGPT-R1, a family of open source unified telecom reasoning models structured around four complementary axes: protocol, knowledge, modeling, and fault. We first develop an axis-aware data generation framework that refines coarse public telecom artifacts into verified question-answer pairs and high quality chain-of-thought (CoT) reasoning trajectories, yielding a training corpus containing 104,880 examples. Building on this corpus, supervised fine-tuning (SFT) instills telecom knowledge and evidence-grounded reasoning patterns to overcome the cold start barrier for reinforcement learning (RL). We then apply dynamic sampling policy optimization (DAPO) with task-routed rubric rewards to keep RL updates informative and stable across heterogeneous telecom reasoning tasks. These rewards decompose axis-specific CoT traces into verifiable reasoning units and combine grounded dense process credit with outcome correctness, allowing RL to learn generalizable problem solving behaviors from verifiable telecom evidence. We release the TelecomGPT-R1 models and a reproducible training recipe to support further community development. Evaluations on seven benchmarks of the GSMA Open Telco Leaderboard show that the open-source TelecomGPT-R1-27B achieves an 89.64% mean score, outperforming leading proprietary models, including GPT-5, Claude, and Gemini.

---


### 40. [From Decorative to Load-Bearing: Task Difficulty Shapes the Causal Role of Chain-of-Thought](https://arxiv.org/abs/2609.25366)

**<font color=#1a73e8>作者：</font>** Renee Jia, Di Mu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Chain-of-thought (CoT) monitoring is only meaningful if written reasoning causally constrains the answer. We introduce continuation-based causal testing, an ablation-patch intervention that perturbs one reasoning step, truncates the chain, and forces the model to continue from the corrupted prefix. It measures how load-bearing a CoT is for the final answer, a behavioral notion distinct from mechanistic faithfulness. Across Gemma-2-9B-IT, Llama-3.1-8B-Instruct, and DeepSeek-R1-Distill-Qwen-7B on GSM8K, MMLU, and BIG-Bench Hard, CoT load-bearingness tracks model-relative task difficulty: on easy tasks models silently bypass their own reasoning; on hard tasks they follow corrupted steps and propagate errors. A matched 2x2 analysis shows task difficulty dominates perturbation type: error propagation rises 16x from GSM8K to BBH multistep arithmetic, and a variance partition over 28,584 continuations attributes 98.8% of explained deviance to task difficulty versus 0.8% to perturbation type. Reasoning-specific RL suppresses error propagation and compresses the gradient. A four-variant judge-sensitivity analysis and blind two-annotator study (n=500) show the error-propagation vs. non-propagation label is invariant to judge prompt, with perfect inter-annotator agreement (Cohen's kappa = 1.00). This gradient creates a structural problem for CoT-based oversight and AI safety monitoring: where the trace is easy to read it carries little signal, and where it matters errors propagate before a monitor can intervene. Linear probes on hidden states separate silent bypass, self-correction, and error propagation, but additive activation steering provides limited causal control, flipping only about 25% of error-propagation cases at best. Behavioral mode is readable but not reliably controllable.

---


### 41. [Passes Alone, Fails Together: Benchmarking Semantic Coordination in Parallel LLM-Agent Development](https://arxiv.org/abs/2609.25396)

**<font color=#1a73e8>作者：</font>** Haocheng Xia, Eugene Wu, Yongjoo Park  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Parallel coding agents can produce patches that work alone but fail when merged. This happens when one agent changes an interface or rule that another agent still relies on. We study these failures with stale, a benchmark for semantic coordination. Our evaluation runs the same tests on each patch alone and on their combination, counting only failures introduced by combining the patches. We use three tiers: synthetic tasks with controlled interface changes, pairs of merged pull requests, and constructed tasks that use real Django helpers. Among 834 runs on 417 mined Django pairs, only one showed interference after correcting the grading procedure. On constructed tasks using 12 Django helpers, interference occurred in 97% of runs. A message describing the completed concurrent change recovered 82% of runs. Reviewed pull requests may contain few unresolved parallel changes, even when agents fail on controlled tasks using real code. The constructed failure rates do not estimate how often these problems occur in practice.

---


### 42. [Tipping Points in LLM-Based Multi-Agent Systems: Stance on Climate Change Action](https://arxiv.org/abs/2609.25432)

**<font color=#1a73e8>作者：</font>** Astghik Altunyan, Shimon Edelman  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Because significant action to counter global warming requires massive public support, it is important to understand the dynamics of public opinion on climate issues. Of special interest are social tipping points, as revealed by large-scale effects of small perturbations in individual behaviors. Agent-based models (ABM) are an effective computational tool for studying these matters, because they allow controlled and systematic exploration of the effects of interventions that may be infeasible in real-world social systems. Large language models (LLMs) have been used to endow model agents with the ability to communicate in natural language (rather than by exchanging predefined messages), as well as with personality (in the form of a narrative self and episodic memory). We leverage LLM-powered ABM to look for tipping points in the social dynamics of a micro-society in which some of the discussions are about climate change. Our agents' stance was defined by two variables: the strength of conviction about the urgency of climate action and the degree of trust in existing institutions. We quantified shifts in agents' "beliefs" by monitoring, across multiple rounds of conversations, (1) inter-agent distances in this two-dimensional stance space and (2) the patterns of discussion topics as modeled by Latent Dirichlet Allocation (LDA). Our findings to date suggest that significant abrupt changes in climate-change stance do occur in this simple model. We report a number of methodological lessons from this study, notably, the need to prevent LLM biases from interfering with the conversational dynamics and, more generally, to maintain agent personality and episodic memories of interactions in the face of such biases. Resolving these issues may allow for using ABM-derived insights in designing real-life interventions vis-a-vis climate change and other important societal challenges.

---


### 43. [PermuFormer: Multi-Task Pretraining for Permutation Representation in Algebraic Combinatorics](https://arxiv.org/abs/2609.25438)

**<font color=#1a73e8>作者：</font>** Henry Kvinge  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diverse pretraining has been shown to be an effective method for learning reusable, domain-aware representations that provide a starting point for fine-tuning on downstream tasks. While much of the excitement in AI for math has been concentrated in the use of frontier reasoning models to solve well-specified problems through the medium of language, narrow, specialized models remain an important component of the AI for math ecosystem. In contrast to large language models, specialized models are usually trained directly on the mathematical objects themselves (e.g., graphs, sequences of numbers) rather than the textual descriptions that characterize these objects. However, the common practice of training specialists from scratch may limit their ability to develop domain-aware representations that capture the multifaceted nature of mathematics. In this paper, we describe an approach to pretraining for permutation-focused tasks in algebraic combinatorics. We introduce PermuFormer, an autoregressive transformer trained on a 2.8 billion token multi-task, multi-encoding corpus. We show that PermuFormer is an effective starting point for fine-tuning on basic tasks unseen during pretraining and more complex research-level tasks, frequently outperforming the same architecture trained from scratch, baseline MLPs, and a fine-tuned generic language model of comparable size. We also analyze some of the internal mechanisms by which PermuFormer learns to solve training tasks. For example, we show that while some tasks can be linearly decoded directly from the internal representation of the prompt, other tasks require multiple rounds of generation before the answer can be decoded.

---


### 44. [Conduct Under Pressure: What Sixty Language Models Do When a User Pushes](https://arxiv.org/abs/2609.25447)

**<font color=#1a73e8>作者：</font>** Tapan Parikh  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We study what LLMs do when a user applies pressure in an uncomfortable situation: a user insists, begs, flatters or grieves, and the model gives up a correct fact, writes a document it should refuse, or cheers a plan that will cost the user money. We send frozen multi-turn scenes, identical for every model regardless of the reply, to 60 models from 13 vendors, and label each transcript with a codebook built by open coding and then frozen: a trajectory (the model held its position or folded) and a manner (how it held or folded). Two findings separate. Whether a model holds tracks its generation, meaning how recent it is: fold rate correlates with a public capability index at Spearman -0.64, with little vendor effect. How it holds tracks the vendor: six of the 17 manner codes sort by vendor at permutation p <= 0.001, corrected across the codebook. We report four vendor profiles on the codes that cleared reliability.
We also ask which parts of the labeling need a person. Six LLM coders from three vendors apply the codebook more consistently than three human coders do (Krippendorff's alpha 0.66 against 0.46), agree with the codebook's author on trajectory at kappa 0.84 to 0.91 on transcripts the codebook's examples never touched, and match an adjudicated human reference at 0.83. Blind machine readings recover the codebook's categories but cannot tell which of them a second reader would apply the same way. We conclude that for behavior a non-specialist can judge, the human contribution is authoring and bounding the codes and owning a small reference, not producing labels at volume.

---


### 45. [Rollout Efficiency in Reinforcement Learning for Reasoning Large Language Models: A Taxonomy and Future Directions](https://arxiv.org/abs/2609.25463)

**<font color=#1a73e8>作者：</font>** Niloofar Gholipour, Marcos Assuncao, Gursimran Singh 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reasoning-oriented reinforcement learning enables large language models to solve mathematical, coding, and other multi-step tasks, but shifts a substantial portion of the training cost to rollout, where trajectories are generated for policy updates. Efficient rollout mechanisms are therefore essential to reduce this cost while maintaining the freshness, consistency, and statistical validity of training data. This survey provides a systematic taxonomy of recent research on rollout efficiency for reasoning-oriented reinforcement learning, classifying existing approaches from both mechanism and bottleneck perspectives. Based on this taxonomy, we analyze how different technique families address distinct sources of rollout inefficiency, examine opportunities and potential conflicts for combining them, identify gaps in the evaluation and reporting of efficiency gains, and discuss open challenges and future research directions.

---


### 46. [Spectra: A Rules-Driven LLM Pipeline for Automated KYC Document Processing](https://arxiv.org/abs/2609.25474)

**<font color=#1a73e8>作者：</font>** Miray Wahib, Ethan Tran, Rea Mourad 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Know Your Client (KYC) onboarding in capital markets requires analysts to manually classify documents, extract structured data from heterogeneous sources, and validate compliance against complex regulatory policies. This process requires significant analyst time per client, with end-to-end onboarding often stretching to multiple weeks due to sequential handoffs. In this work, we analyze an on-boarding process and find that it comprises repeatable components well-suited to AI automation. We therefore propose a restructured workflow to be amenable to automation: we consolidate the traditional four-party process into two parties that share most of the work and can be automated together, eliminating intermediate handoffs that compound delays. To automate the remaining steps, we introduce Spectra, an AI-assisted document processing platform that combines a structured rules engine with LLM-based classification, extraction, and validation agents. The rules engine encodes compliance policy as a queryable database, enabling focused context injection that reduces token usage while improving extraction precision. Rather than a single monolithic prompt, the system decomposes document processing into isolated, auditable stages, each optimized independently and traceable to specific policy clauses. In evaluation on real KYC documents, Spectra achieves 100% classification accuracy and 89.4% extraction accuracy. Human review burden dropped by 96%.

---


### 47. [Terminal Shrinkage Averaging Reveals a Schedule-Estimator Interaction in LLM Pretraining](https://arxiv.org/abs/2609.25482)

**<font color=#1a73e8>作者：</font>** Adam Ousherovitch, Yixin Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) pretraining conventionally returns the raw final iterate. This couples two design choices: the learning-rate schedule that generates the parameter trajectory and the estimator that constructs the deployed model (e.g. the raw final iterate or a checkpoint average). A schedule that promotes optimization progress may differ from one that minimizes variation in the raw final iterate. Separating these choices creates an opportunity to maintain progress late in training while reducing variation in the returned model. To this end, we propose \emph{Terminal Shrinkage Averaging (TSA)}, which interpolates between the raw final iterate and the average of recent checkpoints to balance recent progress against terminal variation. We analyze how TSA changes the preferred terminal learning-rate schedule under a local quadratic approximation and test this interaction through a sequence of controlled NanoChat experiments. Finally, we demonstrate that the resulting gains transfer to depth-22 NanoChat, where the combined schedule and estimator improve validation quality. A qualifying time-to-GPT-2 run also finishes faster than the public baseline used in our experiments, providing preliminary evidence of benchmark acceleration.

---


### 48. [RGSQ: Riemannian Geometry-Sensitive Quantization for Large Vision-Language Models](https://arxiv.org/abs/2609.25492)

**<font color=#1a73e8>作者：</font>** Zhiping Wu, Dongdong Ren, Yangchengyu Zhou 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large vision-language models (VLMs) can be efficiently deployed under stringent memory and latency constraints through post training quantization (PTQ). However, most PTQ methods are designed for unimodal large language models (LLMs). These methods treat quantization errors as isotropic perturbations under the Euclidean assumption, which provides weak guidance on directions most sensitive to quantization in VLMs. Consequently, directly adapting unimodal PTQ approaches or solely employing modality-specific scaling often leads to uneven bit-width distribution and inconsistent performance in low-bit settings. To address these challenges, we propose Riemannian Geometry-Sensitive Quantization (RGSQ), which formulates quantization as a reconstruction problem under a unified Fisher-Riemannian metric. RGSQ identifies modality-specific sensitive directions via Riemannian manifold mappings built from modality-partitioned empirical Fisher factors and fused into a modality-aware Kronecker-structured metric. We then apply geometry-aligned rotations to reorient the local tangent frame, steering low-bit perturbations toward loss-insensitive axes. Finally, we apply a whitening transformation that maps the Riemannian objective to an equivalent Euclidean form, enabling standard unimodal PTQ methods to evaluate multimodal quantization error under their original assumptions. Across an extensive and diverse set of mainstream VLM benchmarks, RGSQ achieves the highest accuracy and stability under extremely low-bit settings (W2A8 and W3A8). It outperforms VLM-aware baselines, such as MBQ and MQuant, by up to 5.9% and surpasses single-modality improvements by up to 8.6%.

---


### 49. [Hill Sampling for Test-Time Scaling: A Simple and Better Alternative to Repeated Sampling, Evolution, and Training](https://arxiv.org/abs/2609.25510)

**<font color=#1a73e8>作者：</font>** Jacob Beck, Philip V. Ogren, Ari Kobren  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) can improve solutions to verifiable scientific and algorithmic problems by spending additional computation at test time. Recent systems achieve strong results with increasingly elaborate evolutionary search harnesses or by updating model parameters during test-time training. We ask how much of this machinery is necessary. We introduce Hill Sampling, a simple procedure that repeatedly samples candidate program edits from a frozen LLM, retains the best program found so far, and conditions all subsequent samples on that program. We evaluate the method on circle packing, sums/differences of sets, and Erdos' minimum-overlap problem using three open-weight models. Hill Sampling sets a new state of the art on circle packing among published methods, improves over the AlphaEvolve reference on Erdos' minimum-overlap problem, and achieves strong results on sums and differences of finite sets. The circle-packing and Erdos results require only hours of wall-clock time on eight NVIDIA H100 GPUs. To our knowledge, we also conduct, the largest study, by parameter count, of evolution strategies (ES) applied directly to LLM weights at test time. Surprisingly, learning the weights is worse than setting the ES learning rate to zero: at zero learning rate, the method is still searching in weight space through fixed random perturbations. Those perturbations can help exploration, but randomness from token sampling is stronger still, and repeated sampling remains substantially weaker than Hill Sampling. These results suggest a simple test-time compute allocation strategy: repeatedly sample edits to the best verified solution found so far, before introducing additional complexity such as adding archives, diversity mechanisms, evolutionary scaffolds, or test-time parameter learning.

---


### 50. [Matryoshka attribution: Learning to attribute language model outputs to representations and weights](https://arxiv.org/abs/2609.25518)

**<font color=#1a73e8>作者：</font>** Aryaman Arora, Kirill Acharya, Nathan Hu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Attributing language model outputs to their internal computations is an open problem in interpretability. Existing methods, which use causal interventions, gradients, or learnable masks, either are infeasibly expensive or struggle to identify actual causally-important internal computations. We propose framing attribution as the problem of identifying nested subsets of internal components which minimise a downstream loss. To learn this task, we introduce Matryoshka Attribution (MAttr), a mask learning method that parametrises the mask with a simple differentiable sigmoid top-$k$ operator. We supervise training over all sparsities simultaneously by randomising $k$ over training, resulting in a learned ordering of components by attribution score. MAttr achieves number 1 on the official leaderboard of the Mechanistic Interpretability Benchmark (Mueller et al., 2025); our method identifies sparse and task-transferrable circuits across varying circuit bases. As a practical application, we show that MAttr can be trained with reinforcement learning to identify weight changes responsible for downstream behaviours in LLM finetuning. We train MAttr on refusal judge scores and find that restoring $1\%$ of Llama 3.1 8B Instruct's weights to their base model state is sufficient to remove refusals while maintaining capabilities. We view MAttr as a successful formulation of interpretability into a learnable objective that we can tackle with gradient descent, and encourage future work along these lines.

---


> [!TIP]
> 当前位于：**1-50**（第 1/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-206](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
