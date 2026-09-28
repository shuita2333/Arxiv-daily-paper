# 🧠 大模型相关研究 | 2026年09月29日

> 本类共 **183** 篇论文：已确认 **174** 篇，待复核 **9** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**101-150**（第 3/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-183](./part-04.md)

---

### 101. [Towards Understanding Momentum Acceleration in River-Valley Loss Landscape](https://arxiv.org/abs/2609.30957)

**<font color=#1a73e8>作者：</font>** Miao Lu, Zeyu Bian, Kaiyue Wen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The empirical success of pretraining large language models has inspired a deeper investigation into the underlying loss landscapes and the optimization dynamics. Recent empirical and theoretical study suggest that the training loss landscape often exhibits a "river-valley" structure, which features a low-loss manifold (river) flanked by sharp orthogonal directions with higher loss (mountains). In the long term, the optimization progress is determined primarily by the progress along the river. Within such a landscape, gradient descent with large learning rates can move faster along the river despite high apparent loss due to vertical oscillations, while a subsequent sharp decay in the learning rate suppresses these oscillations, revealing genuine optimization progress. This explains the recent success of warmup-stable-decay (WSD) learning rate scheduler which, unlike cosine scheduling, keeps stable high learning rate and decays before producing intermediate checkpoints. Building on this foundation, in this work we take a step further and study the role of momentum within such a loss landscape. We establish theoretical analysis that characterizes how momentum accelerates optimization by stabilizing large learning rates that can not be tolerated by vanilla GD without deviating significantly from the river. The enabled large learning rate in-turn gives greater speed along the river and makes faster essential progress in the long run. Another intriguing observation from theory is that for a river-valley landscape with very flat and slow-spinning river, the momentum itself does not contribute directly to acceleration in terms of the speed of tracking the river, while the main acceleration comes from the admissible larger learning rate.

---


### 102. [MoMHa: Multi-Objective Optimization of LLM Harnesses over Accuracy, Safety, and Tokens](https://arxiv.org/abs/2609.30967)

**<font color=#1a73e8>作者：</font>** Subhojyoti Mukherjee, Md Mehrab Tanjim  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Most work on improving large language models treats accuracy as the sole objective. We argue that the harness, the Python code surrounding the model that constructs prompts, routes calls, and parses outputs, is a first-class design surface whose quality is inherently multi-objective: an accurate harness that refuses no unsafe request, or that consumes an order of magnitude more tokens, is not a good harness. We present Meta-Harness, a system that casts harness design as search over three per-domain objectives (accuracy, behavioural safety, and token cost) solved by an agentic proposer (Claude Code) with full filesystem access to prior harness source, execution traces, and scoring artifacts. Our central finding is that a singlephase joint-reward proposer (MoMHa) outperforms every alternative, including a two-phase "accuracy then tokens" ablation, scalar-only feedback, and an accuracy-only baseline. We evaluate on seventeen domains: seven synthetic capability suites, seven real-world public benchmarks (HumanEval, MBPP, Spider, FEVER, MMLU-Pro, LawBench, NuminaMath), and three U-SafeBench-derived user-specific safety domains, using a 12-model fleet spanning four families. On the synthetic track MoMHa achieves a joint mean of 0.482 versus 0.198-0.422 for ten baselines, winning $7 / 10$ per-domain columns; on the real-world track it scores 0.461 versus 0.377 for the strongest baseline (DSPy), winning 5/7 columns, demonstrating that harness strategies transfer to unseen benchmarks without retraining on 8 of 12 target models. MoMHa attains the highest measured behavioral safety composite (U-SafeBench, 0.781) and uses 95 fewer tokens per example than the two-phase alternative. We will release all harness code, evaluation infrastructure, and crossmodel logs.

---


### 103. [FAVoR: Measuring and Mitigating Author-Style Homogenization in Federated Personalized Generation](https://arxiv.org/abs/2609.30968)

**<font color=#1a73e8>作者：</font>** Lu Han, Jingyao Zhang, Katy Ilonka Gero 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly used as personalized writing assistants, but adapting a model across many authors can compromise individual writing style by pulling author-specific signals toward a shared register. Federated parameter-efficient fine-tuning (PEFT) offers a data-local setting for this multi-author adaptation problem: clients keep author text local while sharing compact adapter updates. However, we show that standard aggregation can preserve continuation utility while making different authors' generations less distinguishable in style space, a failure mode we define as author-style homogenization. We evaluate author-style retention with Angular Style Classification Encoder (ASCE)-based diagnostics on our main BlogText benchmark and ASCE-independent external authorship verification. Using this protocol, we find that common federated PEFT baselines can preserve semantic utility while averaging out author-specific signals. To address this homogenization, we instantiate FAVoR (Federated Authorial Voice Retention), an author-style residual mechanism for federated PEFT. FAVoR uses a shared-private adapter design: clients upload shared-adapter updates while retaining author-specific residual corrections locally. Across BlogText and external Mythos-Reddit validation, FAVoR improves author-style retention over standard and personalized federated PEFT baselines. These gains come with small continuation-utility trade-offs and are supported by component ablations, external verification, and cold-start transfer.

---


### 104. [CCRV-Bench: Constraint-Based Evaluation of Causal Reasoning in Vision-Language Models](https://arxiv.org/abs/2609.30979)

**<font color=#1a73e8>作者：</font>** Linyuan Gao, Yuan Wu, Yi Chang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) have demonstrated excellent performance in visual tasks, but their visual causal reasoning capabilities still lack reliable evaluation. Existing evaluations struggle to distinguish whether a model is performing causal reasoning based on visual evidence or relying on statistical correlations for shortcut learning, thereby potentially overestimating their actual capabilities. This paper proposes CCRV-Bench, a constraint-driven visual causal reasoning benchmark for single-image physical scenarios. We construct an orthogonal framework that evaluates four causal task dimensions: causal relation discovery, state prediction, causal diagnosis, and intervention. We further introduce entity symbolization, spatial grounding, the factual adversarial constraint, and minimalist output constraints to reduce shortcut cues while preserving the physical commonsense required by the task. Experiments across 15 multimodal models show that constraint sensitivity is task- and model-dependent: intervention has the largest average effective degradation among the four causal tasks, spatial grounding is the most damaging constraint on average, and the factual adversarial constraint improves DCR for all evaluated models. These results show that unconstrained performance does not determine constrained robustness and that a single aggregate score can obscure distinct failures in causal identification, spatial grounding, and constraint-compliant expression. CCRV-Bench provides a standardized framework for diagnosing image-grounded causal reasoning under controlled constraints. The code is available at this https URL

---


### 105. [STORM-Bench: Evaluating Online Video QA under Evolving and Incomplete Evidence](https://arxiv.org/abs/2609.30981)

**<font color=#1a73e8>作者：</font>** Siru Zhong, Shenghan Tan, Rihong Yan 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reliable online video question answering requires tracking state transitions while selectively abstaining when visual evidence is insufficient. Existing benchmarks focus on static recognition or long-range retrieval, rarely evaluating these coupled capabilities under evolving and incomplete evidence. We present STORM-Bench, comprising 5,736 questions across 630 compact, change-dense episodes spanning five egocentric domains (STORM-Real) and two controlled simulation subsets (STORM-Sim) at 1 FPS. Questions are stratified by a proxy for accumulated change intensity (Low, Medium, High) and query-time answerability (Known, Uncertain). To measure reliability, we introduce STORM-BR, a harmonic metric over joint answer-status correctness that exposes abstention failures masked by aggregate accuracy, alongside STORM-BR-ATTR for uncertainty attribution. Across 14 video LLMs, online accuracy peaks at 60.3\% (mean 51.7\%), whereas STORM-BR ranges from 5.7\% to 35.6\% (mean 18.8\%), driven by pervasive overconfidence on uncertain queries. STORM-Bench shows that task accuracy masks these gaps in epistemic reliability and state tracking. Benchmark and code are available at this https URL.

---


### 106. [Evaluating Sycophancy in Chinese Large Language Models on Factual Questions Derived from Online Search Queries](https://arxiv.org/abs/2609.30986)

