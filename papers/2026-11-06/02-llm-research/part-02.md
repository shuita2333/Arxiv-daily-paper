# 🧠 大模型相关研究 | 2026年11月06日

> 本类共 **207** 篇论文：已确认 **189** 篇，待复核 **18** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**51-100**（第 2/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-207](./part-05.md)

---

### 51. [Phonological Knowledge of Chinese Characters in Language Models](https://arxiv.org/abs/2611.05803)

**<font color=#1a73e8>作者：</font>** Xiaozhe Ji, Renfen Hu, Hai Hu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> How much phonological knowledge do language models (LMs) possess about Chinese characters, and how is this knowledge represented and used? We introduce PinyinBench, a controlled benchmark covering homophones, phonological features (initials, finals, and tones), and polyphonic characters. We investigate 17 text-only and multimodal LMs through three complementary approaches: behavioral evaluation, layer-wise probing, and activation steering. Behaviorally, models demonstrate substantial knowledge of initials and finals, with a frontier model (DS-v4-flash) scoring 90%+ in homophone judgment, when two characters share no phonological features. However, its accuracy drops sharply to 72% when two characters differ only in lexical tone. Probing reveals that tone is highly decodable from embeddings and improves modestly across layers, whereas segmental information starts less decodable and improves substantially with depth. Activation steering shows that segmental representations can systematically influence generation, while tone exhibits much weaker effects. Furthermore, audio-bearing training improves phonological decodability, including tone, without corresponding improvements in steering effectiveness. Together, these findings reveal distinct representational and functional profiles for segmental and tonal information, with tonal information much harder to access and manipulate, demonstrating the necessity for combined evaluation, probing, and causal intervention for understanding linguistic knowledge in LMs.

---


### 52. [When File Ingestion Misleads Language Models: Measuring and Mitigating Divergences in Office Documents](https://arxiv.org/abs/2611.05806)

**<font color=#1a73e8>作者：</font>** Penghui Li  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Office documents are now routinely uploaded to large language models (LLMs) for processing. However, an LLM does not always see what a human sees, because it typically reads the text that an extractor produces from the document's underlying Office Open XML (OOXML) files. Depending on the implementation, extractors differ in which OOXML parts they read and how they interpret them, so their output can differ from what Office applications display. For example, by slightly shifting the positions of text boxes on a slide, an adversary can swap the order in which the model reads them while the slide looks unchanged. We show that this extraction divergence is an attack surface for LLM applications.
In this work, we first measure what an adversary can exploit by analyzing the widely used extractors that LLM applications rely on. By combining static source code analysis with dynamic analysis, we identify 19 OOXML channels where extractors read content a human cannot see and 12 where they drop content a human can. We also find that widely used extractors ignore display formatting and reading order, so even visible content reaches the model in a different form. Building on these findings, we construct five attacks that lead the model to interpret a document differently from a human reviewer, without injecting any instruction. We test the attacks on four major chat assistants (ChatGPT, Claude, Gemini, and Microsoft 365 Copilot) and four coding agents (Codex, Claude Code, Antigravity, and GitHub Copilot CLI), and every one of them is misled by at least one attack. Finally, we propose Prism, a lightweight defense that reconstructs the human view from the OOXML specification before passing the text to the model. Prism also generalizes to unseen attack payloads.

---


### 53. [Learning When Human Decisions Matter: Executor-Relative Consultation Value for LLM Agents](https://arxiv.org/abs/2611.05814)

**<font color=#1a73e8>作者：</font>** Shuli Jiang, Khushbu Pahwa, Yuting Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models increasingly automate complex tasks, but human decision capacity does not scale with their capabilities. In many applications, humans remain essential for providing private context, authority, or judgments unavailable to the agent. We formulate human decision capacity allocation: given multiple consultation opportunities and a limited budget, at which decisions should an LLM agent consult a human? The central challenge is estimating consultation value, which is executor-dependent because the same human input may benefit different downstream agents differently. We introduce Consultation Value Distillation (CVD), which estimates consultation values offline using Monte Carlo executor rollouts and distills these values into lightweight predictors for budgeted allocation, requiring no rollout-based value estimation at deployment. Across five batch and three sequential settings with two frontier executors, CVD improves allocation through joint and continuation-aware value learning, while independent consultation values remain competitive in several settings. CVD also broadly outperforms direct prompting and Value of Information where applicable, remains robust with substantially less rollout supervision, and enables nearly lossless approximate allocation at low search cost.

---


### 54. [A Hybrid Approach for Automated Security Pattern Recovery](https://arxiv.org/abs/2611.05823)

**<font color=#1a73e8>作者：</font>** Anh Minh Nguyen, Tuan Dat Tran, Alzubair Hassan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Security-by-design emphasises integrating security into software design and development. Security pattern catalogues operationalise this principle by prescribing reusable architectural solutions to recurring security problems. However, recovering their implementations from source code remains challenging because security patterns are abstract, span multiple components, and admit many valid implementations. We present SecPatRec, a hybrid approach for automated security pattern recovery from source code repositories. We treat a security pattern as a reference architecture and frame its recovery as a deductive task: determining which prescribed roles are present, grounding them in code entities, and recovering their interaction sequences. SecPatRec pairs a ReAct-style LLM agent equipped with semantic and lexical code search for role detection and grounding with static code property graph analysis for interaction recovery. We curate a human-validated ground-truth dataset of 100 pattern instances covering five security patterns across 93 open-source Java and Python repositories, and introduce a three-level evaluation framework measuring recovery correctness against this ground truth. We evaluate SecPatRec using four LLMs, including proprietary and open-source models. Averaged over all models and pattern instances, SecPatRec achieves role-detection accuracy of 0.84, role-grounding similarity of 0.84, and an interaction-recovery score of 0.66. Compared to a one-shot end-to-end LLM baseline, SecPatRec achieves higher aggregate recovery scores and lower estimated LLM API costs per run, while processing repositories that exceed the baseline's configured input limit. The recovered role mappings and statically derived interaction sequences provide structural and behavioural evidence that can support inspection of security-pattern implementations.

---


### 55. [TandemBench: Benchmarking Decision Models for Multi-Agent Collaboration](https://arxiv.org/abs/2611.05827)

**<font color=#1a73e8>作者：</font>** Baohang Li, Xiaocheng Feng, Bing Qin  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Decision models choose among predefined options in tasks such as routing and action selection. In multi-agent collaboration, a decision determines how members divide work, exchange resources, and act in parallel. We introduce TandemBench, a benchmark of 1,200 questions in multi-agent cooking scenarios where coordination choices affect goal completion. Models receive complete global information and candidate team plans, with reference answers established through execution and exact search. Models select an optimal team plan and, in paired variants that retain or remove it, judge whether better arrangements exist beyond the supplied options. We evaluate 40 native decision models and compare them with 10 general-purpose language models. The best native decision model achieves 62.50% decision accuracy. Native decision models remain close to chance in optimality verification. Paired tests reveal that some report better alternatives regardless of whether an optimal plan is already present. These findings show that team-plan decision accuracy alone can conceal systematic errors in judging whether the supplied options contain an optimal arrangement. The dataset and evaluation code are publicly available at this https URL.

---


### 56. [Pathwise-Budgeted LLM Routing: Online Allocation with K-Bit Tail-Cost Learning](https://arxiv.org/abs/2611.05835)

**<font color=#1a73e8>作者：</font>** Hanzhang Qin, Sophie H. Yu, Yuewei Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Firms using large language models under fixed budgets must decide which model to call and whether to retry a failed task. Because a call's charge is revealed only after completion, one long response can exhaust the remaining budget and leave later tasks unserved. Our objective is to maximize the number of tasks solved before service stops. We develop a contextual bandit policy, ADP-HT, which learns each model's task-specific success probability and constructs conservative cost estimates from coarsened response-length labels on a quantile grid with $2^K$ intervals. The policy weighs predicted success against these costs, adjusting the cost penalty to realized spending and the budget available per remaining task. Under calibration, local regularity, and grid-coverage conditions, we bound the excess allowance in the policy's conservative cost estimates. At a fixed sample size, increasing $K$ reduces the discretization term but increases the estimation allowance. At the tightest tested budgets, ADP-HT solves more than twice as many MATH500 and GPQA tasks as the best implemented baseline. It achieves the highest mean cumulative score at ten of fourteen RouterBench budgets. On LiveCodeBench, it outperforms a deployed commercial router in both default and cost-saving modes at the three lowest test budgets.

---


### 57. [Vision Paper: Why Distributed LLM Post-Training and Decentralized Alignment Are Now Essential](https://arxiv.org/abs/2611.05841)

