# 🧠 大模型相关研究 | 2026年10月23日

> 本类共 **204** 篇论文：已确认 **192** 篇，待复核 **12** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**101-150**（第 3/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-204](./part-05.md)

---

### 101. [Signals and Queries: Token-Efficient Agentic Context Discovery](https://arxiv.org/abs/2610.29326)

**<font color=#1a73e8>作者：</font>** Yam Marcovitz  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> User-facing LLM agents must identify which behavioral policies apply at each turn, but evaluating every policy with an LLM is costly. We introduce Signals and Queries (S&Q), a lightweight first-stage relevance filter developed for Parlant 4.0 that removes at least 30% of candidate policies before downstream evaluation while preserving high recall. For each policy, an LLM generates activating examples and hard negatives offline. An independent logistic classifier trained on their embeddings then predicts relevance using embeddings and vector dot products, with no per-turn LLM calls. This shifts expensive relevance evaluation to a smaller candidate set, while allowing each policy's classifier to be updated independently. Evaluated against 9,144 LLM-judge relevance labels covering 254 $\tau^2$-bench conversation prefixes and 36 airline policies, S&Q achieves higher precision than top-K and cosine-threshold retrieval at every evaluated recall level, with consistent results across two embedding providers. These findings support inexpensive, per-policy classification as a practical first stage for reducing downstream evaluation workload in customer-facing agents.

---


### 102. [Seeing the Forest for the Trees: Emergent Agreement from Individual Conversations](https://arxiv.org/abs/2610.29328)

**<font color=#1a73e8>作者：</font>** Adi Simhi, Yaniv Nikankin, Jonathan Herzig 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As LLM agents interact in the wild and shape each other's decisions, understanding how they converge toward agreement becomes important. We study this in multi-turn conversations where two LLMs discuss subjective matters, can agree or disagree, and may change their stances. Using a linear classifier on individual conversation activations, we identify an internal representation of agreement. We find that it varies substantially across turns and conversations and does not reliably track external agreement at the individual conversation level. We therefore move beyond the representation of agreement in individual conversations, by aggregating the agreement representation across conversations. Externally, this aggregate view reveals a simple structure: when pooled across conversations, agreement can be predicted well with a Markov process, with agreement at each turn being a direct function of agreement at the previous turn. Similarly, when internal agreement is aggregated, it couples with the external Markov agreement through a power-law mapping, exposing Markovian dynamics in internal representations. Additionally, we find that after a change of stance, models express agreement externally before their internal representations reflect the same shift. These results reveal a joint structure between internal and external agreement that emerges only when internal features are aggregated across conversations. Code available at this https URL.

---


### 103. [AgentMonopoly: Behavioral Patterns and Persona Control in LLM Agents](https://arxiv.org/abs/2610.29330)

**<font color=#1a73e8>作者：</font>** Changshun Wu, Mengyu Li, Mathis Marsault 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> How do LLM agents' strategies differ, and how much can instructions to adopt a persona change their behavior over a game? We study these questions with AgentMonopoly, an environment where agents communicate, buy and trade properties, and make decisions that affect later turns. We compare models from four families, each at two sizes, in games with identical models, different sizes of the same family, or different families. We also assign one agent a persona, a description of how it should behave, intended to change a tendency observed in games without that persona. The tested models differ in how often they trade, waive rent, and manage cash and properties. Larger models do not consistently win more games. Persona instructions change the words agents use and some of their actions, but the changes do not always match the role across all decisions. These results show why persona following should be assessed through actions and outcomes as well as language. As our findings are conditional on the tested checkpoints, prompts, and five seeds per configuration, the open-source nature of AgentMonopoly provides the experimental infrastructure for further extending these comparisons. Our code is available at this https URL.

---


### 104. [From Prompts to Posteriors: Can LLM Agents Perform Bayesian Inference in Context?](https://arxiv.org/abs/2610.29331)

**<font color=#1a73e8>作者：</font>** Linus Filbry, Luckeciano C. Melo, Yarin Gal  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly applied across the scientific discovery pipeline, from synthesizing literature to generating hypotheses to informing experimental design. A unifying principle behind these tasks is the need to continuously update beliefs as evidence accumulates, for which Bayesian inference provides a natural framework. However, existing work assumes that LLMs cannot carry out principled Bayesian belief updating in context, instead relying on simplifications and heuristics. To challenge this assumption, we present a principled evaluation of Bayesian reasoning capabilities in LLMs, analyzing both the model's internal consistency as well as its ability to recover an externally determined posterior. Specifically, we build an evaluation framework spanning qualitative epistemological examples to probe probabilistic coherence, quantitative benchmarks of Bayesian inference capabilities, and analyses of the impact of non-Bayesian updates on downstream task performance. Across different scenarios, we find that LLMs generally violate Bayes' rule when updating their beliefs in context. However, when equipped with modern reasoning abilities and code execution capabilities, their performance drastically improves, enabling even the close approximation of analytically intractable posteriors. Our evaluation shows that current LLMs with access to appropriate tools could already be used to make complex belief updates in scientific discovery, enabling rapid acceleration of the efficiency and scale of AI-powered scientific discovery.

---


### 105. [Benchmarking and Error Analysis of Deep Search and Deep Research LLM Agents](https://arxiv.org/abs/2610.29346)

**<font color=#1a73e8>作者：</font>** Zixuan Yu, Zhenheng Tang, Xiaowen Chu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As Large Language Models (LLMs) evolve into autonomous Deep Search and Deep Research Agents capable of executing long-horizon, multi-step tasks, evaluating their reliability becomes increasingly critical. However, existing evaluation paradigms predominantly focus on final task outcomes, leaving a significant gap in understanding the intermediate execution traces, where agents are highly susceptible to various errors. To address this critical gap, we introduce a comprehensive methodology and analytical framework designed specifically to diagnose errors in intermediate workflows. Building upon this framework, we establish a structured taxonomy that categorizes these vulnerabilities into two primary dimensions: System-Level Errors and Task-Level Errors. Through a systematic examination of step-by-step execution traces and agent-environment interactions, we reveal how these underlying errors affect overall performance. Finally, through empirical experiments and systematic analysis of the identified error types, we provide actionable design guidelines, aiming to enhance the robustness, reasoning capabilities, and reliability of Deep Search and Deep Research agents.

---


### 106. [Data Schedules and Learning Rate Schedules Should Be Designed Together](https://arxiv.org/abs/2610.29348)

**<font color=#1a73e8>作者：</font>** Haodong Wen, Kairong Luo, Tingkai Yan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mid-training (MT) is a training phase in LLM training pipelines that continues pretraining (PT) on smaller datasets of higher value. Taking the PT and MT phases as a whole, training usually starts with only PT data and then transitions completely to MT data. In this work, we view this complete transition from PT to MT data as a special case of a broader class of data mixing schedules that specify how the proportions of PT and MT tokens in each batch change over training. Under fixed total training compute and MT token budgets, we ask: Is this complete transition to MT data optimal for minimizing final MT loss? We show that the answer depends on the learning rate (LR) schedule: one data schedule may outperform another under one LR schedule, but changing only the LR schedule can reverse the outcome. Specifically, when the LR decays throughout continued training, introducing MT data earlier and mixing it with PT data lowers the final MT loss compared with placing all MT data at the end of training, but this result is reversed if we use constant LR. We therefore study how to jointly choose when to introduce MT data and when to decay the LR through ablation studies, and find that it is better to decay the LR only after MT data enters training. Finally, we develop a theoretical model that explains why the optimal data schedule for a fixed MT token budget depends on the LR schedule.

---


### 107. [B-CARE: Blind Classwise Assessment of Relative Evidence for Stance Error Ranking](https://arxiv.org/abs/2610.29350)

**<font color=#1a73e8>作者：</font>** Meysam Sabbaghan, Doina Caragea  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Stance classifiers make errors that can be costly to identify under limited human-review budgets. Prioritizing potentially incorrect predictions remains challenging, particularly across heterogeneous base models. We introduce B-CARE (Blind Classwise Assessment of Relative Evidence for Stance Error Ranking), a prediction-blind framework for identifying high-risk stance predictions. Given only a target and text, a fixed LLM verifier assigns ordinal evidence scores to all candidate stance labels without observing the base model's prediction or confidence. B-CARE constructs a comparative risk score by contrasting the strongest alternative-class evidence with the evidence supporting the predicted class. The resulting classwise evidence profile can be reused across multiple base models without training a separate error detector or calibrating risk scores. We evaluate B-CARE on four stance benchmarks and three heterogeneous base LLMs, covering 12 dataset-model settings and 5,206 unique test instances. Evaluation includes error-ranking discrimination (AUROC and AUPRC), selective prediction (E-AURC), and review effectiveness (ErrorCapture at fixed review budgets). B-CARE achieves a mean AUROC of 0.735 and a mean AUPRC of 0.524, capturing 41.06% of errors within the highest-risk 20% of predictions. Although B-CARE does not uniformly outperform strong confidence-based baselines, it provides a reusable, complementary evidence signal for prioritizing potentially incorrect stance predictions across heterogeneous models.