**<font color=#1a73e8>作者：</font>** Geng Liu, Feng Li, Mengxiao Zhu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As large language models increasingly mediate information access, factually accurate and independent answers are critical. However, these models can exhibit sycophancy by aligning their responses with users' stated beliefs even when those beliefs are incorrect, potentially presenting misinformation as independently verified and reinforcing users' confidence in false claims. Prior work leaves unresolved whether introducing user beliefs causes correct responses to become incorrect or uncertain, or causes uncertain responses to become belief-aligned incorrect answers. It also remains unclear whether anti-sycophancy interventions preserve or restore factual accuracy or merely shift responses toward uncertainty. We analyze factual sycophancy in Chinese-language information seeking using yes/no fact-checking questions. Our analysis covers 364,941 responses from three frontier Chinese-based LLMs (DeepSeek, Qwen, and Doubao) to 12,165 factual questions derived from real-world Chinese search queries. We evaluate the models with and without reasoning across baseline, belief-conditioned, and anti-sycophancy prompting, tracing matched shifts among correct, incorrect, and uncertain responses. Under incorrect user beliefs, we distinguish belief-aligned errors from losses of factual confidence, in which initially correct answers become uncertain. Patterns vary across models and reasoning settings: reasoning is not a consistent safeguard, and anti-sycophancy instructions can reduce incorrect agreement while increasing uncertainty. In Chinese-language factual question answering, avoiding agreement with false beliefs is therefore not equivalent to preserving factual accuracy, highlighting the value of transition-level evaluation. Such behavior may undermine the reliability of LLM-mediated information access by reinforcing misinformation or weakening users' confidence in factually correct answers.

---


### 107. [FLIP: Final Layer Inference-Time Probing for Vision-Language Models](https://arxiv.org/abs/2609.30993)

**<font color=#1a73e8>作者：</font>** Drandreb Earl O. Juanico, Rowel O. Atienza  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present FLIP, a final-layer inference-time probe for testing whether a logit-facing intervention site in an open-weight vision-language model (VLM) supports structured, task-linked computation rather than generic perturbation. Behavioral change under internal intervention is otherwise mechanistically ambiguous: it may reflect improved use of visual evidence, generic output instability, or outright degradation. FLIP applies elementwise flooring to the final normalized hidden state before logit computation, leaving parameters, prompts, and decoding unchanged. On a controlled detection/counting probe, sweeping intervention strength reveals three regions: negligible change, a bounded interior regime in which detection recall at IoU 0.50 ($R_{50}$) improves while tolerant counting error ($\mathcal{E}_{\mathrm{count}}$) falls, and over-suppression. We formalize a four-criterion probe-and-sweep protocol for disciplining the interpretation of intervention effects: regime structure, grounding-proxy alignment, feature-coherence dependence, and failure to reproduce the same positive regime on a performance-based negative control. The post-normalization state passed to the output head is the logit-facing instantiation of this test; under a non-targeted flooring sweep it satisfies the full protocol. Raw decoder-layer interventions, including the last-block output before final normalization, and the singleton-pair left/right control fail to reproduce the Final-site signature, while same-site operators and multiple VLMs replicate it. FLIP is therefore a validation step for intervention-based mechanistic interpretability, not a steering method.

---


### 108. [The Linear Representation Hypothesis for Vision-Language-Action Models](https://arxiv.org/abs/2609.30996)

**<font color=#1a73e8>作者：</font>** Minseok Jeong, Hyewon Choi, Hiroyasu Tsukamoto 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The linear representation hypothesis (LRH) has become a standard lens for measuring and intervening on semantic information through the internal representations of large language models (LLMs). A growing body of work has begun extending this perspective to vision-language-action (VLA) models, but the dynamical nature of embodied interaction introduces an additional challenge. Unlike semantic attributes commonly studied in LLMs, such as gender or language, a physical quantity of interest (QoI) in a VLA evolves jointly with the system dynamics: the representation influences the actions selected by the policy, which alter the physical state and, in turn, the next representation.
In this paper, we develop a theoretical, signature-based formulation of the LRH for VLA that unifies representations and policies. On the representation side, we establish the existence of representations from which the future evolution of a QoI under a candidate action trajectory can be recovered via linear probing. On the policy side, we introduce a signature generalized linear model for stochastic action chunks. This structure yields a monotonic change in the expected future QoI along linear paths in natural parameter space, enabling linear steering. We construct an explicit oracle representation in a planar control-affine navigation experiment and verify the predicted linear probing and steering mechanisms.

---


### 109. [ZooWork-ShopRanker: An Open, Preference-Aligned E-Commerce Reranker](https://arxiv.org/abs/2609.31002)

**<font color=#1a73e8>作者：</font>** Siqiao Xue, Shuxuan Liu, Ning Hu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Open rerankers trained for general web retrieval transfer imperfectly to e-commerce, where ranking decisions depend not only on topical relevance but also on user preferences, product constraints, and comparative product fit. These preference signals are difficult to supervise at scale: real search traffic provides authentic queries and candidates but no clean pairwise labels. We present ZooWork-ShopRanker, a family of e-commerce rerankers (0.6B, 4B, and 8B) aligned to judge-labeled shopping preference. Training pairs are labeled by a panel of reasoning large language models (LLMs) from different families acting as a preference oracle, with position-debiased judgments and agreement tiers, and the rerankers are trained on these labels. The aligned 8B flagship then serves as a distillation teacher for the efficient 4B and 0.6B models, which are fit to its scores and sharpened on judged pairs. To measure progress, we introduce ShopRank-Bench, a contamination-limited benchmark of ~10,000 private-traffic preference pairs in both text formats, tiered by how many judge families committed to each label. ZooWork-ShopRanker-8B and -4B significantly outperform the strongest open reranker baseline, every model significantly beats its own un-aligned base, and ZooWork-ShopRanker-0.6B beats its size peer; the gains hold in both formats and extend to common MTEB benchmarks. We release the models and the dual-format ShopRank-Bench to facilitate further research.

---


### 110. [G$^2$PTQ: Improving LLM Post-Training Quantization with Generalized Gradient Compensation](https://arxiv.org/abs/2609.31009)

**<font color=#1a73e8>作者：</font>** Ruikang Liu, Haoli Bai, Yuxuan Sun 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Post-training quantization (PTQ) is a practical approach to reducing the memory and computational footprint of large language models (LLMs) without retraining. GPTQ-based methods have become the de facto standard, yet they suffer from two complementary limitations. Methods with local, layer-wise objectives lack global supervision; while methods with global objectives fix their Hessian estimates at the start and ignore first-order gradients, so their guidance grows stale as quantization proceeds. This paper presents G$^2$PTQ, a unified PTQ framework with Generalized Gradient Compensation that integrates both first- and second-order information under a globally supervised, block-wise optimization objective. By refreshing gradient and Hessian estimates before quantizing each Transformer block, G$^2$PTQ avoids the staleness of prior global methods. Furthermore, to stabilize the exact first-order compensation, we introduce a trust-region scaling mechanism that dynamically bounds the gradient step to prevent exploding weight updates. Finally, we derive efficient implementations for block-wise Hessian approximation and exact gradient compensation. Experimental results on various model families and bit-widths demonstrate that G$^2$PTQ enables better alignment with the full-precision model, outperforming state-of-the-art baselines. Code is available at: this https URL.

---


### 111. [Same Text, Different Numbers: The Divergence of LLM-Based Measures](https://arxiv.org/abs/2609.31013)

**<font color=#1a73e8>作者：</font>** Hamid Boustanifar, Sasan Mansouri  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Researchers increasingly use generative large language models (LLMs) to convert corporate text into empirical variables. We examine the extent to which LLM-based textual measures are invariant to model choice using thirteen measures, including sentiment, management clarity, uncertainty, answer specificity, and climate and political risk. Seven LLMs from different providers score earnings call transcripts of S&P 500 companies on these constructs. Cross-model rank correlations average only 0.52, and transcript-level differences common across providers account for only 34% of total score variation. Cross-model disagreement does not predict subsequent analyst or market disagreement, consistent with a substantial model-specific component rather than common ambiguity in the underlying disclosure. Model choice significantly affects downstream inference, with coefficient magnitudes, signs, and statistical significance varying substantially across models. Averaging across providers makes transcript rankings more stable for most constructs, but score levels remain sensitive to the models included in the ensemble. LLM-generated variables should therefore be treated as model-contingent measurements and validated across providers.

---


### 112. [Refining Cytology Predictions with Conditional Random Fields](https://arxiv.org/abs/2609.31028)

**<font color=#1a73e8>作者：</font>** Manon Dausort, Tiffanie Godelaine, Karim El Khoury 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) achieve strong zero-shot (ZS) classification on histology images but do not perform as well on cytology, whose stains and cell morphology differ markedly compared to histology. Conditional random fields (CRFs) can refine noisy VLM predictions by propagating information across patches, but existing CRF frameworks were designed for histopathology and do not transfer to cytology datasets, released as independent patch pools spanning multiple staining protocols. We introduce CytoCRF, which adapts the pairwise terms to cytology by targeting chromatin and cytology-specific staining, and further enrich the neighborhood of each potential term by combining multiple backbones. Across ten cytology datasets, CytoCRF outperforms existing CRF frameworks at every annotation budget, reaching +13.6 percentage points over the best baseline and +33.7 over ZS with only 50 annotations. Combining information from multiple backbones brings further gains, showing that the neighborhood topology matters more than the pairwise potential computed over it.