**<font color=#1a73e8>作者：</font>** Zhanhong Jiang, Qisai Liu, Soumik Sarkar  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This vision paper argues that distributed learning, including federated and decentralized, should become a first-class paradigm in LLM post-training, not merely a privacy add-on. Current methods like RLHF and DPO rest on an invisible assumption: preference data should be centralized. We contend this assumption is scientifically unjustified, practically unsustainable, and ethically problematic. As LLMs deploy into healthcare, law, finance, and multilingual communities, preference data originates from populations that cannot or will not centralize. We develop a three-pillar argument grounded in (1) privacy and data sovereignty, (2) pluralism and representational equity, and (3) robustness and scalability. We formalize key technical challenges unique to this intersection, reference drift, preference heterogeneity, and the DP-utility trade-off for contrastive losses, and propose concrete algorithmic directions, and sketch a research agenda. Our analysis shows distributed post-training is not only necessary but tractable, and ignoring it risks AI that is legally noncompliant, representationally narrow, and brittle at scale.

---


### 58. [PEARL: Prediction Error-Adaptive Regularized Learning for Selective Forgetting under Partial Preference Drift](https://arxiv.org/abs/2611.05842)

**<font color=#1a73e8>作者：</font>** Rashmi Gangadharaiah, Balakrishnan Narayanaswamy  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> User preferences shift as needs, context, and tastes evolve. This matters for personalized recommendation, LLM response generation, and RLHF-trained reward models, which can become miscalibrated as preferences drift. Existing non-stationary bandit methods forget uniformly across all dimensions, but real preference shifts are typically partial: some dimensions go stale while others remain valid. Neural contextual bandits accumulate confidence monotonically via the Gram matrix, with no mechanism to direct uncertainty where predictions have gone wrong. We propose PEARL (Prediction Error-Adaptive Regularized Learning), which reverses the Gram update along feature directions where predictions are surprisingly wrong, while leaving confidence intact elsewhere. We prove that (i) any non-adaptive policy suffers linear regret after a preference shift, (ii) no fixed exploration rate achieves low regret in both stationary and non-stationary regimes, and (iii) PEARL's cumulative regret scales with the number of shifted users N_s, not the total population N. On PRISM, a personalized LLM response selection benchmark (1,500 users, 21 LLMs), PEARL beats greedy by +4.0 points and the best neural bandit baseline by +2.5 points (p<0.001), while performing on par with greedy when preferences are stable. It beats sliding-window and discounted approaches by 3 to 10 points, showing that selective forgetting outperforms uniform forgetting. The selection policy is a ~100K-parameter MLP that runs in milliseconds on CPU, leaves LLM weights frozen, and works with any API-based model.

---


### 59. [Generative AI for urban planning: synthesizing land-use maps with satellite imagery via DualControlNet](https://arxiv.org/abs/2611.05859)

**<font color=#1a73e8>作者：</font>** Qingqi Song, Yuzhou Chen, Lingqian Hu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Various land-use models characterize land-use patterns and facilitate scenario planning. However, existing models are largely predictive, forecasting transitions based on numeric data without synthesizing new land-use maps from simple text prompts. Meanwhile, generative AI in urban systems remains unimodal, weakly controllable, and evaluated mostly by generic image quality rather than domain-specific metrics. To address these gaps, we introduce DualControlNet, a generative land-use model that jointly synthesizes high-resolution land-use maps and satellite imagery, addressing multimodality, controllability, and verification challenges. Trained on over 40,000 paired tiles from Orlando and Chicago, DualControlNet is evaluated using land-use, spatial consistency, and image quality metrics. Relative to unimodal baselines, DualControlNet improves land-use diversity consistency by 62.8% and building coverage ratio consistency by 16.3%, more than doubles cross-modal spatial consistency, and triples visual quality. Scenario-based experiments demonstrate that DualControlNet supports sustainable development through multidimensional controls, increasing density and diversity, and responding to text prompts like "high-density development." Overall, this work advances land-use modeling via a multimodal, controllable, and verifiable generative framework, lowering technical barriers and enabling intuitive exploration of urban futures.

---


### 60. [CARTBench: Rubric-Based Evaluation of Shopping Advice for Complex and Ambiguous Requests with Timelines](https://arxiv.org/abs/2611.05862)

**<font color=#1a73e8>作者：</font>** Yuqin Dai, Zhanwei Zhang, Honghui Yang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) shopping assistants now recommend products in multi-turn conversations. However, reliable evaluation faces Data scarcity and Difficulty Standardizing Criteria. To address these obstacles, we introduce CARTBench for CART (Complex and Ambiguous Requests with Timelines). For Data scarcity, we curate cases from real commercial shopping needs across 17 retail domains, pairing timestamped dialogue with 1,603 product records. For Difficulty Standardizing Criteria, we develop case-specific rubrics guided by Ideal Response Principles, distilled from excellent replies manually selected from successfully completed orders. These principles also guide Principle-Guided CART Prompting, our structured recommendation strategy. The experimental benchmark contains 1,328 expert-annotated criteria across Core, Excellence, and Safety. To answer the CART question, we evaluate 7 flagship commercial API models, including GPT-6.1-Sol and Claude-Opus-5, and 35B+ parameters open-weight models. In the first full-suite evaluation under the frozen rubrics, 3 of 10 models exceed 90% on Core, while none exceeds 45% on Excellence. Therefore, we identify an understanding-to-execution gap between required behavior and high-quality purchase advice. To examine these limitations, we diagnose shared failures in product evidence and unresolved needs, linked to changing requirements and decisive unknowns. Code and data are available at this https URL.

---


### 61. [Auditable Unlearning for LLMs](https://arxiv.org/abs/2611.05866)

**<font color=#1a73e8>作者：</font>** Piyush Tiwary, Anushka Srivastava, Prathosh A.P  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Machine unlearning aims to remove a user's data from a trained model after a deletion request. Existing methods are majorly evaluated on three axes - how well they forget, how much capability they retain, and how robust they are to membership inference attacks, but not on whether the provider can offer the user any evidence that the deletion occurred. To fill this gap, we introduce auditability as a fourth axis, defined as the separation between requested (forget set) and retained (retain set) data under a statistic the provider computes. We show that across eleven unlearning methods on TOFU, MUSE and RWKU no method satisfies all four axes, with different methods falling short on different axes. To address this, we propose a two stage method that can be used on top of any unlearning method, in the the first stage we propose ${GapWiden}$ which uses a hinge loss to increase the difference between audit statistics of forget set and retain set. In the second stage we propose ${GapVeil}$, an inference time rejection-sampler which uses the base model as the drafter and re-samples based on the audit statistics of the drafted response. We observe that using our method, auditability and leakage reach oracle parity for every unlearning method, and forget performance converges to the oracle; retain performance improves for nine of eleven methods but remains short of parity. Our results show that evidence of deletion or auditability can be constructed by design, and that treating it as an explicit requirement changes the viability of existing unlearning methods.

---


### 62. [When Does Better Confidence Improve a Knowledge-Graph Audit?](https://arxiv.org/abs/2611.05877)

**<font color=#1a73e8>作者：</font>** Zehao Lin, Kai Chen, Xixuan Hao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Confidence estimates guide human review in LLM-built knowledge graphs, but better error prediction can yield little improvement in an audit. We study this gap through repairability, selection headroom and label validity. Modelling non-adaptive auditing as budgeted covering, we characterise the minimal decision-relevant error statistics and bound the regret of scalar-preserving first-order planning by a structural mass $\Delta^{\mathrm{cl}}$. We simulate ideal repair against benchmark-aligned labels for five extraction configurations and two cross-document graphs on Re-DocRED, followed by frozen confirmation on test and replication on 500 hash-selected training documents. On the held-out cross-document graphs, an error-rate $\times$ fan-out queue leaves 3.98-4.74 percentage points more errors than a joint model with the same actions. By comparison, opening shared actions for that joint planner reduces residual errors by 0.89-1.43 points relative to its own fact-only plans, in point estimates. Equivalence between joint and independent-block models remains inconclusive. Generic LLM verification improves three of four model-budget configurations on each held-out set. LLM adjudication identifies possible benchmark omissions.

---


### 63. [RECAP: Context-Aware Prediction Recycling with Request-Local and Persistent Memories for Multimodal Speculative Decoding](https://arxiv.org/abs/2611.05894)

**<font color=#1a73e8>作者：</font>** Hengjie Zhu, Dayan Wu, Xinze Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recycling a target model's own predictions offers a training-free source of proposals for speculative decoding. In vision-language models, however, existing recycling indexes predictions by the last token alone, conflating predictions computed under different images and prefixes; we find that such reuse fails most often at image-sensitive decoding states. Longer keys reduce this aliasing but match fewer states. We introduce \method, which stores target predictions under one-, two-, and three-token keys: contextual memories live only for the current request and are thus implicitly conditioned on its image, while token-level memory persists across requests to retain coverage. At each lookup, entropy-confidence weighting fuses the retrieved predictions according to their key specificity and concentration. Best-first search composes the fused transitions into a candidate tree, supplemented by suffix-matched continuations, and one target pass verifies the tree under greedy decoding. Without training or an auxiliary draft model, \method\ achieves mean speedups over autoregressive decoding of $1.66\speed$ and $1.56\speed$ across seven single-turn benchmarks on Qwen2.5-VL-7B and LLaVA-1.6-7B, exceeding the strongest training-free baseline, Token Recycling ($1.51\speed$ and $1.37\speed$). Our implementation is available in this https URL.

---