---


### 108. [GaP-MoE : Explicit Expert Specialization in Mixture-of-Experts via Orthogonal Gradient Accumulation and Projection](https://arxiv.org/abs/2610.29355)

**<font color=#1a73e8>作者：</font>** Donghyun Jeong, Yoon-Yeong Kim  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sparse Mixture-of-Experts (SMoE) models improve scalability by routing input tokens to only a subset of expert networks, but they often suffer from representation collapse, in which multiple experts converge toward similar functions and lose their intended diversity. Prior work has addressed this limitation either by improving router architectures or by introducing auxiliary loss terms that implicitly penalize similarity among experts. However, router-based approaches remain vulnerable to routing collapses, and loss-based approaches can conflict with the task's original objective during optimization. In this work, we propose GaP-MoE (Gradient Accumulation and Projection in MoE), which induces expert specialization by directly manipulating expert output gradients rather than modifying the loss function. At each training step, GaP-MoE stochastically selects one of the $TopK$ routed experts as a leader based on normalized routing scores, and projects the gradients of the remaining follower experts onto the orthogonal complement of the subspace spanned by the leader's recent gradients. This removes directional overlap between expert gradients without altering the task loss, allowing specialization to emerge as a direct consequence of the optimization dynamics rather than an externally imposed constraint. We evaluate GaP-MoE in both fine-tuning settings (BERT-based, on GLUE) and from-scratch pretraining settings (GPT-2-based, on WikiText-103, enwik8, and text8), and further confirm its compatibility as a drop-in module for existing SMoE architectures. Experimental results show that GaP-MoE achieves performance comparable to or better than standard SMoE.

---


### 109. [Reading the Mask: Descriptor-Grounded BI-RADS Rationale Generation for Breast MRI Segmentation](https://arxiv.org/abs/2610.29358)

**<font color=#1a73e8>作者：</font>** Hrishikesh Singh, Aarti Sharma, Divyanshu Kumar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep learning based models accurately delineate tumours on dynamic contrast-enhanced MRI (DCE-MRI), but segmentation masks alone do not provide the rationales or reasoning used by radiologists to assess the lesion suspicion. This limits the explainability as well the clinical integration. We investigate whether clinically relevant descriptors can instead be derived from the segmentation masks and their dynamic contrast-enhancement series. We have used Breast Imaging Reporting and Data System (BI-RADS) guidelines as a structured framework. Using these guidelines we designed a BI-RADS decision tree with eight quantitative measurements using radiomics, together with the lesion size and component count, that determine the descriptors at eight nodes. Using these descriptors we generate natural-language rationale using a large language model. The model was constrained to express only the derived records from the decision tree. After applying this framework to the expert and automatic masks of each of the 1,506 cases in the MAMA-MIA dataset, we generated a reproducible corpus of 3,012 BI-RADS grounded rationales. We obtained a faithfulness score of 99.98% and a counterfactual accuracy of 99.3%, indicating that the generated rationales faithfully verbalises the measured descriptors and correctly reflects changes in the underlying record. Agreement between the descriptors from expert and automatic masks falls from 0.832 to 0.549 as mask quality falls from Good to Missed. The generated rationales are intended as draft representations for radiologist review and final sign-off rather than autonomous clinical reports.

---


### 110. [Right On Q: Recovering Reasoning under Quantization via Self-Generated Trajectories](https://arxiv.org/abs/2610.29378)

**<font color=#1a73e8>作者：</font>** Boyuan Zheng, Jing Xiong, Chenwei Wu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Quantization-aware training (QAT) aims to recover reasoning capabilities in low-bit large language models (LLMs). Existing recipes typically supervise the quantized student with the original full-precision model on fixed response sequences. However, the resulting low-bit quantized models still struggle on long-horizon reasoning tasks and often fail to terminate within a token budget that suffices for the full-precision model. We identify two challenges in closing this gap. First, fixed-response supervision leaves a mismatch between training prefixes and those encountered during student generation, and this trajectory divergence grows as responses lengthen. Second, on its own prefixes, the student underpredicts some next-token candidates and overpredicts others, and this distributional misalignment becomes more frequent at high-entropy prefixes. We present OnQ, a low-bit recovery pipeline that combines on-policy distillation and candidate-wise Dynamic KL. Starting from block-wise calibration, the quantized student generates responses and receives full-precision teacher supervision on its own prefixes. Dynamic KL weights forward and reverse KL by each candidate's teacher-student probability ratio to balance correction of under- and overprediction. Across Qwen3-1.7B, 4B, and 8B at 2- and 3-bit precision, OnQ achieves the highest nine-benchmark average, with the largest gains on long-horizon reasoning benchmarks. At 2 bits, it outperforms every baseline on every benchmark at every model size, improving the Qwen3-8B average by 10.26 points over the strongest baseline. It also produces shorter responses with fewer truncations and repetitive errors.

---


### 111. [Where AI Vulnerability Discovery Harnesses Go Quiet: Structural False Negatives and Hidden Vulnerabilities](https://arxiv.org/abs/2610.29379)

**<font color=#1a73e8>作者：</font>** Gadi Evron  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLM-based vulnerability discovery harnesses can miss real, reachable vulnerabilities because of how the harness around the model is built. Steps that select code, filter it, and store and merge findings can drop a vulnerability before or after the model runs, independently of the model's capability, and the report usually gives no sign that this happened. These drops come from engineering choices, and errors. They leave vulnerabilities undetected, and an attacker who knows the harness's rules can also use them to hide a vulnerability on purpose. Understanding these drops shows how to build harnesses that fix or disclose them and are harder to evade. Starting from the two harnesses we maintain, Knostic's OpenAnt and raptor, and then examining 10 additional open-source harnesses, we mapped 13 points where such drops occur and organized them into a taxonomy. Using each harness's own code, we show a single file that six harnesses dropped before their model saw its code, five of them without notice. We propose engineering failure patterns mapped to these drops, and relate them to Ptacek and Newsham's work on intrusion detection evasion. The paper also covers content-steered verdicts and prompt injection, and gives design principles and tests for harnesses that report accurately what they analyzed. The reliability findings likely apply to other LLM harnesses, beyond vulnerability research and application security, and the evasion findings apply wherever an attacker can write or influence the code being checked. We also argue that harnesses built to be descriptive can, in effect, be prescriptive. Rules written to describe typical code and typical model replies end up deciding what is analyzed, and anything that does not conform is treated as absent or as "no vulnerability."

---


### 112. [Parallelizable Probabilistic Latent Reasoning for Diverse Reasoning Trajectories](https://arxiv.org/abs/2610.29385)

**<font color=#1a73e8>作者：</font>** Seokhyun Lee, Seongjun Lee, Changhee Lee  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Language models relying on verbalized Chain-of-Thought (CoT) are constrained to token-by-token generation in the language space, where many tokens serve textual coherence rather than core reasoning. This entangles genuine differences in logical trajectories with superficial variations in verbalization. Moving reasoning into a compact, continuous latent space offers a promising alternative for efficiently representing and exploring diverse reasoning trajectories. However, current latent models remain largely deterministic, capturing only a single reasoning trajectory rather than modeling a distribution over multiple valid alternatives. While stochastic approaches parameterize distributions over latent reasoning steps, they frequently suffer from unstable optimization and limited empirical performance. Furthermore, their reliance on autoregressive latent prediction during training precludes effective parallelization, leading to prohibitively long training times. To overcome these bottlenecks, we propose Probabilistic Latent Reasoning Models (PLRM), a parallelizable variational framework for probabilistic latent reasoning. PLRM adopts a JEPA-style objective in which the posterior infers latent distributions in parallel from observed reasoning trajectories, while the prior learns to predict the subsequent latent distribution via teacher forcing. To model heterogeneous reasoning processes, we introduce a discrete strategy variable together with a mixture-based prior, allowing the model to preserve the Gaussian-mixture structure induced by multiple distinct reasoning trajectories rather than collapsing them into a single Gaussian. Across diverse benchmarks, PLRM achieves performance competitive with deterministic latent reasoning models on single-trajectory datasets while enabling efficient training and consistently outperforming competing stochastic baselines on multi-trajectory datasets.