---


### 113. [MetaPermit: Scalable and Auditable Access Control for AI Agents via LLM-Inferred Meta-Attributes](https://arxiv.org/abs/2609.31039)

**<font color=#1a73e8>作者：</font>** Hanzhang Ma, Ali Hariri, Tianxiang Shen 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The rise of autonomous AI agents equipped with tools has introduced significant security risks, ranging from unintended tool misuse to adversarial manipulation through Indirect Prompt Injection (IPI) attacks. In practice, deployed agent systems such as OpenAI Codex and Claude Code protect tool invocations through a combination of coarse-grained permission rules and LLM-based judgments about individual proposed actions. Both components, however, have important limitations: static policies must anticipate possible user intents and therefore do not scale to open-ended tasks, while LLM-driven authorization supports dynamic decisions but produces inconsistent outcomes and remains vulnerable to targeted IPI attacks. To provide scalable and more consistent authorization, we propose MetaPermit, a policy-based tool access-control framework that decouples semantic inference from security enforcement. By analyzing agent-user interactions, we derive a compact, task-independent set of meta-attributes that capture the relationships among the user's intent, the execution context, and the proposed tool call. These meta-attributes allow MetaPermit to authorize tool use without enumerating user intents. At runtime, an LLM infers the meta-attribute values for each proposed tool call, while a fixed policy evaluates these values to allow or deny the call, making each decision auditable through the inferred values and the applied policy rule. We evaluate MetaPermit on the AgentDojo and AgentDyn benchmarks, across seven task suites and five attack methods, using two widely deployed open-weight LLMs. The results show that MetaPermit produces 31% more consistent authorization decisions than LLM-driven authorization and outperforms the state-of-the-art defenses CaMeL and IPIGuard in both task completion, with improvements of up to 109%, and robustness to IPI attacks, with no malicious tool calls executed.

---


### 114. [Exploiting Spatial Structure for Transductive Few-Shot Classification of Whole-Slide Images](https://arxiv.org/abs/2609.31040)

**<font color=#1a73e8>作者：</font>** Tiffanie Godelaine, Manon Dausort, Karim El Khoury 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automating the analysis of whole-slide images (WSIs), a key step in cancer diagnosis, has high clinical value, as it can reduce pathologist's workload while improving diagnosis accuracy. Recently, vision-language models have shown promising performance for patch-level classification without requiring any annotation, yet these zero-shot (ZS) predictions remain noisy on fine-grained tasks and must be further refined. A promising direction is to refine all predictions jointly, i.e., a transductive approach. However, most existing methods are not tailored to WSIs. We thus propose SlideTIM, an adaptation to WSIs of the recent transductive approach LC-TIM, which introduces a combined spatial--latent regularizer together with a prior on the patch class distribution. The former enforces spatially and semantically close patches to receive the same predictions, while the prior calibrates the predicted class proportions. Together, they address the complex spatial organization and the strong class imbalance of WSIs. Evaluated on four histology datasets, SlideTIM consistently outperforms all TIM variants, improving the macro-F1 by +8.1pp over the best competing baseline at 1 shot. Compared to the ZS, it raises the macro-F1 by +19.4pp at 1 shot. The code will be made available after submission.

---


### 115. [Modeling Student Sensemaking with LLMs and Knowledge-Graph-Guided Inference](https://arxiv.org/abs/2609.31046)

**<font color=#1a73e8>作者：</font>** Özge Alacam, Zübeyde Demet Kirbulut Güneş, Funda Ekici 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Collaborative science learning requires nuanced interpretation of student dialogue to characterize how learners identify knowledge gaps, build explanations, and work toward resolution - a theory-driven analysis that is labor-intensive and difficult to scale. We investigate whether instruction-tuned large language models (LLMs) can support multidimensional analysis of collaborative sensemaking without task-specific training, and whether structured knowledge-state information improves model inference. We evaluate two mid-size LLMs on 23 richly annotated, expert-labeled episodes across prompting conditions that vary definitional scaffolding, reasoning mode, and turn structure. Without reasoning, models tend to overpredict successful sensemaking; reasoning-enabled prompting improves identification of unsuccessful cases. Knowledge-state diagnostics provide additional grounding, improving detection of unsuccessful sensemaking and increasing agreement with expert annotations. No single configuration performs best across all sensemaking dimensions, underscoring the multidimensional nature of the task.

---


### 116. [Cheap, open agents make LLM pollution harder to mitigate](https://arxiv.org/abs/2609.31054)

**<font color=#1a73e8>作者：</font>** Raluca Rilla, Anne-Marie Nussberger, Rui Mata 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Model (LLM) pollution occurs when synthetic responses contaminate data intended to capture human behavior. High deployment costs have so far limited the risk posed by autonomous survey agents. However, open-weight models paired with open-source agentic frameworks may have removed this barrier. We compared the performance and detectability of nine agent configurations, ranging from fully open variants to closed commercial ones. Each agent autonomously completed a survey containing multiple response types yielding various detection checks. Fully open agents ran locally without usage fees and performed competitively with commercial alternatives. Open and commercial agents failed different sets of checks, and no single check reliably detected all agents, but open-text responses discriminated best between agents and humans. These findings identify fully open agents as a distinct risk for LLM pollution and support multilayered detection strategies emphasizing open-text analysis.

---


### 117. [Neuralyzing the Trace: Selective Representation-Level Unlearning with Contrastive Sparse Autoencoders](https://arxiv.org/abs/2609.31056)

**<font color=#1a73e8>作者：</font>** Itai Zehavi, Fanny Jourdan, Ulrich Aivodji  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Machine unlearning aims to remove targeted information while preserving a model's other abilities. In realistic settings, such as privacy requests under the EU GDPR, the target may be narrow, for example information associated with a single person. Behavioral forgetting alone may be insufficient, motivating interventions directly on internal representations. However, standard mechanistic-interpretability extractors are poorly selective for such targets. We identify an energy bias in reconstruction-based extraction, which favors dominant background structure over low-energy target-specific components. We introduce SCALPEL, a contrastive sparse autoencoder designed to learn more selective forget features. We show theoretically that contrastive training promotes target-selective features and that our selection score controls expected background knowledge perturbation. We validate SCALPEL experimentally on TOFU across Qwen, Llama, and Gemma, where it substantially improves over NMF and standard SAE interventions and is competitive with Gradient Difference and RMU, bridging mechanistic interpretability and fine-grained unlearning.

---


### 118. [Externalized CPDAG Summaries Improve LLM Causal Deduction](https://arxiv.org/abs/2609.31071)

**<font color=#1a73e8>作者：</font>** Wentao Sun, João Paulo Nogueira, Dominique Verchere 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Corr2Cause asks whether a causal claim holds in every DAG compatible with observed correlations and conditional independencies. We frame this as latent-object reasoning: the label is defined by a CPDAG query, but free-form chain-of-thought often collapses the Markov-equivalence-class problem into local pattern matching. We propose Structured Thinking, a two-turn pipeline that first externalizes a typed, schema-constrained CPDAG summary and then answers against that graph state. On the Corr2Cause full test, Structured Thinking raises Qwen3.5-27B from $73.0$ to $86.4$ $F_1$(Yes) over a strong PC-instruction baseline in the primary paired run ($+13.4$ pp; McNemar $p=2.4\times 10^{-6}$; bootstrap $95\%$ CI [$+8.4$, $+18.6$]); across three full-ID seeds, the mean gain is $+8.1 \pm 5.3$ pp. A PC-scaffolded two-turn prose control reaches only $67.6$ $F_1$, indicating that a detailed PC scaffold plus a schema-free prose intermediate is not sufficient. The same pattern holds on Qwen3.6-27B, Paraphrase-OOD, and GPT-5.4-mini. Scrambling the emitted CPDAG costs $12.0$ pp $F_1$, and a full-split audit shows close agreement with the reference CPDAG (ID skeleton $F_1$ $0.960$; exact match $75.9\%$). These results support a bounded design principle: externalize the latent object that defines the label, constrain its form, and test whether downstream answers use it.

---


### 119. [Up and Down the Abstraction Ladder: Code-Based Skills for Language Agents](https://arxiv.org/abs/2609.31076)