### 64. [Selective, Risk-Controlled Emotion Forecasting in Conversation: From a Persistence Barrier to Departure Detection with Conformal Guarantees](https://arxiv.org/abs/2611.05896)

**<font color=#1a73e8>作者：</font>** Bin Wen, Dai-Qiao Zhang, Tien-Ping Tan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Forecasting emotion in conversation is increasingly framed as predicting the next emotional state's value. We show this targets a hard quantity in a state-observed testbed and propose a learnable, deployable reformulation instead. On valence-arousal-dominance trajectories from a dyadic corpus, repeating a speaker's own previous state sets a persistence baseline that no frozen-encoder correction meaningfully improves upon and a state-space filter exceeds; the floor requires the historical state to be observed, since an estimated anchor collapses persistence below a direct forecaster. What survives is the timing of a departure from persistence, learnable on three of four corpora and near chance on the highest-base-rate corpus, a negative result we report. We recast the task as selective departure forecasting: a lead-time-weighted metric with a leakage protocol, and commitment policies whose best choice switches with the departure rate. A dialogue-level conformal risk control bounds the expected loss of committed predictions, meeting the target in all twelve configurations tested, though the guarantee is bought through abstention, with coverage and alarm recall falling sharply on the hardest corpus. One tested language model's confidence fails as a ranking signal where another succeeds, a model-dependent failure not yet attributable to family versus scale. Code and result logs are available from the corresponding author upon request.

---


### 65. [EchoKV: Self-Corrective KV Cache Eviction via Iterative Query Feedback](https://arxiv.org/abs/2611.05903)

**<font color=#1a73e8>作者：</font>** JianKun Zou, Tongtong Yuan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> KV cache eviction is not merely a token-ranking problem: the workspace retained for generating eviction queries also determines the quality of those queries. Consequently, an early workspace error can distort later query observations and reinforce an incorrect final eviction decision, particularly when evidence is dispersed across a long context. We present EchoKV, which discovers and addresses this failure mode with iterative correction. It initializes a feedback-compatible bootstrap workspace using proposals at future decode positions, then uses early decode-generated queries to recover the workspace before the remaining lookahead steps. It uses the same number of workspace forward passes as LAQ while adding a tensor re-scoring operation for workspace repair. On LongBench (16 tasks, Mistral-7B-Instruct-v0.2 and Qwen2.5-7B-Instruct), EchoKV shows notable improvements over LAQ on several tasks requiring dispersed evidence, including multi-hop cross-document QA and long single-document comprehension. Across budgets and backbones, EchoKV selectively improves evidence-intensive tasks while maintaining comparable performance on the remaining LongBench subsets. These results identify query--workspace coupling as a practical failure mode of query-driven KV eviction.

---


### 66. [CHARM+: Cross-Hardware Attention with Re-Merge Multistream Mechanism](https://arxiv.org/abs/2611.05906)

**<font color=#1a73e8>作者：</font>** Xinhang Zhang, Boning Zhang, Chengchun Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As sequence lengths continue to grow, distributed attention based on sequence parallel (e.g., Ring-Attention) has become a mainstream solution for large language models (LLMs). Nevertheless, inherent communication dependencies limit computation-communication overlap, reducing GPU utilization. Moreover, in cross-hardware (NUMA or node) architectures, due to imbalanced communication bandwidth, frequent communication synchronization will limit overall performance. Based on these insights, we propose CHARM+, Cross-Hardware Attention with Re-Merge Multistream Mechanism. We reorganize sequential communications into several levels and achieve intra-level parallelism and computation overlap. Furthermore, we decouple cross-hardware communication from intra-hardware communication, eliminating synchronization overhead caused by bandwidth imbalance. Forward and backward algorithms were evaluated on multiple hardware architectures and consistently outperformed state-of-the-art methods. Compared to Ring-Attention, our forward and backward algorithms achieve average speedups of 1.3x and 1.7x on a dual-NUMA PCIe architecture, and 2.8x and 2.9x on a dual-node NVLink architecture, respectively.

---


### 67. [Routes of Reasoning: Reading and Reshaping Test-Time Compute in MoE Models](https://arxiv.org/abs/2611.05919)

**<font color=#1a73e8>作者：</font>** Shengjie Wang, Mohsen Fayyaz, Nanyun Peng  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reasoning models allocate test-time compute across distinct behaviors such as planning, deriving, and verifying. However, models frequently "overthink," continuing to verify and re-derive long after finding a correct answer. This wastes expensive compute and can even degrade performance. Existing interventions, such as token budgets or steering, primarily regulate reasoning duration rather than targeting specific behaviors. In this work, we demonstrate that Mixture-of-Experts (MoE) routers provide a natural, training-free interface for behavioral control. We first split reasoning traces into sentence-level segments and label each with one of six reasoning behaviors (planning, execution, restatement, fact, reflection, and conclusion), so that every token carries the behavior of its segment. Linear probes on router logits predict this label nearly as well as probes on the residual stream, the model's full hidden state and the standard target for probing, while using about half as many features. These signals generalize: experts associated with a reasoning behavior on one dataset predict the same behavior on the others, across six datasets spanning five domains (math, code, science, knowledge, and commonsense). Building on this, we selectively edit expert router scores during inference to curb overthinking. Across four models and four benchmarks, this intervention reduces the number of generated tokens by a median of 30.4% (and up to 63.3%). Crucially, it encourages the model to stop once the problem is solved, rather than skipping essential reasoning steps. Accuracy never drops by more than 0.5 percentage points, and frequently improves. Ultimately, MoE routing offers both an interpretable lens into reasoning states and a lightweight mechanism for optimizing test-time compute.

---


### 68. [Modality-Aware Expert Pruning for MoE-Based Multimodal Large Language Models](https://arxiv.org/abs/2611.05927)

**<font color=#1a73e8>作者：</font>** Donggeun Kim  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Mixture-of-Experts (MoE) enables multimodal large language models (MLLMs) to scale capacity efficiently, but expert parameters dominate memory even though only a few experts are activated per token: they account for over 90% of model size in modern MoE-MLLMs (e.g., 54 GB out of about 58 GB in BF16 for InternVL3.5-30B-A3B and Qwen3-VL-30B-A3B). Expert pruning has emerged as an effective compression strategy, but existing methods aggregate importance uniformly across tokens, ignoring that the same expert may serve different roles for vision versus language processing. To address this, we propose MAEP (Modality-Aware Expert Pruning), a training-free framework that decomposes expert importance by modality in a single forward pass. MAEP introduces (1) Delta-H Output ($\Delta H$), a redistribution-aware metric measuring the MoE output change when an expert is removed, and (2) low-attention vision tokens as a vision-side pruning signal that is dataset-stable: its expert-importance ranking remains stable across different datasets. Text-side importance serves as a preservation signal while vision-side importance serves as a pruning signal, and experts are ranked globally across layers. Experiments on three MoE-based MLLMs across multimodal and text benchmarks show that MAEP outperforms modality-agnostic baselines on the majority of multimodal benchmarks while remaining competitive on text-only tasks, reducing the BF16 expert weight footprint by about 27 GB (about 47% of total memory) so that the full weight footprint of an approximately 58 GB model fits within a single 40 GB GPU. Code is available at this https URL.

---


### 69. [Reward Budgeting Reduces Premature Convergence in Reinforcement Learning for LLM Reasoning](https://arxiv.org/abs/2611.05942)

**<font color=#1a73e8>作者：</font>** Mengni Jia, Mengyu Zhou, Xiaoxi Jiang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> RL for LLM reasoning often reaches an early performance plateau as the policy distribution becomes increasingly sharp. Recent work has studied policy entropy as both a diagnostic and a control signal for this behavior. In our experiments, however, increasing entropy alone does not reliably change the eventual plateau. We analyze RL through its implicit target policy and derive a sharpness factor $\kappa$, together with an effective counterpart $\kappa_{\mathrm{eff}}$, that describes how strongly reward or advantage gaps are translated into probability-ratio gaps. Motivated by this view, we introduce \emph{reward budgeting}, a plug-in advantage construction that assigns a fixed total reward budget to each prompt. For binary rewards and independent on-policy rollouts, its unclipped score-function estimator follows the gradient of an exact finite-$G$ concave objective with diminishing returns, while its advantage gap decreases as more rollouts become correct. For general rewards, a shifted log-mean interpretation holds asymptotically under the stated regularity conditions. These results motivate, rather than establish exact objective equivalence for, the clipped implementations. On Qwen3-8B and Llama3.2-3B-Instruct, reward budgeting consistently improves a range of RL baselines, with gains up to +12.50 on AMC23 and +10.00 on AIME24 and AIME25. Overall, our results support an update-dynamics view of premature convergence and show that strong gains can be obtained without explicitly preserving entropy.

---


### 70. [Graph-Mediated Large Language Model Systems in the Agentic Era: Reasoning, Knowledge, Retrieval, Execution, and Coordination](https://arxiv.org/abs/2611.05953)