---


### 113. [Nominate-then-Adjudicate: LLM-Assisted One-Pass and Per-Instance MIP Solver Tuning](https://arxiv.org/abs/2610.29391)

**<font color=#1a73e8>作者：</font>** Yifan Zhao, Qianyang Zhao, Xinyu Guan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mixed-integer programming solvers expose hundreds or even thousands of parameters whose best setting varies per instance, yet per-instance search is prohibitively expensive. We frame this as configuration for heterogeneous Big Data optimization workloads and propose a nominate-then-adjudicate pipeline built around two design choices. First, a fixed portfolio is sampled once and reused across instances, removing per-instance configuration search at inference; on the evaluated families, the resulting shortlist retains substantial oracle headroom, making selection within it the empirical focus. Second, the fixed 20-feature representation can map structurally different instances to the same vector, preventing a feature-only selector from distinguishing them even when they prefer different configurations. The foundation model receives no task-specific weight updates, and selection is one-pass: one model call and no solver calls at inference. The study represents structural Variety through distinct formulation families and decision Value through solver-performance outcomes; the one-call, zero-solve protocol specifies the decision interface and leaves end-to-end latency unmeasured. Among comparisons exceeding a 20% practical-difference threshold, the complete adjudicator records 538 wins and 185 losses against the top nominee, while its win rate against the default rises from 84.9% to 90.2%. Against per-instance configuration baselines under a matched one-pass protocol it leads the cluster-level methods and the best-performing evaluated per-instance baseline, ISAC+.

---


### 114. [CertMoE: Robustness Certification for Mixture-of-Experts LLMs via Routing-Aware Smoothing](https://arxiv.org/abs/2610.29395)

**<font color=#1a73e8>作者：</font>** Qingyue Wang, Yudong Gao, Lixia Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Provable robustness is a cornerstone of trustworthy machine learning, aiming to guarantee model predictions under adversarial perturbations. Existing certification frameworks, inspired by abstract interpretation or symbolic execution, typically assume a fixed computation graph, where input perturbations or variations affect only model outputs but not the underlying execution path. This assumption, however, is violated in Mixture-of-Experts (MoE) Large Language Models (LLMs), whose input-dependent routing induces discrete and dynamic execution paths. Crucially, this dynamic computation changes the certified object from a single fixed function to a composition of input-dependent sub-functions, leading to unreliable certification guarantees.
This paper presents \textsc{CertMoE}, the first routing-aware robustness certification framework for MoE LLMs, which explicitly accounts for input-induced routing dynamics in certification. Specifically, we introduce a relaxed routing-containment criterion, which certifies that perturbed Top-$K$ routing is contained within a larger certified expert pool. Based on this guarantee, \textsc{CertMoE} then constructs the corresponding induced sub-network and certifies its prediction consistency. This hierarchical certification procedure yields a joint probabilistic guarantee over routing containment and sub-network robustness, providing sufficient conditions under which the original prediction remains invariant. Extensive experiments across recent MoE LLMs demonstrate that dynamic routing makes certificates issued by existing methods frequently violated, while \textsc{CertMoE} reduces the empirical violation rate with routing-aware guarantees, e.g., from more than $30\%$ to $0$, yielding certificates that more faithfully reflect the robustness of MoE models.

---


### 115. [VideoGen Model 1: Prompt Expansion Versus Formatting in Audiovisual Generation](https://arxiv.org/abs/2610.29407)

**<font color=#1a73e8>作者：</font>** David Grossman, Anton Koenig  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Creative prompt expansion improved overall audiovisual quality scores over raw prompts in a controlled pilot of VideoGen Model 1, our post-trained version of MiniMax H3. We compared the raw, reformatted, and expanded versions of 30 prompts, holding the generator, seed, and sampling settings fixed. Each clip was rated separately on five dimensions. Their mean formed an overall score on a 1-10 scale. Compared with formatting alone, overall scores increased by 0.63 points (95% interval: [+0.11, +1.15]) under VA-Judger and 0.15 points (95% interval: [-0.03, +0.35]) under Gemini 3.8 Flash, whose overall change remained uncertain. Prompt-alignment scores increased by 0.97 points under VA-Judger and 0.50 under Gemini. VA-Judger also showed higher audio quality; visual-quality ratings changed little under either judge.

---


### 116. [LLMSeg: Training-Free Text-Prompted Image Segmentation with B-Splines](https://arxiv.org/abs/2610.29409)

**<font color=#1a73e8>作者：</font>** Abdullah Hamdi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Promptable segmentation models such as SAM 3 achieve remarkable open-vocabulary performance but require dedicated architectures, large-scale annotation engines, and task-specific training. We ask a different question: can a general-purpose multimodal large language model (MLLM) segment images directly, without an added segmentation head, mask decoder, or training? We present LLMSeg, a training-free pipeline that turns a vision-capable LLM into a text-prompted image segmenter. LLMSeg decomposes segmentation into three LLM-driven stages. First, detect localizes all instances matching a free-form text query and describes their coarse morphology. Next, segment traces each instance using closed periodic B-splines confined to its detected box. These splines define an outer boundary and optional hole loops. Finally, refine iteratively proposes focus boxes around residual errors and retraces confined splines. The process ends when the mask stabilizes or the pass budget is exhausted. The output is a binary mask with inspectable intermediate geometry. We evaluate LLMSeg across ten referring and reasoning segmentation splits (ReasonSeg and RefCOCO/+/g). We also evaluate open-vocabulary instance segmentation (LVIS, COCO, and SA-Co), semantic segmentation, and zero-shot detection (ODinW13 and RF-100VL). With an off-the-shelf Gemini-3.7-Flash backend, LLMSeg is competitive with and often surpasses the specialist SAM 3 model on identical items. It reaches 71.5 cIoU on ReasonSeg val without additional segmentation-specific training. Backend model updates can improve accuracy without retraining the pipeline. The code is available at this https URL .

---


### 117. [ECHO: Emergent Common-Mode Hidden Offsets Drive Vocabulary Collapse in Preference Optimization](https://arxiv.org/abs/2610.29410)

**<font color=#1a73e8>作者：</font>** Yun Li, Ehsan Javanmardi, Simon Thompson 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Preference optimization can improve every ranking metric while building a hidden, shared representation shift that the relative loss barely sees, one that can eventually destroy generation. We trace this failure to the common-mode offset, a shared directional shift in the model's hidden states that appears across token positions, prompts, and both chosen and rejected responses. Because it moves chosen and rejected representations together, the relative ranking loss barely reacts to its accumulation. As this offset grows, it projects onto the output layer to form a vocabulary well, elevating a single token's probability until it dominates decoding and causes generation collapse. The isolated offset alone reconstructs the vocabulary well, injecting the learned offset into an untreated base model recreates the collapse where norm-matched random directions do not, and masking this common component from the loss prevents the well in our flagship setting. Under the per-token ranking loss we study, the same collapse appears in 14 of 17 base-model lineages and under full-parameter fine-tuning. Moreover, the offset is not merely an artifact of collapse, since it is already present in textbook DPO and SimPO runs that form no well. Textbook DPO keeps it weakly aligned with any single vocabulary direction even with three times our base budget. Trained from base models for that budget, however, full-parameter SimPO drives it into collapse on both Llama-2 and Llama-3.1, and the same kind of offset grows, without a well, from a public SFT checkpoint under the official SimPO recipe. Across 17 UltraFeedback runs, the better a run ranks held-out responses, the less often two public reward models prefer its samples to the base model's. These findings expose a blind spot in standard ranking metrics and introduce a representation-level signal that can warn of generation collapse before it occurs.

---


### 118. [BIRD-RL: Scaling Agentic Reinforcement Learning over Stateful Data-Centric Environments](https://arxiv.org/abs/2610.29426)