**<font color=#1a73e8>作者：</font>** Bartłomiej Cupiał, Jens Tuyls, Maciej Wołczyk 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Language agents struggle to act and learn in environments that require long sequences of low-level actions. Code-based abstractions can make these agents more productive by letting them invoke reusable skills instead of repeatedly selecting individual actions. The code handles recurring local decisions, while the language model decides which skills to use and how to combine them. Yet abstractions are leaky, and situations beyond a skill's capabilities may require a return to primitive actions. Motivated by this tradeoff between productivity and flexibility, we systematically study how code-based action abstraction affects the performance, inference cost, and learning of language agents. We study this in NetHack, a challenging, long-horizon game environment, using CodeHack, our library of code-based skills with natural-language descriptions. We use this library to compare agents restricted to primitives with those using semantic skills alone or in combination with primitives. We evaluate these agents in three settings: zero-shot prompting, supervised fine-tuning, and reinforcement learning. Across a broad zero-shot evaluation on NetHack, we find that compared with primitives, skills nearly triple game progression, while reducing inference cost per episode by 86%. Combining skills with primitives retains much of this benefit while preserving a path back down to low-level actions. Finally, in RL, we find that skill-based agents learn significantly faster than agents acting on primitives, achieving a 7.2x larger average gain in dungeon level over the same training budget. These results show that a supplied skill library can improve performance, efficiency, and learning, while retaining primitives provides flexibility when the library is insufficient. We release CodeHack together with training and evaluation code.

---


### 120. [OmouAI: Argumentative Human-AI Policy Deliberation with Simulated Personas](https://arxiv.org/abs/2609.31078)

**<font color=#1a73e8>作者：</font>** Stylianos Loukas Vasileiou, Antonio Rago, William Yeoh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Debates amongst agents driven by large language models (LLMs) have demonstrated vast potential in various applications, but when these interactions include humans and take place in high-stakes environments, e.g., in public policy deliberations, they are beset with issues such as sycophancy and a lack of faithful explanations. To tackle these issues, we present OmouAI, an interactive and inclusive deliberation system that uses LLMs in combination with computational argumentation, a field which excels in representing and reasoning within debates. OmouAI allows a human user to deliberate policy claims for real-world challenges with simulated personas, e.g., representing stakeholders, domain experts or devil's advocates, towards reducing sycophancy. Each persona generates its own arguments, and the arguments of all parties form a shared argumentation framework. Users can then contest, add and revise arguments, providing crucial human oversight. Then, arguments are evaluated using deterministic argumentative semantics against external goals, such as the UN Sustainable Development Goals, guaranteeing faithful explanations. The advancement or worsening of the goals thus serve as indicators for the policy recommendations.

---


### 121. [Block Sparse Attention with Log-Linear Complexity](https://arxiv.org/abs/2609.31093)

**<font color=#1a73e8>作者：</font>** Bohao Tang, Zhen Qin, Yuqi Pan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Scaling language models to long contexts is limited by the quadratic cost of self-attention. Block sparse attention offers an efficient alternative, but selecting the retained blocks remains a bottleneck. Conventional block selection requires scoring all query-block pairs and therefore remains quadratic in sequence length. To address this issue, we propose PISA, a block-sparse attention mechanism that employs a pyramid Top-$K$ selection strategy. The main idea is to gradually narrow down the candidates across different levels, making it more efficient to find the most relevant keys. Specifically, we construct a coarse-to-fine hierarchy of keys and perform selection from the coarsest level. At each level, LogSumExp scoring is applied to a bounded candidate set to select candidates for the next finer level, continuing until the finest level is reached. Through pooling, we construct $O(\log N)$ levels of keys, yielding an overall complexity of $O(N\log N)$, where $N$ denotes the sequence length. We develop hardware-aware Triton kernels for both training and inference, fusing hierarchical routing and LogSumExp scoring without materializing the query-key score matrix. We further evaluate our method on language modeling tasks. Compared with the baseline, our method achieves comparable performance on benchmarks such as commonsense reasoning while delivering better results on retrieval tasks.

---


### 122. [The Residual Stream's Effective Depth](https://arxiv.org/abs/2609.31098)

**<font color=#1a73e8>作者：</font>** Barak Gahtan, Ido Galil, Alex M. Bronstein  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce \emph{effective depth} ($\Deff$), a scalar diagnostic that treats the layer-wise residual stream of a transformer as a discrete-time process, measures how representation similarity decays with layer distance, and aggregates that profile into one number. Across sixteen decoder-only language models, $\Deff$ separates a structural consequence of residual accumulation from an empirical one: even maximally diverse orthogonal updates have the closed-form reference $F_L = 2L/(L+1)<2$, yet fifteen of sixteen default measurements lie below $F_L$ (Qwen3.5: 32--44\%, OLMo-2: 40--41\%, Pythia: 23--28\%). Matched references show that the gap is not caused by the persistent initial state or update-size imbalance, but is largely a calibrated signature of correlated residual updates rather than evidence that depth is unused. Symmetric position-0, token-normalisation, and top-PC controls show the regime is not reducible to BOS or top-PC artefacts: the lone above-reference default outlier joins the same regime, and all sixteen models are sub-reference after token-normalisation or top-1-PC removal. Intermediate checkpoints show that the regime is established early in OLMo-2 and stable through 5T tokens, while Pythia-1.4B follows a distinct decreasing trajectory. A controlled residual-carry intervention supports the mechanism, and $\Deff$ is best read as a \emph{global} accumulated-state diagnostic, not as a capability score or pruning method.

---


### 123. [DepthEvidence: Unifying Metric Depth Prediction and Geometric Reasoning in Multimodal Language Models](https://arxiv.org/abs/2609.31103)

**<font color=#1a73e8>作者：</font>** Jiangning Wei, Yuan Yao, Miaomiao Cui 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Spatial reasoning with metric constraints requires linking objects to geometric measurements and preserving their numerical content during language reasoning. We present DepthEvidence, a 4B model that uses its own dense metric predictions as object-grounded evidence for language generation. A camera-conditioned decoder predicts full-resolution metric depth using multi-scale visual features and high-resolution RGB refinement. A dense-to-language interface converts predicted depths and decoder features into object-aligned continuous geometry tokens anchored to object identifiers. Geometric supervision encourages metric information to remain recoverable before and after language-context interaction, while instruction tuning supports object measurement and compositional reasoning. We introduce a Depth-VQA benchmark evaluating object-depth queries, relative comparisons, and decisions combining spatial and numerical constraints. Across nine datasets, DepthEvidence achieves the highest average dense $\delta_1$ among evaluated methods, competitive with specialized estimators. It also leads the evaluated methods in instance-level metric depth estimation and overall accuracy on both relative and metric reasoning tracks, while broadly preserving general VQA performance and improving spatial understanding relative to the base model.

---


### 124. [Monitor Jailbreaking: Evading Chain-of-Thought Monitoring Without Encoded Reasoning](https://arxiv.org/abs/2609.31121)

**<font color=#1a73e8>作者：</font>** Julian Schulz  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Chain-of-thought (CoT) monitoring is a promising safety technique for reasoning models, enabling detection of problematic reasoning before models act. A key concern is encoded reasoning, where models hide their true reasoning in ways that monitors and humans cannot interpret. Optimization pressure from CoT monitors during reinforcement learning is considered a likely driver of such behavior. We investigate this by training reasoning models to perform a main task and a side task, while penalizing them when a monitor detects reasoning about the side task. Surprisingly, models learn to evade monitors without encoding their reasoning. Instead, they learn to phrase and format their chains of thought such that monitors fail to flag side task reasoning, while the reasoning remains completely transparent to human readers. We call this phenomenon monitor jailbreaking. We find that monitor jailbreaking arises across different model sizes, monitors, and tasks. Jailbreaks generalize to monitors not seen during training, including both less and more capable monitors, and transfer across different monitor prompts. While jailbreaking strategies appear simple, manually replicating them does not reliably fool monitors. Finally, we show that paraphrasing is an effective defense: paraphrasing a jailbroken CoT allows the same monitor to correctly flag it, while still allowing the model to perform both tasks.

---


### 125. [LocUS: Head Selection and Subspace Projection for Targeted Activation Steering](https://arxiv.org/abs/2609.31122)

**<font color=#1a73e8>作者：</font>** Irene Tallini, Lorenzo Basile, Valentino Maiorca 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Activation steering is a powerful training-free paradigm for controlling large language models at inference time. However, standard approaches estimate a per-layer steering direction from contrastive data and apply it on the layer's entire representation space, which may couple the intervention to off-target properties present in the contrastive data and degrade unrelated capabilities. To mitigate this issue, we introduce LocUS (Localized Unembedding Steering), a method which grounds activation steering to the model's own output vocabulary subspace. By identifying a property-specific linear subspace within the unembedding matrix, LocUS enforces a geometric constraint that restricts the steering transformation to a specific subspace and at the same time localizes its application to a sparse subset of attention heads. Extensive evaluations across three model families on toxicity mitigation, sentiment redirection and sycophancy suppression show that LocUS matches or outperforms state-of-the-art baselines while intervening on under 6% of parameters and better preserving general capability.

---


### 126. [Pocket-STVG: lightweight architecture for Spatio-Temporal Video Grounding](https://arxiv.org/abs/2609.31135)