**<font color=#1a73e8>作者：</font>** Haihui Liu, Yang Chen, Zice Qiu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Graphs play an increasingly important role in large language model (LLM) systems, supporting structural reasoning, knowledge grounding, retrieval, and memory. As these systems evolve toward the agentic era, graphs also organize execution dependencies and multi-agent communication, linking intermediate observations and retained information to subsequent decisions. However, understanding their contribution requires distinguishing the function of each graph operation, the component responsible for its computation, and the subsequent use of its output. This survey introduces an operation-level role--locus taxonomy for reasoning, knowledge and evidence, retrieval and memory, execution, and coordination. We compare how graph observations and external computations guide decisions, how memory representations and updates support later tasks, and how dependencies constrain execution and information delivery. These comparisons distinguish improvements in local metrics from downstream task performance while retaining the conditions under which results were reported. We then organize benchmarks, comparison designs, process diagnostics, and system costs into an evaluation framework. Finally, we identify open challenges in adaptive computation and stopping, memory maintenance, and dependency-aware recovery. The survey provides a basis for assessing when graph mechanisms are useful and for evaluating their effects across components and stages.

---


### 71. [Robots in the City: Persona-Based Perceptions of Urban Robots](https://arxiv.org/abs/2611.05954)

**<font color=#1a73e8>作者：</font>** Keonhee Jang, Kanghoon Lee, Seokwoo Yun 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Pedestrians increasingly encounter robots in urban public spaces without interacting with them, but how robots change the perceived safety of a street remains unclear. We examine how robot presence and type affect perceived safety across urban contexts. We generate 18 images of Seoul streets that vary in time of day, road class, and robot condition (no robot, a delivery robot, or a humanoid). Two multimodal large language models (MLLMs), Qwen3.8-27B and Gemma4-26B, each conditioned on 500 synthetic personas, choose the safer image in each pair, and 25 human respondents complete the same task. Both models prefer streets without robots and favor the delivery robot over the humanoid. Robots are chosen more often at night and less often by older personas, whereas road class has smaller effects. In the model rationales, the delivery robot appears as a physical obstacle, whereas the humanoid appears as either a threat or a source of protection. Like humans, both models chose robots more often at night, but chose the humanoid over the delivery robot far less often, and Gemma showed a night effect for the humanoid about three times that of humans. These results show that the effect of a robot on perceived safety depends on when it appears, and that persona-conditioned MLLMs capture only part of human judgments.

---


### 72. [Enforcing Accountable Disclosure in Confidential AI](https://arxiv.org/abs/2611.05971)

**<font color=#1a73e8>作者：</font>** Shumpei Shiina, Haruka Takahashi, Kento Sasaki 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Advances in CPU and GPU confidential computing enable confidential AI, allowing LLMs to process user prompts without exposing them to service providers or infrastructure operators. However, AI agents often need to send prompt-derived information to external services, and providers may also require limited disclosure for safety monitoring and failure diagnosis. We propose CORDE, a system for confidential virtual machines (CVMs) designed to satisfy the principle of Confine or Declare: user-derived data is confined by default, but when necessary, it may leave the CVM only after being "declared." To "declare" data is to record its exact contents, recipient, and stated reason in a user-accessible, tamper-evident declaration log. To put this principle into practice, we present an integrated system design that combines per-user information-flow control in Rust with a TEE-based ledger and remote attestation. Our evaluation on an NVIDIA H100 GPU shows that declaration before disclosure adds little overhead in task latency, about 0.5% on the AppWorld agent benchmark. CORDE provides a basis for accountable disclosure of user data, supporting responsible and transparent data management in AI services.

---


### 73. [On the Design of Hyper-Connections: Simplification, Stability, and Scalability](https://arxiv.org/abs/2611.05984)

**<font color=#1a73e8>作者：</font>** Xiangdong Zhang, Xiaohan Qin, Sunan Zou 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hyper-Connections (HC) architectures are increasingly adopted in frontier language models, yet their components remain insufficiently understood and introduce non-negligible training overhead. In this work, we systematically study the HC architecture to understand its components and identify simpler, more efficient designs. We find that learned read/write gating without mixing and unconstrained mixing with fixed gates form two effective interaction groups: either alone achieves performance comparable to mHC. We also identify repeated access to the expanded residual state as a major source of training overhead, even without mixing. These findings lead to SimpleHC, which simplifies the architecture by removing residual mixing and simplifies execution through shared memory access, using the resulting additive structure and shared gate inputs. Layer-specific gates share a group-entry state, enabling batched reads and deferred writes; scalar corrections exactly preserve preceding sublayer output contributions. Our analyses support both the retained residual structure and the design of shared memory access. SimpleHC incurs only 2.4% extra end-to-end training time over a vanilla residual baseline at the largest tested scale. It maintains performance comparable to mHC when scaling from 15B to 30B MoE models, exhibits smoother gradient dynamics during standard training, and remains stable under stress. We hope SimpleHC will encourage a broader pursuit of simplicity in foundation model design, making performance gains more accessible and practical at scale.

---


### 74. [Clips2Story: Training-Free Video Storyboarding and Editing Using Multimodal Retrieval-Embedded Generation](https://arxiv.org/abs/2611.05992)

**<font color=#1a73e8>作者：</font>** Junnuo Wang, Weihan Xu, Hao-Wen Dong  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video editors often work with large collections of fragmented footage and must select and organize relevant clips into a coherent story. However, many existing video editing and summarization methods assume a temporally ordered source video and aim to preserve its original narrative and temporal structure. In this paper, we introduce Clips2Story, a training-free, LLM-based pipeline that enables users to create keyword-specified short videos from a pool of video clips. Given a pool of clips and a user-specified keyword, we first extract text-based multimodal descriptors for each clip and retrieve the clips most relevant to the keyword. We then provide the textual descriptors of these candidate clips to an LLM, which selects and arranges them into an editable storyboard with connective narrations. Finally, we assemble the selected clips and retrieve accompanying visuals for the narrations to compose the output video. To evaluate the proposed pipeline, we construct a synthetic evaluation dataset from 100 long-form videos across five genres by segmenting each video into short clips using a scene-change detection model and shuffling the resulting clips to remove their temporal order. Through objective evaluation and qualitative examples, we demonstrate that Clips2Story can effectively retrieve keyword-relevant clips and compose coherent storyboards based on user-specified keywords. Human evaluation further shows that Clips2Story outperforms a strong baseline in terms of narrative coherence, keyword alignment, and overall realism.

---


### 75. [FedIA: Instance-Aware Cross-Modal Representations for Federated Prompt Learning](https://arxiv.org/abs/2611.05994)

**<font color=#1a73e8>作者：</font>** Xuanjing Zhang, Qi Guo, Yanan Qiao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Federated Prompt Learning (FPL) enables parameter-efficient adaptation of pre-trained Vision-Language Models across decentralized clients without exchanging raw data. To cope with cross-client heterogeneity, existing FPL methods typically pair a globally shared prompt with a client-specific local prompt. However, this design personalizes only at the client level: the same local prompt is applied to all samples of a client, and the global and local prompts are combined in an input-agnostic, fixed manner. Consequently, it overlooks the substantial visual variations among samples within the same client and cannot adjust the balance between shared and personalized knowledge to each input. To address these limitations, we propose Federated Prompt Learning with Instance-Aware Cross-Modal Representations (FedIA), an FPL framework that learns instance-aware cross-modal representations. Specifically, FedIA first uses global text prompts as client-invariant semantic anchors to select image patches most relevant to each candidate class, suppressing distracting regions. The selected visual evidence then conditions the generation of instance-aware local text representations. Finally, an adaptive global-local fusion module calibrates the contributions of local and global text representations for each image-class pair. In this way, FedIA shifts personalization in FPL from the client level to the instance level while preserving the semantic knowledge shared across clients. Extensive experiments under domain shift, pathological label skew, and Dirichlet-based label skew show that FedIA outperforms FPL baselines, with maximum accuracy gains of 1.44\%-4.37\% over the latest baseline across the three settings. Ablation studies and analyses further verify the complementary contributions of instance-aware representation generation and adaptive global-local fusion.

---


### 76. [How Far Can You Steer? Behavior-Capability Frontiers in Contrastive Activation Addition](https://arxiv.org/abs/2611.06001)

**<font color=#1a73e8>作者：</font>** Deepanshu Raj  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Activation steering can modify language-model behavior without parameter updates, but behavioral efficacy alone does not determine whether an intervention is usable. Contrastive Activation Addition (CAA) steers targeted behaviors using activation directions derived from contrasting examples, potentially degrading unrelated model capabilities in the process. We therefore study CAA through a behavior-capability frontier, selecting interventions that maximize behavioral gain subject to an explicit bound on capability degradation. We evaluate this framework across four instruction-tuned models, seven behaviors, and capability-loss budgets of 1%, 3%, and 5% (absolute percentage points). Validation-selected behavioral effects generalize strongly to held-out data ($\rho = 0.945$), while joint behavior-capability survival among nonzero operating points rises from 37.5% at the 1% budget to 72.7% at 3%, with limited additional improvement at 5%. Control experiments indicate that these effects depend on learned behavior directions rather than generic activation perturbations. Representational geometry is significantly but only modestly predictive of causal cross-behavior transfer. Finally, secondary capability, out-of-distribution, and open-ended evaluations show that interventions satisfying protected benchmarks can still degrade untested capabilities or transfer unevenly to free-form generation. These results characterize activation steering as a constrained intervention whose usable range depends on model, behavior, direction, layer, and evaluation budget, rather than a universal control knob.