**<font color=#1a73e8>作者：</font>** Ge Qu, Jinyang Li, Xiaohan Xu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While agentic reinforcement learning (RL) has emerged as a promising paradigm for training small language models (SLMs), existing frameworks are predominantly tool-centric and struggle with data-centric environments. Specifically, applying tool-centric frameworks to stateful tasks like SQL debugging introduces severe spatial inefficiencies since proper environment isolation typically requires a separate database container per rollout. Naively reusing databases without tracking evolving states across multi-turn interactions causes trajectory contamination and cross-trajectory interference, which severely destabilizes policy updates. To overcome these bottlenecks, we introduce BIRD-RL, a novel four-stage agentic RL curriculum that alternately enhances foundational agent reasoning and trajectory-adaptive on-policy exploration to circumvent the instability inherently associated with direct end-to-end learning. Crucially, to support this curriculum, BIRD-RL is driven by a Trajectory-scoped Persistent Execution Infrastructure, which enables safe database replica reuse while preserving trajectory isolation. This design improves spatial RL efficiency by 12.8x, successfully enabling scalable agentic RL for complex data-centric tasks without needs of Kubernettes. Empirical evaluations on the BIRD-CRITIC-SQLite benchmark demonstrate that our 7B and 14B models achieve Success Rates of 44.40% and 48.00%, respectively, showing competitive performance against strong proprietary model-based agents such as Claude-Opus-4.6 Agent (48.20%). Furthermore, BIRD-RL successfully trains unified SLMs capable of both advanced SQL debugging and generation, highlighting its broader potential for multi-objective optimization across heterogeneous, real-world data-centric tasks.

---


### 119. [One Act, Many Masks: Effect-Marginal Policy Optimization for Long-Horizon Agents](https://arxiv.org/abs/2610.29427)

**<font color=#1a73e8>作者：</font>** Shaojin Ma, Ruitao Wang, Pengyi Li 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent advances in multi-turn reinforcement learning (RL) have substantially improved the performance of LLM agents on complex, long-horizon interactive tasks. However, despite progress in fine-grained credit assignment, policy optimization still applies these learning signals through response-specific probability ratios. Different textual responses can induce the same executable effect, yet credit differences arising from subsequent outcomes remain tied to their individual textual realizations. We identify this mismatch as credit-update misalignment. Our analysis reveals that credit-text pairing directly shapes policy-update directions, even when the policy context and executable effect are held fixed. Motivated by this finding, we propose Effect-Marginal Policy Optimization (EMPO), which aligns policy optimization with execution-level equivalence through an effect-level surrogate that couples updates across alternative textual realizations. EMPO preserves the original credit signals, integrates with both trajectory-level and step-level credit estimators, and requires no additional critics or rollouts. Experiments on ALFWorld, WebShop, and Sokoban show that EMPO outperforms strong baselines in both task performance and learning efficiency.

---


### 120. [DynaWeave: Learning to Adapt through Dynamic Scenario Synthesis](https://arxiv.org/abs/2610.29443)

**<font color=#1a73e8>作者：</font>** Xuan Yang, Chunxiao Liu, Hongsheng Xin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents increasingly use tools to complete tasks in stateful environments. However, many training environments remain largely static apart from changes caused by the agent's own actions, whereas external events introduced by other users, services, or sudden contingencies in real environments can invalidate ongoing plans. To address this gap, we introduce DynaWeave, an automated synthesis framework that transforms existing static tasks into verifiable dynamic scenarios. The framework generates exogenous events relevant to each task, covering changes in task requirements, environment state, and external information. It uses directed acyclic graphs (DAGs) to represent dependencies between events and an execution engine to activate them during agent interaction. A dynamic verifier revises only the evaluation checks affected by events that actually occur and retains all other checks. Using DynaWeave, we collect 2,095 verified interaction trajectories across 36 environments and use them for supervised fine-tuning of Qwen3.5 models. Experiments on Gaia2, CostBench, and ToolMaze show that DynaWeave achieves consistent improvements in overall performance across all three evaluated model sizes, increasing the task completion rate on CostBench by 67.34 percentage points and even exceeding the performance of Gemini-3.1-Pro-Preview on ToolMaze. These results support dynamic scenario synthesis as a practical approach to training agents to adapt to changing environments. Our code is available at this https URL.

---


### 121. [Omnilingual-MsASR: Benchmarking Multimodal, Multilingual, Long-Form Multi-Speaker ASR of Omni Large Language Models](https://arxiv.org/abs/2610.29455)

**<font color=#1a73e8>作者：</font>** Yuan Ge, Pei Zhang, Xize Cheng 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Omni-modal large language models (LLMs) have achieved remarkable progress in audio and video understanding. However, existing models struggle with long-form, multi-speaker videos, especially in understanding the entire video and recognizing who says what and when. To characterize the capability limit of current omni LLMs and guide future model development, we introduce Omnilingual-MsASR, a multilingual, multimodal benchmark for long-form Multi-speaker Automatic Speech Recognition (MsASR) covering six languages, recordings up to 30 minutes, and scenarios with up to 20 speakers. Omnilingual-MsASR provides parallel audio and video inputs to evaluate models' cross-modal consistency and their ability to exploit complementary cues across modalities. Extensive evaluations of leading omni-modal LLMs reveal substantial performance bottlenecks, while their tcpWERs frequently exceed 100%. These findings highlight fine-grained temporal localization, speaker disambiguation, and cross-modal synergy as key challenges for future omni-modal foundation models. Our work is available at this https URL.

---


### 122. [Harness Scaling for Generalizable Agentic Reinforcement Learning](https://arxiv.org/abs/2610.29458)

**<font color=#1a73e8>作者：</font>** Fei Bai, Huatong Song, Chuan Hao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Agent harnesses have become a central component of modern agentic systems, shaping how models use tools, manage context, and coordinate long-horizon interaction. Realizing the benefits of these harnesses depends on how effectively the underlying model can make use of them, motivating reinforcement learning directly through the harness. However, existing approaches typically train through a single fixed harness, which can lead to specialization and limited transfer across harness configurations. To address this, we introduce \textbf{Harness Scaling}, a new scaling dimension for agentic RL that extends training from a single harness to diverse execution configurations. Concretely, we construct a factorized harness space, select a compact training subset with balanced factorial coverage, and organize cross-harness training to combine global coverage with controlled variation for the same task. Across multiple benchmarks, model scales, and RL algorithms, Harness Scaling consistently improves generalization to unseen white-box configurations. Moreover, models trained through structured white-box variation transfer effectively to unseen external black-box harnesses, outperforming models trained through a single complex black-box harness. These results establish harness diversity as a meaningful scaling dimension for agentic RL and highlight the importance of how this diversity is organized for cross-harness generalization.

---


### 123. [OmniSimulator: Aligning Small Language Models for Authentic Heterogeneous Behavior Modeling](https://arxiv.org/abs/2610.29472)

**<font color=#1a73e8>作者：</font>** Jiawei Chen, Ruoxi Xu, Boxi Cao 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have shown great potential as general-purpose user simulators for interactive systems. Prior studies have demonstrated that training on high-quality data can substantially improve model reasoning and downstream task performance. However, the upper bound of user simulation is still constrained by the model's reasoning paradigm: native chain-of-thought often degenerates into shallow pattern matching and fails to adequately model the behavioral factors underlying real user decisions. In this paper, we propose OmniSimulator, a novel training framework designed to improve the predictive ability of small LLMs for realistic user simulation on short-video platform environments. Specifically, OmniSimulator organizes behavior-oriented reasoning through a structured schema with five dimensions, carefully selects data from real user-behavior scenarios, and introduces a teacher model to generate high-quality reasoning traces under the proposed schema, helping small models learn behavior-relevant reasoning patterns rather than relying on superficial behavioral correlations. Based on this process, we construct 9,881 high-quality training instances from three months of historical interaction trajectories of 200 real users, averaging about 50 distilled examples per user. Experimental results show that OmniSimulator improves the average score of Qwen3-8B by 34.33%, achieves performance competitive with Claude-Sonnet-4.5, and supports smaller-scale, self-hosted deployment. These results suggest that learning structured behavior-oriented reasoning patterns is a promising direction towards scalable and high-fidelity LLM-based user simulation.

---


### 124. [TenetBench: A Clause-Anchored Russian Corpus for Evaluating Language Models against Professional Codes of Ethics](https://arxiv.org/abs/2610.29477)

**<font color=#1a73e8>作者：</font>** Yegor Anichkov, Valery Vinogradov, Andrey Furov 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Codes of professional ethics guide and restrict specialists, who increasingly work with assistants built on large language models. Such an assistant can breach the user's code, or help the user breach it, without the user noticing. Evaluations reporting broad categories of harm cannot show how often this happens or which provision is breached. TenetBench pairs 3,433 requests conflicting with clauses of fifteen Russian-language professional codes with benign twins that differ only in the legitimacy of what is asked. An automated pipeline generates the tasks from the text of a code, so the corpus grows with every code added and a provision yields new tasks on every run. It also produced tasks and human-validated verdicts from two English codes of other jurisdictions. In human validation of the frozen pipeline, specialists rated 0.995 of the conflicting tasks plausible, and the model judge agreed with the adjudicated label at Gwet's AC1 of at least 0.894 on 1,860 elements. We evaluated fourteen model and reasoning-mode combinations on whether they produce the conflicting text, decline or warn. Eleven of the fourteen produce conflicting content on most such requests, mostly without a warning, and nearly three warnings in four accompany conflicting content. The models that conform more do so by declining while still serving the legitimate twin, and enabling reasoning halved the refusals of two models. We hope the dataset and pipeline will help evaluate how language models observe professional norms and let diagnostic datasets be built for particular professions and organisations.