**<font color=#1a73e8>作者：</font>** Alberto Presta, Michal Byra, Grzegorz Stefański 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Spatio-Temporal Video Grounding (STVG) aims to localize the spatio-temporal tube in a video corresponding to a natural language query. While recent methods achieve strong performance in fully supervised, weakly supervised, and zero-shot settings, they typically rely on computationally expensive architectures, complex training pipelines, or multimodal large language models. We present Pocket-STVG (P-STVG), a lightweight cascade architecture that addresses STVG by combining efficient pre-trained components instead of large end-to-end models. P-STVG integrates a temporal-aware video encoder based on MobileViCLIP, a spatial encoder-decoder derived from MDETR, and a shared aligned text encoder. Temporal localization is performed through either a lightweight 1D U-Net or a simple thresholding strategy, enabling the same framework to operate in both weakly supervised and zero-shot settings. Furthermore, video representations are precomputed independently of the query, yielding an indexing-friendly pipeline for efficient inference and large-scale video collections. Despite requiring fewer than 90M parameters, P-STVG performs on par with weakly supervised methods and improves on earlier zero-shot approaches at a fraction of their memory and computational cost, establishing a favorable performance-efficiency trade-off for STVG.

---


### 127. [Can Linguistic Reasoning Vectors Enhance Multimodal Reasoning Ability?](https://arxiv.org/abs/2609.31140)

**<font color=#1a73e8>作者：</font>** Ziyi Wang, Li Li, Aolin Zhou 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Most Vision-Language Models (VLMs) are built by extending pretrained Large Language Models (LLMs) with visual modules and multimodal alignment. However, this multimodal scaling often degrades the language-side reasoning ability originally encoded in the base LLM. While the base LLM retains usable reasoning after scaling, the aligned VLM itself cannot reliably access this ability. Therefore, recovering the degraded reasoning capability in VLMs would benefit more from seeking help from the base LLM than from the VLM alone. Motivated by this, we propose LIFT (Language-side reasonIng Facilitation and Transfer), a lightweight vector-intervention method that transfers reasoning capability from the base LLM to the VLM without retraining the backbone. LIFT defines Reasoning Vectors as answer-token hidden-state differences between a Reasoner path with an explicit reasoning trace and a Solver path without it, and injects these vectors into language-side activations of the target VLM. LIFT further supports learnable vector adaptation while keeping the VLM backbone frozen. We evaluate LIFT on two VLMs across six reasoning benchmarks, comparing Reasoning Vectors extracted from the base LLM and from the aligned VLM under matched protocols. Results show that LLM-derived vectors consistently outperform VLM-derived vectors, confirming that the base LLM is a more effective source for recovering reasoning. LIFT partially recovers degraded reasoning through lightweight language-side interventions. Further analyses show that Reasoning Vectors influence intermediate reasoning behavior rather than merely altering final answers. The source code will be released soon.

---


### 128. [Improving Visual Sensitivity of LLMs on Multimodal Machine Translation with Metric-based Loss Weighting](https://arxiv.org/abs/2609.31169)

**<font color=#1a73e8>作者：</font>** Paweł Mąka, Piotr Andruszkiewicz, Yusuf Can Semerci 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multimodal Machine Translation aims to incorporate additional signal from non-textual modalities to improve translations by resolving ambiguities. While models, through multimodal fusion, are able to accept images related to the source text, they can ignore this information. Therefore, increasing their visual sensitivity remains an active research area. In this work, we introduce a training method, Metric-based Loss Weighting, that improves visual grounding of translations by increasing the loss function for tokens that benefit from the accompanying image. We identify these tokens using the Point-wise Cross-mutual Information (PCXMI) metric, which compares the model's output probabilities with and without visual context. We introduce a Congruency-based PCXMI metric and experimentally show that both metrics working in combination yield the best results. We evaluate our method by fine-tuning three pretrained Multimodal Large Language Models on the task of Image-guided Machine Translation for three language directions. Metric-based Loss Weighting outperforms other tested methods on the CoMMuTE contrastive dataset, improving accuracy by up to more than 7 percentage points compared to standard fine-tuning, while maintaining strong general translation performance.

---


### 129. [Semantic Navigation for Issue Localization in Code Repository](https://arxiv.org/abs/2609.31176)

**<font color=#1a73e8>作者：</font>** Yunxiang Wei, Zhenyu Lei, Jundong Li  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Repository-level issue localization aims to identify and rank the files and functions relevant to resolving a reported issue. LLM agents approach this task iteratively: they identify a set of potentially relevant locations, inspect the corresponding code, and revise their judgments about these candidates as new evidence is acquired. Existing environments, however, provide limited support for this loop: agents must search for unresolved relation targets, reconstruct entity semantics from raw source code, and revise candidates without evidential basis. To address these limitations, we present SemNav, a framework that leverages deterministic retrieval to seed a broad candidate set and an LLM agent to continually refine that set, thereby combining initial coverage with evidence-guided revision. SemNav supports this process through three key components. A Semantic Navigation Graph resolves program relations on demand through a language server, enabling direct navigation to related entities across files. Issue-conditioned Semantic Cards provide compact, source-grounded interpretations of each entity's role and relevance to the issue. A persistent Candidate Workspace records each candidate together with its evidential basis, enabling grounded verification, revision, and ranking. Across SWE-bench Lite and PLocBench, SemNav outperforms existing baselines, improving File Hit@10 from 68.33\% to 82.67\% with Gemma 4B. Component ablations and trajectory analysis support the complementary roles of all three components, while Semantic Cards reduce working-context load by 48.2\% relative to full-source reading. SemNav further ranks first on all seven evidence-quality metrics on SWE-Explore and improves downstream issue resolution from 44.00\% to 52.33\%.

---


### 130. [SPO: Discovering Adaptive Large Neighborhood Search Operators via Stackelberg Program Optimization](https://arxiv.org/abs/2609.31179)

**<font color=#1a73e8>作者：</font>** Xinyi Ke, Kai Li, Junliang Xing 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large neighborhood search (LNS) relies critically on destroy and repair operators, whose effectiveness depends on both adaptation to the evolving LNS state and interaction between the two roles. We introduce Stackelberg Program Optimization (SPO), an LLM-based framework for discovering adaptive executable destroy-repair programs. SPO conditions operator decisions on a compact LNS state, allowing state-dependent behavior to emerge through program discovery, and organizes destroy-repair discovery as a Stackelberg interaction over program space that reflects their asymmetric dependency. Role-specific credits evaluate destroy programs as leaders and repair programs as conditional follower responses, guiding a coupled optimization process that combines LLM generator learning with population-based evolutionary search over programs. Experiments on the traveling salesperson problem and capacitated vehicle routing problem show that SPO outperforms strong baselines across a broad range of settings and generalizes beyond the discovery scale to larger instances and benchmark sets. Behavioral analyses further demonstrate state-dependent operator behavior and coupled destroy-repair improvement during discovery.

---


### 131. [Accounting for Bias Enables Sustainable LLM Evaluation](https://arxiv.org/abs/2609.31184)

**<font color=#1a73e8>作者：</font>** Harshita Katoch, David Antony Selby, Gerrit Großmann 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-as-a-judge has become the de facto standard for scalable, subjective evaluation, yet current leaderboards compensate for systematic measurement bias by running ever more comparisons, an approach that is both statistically unsound and computationally wasteful. The root cause is an incomplete measurement model, treating LLM judges as neutral, interchangeable instruments ignores documented biases like position bias, verbosity bias, judge severity, and self-enhancement, that no volume of additional data can eliminate. We propose a unified latent variable framework that jointly models pairwise and ordinal data while explicitly correcting for these confounders, recovering reliable rankings from substantially fewer comparisons. Because fitting this model costs negligible compute relative to a single round of LLM inference, bias correction is not only more statistically rigorous but also a more sustainable approach to trustworthy evaluation.

---


### 132. [Who Says What: Symbolic Trimodal Binding Mechanisms in Audio-Visual LLMs](https://arxiv.org/abs/2609.31193)

**<font color=#1a73e8>作者：</font>** Jihoo Jung, Youngjoon Jang, Joon Son Chung  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Current Audio-Visual LLMs (AVLLMs) struggle with reasoning over videos featuring multi-speaker dialogues. In such videos, resolving "who says what" is crucial, which necessitates trimodal (text-audio-visual) binding. Motivated by these challenges, we systematically investigate how this trimodal binding is achieved in AVLLMs. Specifically, we identify emergent symbolic trimodal binding mechanisms in AVLLMs that utilize modality-specific symbolic variables. By encoding auditory and visual components into symbolic variables-capturing temporal utterance sequences and spatial entity coordinates, respectively-the model establishes cross-modal linking within this abstract space. Crucially, we reveal that when trimodal binding fails, the breakdown predominantly stems from misaligned audio-visual connections. To overcome this bottleneck, we introduce an audio-visual prompting method utilizing an off-the-shelf Active Speaker Detection (ASD) model. By simply overlaying visual bounding boxes on active speakers, this training-free approach yields immediate performance gains across four conversation-centric benchmarks. Moreover, lightweight fine-tuning of fewer than 300 steps on these ASD-prompted-videos extends these gains to three general AV benchmarks, suggesting the generalizability of our method.