---


### 77. [MotoVerse: A Benchmark for Predictive Perception of Motorized Two-Wheelers in Dense Unstructured Traffic](https://arxiv.org/abs/2611.06007)

**<font color=#1a73e8>作者：</font>** Varun A. Paturkar, Shankar Gangisetty, C.V. Jawahar  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Motorized Two-Wheelers (MTWs) dominate personal transport across much of the Global South, yet remain largely overlooked in predictive perception research for autonomous driving and ADAS. We introduce MotoVerse, a benchmark for predictive perception from an MTW's ego-centric perspective. MotoVerse comprises 949 maneuver clips collected in dense, unstructured traffic and trajectory annotations for over 31,000 surrounding road agents, including over 16,000 MTWs, enabling two complementary tasks: Ego-Rider Maneuver Anticipation (ERMA) and Traffic Agent Trajectory Prediction (TATP). Each clip is further annotated with an MTW-specific challenge taxonomy comprising dynamic ego-motion, weak traffic structure and contextual occlusion, enabling challenge-aware evaluation. We benchmark established conventional prediction models, general-purpose Vision-Language Models (VLMs), driving-specific VLMs and vision-language-action models. Our experiments reveal three key insights: (i) video backbones reach most of their full-observation accuracy from the first fifth of a maneuver, whereas zero-shot VLMs need most of the maneuver to be observed; (ii) zero-shot VLMs, whether general-purpose or driving-specific, largely remain close to simple baselines on both tasks; a preliminary LoRA study shows that adaptation lifts anticipation sharply but leaves trajectory prediction behind conventional models; and (iii) the rider's own motion drives forecasting difficulty: for every model, including a static baseline, errors are highest during left turns and rise under dynamic ego-motion. We believe MotoVerse will serve as a challenging benchmark for safer and more robust predictive AI for intelligent two-wheelers. The dataset and evaluation code are publicly available at this https URL.

---


### 78. [Who Pays for the Knowledge Models Copy? Model Collapse as Rogers' Paradox](https://arxiv.org/abs/2611.06022)

**<font color=#1a73e8>作者：</font>** Nam H. Le  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generative models trained on the output of earlier models lose knowledge across generations, rare knowledge first. The remedies that work all bring in information from outside the loop, and the theory of model collapse treats that supply as given: a fixed archive, drawn from a fixed distribution. We argue that the supply is the problem, and that cultural evolution has the theory of it. We read model collapse as Rogers' paradox: a population that comes to rely on copying ends up no better off than one that never copied, because copies go stale unless someone keeps learning for themselves. We test the identification in three steps. First, Rogers' model, fitted only to fully synthetic training, predicts to within a few percentage points how much rare knowledge language models, from word trigrams to a pretrained transformer, retain under other mixtures of fresh data. Second, when the world itself changes, a lineage that copies its own past needs more fresh data to keep up the faster the world changes, as Rogers' model says it must and as analyses that assume a fixed target cannot; a lineage that restarts every generation from fixed pretrained weights is largely insulated, because those weights are knowledge that is never copied. Third, we close the loop: when the people who write a model's training data can ask the model instead of finding things out, the supply of fresh data becomes endogenous. At equilibrium, the model is exactly as reliable as it is costly for people to find out for themselves, the population is no better off than without the model, and every increase in the share of model-written text must be paid for by more people learning for themselves. Users who check what they are told and relearn when it is wrong break the paradox. Filters that select plausible text are conformist and accelerate collapse; only checks that carry new information act as critical learning.

---


### 79. [When Every Choice Is Correct: A Causal Study of Numerical Preference in Language Models](https://arxiv.org/abs/2611.06025)

**<font color=#1a73e8>作者：</font>** Hongnian Huang, Hongliang Liu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> When a language model chooses a number between 1 and 30, every integer in the range is valid, yet the model can favor particular answers. We use numerical choice to study how preference is processed across layers and tokens. Perturbation probing and gradient attribution nominate neurons for activation interventions. In a selected Qwen3-4B case, a pre-answer edit changes 17 to 15 while both runs first emit 1. After the edit ends, selective cache and attention-output replacements trace part of its continuing influence on the second digit. Replacing one attention head's output or the other heads' outputs jointly produces similar immediate readout contributions; both interventions restore 17 but have different final log-odds effects on 7 versus 5. Holding later multilayer perceptron (MLP) outputs at their values from the edited run without either replacement reduces this effect gap from 0.119 to 0.0025 nat. Later computation therefore changes how similar local contributions affect the continuation. Retrospective estimates across eighteen contexts capture much of the probability movement but miss the selected answer switch. Prompt tests also separate influence from answer changes: one held-out prompt retains influence without switching, and only one of twelve fresh wordings qualifies for the reader/MLP test; there, joint MLP clamping again reduces the gap between the two reader effects while the answer remains 17. These results use numerical choice as a controlled case for studying persistent state and conditional downstream processing; they do not establish the origin or a complete circuit of natural numerical preference.

---


### 80. [USI-Brain: Enhancing Underwater Spatial Intelligence via Spatial Data-Driven Vision-Language Modeling](https://arxiv.org/abs/2611.06040)

**<font color=#1a73e8>作者：</font>** Zhiliang Zhu, Zhiqiang Zhao, Xie'an Jiang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Underwater spatial reasoning depends on object boundaries and geometric cues that are obscured by scattering, color distortion, and low visibility. Existing underwater resources capture these cues through images, annotations, and depth maps, but provide fragmented supervision for vision-language models. We present a spatial data engine that connects visual appearance with object-level geometry through enhancement, 2D and geometry-assisted question generation, and expert filtering. It produces 4.27M QA pairs across five capability groups. We use this corpus to train USI-Brain and introduce an Underwater Prior-guided Rectifier (UPR) that applies gated corrections to visual features. USI-Bench evaluates the resulting capabilities with 6,525 held-out QA pairs. On its 15 task metrics, USI-Brain and USI-Brain + UPR improve over Qwen3-VL-8B-Instruct by 5.76 and 7.63 points on average, respectively, using signed differences on 100-point scales. Ablations show that geometry-assisted supervision improves depth and ordering by 4.8 and 6.1 points with UPR disabled, while UPR adds 18.0 points in scene description under matched training data. Both variants use raw images at evaluation. Across NautData, UWBench, and MarineEval, USI-Brain achieves the best or joint-best score on 28 of 32 metrics. Model weights and USI-Bench will be released at this https URL.

---


### 81. [Confucius4-R2T2: A Stable-Prefix Streaming ASR Model for Real Real-Time Transcription](https://arxiv.org/abs/2611.06043)

**<font color=#1a73e8>作者：</font>** Daniel Huang, Qi He, Shaoxiong Duan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Streaming speech recognition is increasingly consumed by machines, such as translators and voice agents, that act on each token as it appears. A token that is later revised costs wasted work or a wrong action. In this work, we present Confucius4-R2T2 (short for Real Real-Time Transcription), a stable-prefix streaming ASR model that never modifies its earlier output while maintaining high accuracy and low latency. R2T2 is obtained by post-training Qwen3-ASR-1.7B on 1,500 hours of Chinese and English audio while freezing its pre-trained audio encoder and projector. The adaptation is based on the concept of Longest Stable Prefix (LSP), a new notion that we introduce in this work. We prove that LSP is monotone under the prefix order, consistent with the full-audio output, and maximal among labels that equal a whole earlier output. Learning from LSP labels converts a full-context model into a stable-prefix streaming one without any architectural change. Extensive evaluations show that R2T2 brings streaming recognition close to the base model's full-context quality while delivering stable text with low emission lag. Its gains extend beyond the post-training languages, demonstrating a practical path from full-context ASR to stable streaming. We open-source the model weights and code at this https URL and this https URL.

---


### 82. [RI-Prune: Relation and Information Aware Visual Token Pruning for Multi-Image Vision-Language Models](https://arxiv.org/abs/2611.06047)

**<font color=#1a73e8>作者：</font>** Dongjin Lee, Eunju Lee, Jinhee Jang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large vision-language models (LVLMs) have recently been extended to handle multiple input images, but this extension dramatically increases the visual token budget, making visual-token pruning not merely an efficiency option but a practical necessity. Existing visual-token pruning methods, primarily designed for the single-image setting, rely on attention-derived saliency signals to estimate per-token importance. However, this attention-centric design transfers poorly to the multi-image regime: it causes substantial performance degradation on multi-image benchmarks, suffers from strong positional bias, and loses discriminative attention signals as the number of input images increases. To test whether attention-selected tokens are truly important for multi-image reasoning, we conduct two complementary causal probes Leave-One-In and Leave-One-Deletion, which measure token importance by restoring individual tokens to a zeroed visual sequence or removing them from the full sequence. Attention-based pruners provide only marginal gains over random selection, showing that attention is a weak proxy for visual-token importance in multi-image reasoning. Motivated by this gap, we propose Relation and Information Aware Pruning (RI-Prune), a training-free, attention-free pre-decoder selector for multi-image visual token pruning. RI-Prune scores each visual token using a z-normalized combination of three signals computed from projector outputs: query relevance, cross-image correspondence with compact per-image prototypes, and intra image representativeness. By integrating these signals, RI-Prune performs balanced per-image Top-K selection to preserve information across input images. Across multiple multi-image benchmarks and three LVLM backbones, RI-Prune achieves a stronger trade-off between token reduction and task performance than prior pruning methods, particularly under aggressive token budgets.