---


### 125. [The Serendiptionnaire: a Questionnaire for Measuring Experienced Serendipity](https://arxiv.org/abs/2610.29487)

**<font color=#1a73e8>作者：</font>** Brett Binst, Annelien Smets  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Serendipity is important to design for, yet it remains difficult to measure and evaluate. No validated questionnaire exists, so studies either borrow ResQue's novelty scale, which does not measure serendipity, or build their own items, which makes findings hard to compare and synthesize. Building on our earlier conceptualization of experienced serendipity as a fortuitous encounter with content that is both refreshing and enriching, we developed the Serendiptionnaire, a questionnaire that operationalizes our framework. We conducted twenty-seven cognitive interviews over three iterations with respondents who varied in age, education level, country of birth, and English proficiency, while they browsed recommendations on platforms such as Instagram, TikTok, YouTube, and Spotify. After each iteration, we revised the items until respondents interpreted them as intended. The resulting instrument consists of modular scales that researchers can combine to target the specific flavor of serendipity they want to study or design for. The Serendiptionnaire offers a ground truth for validating system-centered serendipity metrics and LLM-based evaluations, and it provides a nuanced evaluation of users' experienced serendipity.

---


### 126. [Balancing Foundation Models and Trait-Specific Learning for Forehead-Crease Recognition](https://arxiv.org/abs/2610.29495)

**<font color=#1a73e8>作者：</font>** Geetanjali Sharma, Aryan Jain, Dev Nagaich 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Biometric recognition often degrades under partial facial vis- ibility, where conventional facial cues are occluded. The forehead region remains consistently visible and contains distinctive crease patterns that can serve as a complementary biometric trait. We present a unified eval- uation of forehead-crease recognition across explainable zero-shot rea- soning, domain-adaptive learning, and trait-specific modeling. FIRE en- ables interpretable zero-shot verification using multimodal large language models, while pretrained face-recognition models are adapted to the fore- head domain through margin-based learning. Under open-set evaluation, the best zero-shot model GPT-4o+FIRE achieves 18.22% EER, while Edge-Forehead achieves 8.30% EER and 54.01% TMR@0.1% FMR. The results show that although MLLMs offer interpretable zero-shot verifi- cation, trait-specific learning remains more effective for robust forehead- crease biometric recognition.

---


### 127. [A Strong MoE Is All You Need for Process Supervision](https://arxiv.org/abs/2610.29498)

**<font color=#1a73e8>作者：</font>** Guanzhi Deng, Zengyan Liu, Haibo Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Process reward models (PRMs) provide fine-grained supervision for multi-step reasoning, yet obtaining reliable process labels remains a central bottleneck. Existing approaches typically rely on human annotation, rollout-based estimation, or auxiliary verification. In this work, we explore a different source of process supervision natively exposed by Mixture-of-Experts (MoE) models: expert routing. We show that simple routing statistics provide an intrinsic process-confidence signal that is competitive with conventional output-logit confidence. Building on this observation, we construct routing confidence by combining overall routing mass, head routing mass, and within-step routing variation, and introduce RoCo-Rethink, which identifies the least confident reasoning step and selectively regenerates the subsequent trajectory. We further introduce RoCo-PRM, which uses a strong MoE to automatically annotate reasoning trajectories with routing-derived step scores and distills them into a standalone PRM. Across multiple MoE architectures and diverse reasoning tasks, both RoCo-Rethink and RoCo-PRM consistently outperform strong baselines, while RoCo-PRM transfers effectively across both model architectures and tasks. Our findings suggest that expert routing is more than a computational dispatch mechanism: it provides an architecture-native source of process supervision for reasoning.

---


### 128. [Parallel Thinking for Large Language Model with Path Diversity](https://arxiv.org/abs/2610.29501)

**<font color=#1a73e8>作者：</font>** Jiaru Qian, Yihong Dong, Xue Jiang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Parallel thinking has emerged as a promising paradigm for enhancing the reasoning capabilities of Large Language Models (LLMs) by exploring multiple reasoning paths simultaneously. However, we identify that parallel thinking via Reinforcement Learning (RL) typically suffers from the mode collapse of reasoning paths, where parallel thinking trajectories degenerate into similar ones. This homogeneity undermines the fundamental motivation of parallel thinking, that is, maintaining multiple hypotheses concurrently to prevent premature loss into a suboptimal solution. In this paper, we propose Diverse Parallel Thinking (DPT), a simple yet effective RL approach for parallel thinking designed to encourage path diversity. DPT rewards the model to develop distinct reasoning strategies by penalizing the prefix similarity of parallel thinking paths, thereby enhancing a more comprehensive exploration of the reasoning space. We conduct various experiments and analyses across multiple reasoning benchmarks to demonstrate the effectiveness of DPT. Results show that DPT successfully outperforms previous parallel thinking methods, achieving state-of-the-art performance over baselines. We validate path diversity as a key element to improve parallel thinking. Our code is available at this https URL.

---


### 129. [Keeping Time vs. Understanding Time: Neither Alone Explains Temporal Reasoning in LLMs](https://arxiv.org/abs/2610.29507)

**<font color=#1a73e8>作者：</font>** Auss Abbood, Fernando Martínez-Plumed, José Hernández-Orallo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Temporal reasoning is widely assumed to decompose into two modes: temporal arithmetic (date and time calculations), and temporal semantics (understanding temporal and causal relations). This dichotomy shapes how benchmarks are designed, how models are trained, and how progress is measured, yet its empirical validity has never been directly tested. We provide two lines of evidence that challenge it. First, we test whether tasks labelled as arithmetic or semantic by the benchmarks support transferable gains within their purported mode. Finetuning on these subsets yields predominantly dataset-specific gains ($+6.8$ to $+23.1$ percentage points), while transfer to a different dataset in the same mode ranges from $-3.2$ to $+1.1$ percentage points. Across the two benchmark families used in the transfer analysis, this pattern provides little evidence of coherent, transferable temporal abilities. Second, using cognitive-demand-based model evaluation, we examine which capabilities actually drive performance on these benchmarks. We find that quantitative and logical reasoning, the assumed proxies for temporal arithmetic and temporal semantics, are not the primary drivers; knowledge is. Together, these findings show that current temporal reasoning benchmarks do not cleanly realise the arithmetic-semantics distinction and instead largely reward models for remembering how time typically works.

---


### 130. [Mitigating Query Shortcuts in Chain-of-Thought with Context-Aware Decoding](https://arxiv.org/abs/2610.29518)

**<font color=#1a73e8>作者：</font>** Shin'ya Yamaguchi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While Chain-of-Thought (CoT) prompting improves the reasoning performance of large language models (LLMs), recent studies have shown that final answers do not always depend on the generated rationales. In particular, LLMs may rely on query-specific shortcuts rather than the information provided by their reasoning steps. In this paper, we investigate whether context-aware decoding (CAD), an existing contrastive decoding method, can mitigate such shortcut behavior when applied to CoT reasoning. We study this application as Rationale Contrastive Decoding (RCD), which contrasts the next-token distributions conditioned on the query with and without its rationale, amplifying tokens whose likelihood increases due to the rationale. We provide a theoretical interpretation of this decoding rule via a KL-regularized reward-maximization objective. Experiments across five reasoning benchmarks demonstrate that RCD improves answer accuracy over standard CoT. Furthermore, intervention analyses using ground-truth and random rationales reveal that RCD increases the behavioral dependence of final answers on the rationale content. Our findings suggest that contrastive decoding offers a simple, training-free approach to mitigating query shortcuts.

---


### 131. [RCSD: Reinforcement and Continual Learning for Domain-Specific Speculative Decoding](https://arxiv.org/abs/2610.29527)