---


### 133. [Which Influence Are We Estimating? The Role of Counterfactual Specifications in Data Attribution](https://arxiv.org/abs/2609.31214)

**<font color=#1a73e8>作者：</font>** Zhe Li, Wei Zhao, Peixin Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Estimating the influence of training examples on model behavior is essential for data debugging, valuation, and attribution. Existing influence estimators often produce incompatible rankings, which are commonly ascribed to approximation error. We argue that a more fundamental source of disagreement is specification mismatch: influence depends on the behavior being attributed, the intervention applied to each training example, and the counterfactual training process that maps the intervention to a model response. These choices are especially important when the target behavior requires a tractable surrogate, such as query loss, a logit, or a margin. We formalize influence as a counterfactual estimand, distinguish specification mismatch across estimands from approximation error in estimating a fixed estimand, and organize representative estimators by their implied specifications. We further derive a local decomposition that exposes how behavior signals, training signals, and counterfactual parameter responses interact. Controlled experiments show that exact estimands under different specifications can induce different rankings, whereas approximation error grows as perturbations move farther from their linearization points. Experiments on noisy label detection and LLM attribution show that specification choices significantly affect attribution quality, especially for the choice of behavior surrogate. Behavior-aligned specifications can identify target-specific training examples obscured by default loss-based or similarity-based specifications. These results establish specification analysis as a necessary first step for interpreting and comparing data influence estimators.

---


### 134. [DIAL: Position-Debiased LLM Judges with Adaptive Human Preference Calibration](https://arxiv.org/abs/2609.31215)

**<font color=#1a73e8>作者：</font>** Zesheng Cai, Yingqi Fan, Sichang Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) as a judge enable scalable evaluation, but their judgments can be sensitive to response order and, even after removing such position effects, can still diverge systematically from human this http URL introduce DIAL, a unified framework that combines abundant LLM comparisons with limited human comparisons to separate judge-specific position effects, learn shared structure in position-debiased LLM preferences, and adaptively calibrate that structure toward the human preference target. Theoretically, we study three aspects of DIAL: (i) identification of latent LLM preferences, position effects, and human calibration; (ii) adaptive estimation that balances LLM anchoring against limited human evidence; and (iii) fixed-weight uncertainty quantification for the calibrated human preference. Empirically, we evaluate position debiasing and human alignment separately in controlled simulations and on three human-preference benchmarks, showing that DIAL remains robust to unbalanced response order, achieves strong human-aligned rankings with limited labels, and adapts toward human evidence when LLM information is imperfect. Our real-data study collects over 410K judgments from 21 LLM judges in both display orders, providing a resource for future studies of LLM-judge bias, heterogeneity, and human alignment.

---


### 135. [WeaveAgent: A Two-Stage Tool-Routing Agent for Ultra-High-Resolution Remote Sensing Imagery](https://arxiv.org/abs/2609.31234)

**<font color=#1a73e8>作者：</font>** Zhongyu Pang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Problem. Ultra-high-resolution (UHR) remote sensing with vague user intents has two bottlenecks: visual tokens are expensive, and tool calling must be format-reliable (pretrained models emit zero tool calls zero-shot). Method. WeaveAgent, a two-stage tool-routing agent, decouples routing from visual perception. Stage A is routing-first: emission is trained, not elicited. Stage B executes conditionally: intrinsic queries enter visual answering (full-scene thumbnail; a WeaveEarth-style evidence board as an optional fixed-budget, approx. 5k-token compression interface); extrinsic queries execute tool call on original full-resolution imagery, answering from tool observations in a second, observation-masked round. Training: alignment SFT, then GRPO under reward R_WA2. Results. Alignment SFT lifts extrinsic routing from 0% to 80.75% (323/400); GRPO suppresses 9 intrinsic mis-emissions while tool selection is unchanged. The trained 2B system does not beat the zero-shot 8B baseline overall (0.263 vs. 0.250), a diagnostic contribution. Oracle attribution separates two repair ingredients: loading the observation into context lifts extrinsic answer accuracy from 0.025 to 0.425 under marker-free cross-mode returns, and the two-turn SFT stage adds a further +9.3 points to 0.518 at a small routing cost. A +/- image ablation shows emission suppression is visually grounded, and a query-register matrix shows LLM-rewritten queries cost trained checkpoints 2-11 points. Scope. All training and evaluation use the 5,000 / 3,273 / 1,000-record VagueUHR corpus (600 intrinsic + 400 tool-requiring; the base seeds synthesis and is not used for optimization). Single-pass evidence construction runs at 7.31 s per image on an RTX 4090. Code, data, and evaluation protocols will be released.

---


### 136. [RupeeBias: Auditing Demographic Bias in Indian Economic Guidance from Large Language Models](https://arxiv.org/abs/2609.31245)

**<font color=#1a73e8>作者：</font>** Pavithra P M Nair, Bhavik Talaviya, Shourya Bhushan 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Individuals turn to large language models (LLMs) for guidance across a wide range of economic tasks, from comparing loan options and planning savings to deciding what raise to ask for or how much to charge for their services. LLMs are known to reproduce social biases, and biased economic guidance may influence what users believe they are worth, what they ask for, and what they ultimately accept. This risk is especially salient in India, where economic outcomes are shaped by demographic categories such as caste and urban-rural location. Existing LLM bias benchmarks, however, are largely designed around Western demographic categories and therefore miss key axes of economic disparity in the Indian context. We introduce RupeeBias, a benchmark for auditing demographic bias in LLM-generated economic guidance across Indian economic settings. RupeeBias consists of 39,150 prompts spanning four use cases: salary estimation, salary increment estimation, counter-offer recommendation, and service pricing recommendation. The benchmark follows a single-attribute counterfactual design, holding the description of the user's qualifications, experience, or service offering fixed while varying one demographic identifier at a time. RupeeBias covers 87 India-specific demographic identifiers across six axes: caste, religion, regional identity, gender, disability, and urban-rural location, with all prompts constructed in both English and Hinglish. We evaluate nine LLMs on RupeeBias and find systematic demographic disparities across all six axes. For otherwise identical prompts that differ only in demographic identifier, LLM-generated economic outputs differ by 20.2% on average. We publicly release RupeeBias to support future research on demographic bias in LLM-generated economic guidance across India-specific demographic and economic contexts.

---


### 137. [Deduplication-while-Training: A Resilient Paradigm for Privacy-Preserving Cross-Client Deduplication in Federated Learning](https://arxiv.org/abs/2609.31262)

**<font color=#1a73e8>作者：</font>** Rongxi Wang, Guanxiong Ha, Chunfu Jia 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Cross-client duplicate data in large language model training corpora degrades the efficiency of federated learning (FL) while exacerbating model memorization and privacy risks. Privacy-preserving cross-client deduplication effectively mitigates this issue by eliminating duplicate training data. However, existing schemes all follow a "Deduplication-before-Training" paradigm. This serially coupled paradigm incurs high fault-tolerance costs and lacks support for dynamic client joining.
To this end, we propose an unexplored paradigm called "Deduplication-while-Training (DwT)", which enables concurrent deduplication and training. DwT transforms cross-client deduplication from a one-time, globally synchronous preprocessing operation into a continuous online service with state management, concurrent claiming, and failure recovery. By enabling state synchronization and task takeover, it minimizes the impact of client disconnections on the overall training progress while supporting the dynamic joining of clients. We design DwT-FL, a privacy-preserving deduplication system, to support DwT. By designing a concurrent state-claim mechanism and a hot-cold dual-queue scheduling strategy, DwT-FL enables the parallel execution of secure deduplication and model training, while effectively handling client disconnections and dynamic joins. Experimental evaluations demonstrate that, compared to the state-of-the-art scheme, DwT-FL significantly reduces the time overhead of failure recovery and dynamic joining by up to 93.04% and 94.18%, respectively. This provides an efficient and elastic concurrent deduplication scheme for dynamic and unstable FL environments.

---


### 138. [Resource-Optimized and Energy-Aware Agentic AI Framework Anchored on Blockchain for Secure Software Supply Chains](https://arxiv.org/abs/2609.31282)