---


### 83. [SVGFaith: A Two-Layer Meta-Evaluation of Faithfulness Metrics for Text-to-SVG Generation](https://arxiv.org/abs/2611.06048)

**<font color=#1a73e8>作者：</font>** Guotao Liang, Haitao Zhou, Biao Liu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-SVG systems are commonly evaluated by applying raster-image metrics to rasterised outputs, yet whether these scores capture fine-grained prompt faithfulness remains unclear. We introduce SVGFaith, a two-layer meta-evaluation framework in which the more faithful candidate of each pair is determined by construction or by human judgment. SVGFaith-Diagnostic contains 1,842 controlled contrastive pairs across eight capability axes, split evenly between two directions: two renderings compared against one prompt, and two descriptions compared against one rendering. SVGFaith-Arena contains 1,327 human-annotated comparisons of real generator outputs. On SVGFaith-Diagnostic, CLIP and three other image--text embedding metrics reach at least 0.789 pairwise accuracy on object identity but at most 0.672 on spatial relations and attribute binding, where chance is 0.5. We further introduce SVGFaith-Score, an interpretable pointwise metric. A domain-tuned decomposer turns each prompt into a dependency graph of atomic visual requirements, a visual question answering model scores whether each requirement is satisfied, and a requirement's score is discounted when its prerequisites score low. In addition to the overall score, the per-requirement scores show which requirements are judged unsatisfied and which inherit discounts from their prerequisites. SVGFaith-Score significantly outperforms all nine baselines, including a Qwen3.5-122B-A10B judge, on Arena and in both Diagnostic directions. Code and data: this https URL.

---


### 84. [Reglos: A Self-Evolving Personal Memory Agent with Recursive Self-Improvement](https://arxiv.org/abs/2611.06049)

**<font color=#1a73e8>作者：</font>** Sen Yang, Jiaduo Lin, Zehong Huang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Personal agents draw on past conversations to tailor their responses to each user. Their memory systems store and update what each user says, and coding agents now also rewrite the harness that turns this memory into the model's context. Such patches risk overfitting, because one tested only on the failures it targets can fix those cases and help nowhere else. We present Reglos, a training-free personal memory agent that tests whether harness changes help beyond the failures they were written to fix. Its self-evolving memory adds to each user's append-only record with every conversation, as new preferences supersede old ones and facts can be forgotten. Its harness improves through recursive self-improvement, in which a coding agent proposes patches from failure traces and a critic from a second model family screens each one for benchmark gaming. After the harness is frozen, a fixed evaluator decides which further patches to accept. With the same backbone behind every system, Reglos outperforms state-of-the-art memory systems such as Mem0, MemOS and EverOS, reaching 61.3% and 84.0% on PersonaMem-v2 and LongMemEval-S with Qwen3.8-27B, and 57.5% and 87.2% with GPT-5.6 Luna.

---


### 85. [Adapting Qwen3 to Tajik from 0.6B to 8B: Lower Text Loss Did Not Mean Better Understanding](https://arxiv.org/abs/2611.06062)

**<font color=#1a73e8>作者：</font>** Tohir Saidzoda, Madina Abdusalomzoda, Nasimjon Rajabov 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Small LoRA adapters trained on Tajik news and books lowered Qwen3's Tajik text loss at every size we tried, from 0.6B to 8B, by 0.60 to 1.45 nats per token, but none of them improved Tajik reading comprehension where it can be measured. On Belebele the 1.7B and 8B adapters left accuracy unchanged and the 4B adapter lowered it by 3.7 points; at 0.6B the score rose by 4.2 points but sits near chance and coincides with a change in which answer letter the model prefers, so we do not read it as understanding. At 8B, continued pretraining on about 375 million tokens of raw Tajik text was followed by a Belebele gain of 9.9 points. After a further supervised fine-tuning stage, our main model, e3, is 11.4 points above Qwen3-8B on Belebele; its English MMLU changed by -1.2 points, and a loss larger than 3.3 points is excluded. The same heavy recipe applied to Qwen3-0.6B-Base brought its text loss close to that of the 8B model after books-only pretraining, while its multiple-choice answers stayed near chance and its English MMLU fell by 7.6 points. We report 15 trained models and their 5 starting models from June to October 2025, scored in 2026 on one harness with paired intervals, and we report what went wrong: lost training records, a thinking-mode dataset with almost no reasoning in it, later branches whose training data was never documented, and a 4-bit release that contains no transformer layers.

---


### 86. [UniCompress: From Multi-LoRA Experts to One Compact Model for Edge Intelligence](https://arxiv.org/abs/2611.06075)

**<font color=#1a73e8>作者：</font>** Mingkang Liu, Peipei Jiao, Weiming Meng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Embodied and edge systems increasingly rely on vision-language models (VLMs) to support heterogeneous skills, yet deploying a separate task adapter for each skill while retaining a high-precision backbone creates substantial memory and management costs. We present UniCompress, a deployment-oriented framework that converts multi-task expertise into one compact, adapter-free model. Starting from a consolidated BF16 Qwen3-VL-4B teacher, UniCompress constructs an asymmetric INT2 student using GPTQ initialization and teacher-guided quantization recovery. The approach jointly quantizes and recovers the projection weights in the vision encoder and language backbone, enabling aggressive compression of the complete vision-language model while preserving its multi-task behavior. We evaluate UniCompress on four heterogeneous embodied tasks: posture recognition, household-safety understanding, multimodal dialogue routing, and mobile-GUI action prediction. UniCompress reduces the approximate weight storage from 8.9 GB in BF16 to 2.1 GB in INT2, corresponding to a reduction of approximately 76%. It improves the INT2 macro task score by 34.3 percentage points over GPTQ-INT2 while remaining within 0.9 points of the consolidated BF16 teacher. These results demonstrate the potential of teacher-guided joint vision-language INT2 recovery for deploying a single multi-skill VLM on resource-constrained embodied platforms.

---


### 87. [SleuthVLM: Do We Really Need Audio-in-Video for Omni Video Understanding?](https://arxiv.org/abs/2611.06083)

**<font color=#1a73e8>作者：</font>** Peiran Wu, Fangfei Gou, Zhaoxi Mu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Omni models answer questions about videos by jointly processing sampled frames and audio in one turn, with progress driven largely by scaling model size and omni training data. We ask whether a model needs to hear the audio directly at all, and present SleuthVLM, an agent harness built on a VLM that never hears the audio directly: speech will be transcribed into text, and the VLM will sleuth the video on its own without any predefined workflow. On four omni benchmarks with videos up to 90 minutes, SleuthVLM achieves the best average accuracy: \textbf{75.0%}, 2.6 points above Gemini 3.8 Flash, and it also tops the Video-MME-v2 leaderboard with \textbf{77.8%}; with an open-source 27B VLM, it beats all open-source omni models. We draw three findings: SleuthVLM beats a model that glances; hearing is not the bottleneck, agentic ability is; omni understanding needs better agentic ability, not just more omni data for modality alignment. So we provide a simple but effective starting point for doing omni video understanding. Omni understanding needs better agents, not just bigger models that hear.

---


### 88. [Shallow Encoding Emits Deep Memories](https://arxiv.org/abs/2611.06084)

**<font color=#1a73e8>作者：</font>** Mingyuan Ma, Yangmin Li, Harris Nover 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hybrid language models interleave a few softmax-attention layers with many linear-attention or state-space layers, so every layer keeps a memory of earlier tokens: a key-value cache or a fixed-size recurrent state. Serving them spends more compute and high-bandwidth memory on these memories than the output requires. The prefill runs every layer for every prompt token, and every decode step loads and stores whole recurrent states, which on Qwen3.8-Flash-Next take as many bytes per request as the attention cache of thousands of tokens. We find two properties of trained hybrids that locate this excess. First, writes are easier than reads: writing a deep layer's memory of a token needs little of the deep computation that predicting the next token needs. Trained copies of the deep layers' write paths, which we call emitters, therefore write a prompt's deep memories from the residual stream of a shallower anchor layer, and all prompt tokens but the last run as few as 63% of the layers. Second, recurrent states have a state sink: most of their energy lies in a rank-one term along a fixed direction of each head, and the rest is a low-rank working memory. SEED builds on both: it makes the prefill shallow in depth and the decode state shallow in representation. Each recurrent state is stored as its sink plus low-rank factors, which the Gated DeltaNet, Kimi Delta Attention and Mamba-2 updates extend exactly; we prove that the open-loop error of the periodic compressions back to low rank is bounded independently of their number. SEED keeps the original weights frozen, compresses no attention cache, and runs all layers for every generated token. On six checkpoints of five production hybrids of 30B to over 300B parameters, it is nearly lossless on eleven official exams. Served with SGLang on NVIDIA GB300 GPUs on an agentic-coding trace, it raises the per-GPU throughput of Qwen3.8-Flash-Next 1.2-1.4x.