**<font color=#1a73e8>作者：</font>** Mingkang Liu, Weiming Meng, Peipei Jiao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Speculative decoding accelerates large language model inference by employing a compact draft model to propose candidate tokens that are verified in parallel by a target model. Conventional training relies on soft-label distillation, which forces the draft model to mimic the target's full output distribution, including high-entropy regions that degrade acceptance rates and increase early rejection risk. We propose RCSD (Reinforcement and Continual Learning for Speculative Decoding), a training framework that aligns draft model optimization with the system-level objective of maximizing acceptance length. RCSD leverages naturally occurring accepted and rejected sequences during speculative inference to construct implicit preference pairs, with masked loss to avoid penalizing target-aligned tokens. Evaluated across multiple benchmarks, RCSD improves average acceptance length by 35% over HASS and achieves 1.35x faster end-to-end inference than HASS on practical workloads, without compromising generation quality.

---


### 132. [Melange: A Synthetic Visual Bias Benchmark for Multi-modal Large Language Models](https://arxiv.org/abs/2610.29537)

**<font color=#1a73e8>作者：</font>** Razieh Rezaei, Ehsaneddin Asgary, Masoud Jalili Sabet  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-modal Large Language Models (MLLMs) have seen broad adoption, but their biases are still far less examined than those of standard LLMs, creating possible social harms when deployed in real-world settings. Prior efforts to extend bias analyses from LLMs into the multi-modal space either cover only a few bias categories or do not ensure that the groups being compared are clearly addressed by visual cues in the images. To overcome these limitations, we introduce Melange, a wide-ranging synthetic visual benchmark covering seven categories for assessing social biases in MLLMs. It is grounded in the widely used language-only BBQ dataset (Bias Benchmark for Question Answering) from BigBench, carefully extending its constructed contexts via controlled generation of visual scenarios so the target attributes appear visually and clearly. To maximize reliability, our generated images pass through two stages of validation: automated screening using visual question answering (VQA) and subsequent manual inspection by human annotators. By systematically evaluating 23 open-source MLLMs across three matched evaluation settings---text-only, image-only, and image-with-context---Melange isolates the fairness effect of the input modality. Switching from text to vision reduces fairness by 0.291 on average, a gap that varies by model family rather than by scale alone. A perception control confirms that this gap is not an artifact of visual comprehension: models identify the depicted attributes at 90--95\% accuracy yet still fail to abstain. When models do commit to a biased answer, polarity-aware stereotype alignment shows they choose the human-stereotypical response roughly three-quarters of the time.

---


### 133. [PACE: Periodic and Channel-Aligned Encoding of Four-Bit Recurrent States](https://arxiv.org/abs/2610.29545)

**<font color=#1a73e8>作者：</font>** Patrick Haller, Filipe Laitenberger, Alan Akbik  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Linear-attention language models keep their context in a recurrent state of fixed size, where an inference system stores one copy of this state for every sequence it decodes at the same time. Storing the state at lower precision therefore lets more sequences share an accelerator. Existing state quantizers round the state after every generated token and report that four bits lose accuracy unless the bit width is raised or the model is fine-tuned.\par We introduce PACE, a post-hoc four-bit state quantizer. PACE rounds the state only once every few generated tokens, as chunked kernels already do once per chunk during prefill, and keeps the tokens generated in between in a small buffer. Rounding less often reduces the error that accumulates in the state. Additionally, we find that the large entries of the gated-delta state gather in columns, because some channels of the update written at each token remain large across many tokens. PACE therefore shares each quantization scale within one column. It also keeps the heads that retain rounding error longest at eight bits. On four hybrid models from 4B to 35B parameters, PACE with mixed four- and eight-bit heads is competitive with eight-bit DAMP on the three larger models at about two thirds of its memory, PACE with four-bit heads throughout scores higher than Q-Mamba at equal memory, and rounding every few tokens preserves the decoding speedup of the buffer.

---


### 134. [Generalized CycleGRPO for Fine-Grained Multimodal Understanding and Grounding](https://arxiv.org/abs/2610.29552)

**<font color=#1a73e8>作者：</font>** Xin Zhang, Haochen Wang, Beibei Lin 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Fine-grained multimodal intelligence requires models to both understand a designated region and localize it from language. Existing methods learn these directions with separate objectives and task-specific annotations. We present Generalized CycleGRPO, the first unified reinforcement learning framework coupling region understanding and localization across spatial, temporal, and spatio-temporal domains. Given a region, a multimodal large language model generates candidate descriptions and then localizes each description to reconstruct the input region. Reconstruction overlap provides a verifiable reward for captioning, while individual localization rewards improve the inverse mapping. A common region-space formulation extends this cycle from image masks and boxes to video intervals and timestamped spatial evidence, without reference captions or an external language-model judge during reinforcement learning. In videos, the cycle encourages descriptions that distinguish a target event from similar recurrences. We introduce DOVE (Distinctive Occurrence-level Video-caption Evaluation), a human-verified contrastive benchmark for this temporal distinctiveness. CycleGRPO improves SAMTok's overall gIoU from 57.5% to 68.2% on GroundingSuite and average gIoU from 71.2% to 78.7% on GRES. For temporal tasks, it achieves 51.9% tIoU on Charades and 33.3% Temporal Evidence Coverage on DOVE, compared with 45.6% and 14.8% for the Qwen3-VL initialization. These results establish region-text cycle consistency as a general self-evaluation principle for multimodal understanding and localization. Models, code, and DOVE are available at this https URL.

---


### 135. [WRDO: Weighted Refusal Direction Optimization in Aligned Language Models](https://arxiv.org/abs/2610.29555)

**<font color=#1a73e8>作者：</font>** Grigoriy Evseev, Vladimir Solodkin, Dmitry Bylinkin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Aligned large language models are trained to comply with benign requests while refusing harmful ones. However, recent work shows that this refusal behavior is fragile and can often be disrupted by simple activation- or weight-space interventions. In particular, refusal has been shown to be largely mediated by a single residual-stream direction, typically computed as a difference-of-means vector between harmful and harmless prompts. However, this standard construction aggregates heterogeneous harmful prompts into one uniform average, potentially conflating distinct refusal-related phenomena. In this work, we study whether refusal interventions can be strengthened by learning how to combine prompt-specific refusal directions. We propose Weighted Refusal Direction Optimization (WRDO), a procedure that constructs a composite refusal direction from a bank of per-prompt directions using learned aggregation weights. This approach allows different harmful prompts to contribute unequally to the final intervention direction. We evaluate WRDO against prior single-direction methods on three open-weight language models using three guard judges and HarmBench as an external evaluator. We further measure the effect of the intervention on general model capability through standard utility benchmarks. Finally, we investigate a defense-oriented setting in which the same optimization machinery is used in reverse to restore refusal behavior in an abliterated model checkpoint. Our results show that weighted aggregation provides a more effective and flexible mechanism for manipulating refusal representations.

---


### 136. [Unlocking Spatial Grounding in Flow-Matching Models via SNR Tuning](https://arxiv.org/abs/2610.29581)

**<font color=#1a73e8>作者：</font>** Martin Thißen, Elke Hergenröther  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite the success of foundation models in image synthesis, achieving fine-grained spatial control remains a significant challenge, typically requiring auxiliary structural adapters or complex inference-time steering. While modern vision-language (VLM) text encoders possess the latent capacity to represent spatial coordinates, generative models often fail to leverage this information. We demonstrate that the signal-to-noise ratio (SNR) distribution is a critical determinant of spatial grounding in flow-matching models. Using a novel synthetic benchmark of geometric primitives, we isolate structural mechanics from textural complexity inherent in natural imagery and introduce a rigorous color-aware layout metric to quantify spatial fidelity. We show that training on a centered SNR distribution results in poor layout adherence (25.9%). Instead, we identify high-noise regimes as a "critical learning phase" for spatial grounding. Shifting the training focus toward these stages increases layout adherence to 80.8%, effectively reaching the 83.6% reconstruction ceiling of the underlying variational autoencoder. We find that the necessity for this shift scales with resolution and aspect ratio variance, and that the conservative noise schedules employed by models like FLUX.1 are insufficient for precise layout adherence. Finally, we show that these findings translate to real-world imagery via the COCO dataset (1.0 vs. 57.3 Average Precision), where state-of-the-art layout adherence is unlocked through distribution tuning alone, without architectural modifications.

---


### 137. [A Diagnostic Study of Faithfulness in Diffusion Language Models for Table-to-Text Generation](https://arxiv.org/abs/2610.29602)