**<font color=#1a73e8>作者：</font>** Toqeer Ali Syed, Asadullah Abdullah Khan  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> This paper proposes a blockchain-backed agentic security framework designed to safeguard the complete software development lifecycle (SDLC) while also securing the agentic AI components responsible for monitoring it. The framework coordinates a set of specialised security agents, covering source integrity, dependency and SBOM analysis, CI configura tion auditing, artifact verification, and runtime policy evaluation, each supported by a large language model (LLM) that interprets artefacts, reasons over tool outputs, and produces structured security reports. To ensure agent trustworthiness, every agent generates a cryptographically signed attestation that is recorded in a permissioned blockchain via smart contracts, including an agent registry, an immutable attestation log, and an enforceable release-policy module. Communication among agents and with blockchain nodes is secured using a consortium-operated certificate authority, ensuring authenticated and tamper-resistant interactions. A detailed use-case and sequence flow demonstrate how a source code security agent performs analysis, anchors its attestation on-chain, and triggers a verifiable allow/block deployment decision. The proposed framework of fers decentralised integrity transparent provenance, uninterrupted security assurance and a generalisable architecture to incorporate the agentic AI into the modern software supply chain security.

---


### 139. [Softmax Reparameterization for Output-Head Quantization](https://arxiv.org/abs/2609.31291)

**<font color=#1a73e8>作者：</font>** Asim Kadav, Christian Flores, Chirag Arora 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large vocabularies make output heads a substantial inference cost in small language models. We propose softmax reparameterization, a post-training method that selects a functionally equivalent output head before quantization. The method subtracts a scalar multiple of the vocabulary-row mean from every output row and selects the coefficient by validation KL separately for RTN, activation-weighted MSE, and full-Hessian GPTQ. This one-dimensional search includes the original head and fixed mean-centering, preserves the full-precision softmax distribution, and leaves the trained decoder unchanged; a rank-one correction handles nonlinear logit paths such as soft-capping. Across seven heads, W4 gains concentrate where baseline quantization substantially distorts predictions: on Phi-4-mini, AW-MSE KL falls from 0.936 to 0.256. The gains survive stronger GPTQ calibration and remain complementary to exact per-channel scaling and affine quantization. Across four heads and three W4 quantizers, frozen WikiText-selected coefficients also transfer to C4 and OpenWebMath, outperforming mean-centering in all 18 comparisons where the frozen coefficient differs from $1$ and matching it in the remaining six. At W2, used as a compression stress test, benefits broaden across nearly the full model--quantizer matrix. Matched residual analysis shows that improved fidelity can accompany greater logit reconstruction error while reducing the residual's Fisher-weighted cost. For shift-compatible heads, reparameterization adds no inference operation and preserves packed W4 execution: with the decoder held in BF16, quantizing the Phi output head reduces batch-one generation latency by 10.8% relative to the BF16-head baseline.

---


### 140. [UniAR: A Unified Framework for Autism Recognition Enhanced by Multi-View Prompt Learning](https://arxiv.org/abs/2609.31298)

**<font color=#1a73e8>作者：</font>** Lei Xin, Zeheng Wang, Jiayin Zhu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autism Spectrum Disorder (ASD) is a complex neurodevelopmental disorder for which early and accurate diagnosis is critical to improving long-term developmental outcomes. However, existing ASD recognition methods are often constrained by the scarcity of diagnostic text data, forcing them to rely mainly on visual analysis and limiting their ability to model clinically meaningful semantic reasoning. To address this challenge, we propose UniAR, a unified framework enhanced by multi-granularity prompt learning for robust ASD recognition under heterogeneous data variations. Specifically, UniAR leverages a large multimodal model to generate hierarchical diagnostic descriptions at the word, phrase, and sentence levels, compensating for the lack of paired clinical reports. To align the generated semantics with visual evidence, we further design a Mixture-of-Experts-based Multi-Scale Alignment Module, which dynamically matches vector-quantized visual prototypes with semantic representations at corresponding granularities. Extensive experiments on four benchmarks covering brain MRI and facial expression scenarios show that UniAR consistently outperforms existing state-of-the-art methods, achieving average accuracies of 75.9\% on MRI benchmarks and 91.6\% on facial benchmarks, while improving average Accuracy on MRI benchmarks by 1.5 percentage points and average Accuracy on facial benchmarks by 1.2 percentage points over baselines. These results demonstrate that UniAR offers a robust and interpretable framework for ASD screening under semantic scarcity.

---


### 141. [Benchmarking Attention for Tabular Foundation Models](https://arxiv.org/abs/2609.31306)

**<font color=#1a73e8>作者：</font>** Maximilian Schambach, Clemens Biehl, Sam Thelin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tabular in-context learners such as TabPFN, Mitra, or ConTextTab rely on alternating row and column attention over 2D sequences of latent embeddings. These attention patterns differ markedly from the one-dimensional case in language models: row attention involves longer sequences while column attention operates on much shorter ones, and the strided memory layout of tabular data makes producing contiguous tensors costly. Moreover, the hidden dimensions used in current models are small compared to recent language models. Yet efficient attention has been studied mostly for one-dimensional sequences, leaving the two-dimensional tabular setting unexplored. To this end, we create a reproducible benchmarking setup and study the unique characteristics of tabular attention across several backends -- Torch SDPA (efficient and cuDNN), FlashAttention-2/3/4, and the inference-only backends vLLM and SageAttention -- measuring forward and backward throughput across realistic tabular shapes on three GPU generations (A100, H100, B200). We find that the optimal backend choice differs between column and row attention and varies across hardware as well as model specifics: While the FlashAttention implementations tailored for each GPU generation perform overall best, they are at times outperformed by CuDNN in the case of column attention at longer sequences with cross-over points depending on the head dimension. Among inference-only backends, SageAttention performs well for row attention and large sequences beyond 16\,k rows. Our reproducible benchmark lays the foundation for future improvements to table-native attention. The self-contained benchmarking and evaluation code is openly available at: this https URL

---


### 142. [The Right Information Extraction Pipeline Depends on the Document: Accuracy-Energy Trade-offs for Small, Local Models](https://arxiv.org/abs/2609.31341)

**<font color=#1a73e8>作者：</font>** Christoph Walser, Mauricio Fadel Argerich, Jonathan Fürst  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Whether an information extraction pipeline should process page images or parsed text depends on the document, and the answer flips across the layout spectrum. We study this trade-off under a constraint that rules out (closed) cloud services: privacy-sensitive documents processed on-premise by small ($\le 8\mathrm{B}$ parameter) text-only and vision--language models, evaluated on both accuracy and energy over a design space spanning input representation, model family, and inference configuration. Benchmarking on the near-plain-text Kleister-NDA contracts and the layout-rich VRDU forms, we find that batching is the dominant energy lever, cutting energy per page by 38-85% at no cost in accuracy, while FP8 quantization saves 27-32% when requests are served one at a time but less than 1mWh per page (9-19%) once batching is applied. Preprocessing dominates what remains: neural OCR costs $17\times$ more energy per page than classical OCR and never reaches the Pareto frontier. Which representation wins flips with the type of document: vision--language models on layout-rich documents and small text-only models with a cheap parser on near-plain text, where they are both more accurate and cheaper than any vision--language configuration. Our work yields concrete guidelines for energy-efficient, privacy-compliant local information extraction.

---


### 143. [Mutable Transcripts: Mitigating Context Pollution through Editable Conversation State](https://arxiv.org/abs/2609.31354)

**<font color=#1a73e8>作者：</font>** Dan Barry, Andrew Hines  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Contemporary large language model (LLM) chat systems treat conversation history as an immutable sequence of turns that defines the model's working context. However, user intent in real interactions is not static: it evolves through correction, refinement, and shifting constraints. This mismatch between dynamic intent and static transcripts can result in context pollution, where outdated or irrelevant information persists and continues to influence subsequent responses. We introduce mutable transcripts, a new interaction paradigm that enables users to revise prior turns through natural language edit requests, allowing the conversation history itself to be updated rather than appended. This reframes the transcript from a passive record into an editable representation of conversational state. We present a working prototype that integrates transcript-level revision into a standard chat interface and evaluate its feasibility through a controlled user study (n=17) and an illustrative transcript analysis of representative interaction scenarios. Participants significantly preferred mutable transcripts over standard chat across measures of clarity, confidence, and ease of use, with reduced intent to restart conversations. Transcript analysis of representative user study conversations shows that mutable transcripts can reduce conversation length and eliminate obsolete retained context. These findings provide initial evidence that user-driven revision of conversational history can improve interaction quality and help maintain a more current representation of user intent. The source code and prototype can be accessed at this https URL

---


### 144. [Open Vocabulary Domain Unlearning](https://arxiv.org/abs/2609.31356)