---


### 89. [GeoBiaset: A Counterfactual Benchmark for Demographic Bias in World-Level Geolocalization](https://arxiv.org/abs/2611.06085)

**<font color=#1a73e8>作者：</font>** Niccolò Niccoli, Silvia Dani, Marco Mistretta 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> World-level image geolocalization is an increasingly important task, yet the biases of current models remain poorly understood. Prior work has identified coarse dataset imbalances noting, for instance, that some cities are absent from training sets and that models tend to perform better in wealthier regions. However, no one has yet examined which visual cues drive these disparities. To do so, we introduce GeoBiaset, the first benchmark designed to measure how geolocalization models are influenced by the apparent race of a person inserted into the image foreground. The dataset consists of 9,541 images, pairing existing geotagged background images with counterfactual edits spanning seven races, holding the ground-truth coordinates fixed. Controlled masking experiments show that occlusion and background drift do not fully explain geolocalization degradation. Alongside the benchmark, we introduce the Person-Origin Perturbation Indicators (POPI), novel metrics that quantify model resilience to these demographic perturbations by measuring whether predictions are pulled toward the region associated with the inserted group. Our evaluation of state-of-the-art geolocalization and multimodal large language models reveals a 16-47% drop in continent-level performance when a subject from a demographically mismatched group is inserted. A landmark versus no-landmark analysis and gradient-weighted heatmaps show that models preferentially attend to geographic landmarks when present, but shift attention to facial features in their absence.

---


### 90. [Overview of the NTCIR-19 SciClaimEval Task: Cross-modal Claim Verification in Scientific Papers](https://arxiv.org/abs/2611.06090)

**<font color=#1a73e8>作者：</font>** Xanh Ho, André Greiner-Petter, Florian Boudin 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper presents an overview of \emph{SciClaimEval}, a pilot task at NTCIR-19 on verifying scientific claims against the tables and figures of the papers in which they appear. Our dataset pairs authentic claims from 180 papers in machine learning, natural language processing, and medicine with contrastive versions of their tables and figures, one supporting the claim and one minimally modified so that it does not. The task comprises two subtasks: deciding whether a piece of evidence supports a claim, and selecting which of two evidence versions does. Twenty-two teams registered, the highest number among NTCIR-19 tasks, and 14 submitted 177 runs. Most systems built on multimodal large language models, relying on prompting and multi-stage inference rather than task-specific fine-tuning. On the first subtask, the best systems reached 98.1\% pair accuracy, but all six top-ranked systems relied on the contrastive pairs; the best system that judged each claim-evidence pair on its own scored 24.3 points lower. Open-weight models, embedded in carefully designed pipelines, matched proprietary ones. Yet verifying a single claim against its evidence, the setting that matters in practice, remains an open problem.

---


### 91. [Reasoning-Trace Overflow in Code Generation: An Empirical Study of Explicit Reasoning Models](https://arxiv.org/abs/2611.06095)

**<font color=#1a73e8>作者：</font>** Lukas Twist, Helen Yannakoudakis, Jie M. Zhang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Explicit reasoning can help language models generate code, but it also introduces a practical risk: the model may spend so much of its output budget reasoning that it never produces usable code. We study this behaviour in relatively small open-weight reasoning models, framing it as reasoning-trace overflow. Across seven models and six code benchmark settings, we measure how much of a fixed 32k-token output budget is spent on reasoning, whether that reasoning improves pass@1, and whether lightweight inference-time controls can mitigate overflow. Our results show that the value of reasoning is highly conditional. Overflow is rare on simpler function-level tasks, but becomes common on harder code-generation benchmarks and for particular model families: on several model--benchmark pairs, more than half of generations exhaust the full 32k-token budget while still reasoning. Most complete overflow is associated with repetitive reasoning loops, although substantial long reasoning also occurs without looping. Disabling reasoning can therefore be competitive for overflow-prone models, simply because it ensures that an answer is produced. At the same time, reasoning remains valuable for stronger models on harder algorithmic and code-understanding tasks. Finally, prompt steering can substantially reduce overflow for some models but is inconsistent, while budgeted transitions provide more direct control and can improve both performance and token efficiency for overflow-prone models. These findings suggest that explicit reasoning should be treated as a controllable resource for code generation, rather than an always-on capability.

---


### 92. [Reconciling Privacy with Provenance for Language Model Watermarks](https://arxiv.org/abs/2611.06100)

**<font color=#1a73e8>作者：</font>** Elise L. Han, Tatsunori Hashimoto  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Watermarking has great potential for regulating the use of language models (LMs), but its deployment has been marred by controversy, as many users argue that fine-grained tracking of LM usage violates their privacy. This tension reduces the effectiveness of watermarks, as users engage in evasion strategies such as paraphrasing that can remove much of the watermark signal. We show that provenance and privacy can be reconciled if we shift the goal of watermark design from tracking individuals to estimating aggregate usage. We develop locally differentially private watermarks which provably limit the evidence that any individual text can contribute to detection, while still enabling accurate estimation of population frequencies. We introduce the Red-Green Sequence (RGS) watermark, a private and computationally efficient watermark that achieves accurate frequency estimation at high privacy levels across various models, sample sizes and generation entropies in settings that reflect realistic deployment scenarios. On C4 language modeling tasks, we attain $0.0019$ MSE with $0.0038$ mean absolute bias at a low $\varepsilon$ of 1, while in more challenging settings such as an essay writing task with only 100 text samples, we still find errors on the order of $0.0113$ MSE with $0.004$ mean absolute bias at $\varepsilon=2$.

---


### 93. [Learning When to Think Aloud in Latent Reasoning](https://arxiv.org/abs/2611.06108)

**<font color=#1a73e8>作者：</font>** Zhehao Zhou, Tongrui Su, Shengyu Zhu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Latent Chain-of-Thought (CoT) reasoning improves efficiency by shifting intermediate computation into continuous hidden states. However, fully latent methods often struggle on precision-critical tasks such as mathematical reasoning, while existing hybrid approaches retain substantial token-generation overhead. We introduce VITAL, an importance-guided hybrid reasoning framework that selectively verbalizes informative tokens as reasoning anchors while keeping most computation latent. A lightweight gating head dynamically selects between explicit token generation and direct hidden-state feedback. VITAL constructs hybrid trajectories from explicit CoT using token- importance estimation and trains the model through curriculum-based supervised training, followed by reinforcement learning with a reward that balances correctness and conciseness. Experiments show that VITAL consistently out- performs existing fully latent reasoning methods, achieving relative average accuracy gains of 9.6% on GPT-2 and 5.1% on Llama-3.2-1B at comparable reasoning lengths. Compared with hybrid baselines, VITAL achieves higher reasoning accuracy with substantially shorter reasoning trajectories on Qwen3-1.7B.

---


### 94. [Beyond Risk Cues: A Mechanism-Level Benchmark and Verifiable Debate for Scam Video Detection on the Web](https://arxiv.org/abs/2611.06110)

**<font color=#1a73e8>作者：</font>** Yifan Wang, Junyu Lu, Shun Zhang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Online scam videos pose significant threats to individuals and society. Existing studies primarily focus on binary classification, offering limited insights into how scams work and the reasoning behind detection decisions. Moreover, they often overlook the challenge of distinguishing scam videos from superficially similar non-scam content, such as advertisements, and the robustness of detection models against misleading arguments. These limitations hinder reliable scam video detection. To address these limitations, we introduce MechScam, a benchmark comprising 6,614 videos covering diverse scam mechanisms and non-scam categories. MechScam provides explanations supported by video evidence, annotations of potential scam elements and their context, and misleading arguments constructed from genuine evidence. Recognizing that genuine evidence can still be used to justify misleading conclusions, we further propose ScamCourt, a debate framework in which trained prosecution and defense debaters present opposing arguments, while a trained judge makes decisions based on a transcript with verified citations. Extensive experiments show that state-of-the-art MLLMs struggle to distinguish scam videos from similar non-scam content. ScamCourt outperforms larger MLLMs and same-backbone fine-tuned baselines, reducing false positives and showing stronger resistance to misleading arguments. Together, MechScam and ScamCourt contribute to more reliable and interpretable scam video detection. The dataset and code are available at this https URL.

---


### 95. [The Harness Is the Model: Agent Scaffolding Changes a Fixed LLM's Compliance with Banking Conduct Rules, Unevenly Across Models](https://arxiv.org/abs/2611.06116)