**<font color=#1a73e8>作者：</font>** Zaynab Merimi, Noussayba El Marrakchi, Arthur Satouf  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Diffusion language models generate by iteratively denoising a masked sequence under bidirectional attention, without the strict left-to-right commitment of autoregressive decoding. Whether this difference affects how reliably they remain grounded in structured inputs is largely unexplored. We study this question in table-to-text generation using ToTTo, where highlighted source cells make factual grounding directly testable. We compare the masked diffusion models MDLM and LLaDA with GPT-2 and GPT-Neo under an identical retrieval-based few-shot protocol, together with a QLoRA-adapted LLaDA, and we score reference similarity and source grounding as separate axes. The two pull apart. Within LLaDA, additional demonstrations raise BLEU from 11.3 to 22.0 while NLI entailment against the source table falls from 0.78 to 0.52; QLoRA reaches the best BLEU of the study, 24.15, and grounds no better for it. Manual annotation shows the failure modes differ in kind: the autoregressive baselines tend to wander off the table, while LLaDA-based models more often stay on topic and swap out individual entities. Reference-based metrics alone are insufficient to assess faithfulness in table-to-text generation.

---


### 138. [Overview of CHIP 2026 Shared Task 1: Patient-Specific Phenotype Concept Recognition in Full-Text Biomedical Literature](https://arxiv.org/abs/2610.29606)

**<font color=#1a73e8>作者：</font>** Xuanlyu Zhu, Feng Tian, Yang Zhong 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automatic phenotype information extraction plays an important role in rare disease diagnosis, genotype-phenotype analysis, and precision medicine. However, accurately identifying phenotype concepts and determining their associations with specific patients remain challenging, particularly in full-text biomedical articles involving multiple patients and complex clinical descriptions. This paper presents an overview of CHIP 2026 Shared Task 1, which aims to promote the development of methods for patient-specific phenotype concept recognition from full-text biomedical literature. The task consists of two subtasks: full-text phenotype concept recognition and patient-specific phenotype association. For this evaluation, we used 200 annotated full-text biomedical articles from the PatientPheX dataset, containing 506 patients, 15,193 phenotype mentions, and 5,656 patient-phenotype associations. A total of 455 teams registered for the competition, with 189 and 103 valid submissions received on the Phase A and Phase B leaderboards, respectively. The best-performing system achieved an overall score of 0.7389 on the final test set, outperforming the baseline by 8.37 percentage points. The top-performing teams explored diverse approaches combining biomedical language models, large language models (LLMs), and ensemble strategies. The evaluation results highlight both the potential of these approaches and the remaining challenges in patient attribution and phenotype normalization from full-text biomedical literature. The post-evaluation phase remains open at this https URL.

---


### 139. [LLMs as survey respondents: Comparison to simple semantic baselines](https://arxiv.org/abs/2610.29645)

**<font color=#1a73e8>作者：</font>** Esko Lehtonen, Tommi Buder-Gröndahl  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have been explored as surrogates for human survey respondents. A more promising application is data augmentation, where LLMs predict new responses from partial human data. However, the semantic similarity between questionnaire items is a known source of correlation between answers. It is thus unclear whether LLMs actually infer meaningful relationships between question-response pairs, or use surface-level comparison between questions as a heuristic. To assess this, we evaluated how three LLMs can predict responses to held-out items in two surveys measuring attitudes toward automated or light-electric vehicles, based on varying proportions of known responses. Performance was compared to two baselines, where new responses were derived by maximizing embedding-similarity to a prior response. While LLMs mostly predicted human responses better than baselines, their performance consistently declined with a lower share of known responses, even aligning with the baseline in one survey. Our results show that LLMs' capacities for augmenting replies varied across surveys, and can revert to the same levels as simpler embedding similarity baselines when less data is available.

---


### 140. [From Association to Decision Value: Testing Paired Instruction Dependence for VLA Corpus Selection](https://arxiv.org/abs/2610.29646)

**<font color=#1a73e8>作者：</font>** Nurmukhambet Serikbayev, Abdul Basit, Muhammad Shafique  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Choosing among robot demonstration corpora is a ranking problem: an upstream diagnostic must preserve which candidates produce better downstream policies, not merely correlate with average performance. We study paired instruction dependence, the rate at which a demonstrator changes its first decision when only the goal changes. Across 136 independently seeded quadruped-navigation corpora, predictions developed on 56 corpora are evaluated prospectively on 80 held-out corpora. The audit is reliable and associated with downstream paired correctness, and lowers mean absolute prediction error when added to a correctness-aware baseline, but the primary proper-log-score increment is +0.059 nats (95% corpus-bootstrap CI [-0.027, 0.133]) and the prespecified top-20% comparison does not establish an incremental selection gain. An exploratory response decomposition suggests a structural source of this predictive-ranking mismatch: under the tested predictor specification, separating both-correct and both-wrong responses yields larger held-out gains than their unsigned switch statistic. Seed-to-seed agreement indicates that the held-out endpoint retains recoverable rank signal. These results show that counterfactual response structure can be reliable and predictive while providing limited incremental decision value in this setting when compressed into an unsigned statistic, motivating diagnostics that preserve outcome-relevant structure and are validated against the decisions they are intended to support.

---


### 141. [Effects of Model Scale and Quantization on Social Bias and Abstention in Question Answering](https://arxiv.org/abs/2610.29657)

**<font color=#1a73e8>作者：</font>** Kuniko Paxton, Ifeoluwa Wuraola, Dhavalkumar Thakker  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The deployment of small and quantized language models in resource-constrained settings raises an important fairness question: when a compressed model produces fewer biased responses, does this reflect fairer behavior or greater abstention? We study this problem in Question Answering (QA) using the BBQ benchmark across multiple model sizes and quantization settings from Qwen3, Gemma-3, and SmolLM2. We also examine whether the observed trends remain stable across alternative prompt formulations and when the ``Unknown'' option is removed in a forced-choice setting. Our results show that larger models achieved higher QA accuracy, but bias showed no simple scaling trend and quantization effects varied across configurations. Notably, 20 of the 26 configurations with fewer biased responses also show increased over-abstention, indicating that lower observed bias can partly reflect greater abstention. These findings show that lower observed bias can partly reflect greater abstention, and that fairness evaluation should consider biased responses, abstention, prompt formulation, and answer-option design jointly.

---


### 142. [SPARE: Sparsity Allocation via Routing Entropy for Efficient MoEs](https://arxiv.org/abs/2610.29662)

**<font color=#1a73e8>作者：</font>** Yifan Yang, Hanling Yi, Dongquan Yang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mixture-of-Experts (MoE) architectures scale model capacity efficiently, yet their substantial memory footprint poses a major barrier to deployment. Expert pruning reduces this footprint, but most methods focus on which experts to remove and prune every layer equally. We propose SPARE (Sparsity Allocation via Routing Entropy), a training-free, selector-agnostic method that decides how many experts to remove from each layer using routing entropy, the entropy of tokens' normalized Top-K gate weights on calibration data. When a token's gate weight is spread evenly, removing one active expert discards little of it, so SPARE prunes layers with more diffuse routing more aggressively. A perturbation bound under random pruning formalizes this intuition, and controlled interventions with a fixed selector link concentrated routing to larger output changes. With the same selector and budget, SPARE improves average accuracy over uniform allocation on Mixtral, Qwen3, and DeepSeek models, especially at high pruning ratios. At 50% expert pruning, it raises the eight-task average of Qwen3-30B-A3B from 57.2% to 63.8%, and the math, code, and science average of DeepSeek-R1 from 80.1 to 82.8.

---


### 143. [TraceForge: Distilling with Your Own Thinking](https://arxiv.org/abs/2610.29680)

**<font color=#1a73e8>作者：</font>** Yan Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Using an LLM to generate training data for another is among the most general ways to train one, and it remains common practice. Some frontier teams have closed that route for their own models: what comes back is an answer, or a short summary, without the detailed reasoning trace behind it. That is a little ironic: they were themselves built on distilling human knowledge, and distilling an open-source model is still entirely routine; the restriction applies to their own outputs alone. Recent work recovers the hidden reasoning by replaying encrypted blocks across models. It somehow works, but it breaks the providers' terms of service, so it is not something a product can be built on long-term.
We built the alternative. We take the context and the teacher's answer as input, and generate the reasoning trace ourselves, in the style of the student's own model family. Training is two-stage, supervised and then adversarial: a generator learns to regenerate the family's own reasoning traces from their context and answer, and a critic learns how real a reasoning trace looks. Applied to a teacher's answer, the generator writes one in the family's style. An independent judge rates how likely traces are to be genuine on a scale from 0 to 1: ours average 0.68, real traces 0.66, and traces selected by the critic from four candidates 0.82. These are authenticity scores, not correctness rates.
We test the idea on five benchmarks with everything else held fixed. On general tasks the five training corpora are about the same; on coding, the generated reasoning beats Fable 5's own thinking content. With the same 5,000 questions and the same teacher answers, HumanEval+ improves by 3.7 points and MBPP+ by 7.1 at the final checkpoint, and the MBPP+ lead holds at every checkpoint. We suspect that reasoning written in the student's family style is easier for it to learn from.