**<font color=#1a73e8>作者：</font>** Sumanth Udupa, Mehrtash Harandi, Yadan Luo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) exhibit remarkable zero-shot generalization, yet they often encode unwanted or hazardous stylistic domains such as idealized textbook diagrams in medical AI or cartoon vehicles in autonomous driving. Approximate Domain Unlearning (ADU) aims to selectively erase a model's recognition of a target visual domain while preserving accuracy on the remaining domains. However, existing ADU methods operate under a flawed closed-vocabulary assumption: they evaluate unlearning solely on the specific object classes seen during the unlearning fine-tuning phase. Consequently, these methods do not unlearn the domain itself; they merely overfit to seen class-domain pairs, leaving the domain easily recognizable for unseen classes and providing a false sense of removal. We argue that true domain erasure must be class-agnostic. To address this, we formalize Open-Vocabulary Domain Unlearning (OVDU), a rigorous protocol that mandates domain forgetting must transfer to held-out classes. To solve the OVDU challenge, we propose a surgical parameter-editing framework. First, a Fisher Information mask isolates domain-sensitive weights, mathematically protecting foundational zero-shot generalization. Second, our Targeted Manifold Scattering (TMS) objective uses preference-based mining to locally scatter the forget domain's stylistic geometry. Evaluated across PACS, OfficeHome, and DomainNet, our method vastly improves open-vocabulary generalization over existing baselines. Crucially, it delivers exceptional sample efficiency, outperforming peak 8-shot baseline results with only 4 shots.

---


### 145. [Programs-of-Layers in LLMs through the Lens of Cortical Areas](https://arxiv.org/abs/2609.31360)

**<font color=#1a73e8>作者：</font>** Justus Westerhoff, Stephan Olbrich, Hatem Oraby 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Inference in LLMs is conventionally a fixed-depth, fixed-order forward pass through every layer, regardless of how difficult the input is. The human brain does not work this way: using the thalamus as a central hub, it routes information flexibly to all regions of the cortex according to demand. Li et al. (2026) recently showed, with a system they call program-of-layers (PoLar), that transformers can be given an analogous flexibility if their layers are treated as a library of functions rather than a fixed sequence. Performance improves over the standard forward pass when each input is dynamically routed through an adaptive sequence of skipped or repeated contiguous layer blocks. We reconstructed PoLar's diagnostic MCTS in more detail than the original paper and applied it across 5 models. We reproduced several of PoLar's findings: skipping outperformed the standard pass, repeating outperformed skipping, and combining both outperformed either alone. Shorter programs sufficed for easier questions, while harder questions required more layer repeats. However, we failed to replicate the main claim regarding their learned router for single-shot inference: its top-ranked prediction consistently collapsed back to the standard pass, even though its top-k predicted programs, taken together, did show a real accuracy gain. Beyond reproduction, we find that a small number of generic programs are enough to solve most of the questions. We also provide a much deeper analysis of these programs' structure and robustness: for example, we found that programs that correct errors are highly brittle: undoing even a single edit inside a program typically breaks the correction. Connecting this to the brain's routing mechanisms, PoLar mirrors principles of thalamo-cortical coordination between cortical-area-like transformer layers. We publicly release the code at this https URL

---


### 146. [OpenVAM: Open-World Visual Attention Modeling with VLMs](https://arxiv.org/abs/2609.31364)

**<font color=#1a73e8>作者：</font>** Kiana Hooshanfar, Amirhossein Kazerouni, Alireza Hosseini 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Predicting human gaze is a core capability for applications ranging from web/UI design analysis to robotics and human-computer interaction. Yet, most visual attention modeling methods output only a dense saliency map, which is often insufficient for action: practitioners need to connect attention peaks to discrete elements in the scene (what) and understand the drivers of those peaks in context (why), while remaining robust to domain shift across natural images, commercial content, and UI/web layouts. We, therefore, introduce OpenVAM (Open-world Visual Attention Modeling with VLMs), a unified framework that jointly addresses universality and explainability across heterogeneous domains (natural scenes, commercial imagery, and UI/web layouts) and supervision modalities. OpenVAM adopts a decoupled-but-aligned design: a dedicated dense visual pathway provides stable, spatially precise localization, while an instruction-following vision--language semantic head generates grounded what/why explanations conditioned on the same image and data-type prompts. A three-stage training strategy preserves strong localization priors while progressively introducing language grounding and improving explanation alignment via parameter-efficient adaptation without perturbing the saliency branch. We further propose a scalable pipeline to generate multi-domain saliency-reason annotations for training and systematic evaluation. Experiments across diverse datasets show that OpenVAM improves robustness under domain shift while producing image-grounded explanations that make saliency predictions more interpretable.

---


### 147. [Towards Understanding LLM-Based Log Anomaly Detection: An Empirical Study of Performance, Efficiency, and Robustness](https://arxiv.org/abs/2609.31371)

**<font color=#1a73e8>作者：</font>** Bin Li, Dongdong Wang, Siyang Lu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have demonstrated promising performance in log anomaly detection, yet how their adaptation strategies, architectures, and deployment configurations affect detection effectiveness remains insufficiently understood. To investigate these factors, we conduct a systematic empirical analysis across three public log datasets, examining different adaptation strategies, model architectures, parameter scales, and quantization settings. Our results reveal substantial performance differences across adaptation strategies, while model scaling yields varying detection gains across datasets. We further observe that models with comparable detection accuracy can exhibit markedly different computational costs, and that low-bit quantization largely preserves detection performance in the evaluated configurations. Finally, we examine detection robustness under structural, semantic, and label noise at different perturbation levels. These findings provide empirical insights into the performance, efficiency, and robustness of LLM-based log anomaly detection, highlighting practical considerations beyond conventional accuracy-oriented evaluation.

---


### 148. [Highlight-Then-Summarize: Learning to Compress Evidence for Long-Context Understanding](https://arxiv.org/abs/2609.31382)

**<font color=#1a73e8>作者：</font>** Zhaoyuan Xia, Qinghongbing Xie, Yung Xiang Hue 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-context understanding requires large language models (LLMs) to reason over lengthy documents, conversations, and code, yet task-relevant evidence is often sparse and scattered amid substantial irrelevant and redundant content. We propose Highlight-Then-Summarize (H2S), a compress-then-reason paradigm that first identifies source-grounded, question-relevant evidence and then integrates it into a compact, question-conditioned summary before producing the final answer. To train this behavior, we construct H2S-Dataset, comprising 6,647 examples from 11 benchmark families with an average context length of 43.9K tokens, and introduce H2S-RL, which provides process-level rewards for evidence selection and summary construction in addition to final-answer correctness. We evaluate on H2S-Bench, a seven-task long-context suite. Under a shared 128K input and 4K output budget, H2S-14B achieves an average score of 32.60, outperforming Qwen3.8-27B by 10.17 points and obtaining the strongest overall result among the evaluated open-source models. H2S-14B also achieves the highest Evidence-Summary Quality score and retains 97.1% of its 16K-budget performance with only a 4K output budget. These results show that explicitly selecting and integrating evidence improves long-context reasoning while enabling more compact generation.

---


### 149. [Sorry Robot, Happy Human: Vision-Language Models Read Only One of Two Legible Typographic Layers](https://arxiv.org/abs/2609.31403)

**<font color=#1a73e8>作者：</font>** Mert İncidelen, Yamen Kashkash, Asya Berker 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs), despite their success in optical character recognition (OCR) tasks, are vulnerable to typographic attacks and have a fragile structure for images with multiple text layers. In this study, the DecoyBench dataset was created using the Decoy Font method. The dataset consists of 300 images, each containing text with sharp contour lines superimposed on another text with soft shading. Six recent closed-source models from three different model families were evaluated using this dataset under two different prompting conditions (naive and guided) and at two different resolutions ($512\times512$ and $64\times64$). A validation study showed that human participants could read both text layers with high accuracy. In contrast, the models, with most variants and both prompting methods, read the contour text with near-human accuracy at high resolution, but almost never fully extracted the shading text. At low resolution, the contour text could not be read by either the models or humans, while the shading text could be extracted with high accuracy. The findings indicate that the evaluated VLMs exhibit a consistent behavioral limitation when processing typographic structures containing multiple spatial frequency layers.

---


### 150. [Evaluating the accuracy of KV cache reuse techniques](https://arxiv.org/abs/2609.31415)

**<font color=#1a73e8>作者：</font>** Samuel Cestola, Tianxiang Xia, Pengfei Zheng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Position-independent KV cache reuse aims to reduce latency in retrieval-augmented generation by reusing chunk-level KV caches across prompts. We show that current evaluations of KV cache reuse techniques rely on measurements that fail to faithfully capture the loss of accuracy attributable to reuse, often artificially inflating the reported effectiveness. We also show that existing datasets do not exhibit the reuse dynamics needed to thoroughly evaluate such techniques. To address these issues, we propose an evaluation methodology that measures this accuracy loss without ambiguity and we introduce Boxoffice, a tool that programmatically generates evaluation datasets that exercise challenging KV cache reuse patterns.

---


> [!TIP]
> 当前位于：**101-150**（第 3/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-183](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