**<font color=#1a73e8>作者：</font>** Mehmet Murat Huyut  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Banks validate language models, but they deploy systems: a model inside a harness that decides what it sees, which tools it can call and who checks its actions. We test whether that harness changes compliance with banking conduct rules when the model is held fixed. Four open-weight models each ran five harnesses (a pipeline that makes one structured decision, a ReAct-style tool loop, a loop in which the policy is reachable only through search, a loop with a long benign customer memory, and a loop with a same-model compliance reviewer) on 156 pre-registered cases in a simulated retail bank whose 11 rule families paraphrase EU consumer-credit, payments, investor-protection, data-protection and anti-money-laundering provisions. Every one of the 3120 two-turn episodes was scored deterministically from the executed tool trace, with violations and over-refusals counted separately. Pooled across models the harness moved the correct-case rate only between 87.3% and 92.1%, but within a model it mattered a great deal: for one model the spread between its best and worst harness was 11.5 percentage points, enough to move it from first to last place among the four models, while for another the harness made no detectable difference; the model x harness interaction itself was suggestive rather than conclusive. The same-model reviewer cut violations from 9.6% to 6.4% without raising over-refusals, contrary to our pre-registered prediction. Rules that require date arithmetic failed in every harness. In an exploratory analysis with two LLM judges and a blind human check, 26% of violations were accompanied by a customer message that denied the action the agent had just executed, which a transcript-only review would record as a correct refusal. For model-risk management the unit of validation should be the model-harness pair, and conduct testing should read the action log, not the conversation.

---


### 96. [From Handcrafted to Generative: RLVR-Optimized Icon Generation for Alexa+](https://arxiv.org/abs/2611.06123)

**<font color=#1a73e8>作者：</font>** Rohan Sequeira, Matthew Rosenberg, Amin Mahmoudabadbozchelou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Alexa+ devices with screens display animated icons during conversations to visually reinforce what is being said. The original set of these icons was hand-drawn by designers one at a time, a process that produces polished results but is time-consuming and cannot scale to the range of topics encountered in open-ended conversation. We describe an automated pipeline, deployed in production, that generates these vectorised animated icons from a text description alone and surfaces relevant animations to customers based on their ongoing conversation. The pipeline decomposes icon creation into a sequence of stages (image generation, semantic decomposition, vectorisation, styling, and animation). Its quality is determined at the very first of these, image generation, on which every downstream stage depends. We therefore focus on improving this first and most critical stage. Because the icons are rendered on small display canvases under strict design guidelines, generations are often unsuitable for production. Supervised fine-tuning is not viable, as no dataset of line-art icons exists under these constraints. Instead, we design objective verifiers that automatically flag generations violating the design guidelines, and use them to fine-tune a flow matching image generation model via reinforcement learning from verifiable rewards (RLVR). The fine-tuned model raises the pass rate from 15.7% to 58.7% (3.7x) under a VLM judge that is independent of the reward model. Both the trained model and the verifier are deployed in the production pipeline, where the verifier also serves as the automated quality gate before final design review.

---


### 97. [ModalSearcher: Weaving Visual Evidence into Autonomous Cross-Modal Deep Search](https://arxiv.org/abs/2611.06131)

**<font color=#1a73e8>作者：</font>** Zhihan Yin, Ruyi Li, Chengyu Fang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Static and incomplete parametric knowledge limits the performance of multimodal large language models on novel-knowledge and knowledge-intensive tasks, especially those requiring multi-hop evidence acquisition. Existing multimodal agentic search methods often fix visual evidence at the input or a predefined trajectory position, making it difficult for agents to select search modalities as their information needs evolve and to handle complex real-world queries. We define this capability as autonomous cross-modal search: an agent chooses among direct reasoning, text-to-text search, text-to-image search, and reverse-image search, actively introduces visual evidence when appropriate, and switches between and integrates modalities across multiple hops. We propose ModalSearch-Pipeline, a scalable procedure for constructing an interleaved multimodal knowledge graph. It samples paths with diverse depths and modality compositions and uses backward question construction to obscure entity names and image targets that would expose reasoning shortcuts while retaining necessary disambiguating clues, yielding text-only, image-initialized, and arbitrarily interleaved multi-hop problems. We train the ModalSearcher Agent with supervised fine-tuning and reinforcement learning in a live Web environment, and construct ModalSearch-Bench. Experiments show that ModalSearcher-8B improves average accuracy by 16.2 points over Qwen3-VL-8B under the same agentic workflow across five multimodal knowledge-intensive QA benchmarks, with consistent gains on independently constructed active visual-search benchmarks.

---


### 98. [Accelerating Long-Context Decoding in Large-Scale Hybrid LLMs Without Retraining](https://arxiv.org/abs/2611.06133)

**<font color=#1a73e8>作者：</font>** João Eduardo Batista, Emil Vatai, Mohamed Wahib  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The full-attention layers of large language models (LLMs) make every generated token more expensive than the previous one, slowing models down on long-context tasks. Hybrid models reduce this cost by replacing most full-attention layers with linear-attention layers, but the first still dominate decoding at long contexts. We accelerate these remaining layers without any training or weight changes using combined sparse attention: each layer attends to a sliding window of recent tokens, a pinned prefix, and a fixed budget of most relevant tokens in the context. The window size and budget are found on a per-layer basis using a multi-objective search algorithm. Across six hybrid models from three families, from 4B to 397B parameters, the selected configurations preserve their baseline model's accuracy on 21 long-context datasets. Decoding 64k/256k tokens becomes up to 1.26x/2.22x faster on Qwen3.5-4B, 1.20x/2.23x on Qwen3.5-122B-A10B, and 1.16x/2.06x on Ornith-1.0-397B.

---


### 99. [KVGuard: A KV Cache Safety Checker for LLM Serving Systems](https://arxiv.org/abs/2611.06138)

**<font color=#1a73e8>作者：</font>** Jonguk Cheong, Myungbin Hwang, Eulgyu Kim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Modern LLM serving systems manage the KV cache through PagedAttention, a custom GPU allocator that partitions a single CUDA-allocated region into fixed-size physical blocks and maps each request to those blocks through a CPU-built block table. This block-based design exposes a previously unstudied class of memory safety bugs in the KV cache, including double-free, use-after-free, out-of-bounds access, uninitialized read, and permission violation, which silently corrupt outputs or break request isolation without ever crashing the system. Existing memory sanitizers cannot detect them, because they reason about CUDA-level addresses rather than KV cache blocks, requests, and block tables, and their redzone- and quarantine-based designs do not fit the scarce GPU memory budget of LLM serving. This paper presents KVGuard, the first systematic memory-safety abstraction for KV cache management in LLM serving systems. KVGuard maintains a compact shadow block for each physical KV block, recording per-request permission and per-entry initialization, and uses this metadata to perform five safety checks across the PagedAttention workflow, spanning CPU allocation, block table construction and translation, and GPU-side block table lookup and KV entry access. Each check fires at the boundary that introduced the violation, enabling early detection during development rather than reporting downstream output corruption many requests later. A prototype of KVGuard on vLLM and SGLang covers all 29 historical real-world KV cache safety bugs collected from the two systems' patch histories. KVGuard further found 8 previously unknown safety violations while reporting no false positives. It adds 3.0% and 7.4% geomean TPOT overhead on Qwen 2.5 14B on vLLM and SGLang and at most 0.11% of the KV cache in memory overhead, two orders of magnitude below NVIDIA Compute Sanitizer on the same workloads.

---


### 100. [SafeStart: Mitigating the Overlooked Safety Cost of Active Expert Reduction in MoE LLM Serving](https://arxiv.org/abs/2611.06147)

**<font color=#1a73e8>作者：</font>** Erfan Baghaei Potraghloo, Saeid Shokoufa, Seyedarmin Azizi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Mixture-of-Experts (MoE) language models send each token through a few of many expert subnetworks. Serving methods make these models faster by running even fewer experts per token, and they are validated on accuracy benchmarks. We show that these methods can weaken the model's refusal of harmful requests, and we introduce SafeStart, which largely restores refusal while keeping most of the speedup. In vLLM on one RTX A6000, keeping about two thirds of the selected experts speeds up offline decoding by 15 to 28% at batch size 8. We find that, at this setting, under a jailbreak that tells the model not to refuse, the share of harmful requests that the model answers rises by 18.4 percentage points on Qwen1.5-MoE, 9.5 on OLMoE, and 6.6 on DeepSeek-V2-Lite, the three of nine models where it rises significantly, while MMLU accuracy drops by less than two points. We discover that most of this increase arises while the model processes the prompt and generates its first few tokens. SafeStart therefore runs all experts for the prompt and the first eight generated tokens, and the reduced set of experts afterwards, through a fused kernel in vLLM. With experts removed, SafeStart keeps at least 85% of the offline decode speedup at batch sizes 8 and 32 and brings the change under this jailbreak to between -2.1 and +1.3 points for three expert-reduction methods on these three models. On 889 held-out requests, in an analysis fixed before generation, truncation raises harmful compliance by 5.8 to 21.4 points, and SafeStart leaves a rise of 0.6 to 2.6 points, non-inferior to the original model on two of the three models. Our results show that faster MoE serving need not cost safety: a serving system can keep most of the gain from running fewer experts by running all of them at the start of each response, and it should test refusal, not only accuracy, before it enables such a method.

---


> [!TIP]
> 当前位于：**51-100**（第 2/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-207](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