---


### 144. [Scaling Multilingual Pretraining of Pixel Language Models](https://arxiv.org/abs/2610.29681)

**<font color=#1a73e8>作者：</font>** Ilker Kesen, Jenny Kunz, Kasra Malihi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Pixel language models process text as rendered images instead of a finite vocabulary, which gives them strong cross-lingual transfer abilities. However, not much is known about how these abilities are influenced by larger-scale pretraining. In this paper, we train a family of MPIXEL models along three axes of variation: more languages, more scripts, and larger model capacity under fixed per-language compute. In evaluations on five tasks covering 83 languages, we find that scaling acts locally: each axis improves the added languages and scripts, while increased capacity mitigates the curse of multilinguality from pretraining on more languages. Transfer to unseen scripts improves with multilingual pretraining, but does not further improve with scaling. On typologically distant low-resource languages, our models outperform subword and character-level baselines across many writing systems. We also show that larger pixel models reserve more layers for visual processing, and that cross-lingual alignment weakens as more languages are added. Overall, our findings characterize how multilingual scaling improves pixel language models.

---


### 145. [Rethinking Post-hoc Debiasing of Large Pretrained Models](https://arxiv.org/abs/2610.29688)

**<font color=#1a73e8>作者：</font>** Divyaansh Mertia, Chirag Bhutra, Himanshu Shekhar 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large pretrained models such as CLIP are widely used as frozen feature extractors. However, their embeddings inherit spurious correlations from training data, introducing bias into the features. A growing body of research has sought to address this issue through post hoc debiasing, leaving the backbone untouched. We discover that despite differing mechanisms, these methods require the bias feature to be identified and expressed in text. This dependency is not innocuous. In this work, we experimentally demonstrate that this requirement incurs an unforeseen penalty in certain scenarios. For example, on the UrbanCars benchmark, having two co-occurring bias attributes, the recent methods underperform a vanilla classifier on biased frozenbackbone features, and even providing ground-truth bias identities does not close the gap. We show that the pattern that such methods seek is readily observable in the frozen geometry. Specifically, cross-class training pairs placed closest together by the frozen encoder almost always share a spurious attribute, regardless of the bias type, without requiring access to the bias labels. Based on this, we propose a novel approach to identify such pairs and learn a single linear map that transforms the features to perform post-hoc debiasing. The proposed approach achieves competitive performance across all datasets without access to bias attribute annotations or any LLMs.

---


### 146. [Retrieval Augmented Generation Compositionality](https://arxiv.org/abs/2610.29722)

**<font color=#1a73e8>作者：</font>** Ido Levy, Segev Shlomov, Leshem Choshen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval Augmented Generation (RAG) grounds large language models in external knowledge. Modern pipelines combine embedding, chunking, retrieval, reranking, query augmentation, context compression, and agentic verification, yet these techniques are typically evaluated one at a time. It remains unclear whether their isolated gains survive composition, whether retrieval quality and answer faithfulness favor the same design choices, and whether conclusions from small corpora hold at large scale. We pre-declare three hypotheses and introduce LASAGNA, an open-source framework for controlled RAG evaluation. We test 450 configurations across eight benchmarks and corpora ranging from 5K to 200K documents. Three findings emerge. First, individually strong techniques from different phases of a RAG pipeline do not necessarily compose: three retrieval techniques predict a +47% combined improvement but deliver only +17% when used together. Second, component gains stack differently for retrieval and faithfulness, and optimizing one can hurt the other. Third, the best composition changes as the corpus grows: the combination that wins on a small corpus may not remain best at large scale. These findings show that gains measured in isolation are not reliable predictors of realistic performance, and that new RAG techniques should be tested with the full surrounding stack. We call on researchers to do so and supply LASAGNA to simplify these experiments.

---


### 147. [Accept or Repair: Preserving Passage-Supported Answers in Contrastive Decoding](https://arxiv.org/abs/2610.29727)

**<font color=#1a73e8>作者：</font>** Jungseob Lee, Seungyoon Lee, Hyeonseok Moon 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models often answer from knowledge learned during training, even when a provided passage contradicts that knowledge. To address this problem, contrastive decoding contrasts the predictions under the full and a modified prompt at every token, but it also alters correct answers that the passage supports. We show that checking answers against the passage removes this trade-off. Based on this observation, we propose Accept-or-Repair (AoR), a training-free procedure. AoR keeps a sampled answer if the passage supports it. Otherwise, it tries up to two replacements with contrastive decoding, returning one as soon as it passes this check. It rejects replacements that repeat the answer generated without the passage when the passage favors another answer. Our experiments show that AoR raises the score over sampling by 12.5 points on counterfactual passages and 2.3 on ordinary ones, surpassing eight contrastive and prompting baselines on both, including when each receives the same rejection rule. Replacing only initial answers that the passage does not support improves the average score of every decoder. These results suggest that models can follow passages that contradict their knowledge while preserving accuracy on passages that agree with it. Code will be released at this https URL.

---


### 148. [Monitorability Is Trainable: Post-Training for Chain-of-Thought Monitorability](https://arxiv.org/abs/2610.29734)

**<font color=#1a73e8>作者：</font>** Usman Anwar, Tim Bakker, Christos Louizos 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Chain-of-thought (CoT) monitoring is one of the few practical tools available for overseeing capable AI systems, but it is fragile: a model's reasoning is only useful to a monitor if it remains coupled to what the model actually does. This coupling can be degraded during training through, for example, CoT compression, optimization against a monitor, and out-of-context generalization from synthetic documents. In this work, we propose an unsupervised post-training objective based on maximizing mutual information between CoT and the output for improving CoT monitorability. Across three model organisms with degraded CoT, it recovers most or all of the lost monitorability. Applied to undegraded policies, it further improves judged monitorability, improves prediction of unsafe behavior by CoT monitors and activation probes, and increases the prevalence of consequential reasoning. These results suggest that monitorability should be treated as a trainable attribute of the policy. A dedicated monitorability post-training stage can extend current practices that protect CoT from direct optimization pressure.

---


### 149. [Bridging Foundational and Agentic Capabilities of LLMs](https://arxiv.org/abs/2610.29751)

**<font color=#1a73e8>作者：</font>** Wei Guo, Yuanjian Xu, Jianing Hao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly deployed as agents, yet it remains unclear how their foundational capabilities translate into agentic capabilities. End-to-end scores leave unresolved whether low benchmark capability or weak deployment drives a failure, limiting actionable diagnosis. We bridge foundational and agentic capabilities through an operation-level measurement framework. We represent each model with a foundational profile derived from capability benchmarks and an operation profile derived from interaction trajectories, and define capability realization gaps as deviations of observed operation performance from predictions based on foundational capabilities. Experiments on fifteen model services in $\tau^2$-Bench show that foundational profiles only partially predict agentic operations. Models with comparable profiles can differ substantially in execution, and these gaps remain consistent across task subsets. Operation profiles add information and substantially improve task-score prediction. The framework locates execution departures at the operation level to inform model development and agent evaluation. We will release our code and analysis artifacts.

---


### 150. [ALIAS: Evaluating Performance and Memorization in LLM-Written TLA+ Specifications](https://arxiv.org/abs/2610.29767)

**<font color=#1a73e8>作者：</font>** Arslan Bisharat, Mujtaba Nazari, Khushboo Bhadauria 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Memorization inflates the benchmark scores of large language models (LLMs), since a model can reproduce answers it saw in training. Researchers test for it with consistent identifier renaming (CIR), which gives every identifier in a task a new name, and treat a lower score on the renamed task as evidence of recall. We test this method on the Temporal Logic of Actions Plus (TLA+) language, whose model checker acts as an oracle by confirming whether a renamed task preserves the exact behaviors of the original. Across 111 TLA+-Bench tasks, renaming lowers the correctness of Claude Opus 4.8 from 28% to 18% and of GPT-5 from 9% to 7%. Most of this decrease comes from how the test grades, which requires exact names that most descriptions never state. Grading by behavior shrinks the decrease to about 3 percentage points for Opus 4.8 and to 0 for GPT-5. In two model families fine-tuned on disjoint halves of the tasks, renaming removes about half of the training gain in likelihood and costs 4.9 percentage points (Qwen) and 1.3 percentage points (Gemma) on unseen tasks. A lower score after renaming therefore mixes memorization, name-based grading, and the cost of new names.

---


> [!TIP]
> 当前位于：**101-150**（第 3/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-204](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
