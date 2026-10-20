# 🧠 大模型相关研究 | 2026年10月21日

> 本类共 **548** 篇论文：已确认 **507** 篇，待复核 **41** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**201-250**（第 5/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-548](./part-11.md)

---

### 201. [Revealing what benchmark scores hide: Jointly measuring the breadth and reliability of LLM capabilities using accessibility profiles](https://arxiv.org/abs/2610.24957)

**<font color=#1a73e8>作者：</font>** Kazem Faghih, Yize Cheng, Shoumik Saha 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Language model benchmarks assign each question a single outcome from one fixed wording, even though the same underlying request can be expressed in many equivalent ways. We argue that the quantity of interest should therefore not be correctness on one wording, but the accessibility of an inquiry, which we define as the probability that a model succeeds across meaning-preserving formulations. The distribution of accessibility across inquiries reveals a structure that accuracy and existing best-, worst-, or average-case prompt scores collapse: how broadly a model's capabilities extend across inquiries and how dependably those capabilities can be elicited. Two models can have the same average performance while one succeeds across more inquiries unreliably and the other succeeds across fewer inquiries but more consistently, leading to opposite preferences depending on whether the task allows multiple retries until one success or when repeated consistent success is required. Across six benchmarks and more than twenty models, this tradeoff is common: for about half of the model pairs with nearly equal mean accessibility, which model looks better depends on whether one success across five formulations is enough or all five must succeed, quantities we call Access@5 and Reliable@5, respectively. For some pairs the two measures diverge significantly, by up to 10 points in opposite directions. Accessibility also reveals that scaling, reasoning, and prompt optimization can redistribute capability across inquiries in ways aggregate accuracy obscures, sometimes broadening the set of inquiries a model can succeed on while making success on them less repeatable. Accessibility turns formulation sensitivity from a nuisance into a measurable property of capability, distinguishing what a model can sometimes succeed on from what users can actually depend on.

---


### 202. [CoworkEnv: Synthesizing Training Environments for Long-Horizon Cowork Agents](https://arxiv.org/abs/2610.24960)

**<font color=#1a73e8>作者：</font>** Zhongwei Xie, Yiming Du, Jiaxin Bai 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI coworkers must coordinate tools, communicate across turns, and act on changing workspace state while respecting workflow constraints. Constructing training experience for these capabilities requires coherent requests, service records, tool interfaces, and grading checks. We present CoworkEnv, a capability-guided framework for synthesizing executable training environments for AI coworkers. Workflow requirements guide task construction, and programmatic validation with feedback repair checks generated specifications and grading behavior. Teacher executions yield curated demonstrations for supervised fine-tuning (SFT), while student interactions provide rollouts and rewards for reinforcement learning (RL). Using these resources, we train compact PocketWorker models. For Qwen3-VL-8B-Instruct, SFT raises the mean score from 46.6 to 64.1 on Claw-Eval, including a 31.9-point gain on Multi-turn tasks. An SFT-only extension to ClawMark demonstrates applicability across coworker benchmarks. We further compare RL training dynamics across configurations that vary reward processing and credit assignment. Improving training rewards provide preliminary evidence that the constructed environments support policy optimization.

---


### 203. [DeGMatch: Target-Aware Reasoning Data Selection via Deconfounded Gradient Matching](https://arxiv.org/abs/2610.24963)

**<font color=#1a73e8>作者：</font>** Changho Lee, Janghoon Han, Rajdeep Mukherjee 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reasoning post-training on long trajectories has substantially improved the reasoning capabilities of large language models, but scaling such training to large datasets is increasingly expensive. We study target-aware reasoning data selection, where a small reference set specifies a target capability and guides the selection of training trajectories for specialization. We find that existing target-aware methods can exhibit limited target discrimination on long reasoning trajectories, while dominant population-level structure in candidate gradients can obscure finer target-dependent variation during gradient matching. To address these limitations, we introduce Deconfounded Gradient Matching (DeGMatch), which first constructs a target-relevance gate and then reranks candidates using model-specific gradients. DeGMatch centers gradients using the candidate-population mean and removes leading principal directions before target matching, reducing the influence of dominant population-level structure and improving target discrimination. Across mathematics, science, and code, DeGMatch outperforms strong heuristic, target-aware, and reasoning-specific data selection baselines, while remaining effective across selection budgets, model families, and scales. Our code is publicly available at this https URL.

---


### 204. [Visual Sufficiency Landscapes: Understanding Query-Conditioned Reliability in Visual Token Pruning](https://arxiv.org/abs/2610.24968)

**<font color=#1a73e8>作者：</font>** Zhenghan Li, Kexin Sun, Wei Zheng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Different visual token pruning strategies retain different subsets while maintaining similar task performance. This motivates a combinatorial question: how many visual subsets can preserve model behavior, and how does their abundance depend on the query? We introduce visual sufficiency landscapes to characterize this abundance. At a fixed layer and budget, visual sufficiency probability is the fraction of uniformly sampled subsets that jointly preserve the dense model's answer, reference-answer likelihood, and output distribution. Independent sampling replicates separate input variation from estimation noise. Across Qwen2.5-VL-7B, InternVL2-8B, and LLaVA-v1.5-7B, differences between inputs on GQA and TextVQA exceed replication error, and different questions about the same GQA image produce distinct landscapes. Sufficiency probability also improves failure prediction for full pruning methods. On LLaVA, adding this probability increases AUC by 0.1151 for FastV, 0.0683 for VisionZip, and 0.1401 for SparseVLM, while reducing log loss and Brier score. Several architecture-adapted configurations on the other two models reproduce these gains. Under controlled selection rules, predictors trained on the original images reduce log loss on new images by 9.0%, 13.0%, and 14.1%, respectively. These results establish successful-subset abundance as a measurable dimension of local prunability and connect it to the identification of high-risk pruning conditions.

---


### 205. [PRECOCIAL: Pretraining with Code Curriculums via Iterative Search for Accelerated Learning](https://arxiv.org/abs/2610.24970)

**<font color=#1a73e8>作者：</font>** Edward Gu, Ali Payani, Kevin Ellis  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fully synthetic pretraining data generated by symbolic programs can bootstrap downstream training on naturalistic tasks, such as language modeling, but the generating programs have so far been designed by hand. We introduce PRECOCIAL, a method for automatically optimizing programs that generate synthetic pretraining data. Starting from an initial generator program, an LLM iteratively rewrites the program, and each rewrite is scored by pretraining a randomly-initialized transformer on its data and fine-tuning it on the downstream task. Because every score requires training, PRECOCIAL keeps a single network for the entire search, continuing its pretraining for each accepted program instead of training a new network per candidate, making it significantly more efficient. On four language and code datasets, at a fixed fine-tuning budget, optimized programs reach lower perplexity than hand-designed curricula, published procedural generators, random program mutation and the program the LLM writes in the first iteration of the search, and reach the same perplexity as the hand-designed curricula with 9-33% fewer fine-tuning steps. PRECOCIAL also ends with lower perplexity than FunSearch and AlphaEvolve, which train a new network for every candidate, at the same number of evaluations and a lower cost. We also observe that an optimized program generator from one domain transfers to datasets in other domains. Additionally, optimized programs allow for better downstream performance on four different reasoning and problem-solving tasks.

---


### 206. [Rubrics Carry the Standard: Shapley Attribution for Checklist-Based LLM Judges](https://arxiv.org/abs/2610.24971)

**<font color=#1a73e8>作者：</font>** Saeid Asgari, Rui Ying, Sara Malvar 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Checklist rubrics applied by large language model (LLM) judges have become a standard instrument for evaluating open-ended outputs and for rewarding them during training. Two assumptions surround this practice: that leniency or strictness is a property of the judge model, and that a rubric can be improved by asking a model to review it. We test both in a controlled grading task with planted flaws and on two human-labeled datasets, SummEdits and RAGTruth. Holding the judge and the outputs fixed, rubric content moves the pass rate of correct outputs from 2% to 100%, whereas changing the judge model or the rendering of the same checks moves it by a few points. Model self-review then drifts the rubric toward the reviser's own standard: it adds requirements the task never stated and deletes checks that human labels had taught, with three reviser models and on all three datasets. To measure and control this, we show that under all-must-pass aggregation the Shapley value of each check has an exact closed form, which yields per-check catch credit, false-fail blame and unique catches in linear time. Attribution shows that self-review deletes the checks that do unique work and keeps the checks that cause false fails. A change-control gate that combines these quantities with a provenance freeze on label-derived checks holds nearly every drifting revision chain at its starting quality, with identical decisions under three judge models.

---


### 207. [A Measurement Perspective on Benchmarking LLM-Generated Text Detectors using Item Response Theory](https://arxiv.org/abs/2610.24972)

**<font color=#1a73e8>作者：</font>** Yanbin Zhao, Zhipeng Chen, Guangsheng Bao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Benchmarking large language model (LLM)-generated text detectors commonly relies on aggregate detector-level metrics such as accuracy, F1 score, and AUC. Although useful for summarizing overall performance, these metrics provide limited insight into how benchmark composition shapes detector comparisons or which texts distinguish detectors with different response profiles. We propose a measurement-based benchmarking framework for jointly characterizing benchmark heterogeneity and detector behavior using multidimensional item response theory (IRT). By treating benchmark texts as measurement items and detectors as respondents, the framework estimates text-level discrimination and difficulty-location parameters alongside multidimensional detector abilities. We apply the framework to a benchmark of 32K human-written and machine-generated texts across four domains, evaluated by 14 detectors. The estimated IRT item-parameter space reveals distinct but overlapping human-machine distributions, with substantial variation across domains and text lengths. The human-machine label shows the strongest multivariate association with this space, while domain and text length further contribute to benchmark heterogeneity. Detector ability profiles reveal multidimensional and domain-dependent response patterns that are not fully reflected in aggregate performance rankings. As a practical application, clustering texts in the estimated IRT space yields a compact subset of 2,088 texts (6.5\% of the full 32K benchmark) that largely preserves the comparative detector-performance patterns observed on the full benchmark. Overall, the proposed framework provides a principled and interpretable methodology for benchmarking heterogeneous detection technologies while jointly characterizing the measurement properties of the texts used for their evaluation.

---


### 208. [CorrectRTL: Boost RTL Generation Quality Through Automated Self-Correction with Instruction Decomposition](https://arxiv.org/abs/2610.24977)

**<font color=#1a73e8>作者：</font>** Jing Wang, Shang Liu, Hangan Zhou 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have shown strong promise in specification-to-RTL generation. Among the explorations, the self-correction paradigm has significantly advanced LLM-based RTL generation. However, two challenges limit further progress. Existing benchmarks are saturated by advanced LLMs, leaving little room to evaluate the agentic self-correction framework. The monolithic self-correction paradigm rewrites the entire design at once, where LLMs are susceptible to error confusion and corruption of originally correct code. To address the benchmark challenge, we contribute ScaleBench, a more challenging benchmark of 200 complex RTL designs. To address the challenge in methodology, we propose CorrectRTL, an agentic framework that realizes a new decompose-then-correct paradigm, in which the LLM agent explicitly decouples scaffold construction from detailed implementation. CorrectRTL contributes three core techniques: (1)~\emph{Structure-oriented decomposition}, (2)~\emph{Snippet-based RAG}, and (3)~\emph{SVA-based self-correction}. On ScaleBench, CorrectRTL improves Pass@1 from 20.5% to 49.0% (+28.5%). On VerilogEval, CorrectRTL achieves up to 96.1% Pass@1, demonstrating consistent improvements across both simple and complex designs.

---


### 209. [The World as Viewed by 136 Countries: An Open, Curated, Annotated, and Multilingual Dataset of 118 Million State Media Articles](https://arxiv.org/abs/2610.24990)

**<font color=#1a73e8>作者：</font>** Bryan Li, Samar Haider, Grace Kim 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> State media outlets often project their governments' narratives to target both domestic and foreign audiences. Because this content is plentiful and free to access, it appears widely in the web corpora that large language models (LLMs) are trained on and that retrieval systems draw from. However, the prevalence of state media in these corpora and its potential influence on LLM outputs remain largely unexplored. In this paper, we introduce WorldStateMedia, an open dataset of 118 million state media articles from 136 countries in 114 languages. We extract these articles from existing pretraining corpora and annotate each outlet with level of state control from State Media Monitor. Using WorldStateMedia to audit these corpora, we find that, in English web crawls, the share of state media pages from editorially controlled (vs. independent) outlets rose from 39% in 2013 to 93% in 2025. In several low-resource languages, state media make up a substantial share of all web data, such as 17.8% for Uyghur and 7.8% for Belarusian. To characterize the differing narratives of news outlets, we compare Russian and Ukrainian state media in English and in their native languages, revealing asymmetric topical focus and opposing framings of contested issues such as Crimea. Furthermore, in a retrieval-augmented generation (RAG) experiment on territorial disputes, retrieving a country's state media shifts model answers toward that country's claims, most strongly for English-language (foreign-targeted) media. We release WorldStateMedia to support multilingual, cross-national insights on state media at this https URL

---


### 210. [Certified Sparse Attention via Perturbed Retrieval](https://arxiv.org/abs/2610.24991)

**<font color=#1a73e8>作者：</font>** Runguo Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sparse attention speeds up long-context decoding by reading few keys of the KV cache, but existing methods do not control the error of a query, and on real KV caches their errors have heavy tails. We show that perturbing the score of every key with an independent Exp(1) variable turns threshold retrieval into sampling keys with probability proportional to their attention weights. Lowering the threshold along a geometric grid gives nested samples, a Horvitz--Thompson estimate of the output at every level, and confidence bounds that hold simultaneously over all levels, so each head stops at the first level whose certificate meets the target error $\varepsilon$. With fresh perturbations at every decoding step, each certificate fails with probability at most $\delta$ during generation. At a suitable threshold, the estimator reads $O(\varepsilon^{-2}\log(1/\delta))$ values regardless of the context length, and no adaptive method reads fewer, up to constants. A 4-bit scan with deterministic bounds, shared across a grouped-query-attention group, generates the candidates exactly but reads every key. On three LLMs and ten settings at 16K--128K tokens, no certificate is violated, and at equal keys read our 90th-percentile error is 4.6--7.9$\times$ lower than that of the best of 15 baseline families. At equal bytes, the best baselines have 0.6--1.6 times our 90th-percentile error and at least 4.9 times our largest. End to end, our method stays within one point of dense attention on tasks and within 0.1\% in PG-19 perplexity, and the strongest baselines at equal bytes score as well. On CPU, decoding steps at 32K--128K tokens run 1.1--1.4$\times$ faster than dense attention on the same 16-bit cache.

---


### 211. [UpLoop: Upcycling Large Language Models with Gated Loop](https://arxiv.org/abs/2610.25004)

**<font color=#1a73e8>作者：</font>** Tieyuan Chen, Huabin Liu, Yingtao Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Looped large language models trade parameter storage for recurrent computation, but most are trained from scratch. In practice, pretraining with looped depth is expensive, making post-training upcycling of a pretrained non-looped LLM an attractive alternative. We introduce \textbf{UpLoop}, a post-training recipe based on \emph{layer-wise} recurrence. Instead of looping a whole model or a middle block, UpLoop loops each selected layer locally, preserving the pretrained depth hierarchy and avoiding feature-space mismatch. To make loop execution useful, we add hidden-wise gates on the attention and MLP residual branches, so later loops act as progressive refinements rather than redundant rewrites. Empirically, UpLoop breaks the commonly observed saturation at two loops ($R=2$) in prior looped models. Starting from Qwen3-4B Base and applying SFT, UpLoop improves the average accuracy across 20 benchmarks by 6.17\% at $R=3$. We use $R=3$ as the main setting for the best accuracy--cost trade-off, while both native and extrapolated $R=4$ yield further gains.

---


### 212. [ReTrace: Visual Backtracking for Efficient Multimodal Large Language Models](https://arxiv.org/abs/2610.25005)

**<font color=#1a73e8>作者：</font>** Guangzong Si, Dong Wang, Yifan Yu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) encode images into dense visual token sequences, creating substantial attention and KV-cache overhead. Existing visual token compression methods reduce this cost by pruning low-saliency tokens in shallow layers, but this practice couples temporary computational deactivation with irreversible information deletion. We show that this coupling breaks an intrinsic inference pattern in MLLMs. Through layer-wise attention analysis, we identify \textbf{Visual Backtracking}: visual pivots remain spatially stable, yet in middle layers they actively retrieve context from tokens that appeared unimportant earlier. Thus, early low-saliency tokens can be inactive for computation while still being useful for later reasoning. Motivated by this finding, we propose \textbf{ReTrace}, a backtracking-aware compression framework that introduces a dormant token state. ReTrace caches non-pivot tokens outside expensive layer-wise computation, restores them during the backtracking window, and prunes only after their information has been absorbed. Experiments on Qwen2.5-VL and InternVL3 demonstrate nearly 90\% reductions in FLOPs and KV cache, a 2.83$\times$ prefilling speedup, and strong performance retention across complex vision-language benchmarks.

---


### 213. [Conjugate Compilation: Self-Improving Agentic Co-Compilation for Speculative Decoding](https://arxiv.org/abs/2610.25012)

**<font color=#1a73e8>作者：</font>** Annabelle Sujun Tang, Rohan Mahapatra, Christopher Priebe 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As LLM adoption surges, scaling model serving requires unlocking stranded GPU capacity alongside deploying more GPUs. Speculative decoding brings two models into the serving process: a small draft model proposes tokens that a larger target model verifies. Yet compiling these models individually leaves their shared execution outside the compiler's optimization boundary. We introduce CONJUGATE COMPILATION, which reframes speculative decoding as a cross-model compilation problem and jointly optimizes the draft and target models within their shared execution rather than treating each in isolation. Our key insight is that cross-model compilation should be informed by the measured performance of the co-located shared execution it produces: an optimization that improves a kernel in isolation need not improve the models when they execute together. To expand cross-model opportunities, we devise operand layouts that interleave blocks from both models within common tiles, co-locating GEMM and non-GEMM work while preserving their mathematics. We realize CONJUGATE COMPILATION through a self-improving agentic search system in which an LLM edits cross-model optimization plans using the compiler and GPU execution as its environment. Each proposed plan is compiled and evaluated through its co-located shared execution, whose measured score, together with kernel-level verdicts and compiler feedback, informs subsequent proposals, while Monte Carlo tree search accumulates rewards to guide exploration. Across six single-GPU speculative-decoding configurations on NVIDIA B300 and RTX 5090 GPUs, CONJUGATE COMPILATION achieves a geometric-mean per-round speedup of 1.37x over conventional execution. Interleaved kernels raise this speedup to 1.45x, reaching 1.59x in the best case. CONJUGATE COMPILATION also improves GPU utilization on average by 1.46x on RTX 5090 and 1.50x on B300.

---


### 214. [IECLA: Interpretable Emotion Contribution Learning for Affective Image Editing](https://arxiv.org/abs/2610.25015)

**<font color=#1a73e8>作者：</font>** Yijie Guo, Dexiang Hong, Weidong Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Affective image editing (AIE) aims to evoke a target emotion while preserving the content and structure of a source image. Existing methods improve emotional expression or visual fidelity, but the target emotion alone does not reveal which source regions should be changed and which should remain intact, especially in complex scenes. We introduce Interpretable Emotion Contribution Learning for Affective Image Editing (IECLA), a framework that separates source-emotion attribution from target-aware editing. IECLA constructs signed object-level supervision through counterfactual interventions and trains a context-conditioned contribution predictor to localize evidence that supports or opposes the source emotion. At inference, an image-level evaluator estimates the source emotion directly from the input, while the predictor identifies editable and preservation evidence without repeated interventions. A target-aware editing agent then translates this evidence and the desired emotion into localized, content-aware operations for existing editors. Extensive evaluations show that IECLA predicts counterfactual contributions more faithfully on both in-domain and cross-dataset tests, while external VLM and independent human references support the quality of its localized evidence. Across six editing backbones, IECLA consistently strengthens target-emotion expression while preserving image content and structure, and user studies further show improved perceived target expression and naturalness.

---


### 215. [LLM Agents as Suppliers of Physical System Models: Calibration and Acceptance in Modelica](https://arxiv.org/abs/2610.25019)

**<font color=#1a73e8>作者：</font>** Jörg Frochte, Herbert Schmidt  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> To procure a model of a device, a client hands a supplier a description, sometimes with recorded data or a target response, and accepts the model against this handover. We let LLM coding agents act as the supplier on handovers with data, building Modelica models from library components for four simulated systems and a real switching magnet, and ask what acceptance certifies. Several agents reach the noise floor, but a handover admits a set of models: the description leaves parts of the structure open, and the data narrow it only to the agreed accuracy. We therefore accept by membership in this set, not by matching one reference, and add layers above behaviour: a physical invariant exposes an energy-creating model at the noise floor. Interpretability becomes a property of the delivered model, tested on a variant, read where none exists and shaped through the handover. Most failures are fits delivered with a systematic residual on their own fitting data, where the handover left open how close is close enough. In a follow-up, stating a threshold makes the agents compare against it, and more deliveries pass. The argument applies wherever a handover underspecifies a model meant to be read, not only run.

---


### 216. [One Head Away from Language Confusion: Single Attention Heads Across Model Families](https://arxiv.org/abs/2610.25026)

**<font color=#1a73e8>作者：</font>** Jiwon Jeong, Anjelo Jann Laroza, Chaewoon Yoon 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models sometimes reply in an unexpected language, a failure known as language confusion. We ablate individual attention heads in 12 model checkpoints spanning seven model series, using FLORES-200 continuations in five languages and Language Confusion Benchmark (LCB) chat replies. In ten models, zeroing one head causes substantially more departures from the expected language than zeroing any other head in its layer; its LCB pass-rate drop persists, though reduced, under mean ablation. Seven heads move 8.0 to 51.5 percent of all FLORES continuations out of the prompt's language, versus at most 1.4 percent for other same-layer heads; the other three mainly affect explicitly requested languages. These seven heads matter less in base models given plain text. In two models, replacing the values a head reads at the requested-language name with another language's mean makes replies fail and shifts some into that language, unlike a random change of equal size. Replacing a head's output with another language's mean redirects 84 to 99 percent of scored non-English monolingual LCB replies into that language in five models. Yet the requested language's mean improves crosslingual replies beyond every control head only in the two Gemma models, whose baselines are low. Code and results are available in the public repository at this https URL.

---


### 217. [Don't Judge an Agent by Its Messages: Private-State Leakage under Passive Monitoring of Agent Communication](https://arxiv.org/abs/2610.25032)

**<font color=#1a73e8>作者：</font>** Daksh Pandey, Sayon Duttagupta, Xinhai Zou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> An AI agent can reproduce the distribution of its messages and of the receiver's task outcomes while disclosing private information that the task never required. We ask what a passive audit can certify when the auditor knows the authorised sender and the exact observable law but has no trusted pairing of messages with the private states behind them. For a single round, compatible mutual-information leakage forms a sharp interval, and fixing the entire task-relevant message law, with every declared task utility, can still leave a full private bit undetermined; total leakage is determined if and only if, in every task state, the remaining private state or the authorised message is a deterministic function of that state. For a sender, such as an LLM, that selects among its own responses, we prove that in a balanced case its change to the message law within each task state equals $(1-2^{-k})$ times the honest messages' dependence on the attribute, which also sets, up to a constant, how many messages a monitor needs. With Qwen2.5-1.5B-Instruct on a synthetic routing task, selection among 16 responses lets a public decoder recover a private bit in all 8,192 held-out rounds at 98.60\% routing accuracy (honest sender 98.90\%). A monitor that knows the selection rule reaches AUC 0.645 on single messages, close to the ceiling of 0.671 that honest messages predict, and 0.972 over 16, while generic monitors stay near chance. A law-preserving sender built from the same samples recovers the bit in 97.7\% of rounds, and every monitor without the true bit stays near chance against it. A canonical task interface preserves every receiver decision and bounds the remaining information about a balanced attribute by twice the routing-error rate, even for a receiver that shares a key with the sender. These results distinguish what passive auditing can certify from what restricting communication can enforce.

---


### 218. [Beyond the Teacher: Understanding and Preserving Distillation Overshoot in Agentic On-Policy Distillation](https://arxiv.org/abs/2610.25034)

**<font color=#1a73e8>作者：</font>** Jike Zhong, Ming Li, Yuxiang Lai 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) trains agents on their own trajectories using supervision from a stronger teacher. We uncover a counterintuitive phenomenon in multi-turn agentic tasks: a smaller, initially weaker student can substantially outperform its teacher during training, only to regress as distillation continues. We term this phenomenon distillation overshoot. Through decision- and task-level analyses, we trace overshoot to two competing effects of OPD: repairing weak student decisions and eroding successful student choices that the teacher disfavors. Early in training, repair outpaces erosion, allowing the student to combine the teacher's corrections with its own strengths and surpass the teacher. As training continues, erosion overtakes repair, causing these gains to vanish. Motivated by this finding, we propose Success-Preserving On-Policy Distillation (SPOD), which selectively masks conflicting teacher supervision on successful student choices and introduces a soft probability floor to counteract their erosion, while retaining teacher guidance elsewhere. SPOD requires only binary episode success and model probabilities already available during OPD. Across two model families and three agentic benchmarks, SPOD consistently outperforms ordinary OPD and evaluated variants, improving final success by up to 15.2 percentage points and surpassing the teacher by up to 20.0 points. Moreover, SPOD's final checkpoints outperform even ordinary OPD's best intermediate checkpoints in all six settings, demonstrating that beyond-teacher gains can be not only preserved but further extended. Code: this https URL

---


### 219. [VLA-Rolling: Fewer Denoising Steps, Better Control via Adaptive Action Reuse](https://arxiv.org/abs/2610.25043)

**<font color=#1a73e8>作者：</font>** Sicheng He, Yi Pan, Qiuting Yu 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Flow-matching vision-language-action (VLA) models generate an action chunk by iteratively denoising Gaussian noise, but typically execute only a short prefix before replanning with updated observations. Under this receding-horizon paradigm, the unexecuted remainder---the action tail---is discarded, and the next chunk is regenerated from fresh noise. We show that this discarded tail retains transferable denoising progress: action-tail initialization can match or outperform a native 10-step Gaussian baseline using fewer denoising steps. However, the optimal denoising budget varies substantially across samples, indicating that tail reuse should be adapted to the updated environment. Based on this observation, we introduce VLA-Rolling, a lightweight inference framework that reuses action tails through three stages: action-tail inheritance, per-action confidence estimation, and confidence-guided refinement through renoising and denoising budget allocation, while the underlying VLA remains frozen. Across $\pi_{0.5}$, SmolVLA, X-VLA, and MolmoAct2 on LIBERO, MetaWorld, LIBERO-Plus, and RoboTwin 2.0, VLA-Rolling reduces action-chunk inference cost in all 16 model--benchmark pairs, achieving up to a $1.48\times$ speedup, while improving success rate in 14 pairs by up to $15.08$ percentage points. These results show that action tails are not merely discarded predictions, but reusable intermediate states that enable more efficient and accurate VLA inference. These results demonstrate that the action tail can support the generation of better actions with fewer denoising steps. Our project is available at this https URL.

---


### 220. [SteadyThought: Mitigating LLM Under-Thinking via Thought-Level Preference Optimization](https://arxiv.org/abs/2610.25045)

**<font color=#1a73e8>作者：</font>** Zhenyue Peng, Lin Yang, Jie Wang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Flexible switching between reasoning trajectories (i.e., thought switching) has significantly enhanced the reasoning capabilities of Large Reasoning Models (LRMs). However, existing models often switch excessively yet fail to sustain promising reasoning thoughts, a phenomenon termed "under-thinking". While recent efforts suppress switching to mitigate this, such over-correction may discard valuable trajectories. To address this challenge, we propose Steady Thought (ST), a novel thought-level preference optimization framework. ST formalizes under-thinking as a preference issue at switching points, forcing single-path continuations from identified points to yield high-quality reasoning. Then, ST performs thought-level preference optimization by treating the newly generated response as preferred and the original one as dis-preferred. Experiments across multiple models and datasets show that ST effectively reduces token consumption, achieving reductions of up to 63.8%, while maintaining strong reasoning accuracy. Further analysis suggests that ST helps models acquire a generalizable ability to reduce redundant switching across domains and languages. Code is available at this https URL.

---


### 221. [PACT: NVFP4 Data-Flow LoRA Fine-Tuning on Consumer GPUs](https://arxiv.org/abs/2610.25048)

**<font color=#1a73e8>作者：</font>** Lei Gao, Hossein Entezari Zarch, Chaoyi Jiang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fine-tuning language models on consumer GPUs is constrained by computation and memory. Although LoRA reduces trainable parameters and optimizer state, frozen projections remain expensive, and activations retained for backward can dominate memory usage. We present PACT, a LoRA fine-tuning system that accelerates frozen projections with native NVFP4 GEMMs while reducing quantization and dequantization overhead and limiting quantization error. To reduce activation memory, PACT reuses quantized RMSNorm outputs and saves gate/up activations in NVFP4 for backward. To limit numerical error, it preserves BF16 inputs for forward nonlinear operations and calibrates frozen weights offline using GPTQ adapted to NVFP4 scales and quantized activations. Fused nonlinear kernels and cached forward and backward weight layouts reduce quantization and dequantization overhead. Evaluations across multiple models and tasks on a 16\,GB RTX~5080 show lower memory usage and faster LoRA fine-tuning with competitive accuracy, enabling model adaptation on resource-constrained consumer hardware.

---


### 222. [One Skill Takes Over: Clashing Agent Skills and a One-File Fix](https://arxiv.org/abs/2610.25064)

**<font color=#1a73e8>作者：</font>** Parsa Razmara, Seyedarmin Azizi, Ardalan Aryashad  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agent Skills are instruction files that tell a coding agent how to do one job. Users install skills from many authors, so two skills for the same job can be active at the same time. We ask what a model does when both skill files are in its context: does it combine their compatible rules, or follow one skill and drop the other? We build SkillClash, 16 pairs of same-job skills in which code checks every rule and a reference output shows the best result that can be reached. On seven models from five families, from 4B open models to Qwen3-235B and GPT-4.1, a skill's rules are followed 93 to 99% of the time when it is loaded alone and 61 to 62% when a same-job skill is loaded next to it. Most outputs show takeover: every rule that only one skill asks for is followed, and every rule that only the other skill asks for is dropped. The worked examples inside the skills drive this. When each skill file instead ends with one example that follows both skills, takeover falls to 1 to 15% on the six models we tested. Telling the model which skill has priority does not bring the dropped skill back, and telling it to apply both skills brings the dropped skill back only on the two strong models and leaves the interacting rules broken. One merged skill file written by the strongest model we used, Claude Opus 5.5, lets all seven models follow 96 to 99% of the achievable rules. Most of its gain over a plain list of both skills' rules comes from its one worked example, and such an example helps only when it is correct. Code and data: this https URL

---


### 223. [Locate, Then Reason: End-to-End Patch Presence Testing in Stripped Binaries](https://arxiv.org/abs/2610.25071)

**<font color=#1a73e8>作者：</font>** Huaijin Wang, Tongda Wang, Zhibo Liu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Binary patch presence testing (PPT) determines whether a security fix is present in a stripped binary. Prior systems often assume that patch-relevant code is known or successfully matched. Function-level matching is brittle to compilation changes, inlining, finite model context, and missing usage context; moreover, similarity suppresses the patch-sized distinction needed for the verdict. We present PatchAlign, an end-to-end binary PPT workflow, which performs large-scale localization that maximizes recall economically, then the final verdict reasons for patch-specific evidence. PatchAlign uses instruction-aligned retrieval and caller-callee context to accurately locate patch-relevant binary code pieces, then screens the shortlist and compares target binary code with vulnerable and patched references using an LLM. Our experiments indicate that PatchAlign can precisely localize patch-relevant code and determine patch status without a target-location oracle.

---


### 224. [P2N: Reusing Deep Representations for Greater Effective Depth](https://arxiv.org/abs/2610.25076)

**<font color=#1a73e8>作者：</font>** Yiqin Hao, Boyi Zeng, Zitong Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Mathematical problem solving and autonomous agents are increasingly important applications of language models, demanding stronger reasoning capabilities. Computational depth is a key resource for such reasoning, but adding model layers increases both training and inference costs, while test-time scaling incurs substantial additional inference computation. We introduce P2N (Previous to Next), which reuses the previous token's deep representations, already available during generation, to increase effective computational depth with negligible decoding overhead. Specifically, P2N adds the previous token's deep hidden state to the current token's shallow representation, allowing subsequent layers to build on previously completed deep computation. This recurrence extends effective computational depth across tokens, while introducing only a single vector addition per decoding step. We train the recurrence using parallel Jacobi updates restricted to a middle-layer core. Experiments with Qwen-style models show that, at 1.5B parameters, P2N improves GSM8K accuracy by over 10 percentage points under both zero-shot and few-shot prompting, with nearly unchanged decoding latency. The benefits also extend to language modeling and average performance on general downstream benchmarks. on general downstream benchmarks.

---


### 225. [CoEvo-RSI: When Harnesses Evolve, Which Models Should Follow?](https://arxiv.org/abs/2610.25078)

**<font color=#1a73e8>作者：</font>** Jiaqi Su, Guibin Zhang, Jie-Jing Shao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Model--harness co-evolution has emerged as a prominent paradigm for recursive self-improving (RSI) agents, jointly evolving their execution scaffolds and intrinsic capabilities. We study the persistent yet often overlooked brain--body mismatch problem in this paradigm, where an evolving harness (body) demands behaviors its model (brain) has not learned or restricts capabilities it already possesses. We introduce CoEvo-RSI, a RSI framework that advances model--harness co-evolution through agent-driven, bidirectional historical inheritance. Drawing on a shared evolutionary archive and execution feedback, a meta-agent coordinates harness development from historical designs with model checkpoint selection or merging and subsequent adaptation under the selected harness, aligning inherited capabilities with evolving execution requirements to reduce brain--body mismatch. Using only supervised fine-tuning (SFT) on its own rejection-sampled trajectories, CoEvo-RSI makes Qwen3.5-9B competitive with larger models across diverse vertical applications, including multi-agent failure attribution, role-aware text-to-SQL, and smart-home instruction following. It surpasses DeepSeek-V4-Pro on TraceElephant (+14.16 agent accuracy) and GLM-5.3 on HomeBench VM (+4.90 success rate), underscoring the need for brain--body alignment and the potential of bidirectional historical inheritance to advance agent co-evolution.

---


### 226. [Dual-Slot: From Serial Loops to Parallel Slots in Language Models](https://arxiv.org/abs/2610.25086)

**<font color=#1a73e8>作者：</font>** Yiqin Hao, Zitong Wang, Boyi Zeng 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Looped language models increase computational depth by repeatedly applying shared layers, offering a way to improve model quality without adding parameters. However, sequential dependencies between loop iterations increase autoregressive decoding latency. We introduce Dual-Slot, an architecture that reorganizes serial looped computation into parallel latent and prediction slots. Rather than waiting for the current token's latent computation to finish, the prediction slot combines the previous token's deep latent state with the current representation, while the latent slot produces a state for the next decoding step. This shifts the latent dependency across adjacent tokens, replacing two sequential module invocations with a single paired invocation while preserving standard autoregressive generation. To preserve token-level parallelism during training, we use a small number of Jacobi iterations to refine latent states across the sequence in parallel. Experiments on Qwen-style dense and mixture-of-experts (MoE) models show consistent improvements in language modeling and average downstream accuracy. On the 1B dense model, Dual-Slot reduces Pile validation perplexity from 7.25 to 7.00 and improves average five-shot accuracy across nine task configurations by 2.26 percentage points. After supervised fine-tuning, it improves zero-shot GSM8K accuracy by 5.83 and 3.49 percentage points for the 1B dense and A0.6B MoE models, respectively. Across the evaluated batch sizes, Dual-Slot retains 93.1-96.5% of vanilla decoding throughput for the dense model and 98.1-99.6% for the MoE model.

---


### 227. [Beyond Factual Accuracy: A Benchmark for Evaluating Perspective Alignment in LLMs](https://arxiv.org/abs/2610.25087)

**<font color=#1a73e8>作者：</font>** Sunghoon Kim, Sangyeop Kim  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models often generate factually correct responses that fail to maintain user-requested perspectives, blending multiple perspectives and forcing users to filter through unwanted information---a perspective control failure that factual accuracy metrics cannot detect. We introduce PerspectiveBench, a benchmark quantifying perspective alignment by constructing scenarios where multiple valid reasoning paths coexist, and propose the Perspective Alignment Score (PAS) to measure adherence to specified perspectives. Experiments reveal that state-of-the-art models successfully include target content but fail to exclude non-requested perspectives. Providing documents through RAG improves factual grounding but does not resolve perspective drift, as models prioritize comprehensive coverage over strict user constraints. Code and data are available at this https URL.

---


### 228. [Conformal Prediction-Enabled Sequence-level Policy Optimization for Reasoning Language Models](https://arxiv.org/abs/2610.25092)

**<font color=#1a73e8>作者：</font>** Hui Yang, Wan Tian, Tao Ren 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning improves the reasoning capability of large language models through verifiable rewards for mathematical and coding tasks. In token-level methods such as GRPO, clipping acts on individual token ratios while the reward and advantage apply to a complete response. Recent sequence-level methods align these units but still use fixed clipping bands, whose tail probabilities change as the score distribution evolves. We propose Conformal Prediction-Enabled Sequence-level Policy Optimization (CSPO), which adaptively calibrates sequence-level clipping bounds using recent training statistics. The resulting band targets a specified marginal tail budget and adapts to policy drift; calibration conditional on response length requires additional assumptions. We bound the probability that a fresh score falls outside the band by the target miscoverage level plus explicit CDF discrepancy and drift terms. Under additional moment conditions, this bound also controls the objective and gradient error relative to the unclipped GSPO power surrogate. Experiments with the Qwen3-1.7B series show improvements over GSPO on difficult mathematical reasoning benchmarks and ALFWorld, with clipping endpoints that adapt during training.

---


### 229. [Toward Agentic Retrieval-Augmented Generation for Enterprise Retail Workflows over Heterogeneous Data Sources](https://arxiv.org/abs/2610.25096)

**<font color=#1a73e8>作者：</font>** Jeonghwan Choi, Jibin Hwang, Hayoon Park 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Enterprise retail workflows require agents to chain evidence across heterogeneous sources, from structured product and order records to unstructured inquiries and reviews, yet existing agentic RAG benchmarks rarely capture this challenge. To enable controlled evaluation of such workflows, we introduce RetailBridge, a compositional retail benchmark built from persona-driven simulations. Its questions are constructed by linking entities and intermediate answers across heterogeneous sources, requiring agents to identify the relevant sources, carry evidence between them, and produce a grounded answer. To systematically evaluate LLMs on these retail workflows, we develop RetailRAG, a retail-aware framework equipped with auto-schema briefing, source-routed plan chaining, and diagnostic plan revision. RetailRAG consistently outperforms existing agentic RAG baselines across all evaluation axes, serving as a strong reference system for assessing LLM agents on retail workflows. On RetailBridge, evaluating ten LLM backbones with RetailRAG reveals multi-source chaining as the dominant bottleneck across providers and model scales, suggesting that reliable retail agents require explicit cross-source orchestration rather than scaling alone. Code and data are publicly available at \url{this https URL}.

---


### 230. [Deep Fusion Memory: A Chunk-Level Parametric Memory for Large Language Models](https://arxiv.org/abs/2610.25100)

**<font color=#1a73e8>作者：</font>** Rubin Wei, Siyuan Sun, Hao Sun 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models need effective ways to acquire and use external knowledge beyond what they retain from pretraining. Continued pretraining risks catastrophic forgetting, while retrieval at inference time can add substantial overhead. External parametric memory avoids online retrieval, but constructing its training data requires extensive offline search, and output-level interpolation provides only shallow fusion. We introduce Deep Fusion Memory (DFM), a parametric memory architecture that reduces this construction workload and incorporates learned memory into intermediate hidden states. A causal memory predictor learns to generate memory from the preceding context, using retrieved chunk embeddings from the corpus as supervision. The predicted memory is shared across tokens within each chunk and fused into their hidden states through gated cross-attention. Memory prediction and fusion are trained end to end with the backbone frozen, and inference requires no explicit retrieval. Compared with existing parametric memory approaches, which often construct token-level memory targets, DFM requires $32\times$ fewer retrieval queries and $2048\times$ fewer retrieved items to construct its training data. Across six QA tasks, DFM performs better over the strongest baseline by 12.71% on Mistral-7B-v0.3 and 11.19% on Qwen3-8B-Base. Beyond QA, domain adaptation yields average gains of 6.51 and 4.38 points over Qwen3-4B-Base and Qwen3-8B-Base, respectively.

---


### 231. [Explore or Confirm? LLM Agents Misallocate Measurements Under Noise](https://arxiv.org/abs/2610.25111)

**<font color=#1a73e8>作者：</font>** Abdul Karim, Matt Keon  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As model reasoning gets cheaper, the physical experiment becomes the slow and costly step in discovery. Each experiment returns a noisy reading: a high value can mean a good candidate or a lucky draw. With a fixed budget, an AI agent must keep choosing between exploring a new candidate and confirming a promising one by re-testing it. We measure that choice in Wellocate, a simulated assay campaign with known true values. It is built on a generated landscape and on two real protein datasets, GB1 and PhoQ, scrambled so no model can answer from memory. We test five language models as minimal agents, with no tools and no memory beyond the history in each prompt. They misallocate in both directions. Three over-confirm, spending most of the budget re-testing. On the generated landscape one under-confirms, trusting single readings, and there every model ends with a worse final pick than a basic scripted strategy. Each failure has its own cause. The over-confirmers run short of new candidates worth trying: a list of untried candidates cuts their re-testing and, on real protein data, makes two of them pick much better. A running summary of their readings or a description of the landscape changes it by at most five percentage points. For the under-confirmer, re-testing its top candidates in a final round, replayed on its own campaigns, recovers only about a quarter of what it loses by picking the wrong candidate. This suggests confirmation has to run through the whole campaign. We release Wellocate as a benchmark and reinforcement-learning environment with frozen splits and scripted baselines. With it, anyone can measure how an agent splits its budget before trusting it with real experiments, and train agents to split it better. Code, data and the environment are available at this https URL.

---


### 232. [Memory as Belief: Bayesian Evolution of Memory for Self-Evolving LLM Agents](https://arxiv.org/abs/2610.25119)

**<font color=#1a73e8>作者：</font>** Yiming Xu, Qian Yang, Zihan Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents increasingly rely on external memory to accumulate past experiences for continual adaptation. However, effectively reusing memory requires accurately assessing its value, as retrieved experiences may become unreliable when transferred across task contexts. Despite its importance, memory valuation remains largely underexplored, with existing methods relying on historical retrieval success rates that overlook the context dependency of memory usefulness and the varying reliability of estimates under different amounts of evidence. Inspired by the Bayesian brain hypothesis, we propose BEAM (Bayesian-style Evolutionary Agentic Memory), a framework that reformulates memory value evaluation as a parameterized cognitive inference process, where memory value is represented as a context-conditioned dynamic belief rather than a passive historical statistic. Specifically, BEAM infers memory value beliefs from current task contexts and continuously calibrates them using execution feedback as empirical evidence, transforming memory from passive storage into an adaptive cognitive mechanism for continual self-evolution. Extensive experiments across reasoning and code generation benchmarks demonstrate that BEAM consistently improves memory utilization and enables continual self-evolution of LLM agents.

---


### 233. [ClinSDT: LLM-Encoded Clinical Semantic Guidance for Sepsis Treatment via Decision Transformer](https://arxiv.org/abs/2610.25121)

**<font color=#1a73e8>作者：</font>** Yanyan Wu, Guanyu Zhu, Changbin Zhao 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Offline sepsis treatment aims to learn treatment policies from retrospective ICU trajectories. Decision Transformer-based methods provide a natural sequence modeling framework for this task, but they mainly rely on raw physiological states and historical clinician actions. Such raw trajectory tokens may not explicitly capture clinical semantics that clinicians use in practice, such as patient severity, recent treatment response, and current risk priorities. To address this limitation, we propose ClinSDT, an LLM-assisted Decision Transformer framework for offline sepsis treatment. ClinSDT uses a frozen LLM as a semantic bridge rather than a treatment decision maker. It constructs three clinical semantic views from ICU trajectories, namely Profile, Context, and Advisory, and inserts their encoded representations as independent tokens into a Decision Transformer policy. To support policy refinement and rollout, ClinSDT further trains a Treatment-Response Forecaster to estimate the next physiological state, SAPS-II change, and predictive uncertainty from state-action inputs. In the second training stage, the forecaster screens local counterfactual treatment candidates, and only low-uncertainty candidates with lower predicted SAPS-II increase are distilled into the policy after semantic regeneration. During inference, ClinSDT performs closed-loop treatment rollout by refreshing semantic inputs from the currently available patient state. Experiments on MIMIC-III and MIMIC-IV show that ClinSDT achieves consistent relative improvements over representative imitation learning, offline reinforcement learning, and Decision Transformer baselines under the same rollout protocol. Code and data are available at this https URL.

---


### 234. [Behave Like Experts: Fusing Data with Semantic Knowledge for Effective and Efficient Semantic Map Construction](https://arxiv.org/abs/2610.25122)

**<font color=#1a73e8>作者：</font>** Zhu Liu, Zhen Hu, Yuxuan Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Semantic map models (SMMs) construct a graph that reflects conceptual similarity by comparing cross-lingual form-meaning mappings. Experts build such models not only by obeying the data constraint, i.e., the connectivity hypothesis, which states that conceptual nodes belonging to the same form must be connected, but also by incorporating their prior semantic knowledge. Current automatic methods ignore this knowledge, which harms both accuracy and efficiency by enlarging the search space of candidate graphs. In this paper, we fuse the distributional semantic knowledge hidden in the internal representations of language models into a top-down, data-driven algorithm. This expert-like behavior re-sorts the candidates in a huge search space, guided by conceptual semantics similarity. Experiments on a self-collected benchmark of 10 datasets and comprehensive metrics show that our method builds SMMs both effectively and efficiently.

---


### 235. [Memories That Outlive Their Reasons: Dependency-Tethered Memory for Tool-Using LLM Agents](https://arxiv.org/abs/2610.25123)

**<font color=#1a73e8>作者：</font>** Yiqi Wang, Jinqian Ju, Jiaqi Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Agents now act on the Web, publishing packages, models and datasets through registry APIs, and remembering past verifications spares them the work. But a verdict rests on premises. When a signing key is revoked, everything built on it stops passing, yet the advisory names only the key, and the old verdicts of its dependents may never share a retrieval window with it. This non-locality of invalidation turns memory into a liability: in long simulated chats, an agent reading a memory of atomic facts publishes 62% of the objects whose failure lies upstream, each backed by a record that was true when written. Yet derivation is local even when invalidation is not. Tether records, at write time, the exact versions each verdict derives from, and at read time withdraws any verdict whose support has failed anywhere in the store; the agent reads the same fields as before. On Fallout, a generator of versioned worlds with hypothesis-blind simulated histories shared by every memory, Tether publishes 0.3% of upstream-failing objects across three domains when relations are stated with their verdicts, with 37% fewer verification calls than checking everything. A-Mem and Graphiti re-verify most candidates (0.83-0.86 checks per candidate), which limits their savings, yet publish 9% of upstream-failing objects; Mem0 relies on memory more and publishes 42%. Flushing every verdict on any failure is as safe as Tether but costs 32% more checks. The gain over fact memory holds with three open-weight backbones and against a whole-store window. These gains depend on capturing dependencies: when relations arrive in sessions apart from their verdicts, Tether's downstream unsafe publication rate rises to 9.4-22.1%, and a weak writer that misses edges loses safety in the same way.

---


### 236. [Trackable Skill Library Lifecycle Management for Agentic Reinforcement Learning](https://arxiv.org/abs/2610.25126)

**<font color=#1a73e8>作者：</font>** Xi Zhu, Yuanlin Duan, Changyi Yang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Skill-augmented agentic RL has emerged as an effective approach to improving LLM agents on long-horizon tasks. Despite this progress, individual skills may follow distinct trajectories as the policy evolves, with some becoming redundant after the model internalizes their capabilities, others remaining valuable as external scaffolding, and still others turning harmful. However, existing skill library systems fail to identify each skill's true contribution due to free-riding among co-retrieved skills, difficulty confounding across tasks, and the absence of skill-specific counterfactual evidence, which prevents reliable skill lifecycle management. We propose TrackRL, an agentic RL framework where skill tracking drives skill library full lifecycle management. Specifically, within each GRPO group, we turn grouped sampling into online randomized controlled experiments. Independent random injection and within-group contrasts on the same task isolate each skill's true contribution, and reliability-weighted aggregation accumulates evidence across groups. As evidence accumulates, we continuously track skill utility, which measures the skill's causal contribution as external scaffolding, and model mastery, which reflects how far the corresponding capability has been internalized. Along this line, we formulate skill lifecycle management as an evidence-gated state-transition process that governs each skill from generation and admission through protected incubation to retention, retirement, or removal, while a soft capacity bound controls library growth. Experiments show that TrackRL outperforms recent skill-augmented RL baselines in both library-assisted and skill-free evaluation, with further analyses revealing how skill value shifts during policy learning and how evidence-driven state transitions shape skill library evolution. Our code is available at this https URL.

---


### 237. [MemBubble: Benchmarking How Agent Memory Shapes LLM Response Diversity](https://arxiv.org/abs/2610.25127)

**<font color=#1a73e8>作者：</font>** Jiajun Tan, Fei Sun, Xinyu Ma 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Memory serves as the core component of LLM-based agents, enabling personalized responses via extracting and using user preferences from past interactions. However, its use may reduce response diversity, thereby narrowing the range of information available to users. Existing evaluations rely largely on synthetic interactions and cover few memory systems, leaving the effects of memory on response diversity insufficiently evaluated in real-world scenarios. We introduce MemBubble, a benchmark of 1000 instances built on preferences extracted from real user-assistant conversations. To measure the extent to which memory concentrates response distributions, we construct test queries in scenarios distinct from user preferences while preserving topical relevance through shared preference categories. Across multiple LLMs and memory mechanisms, entropy decreases by 34.7% on average compared with directly providing the full interaction history, highlighting the important role of memory processing in diversity loss. We also explore simple user-side interventions and changes in information availability but find that these do not effectively close the diversity gap. Our findings highlight the need to consider preserving diversity and user access to information alongside improvements in personalization when designing and using agent memory systems.

---


### 238. [Many Repairs, One Direction: Steering Code Models Toward Safer Cryptographic API Use](https://arxiv.org/abs/2610.25133)

**<font color=#1a73e8>作者：</font>** Tianhe Lu, Sakuna Harinda Jayasundara, Eric Spero 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Cryptographic API misuse in large language model-generated code can compromise software security. While many existing approaches improve code security by modifying model parameters or inputs, how representation changes associated with different cryptographic API repairs can support a shared intervention for safer code generation remains underexplored. To investigate this, we construct 48,000 matched program pairs across four programming languages and ten cryptographic API misuse categories. Each pair changes a specified API decision while preserving the programming task. Subtracting the misuse program's internal representation from its secure counterpart's gives a repair vector. Across five models, comparisons of mean repair vectors reveal stronger organization by misuse category than by language. These category-specific patterns also support a shared intervention. We introduce CrypSteer, which extracts a shared direction by normalizing repair differences and selecting a principal component aligned with repairs across misuse categories. With model weights fixed, adding one shared direction per model to its internal activations during generation improves aggregate target security rates by 5.28--15.00 percentage points over unsteered generation across languages and misuse categories. These findings connect the shared structure of cryptographic repair representations to a reusable intervention for safer code generation.

---


### 239. [TIRE: Top-Down Formula Instantiation with Reliable Execution for Physics Problem Synthesis](https://arxiv.org/abs/2610.25134)

**<font color=#1a73e8>作者：</font>** Xiaoyu Wu, Zhaoxin Yu, Xinglin Xiao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Advancing physics reasoning in large language models requires scalable training data that connect physical laws, concrete problem scenarios, and verifiable numerical answers. Expert-designed problems offer top-down control over physical laws, conditions, and scenarios, but require costly human effort. LLM-based synthesis from texts scales efficiently, but model-generated answers and assessments leave supervision vulnerable to hallucinations. We introduce TIRE, a framework for Top-Down Formula Instantiation with Reliable Execution that brings knowledge-driven problem construction to large-scale data generation. Top-down instantiation uses reusable physical formulas and their applicability conditions to control the physical relations and numerical configurations of generated problems. Reliable execution establishes reference answers before problem generation, providing a common numerical foundation for problem construction and teacher distillation. Together, these mechanisms combine control over problem content with execution-grounded supervision for both supervised fine-tuning and reinforcement learning. Using TIRE, we construct TIRE-19k, spanning nine subfields of physics. Across 3 backbone LLMs and 4 benchmarks, TIRE-19k outperforms 5 representative datasets with equal amounts of SFT data, exceeding the strongest baseline by 2.86 percentage points on average. Further GRPO raises Qwen3-8B's average accuracy by 1.52 percentage points over its TIRE-19k SFT checkpoint. These results demonstrate the value of generating physics training data from explicit physical knowledge with reliable execution.

---


### 240. [PLANE: Plug-and-Play Fine-Grained Visual Experts for Hallucination Mitigation in Large Vision-Language Models](https://arxiv.org/abs/2610.25146)

**<font color=#1a73e8>作者：</font>** Jianghao Yin, Lang Yu, Qianxi Yu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large Vision-Language Models (LVLMs) commonly suffer from hallucinations, which appear as fabricating non-existent objects or outputting incorrect attributes and spatial relationships in images. Previous works empirically indicate that CLIP-style vision encoders tend to focus on primary objects while ignoring image details, which is one of the causes of hallucinations. To address this issue, we propose plug-and-play fine-grained visual experts (PLANE) comprising two components: LoRA visual experts operating on CLIP for multi-aspect image encoding, and an instruction-aware gate network for adaptive image feature fusion. During training, we construct a fine-grained image-caption pairs dataset, where images are described from three aspects: objects, attributes, and relations between objects. Image-caption pairs from different aspects are used to train the three fine-grained LoRA experts respectively. Aiming at comprehensively evaluate our method's capabilities, we manually annotate a fine-grained hallucination evaluation benchmark for LVLMs which is GPT4-independent during evaluation phase (GIFT). We conduct experiments both on popular hallucination evaluation benchmarks and GIFT. The results show that our method effectively reduces hallucinations across models of different types and sizes while introducing minimal inference latency. Compared to advanced baselines, our model also demonstrates superior performance.

---


### 241. [Morpheus: a fully local, defense-in-depth de-identification engine for Greek clinical text - a benchmark evaluation](https://arxiv.org/abs/2610.25155)

**<font color=#1a73e8>作者：</font>** Filippos-Paschalis Rorris, Nikoleta Stanitsa, Tatiana Rorri 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Background and Objective: Clinical free text cannot leave the hospital without de-identification, yet no de-identification system or benchmark exists for Greek clinical text. We evaluated Morpheus, a fully local de-identification pipeline for Greek clinical documents, on 500 synthetic discharge summaries. Methods: The notes (300 cardiac surgery, 100 cardiology, 100 nephrology) were generated by a frontier large language model (Gemini 3.1 Pro) constrained to authentic Greek hospital document layouts. Notes were pre-annotated at generation; two clinicians then independently reviewed and corrected every note, blinded to each other, with disagreements arbitrated. Primary outcomes were recall over must-redact identifiers and over-redaction of clinical content, measured over must-survive probes. Secondary outcomes: residual leaks flagged by an independent egress-review layer, processing time and reproducibility. Results: Inter-annotator agreement was F1 = 0.998. The de-identification rate was 96.59% (7,666/7,937 identifier instances; 95% CI 96.16-96.96): 98.49% for direct and 93.42% for quasi-identifiers. No patient's own complete identifier survived in any note; of 271 residual instances, 199 (73.4%) concerned institutional identity, chiefly the hospital letterhead. The over-redaction rate was 2.82% (190/6,747 probes; 95% CI 2.45-3.24). The egress guard flagged 2 of 271 residuals, both complete telephone numbers. Two independent runs gave identical verdicts. Conclusions: A fully local, deterministic pipeline removed 98.5% of direct patient identifiers from Greek clinical text while altering under 3% of protected clinical content; most residuals concerned the institution, not the patient. To our knowledge this is the first benchmark evaluation of clinical-text de-identification for Greek and the first quantified evaluation of an independent egress-guard layer.

---


### 242. [Do LLMs Reproduce the Age Gap in Loneliness? Evaluating Survey Simulation against European Survey Data](https://arxiv.org/abs/2610.25158)

**<font color=#1a73e8>作者：</font>** Yuliya Li, Achim Rettinger, Dominik Beyer  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are often used to simulate survey respondents, but matching survey averages does not establish accurate demographic differences. We test whether LLM outputs reproduce within-country age gaps in loneliness using the 2022 EU Loneliness Survey, comparing adults aged 18-34 and 65 or older in France, Italy, Poland, and Sweden. We evaluate simulation with and without age information and direct distribution estimation against a probability-based sample, with a non-probability sensitivity reference. Both human samples show higher mean loneliness among younger adults. Under age-specified simulation with standard response-option order, Mistral Small 4 and GPT-5.6 Terra reverse this ordering under all three prompt framings in three and two countries, respectively, mainly by overestimating older-adult means. DeepSeek V4 Flash preserves the ordering everywhere but underestimates both group means, with errors largely cancelling in France and Italy. Against the probability-based reference, direct estimation has lower absolute age-gap error than simulation for Mistral and Terra in every country. For DeepSeek, simulation has lower gap error but direct estimation has lower group-mean error; these comparisons depend on low-validity older-adult simulation cells. Evaluating LLM outputs as proxies for age groups within countries therefore requires checking both group means and their contrast against human survey data.

---


### 243. [Legal Guidance in the Wild: How Users Seek Legal Help in Real-World LLM Conversations](https://arxiv.org/abs/2610.25159)

**<font color=#1a73e8>作者：</font>** Amirreza Mohseni, Gerasimos Spanakis  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> People ask conversational AI models about their legal rights, obligations, procedures, and personal situations that may have legal consequences. To study this behavior, we first need to distinguish requests for legal guidance from other legally themed discussions and unrelated conversations. We contribute a multi-axis taxonomy of legal queries capturing whether legal guidance is sought, how a request is formulated, and which legal domains it concerns; apply it to 2,122 naturally occurring WildChat-1M conversations; and create a human-reviewed gold evaluation set of 200 conversations. All annotations, model checkpoints, and evaluation code are publicly available. In this enriched sample, 71.1% of conversations containing legal content seek personalized or practical guidance. Rights-and-options advice is the most common primary request type among legal-content conversations, and 25.3% of guidance-positive conversations span multiple legal topics. The gold evaluation set supports a two-stage comparison of ModernBERT-base and ModernBERT-large against a TF-IDF cascade. Our framework supports large-scale studies of legal guidance in conversational AI, and the public release of the annotated data facilitates reproducible research and future model development.

---


### 244. [Indistinguishable Agents: Training Agent Privacy as Twin-World Indistinguishability](https://arxiv.org/abs/2610.25161)

**<font color=#1a73e8>作者：</font>** Jiaming He, Guanyu Hou, Yi Yu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> LLM agents search, shop and send messages for their users, and every action is seen by some party. Existing privacy training rewards agents for not mentioning protected items, yet an observer can infer a private fact from what the agent does. Since an observer learns a fact only if its view changes with the fact, we propose \methodfull (\method), which trains on twin worlds that differ only in the private fact. A frozen distinguisher scores each observer's view by its log-likelihood ratio for the true world, and paired GRPO trains the agent on task success minus this ratio. We prove that this objective controls the Bayes success of every observer on every channel. On shopping and messaging tasks \method removes the leakage that disclosure judges and query-level rewards miss, while the agent still completes its tasks.

---


### 245. [Memory, Know Your PLACE: Governing Lifecycle State and Query-Time Eligibility in Persistent-Memory Agents](https://arxiv.org/abs/2610.25179)

**<font color=#1a73e8>作者：</font>** Chen-Fang Hu, Hong-Han Shuai, Woan-Shiuan Chien  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Persistent memory turns prior interactions into durable agent state, but existing systems provide limited control over whether that state remains valid and whether it should influence a later query. We argue that reliable memory requires governance over both state formation and query-time influence. We introduce PLACE, a factorized governance layer that adds write-side state certification and read-side authorization to a memory backend. A factorial evaluation on Mem0 with Qwen2.5-3B and Qwen2.5-7B isolates the contribution of each mechanism. Results show that write-side governance substantially improves lifecycle state correctness, while read-side governance eliminates measured causal leakage from ineligible memory in the state-correct setting. Their combination achieves the strongest joint performance while preserving query-relevant support. These findings show that reliable persistent memory requires explicit control over both maintained state and query-time information influence.

---


### 246. [Dialogue Generation for Conversational Recommendation Using User Search Interactions and Knowledge Graphs](https://arxiv.org/abs/2610.25182)

**<font color=#1a73e8>作者：</font>** Minsung Hwang, Donggyu Yoon, Gowoon Hwang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large-scale conversational recommendation datasets typically require manual dialogue construction or annotation. We propose SearCl, which automatically generates conversational recommendation dialogues grounded in user search and click behaviors. SearCl segments user interactions into query sessions and derives each recommendation target from content selected after a search query. A configurable probabilistic state machine controls the dialogue flow, while two LLM agents acting as the seeker and recommender generate utterances according to turn-level constraints. To support recommendation, the recommender is provided with knowledge graphs constructed from metadata about the content items used in each dialogue, capturing their attributes and relationships. Using SearCl, we generate 3,538 dialogues from content search and click interaction data, covering 1,731 unique target items. Under an LLM-as-a-judge protocol, the resulting dialogues achieve higher quality scores than dialogues from existing benchmarks. These results demonstrate that SearCl enables controllable and knowledge-grounded dataset construction without human annotations.

---


### 247. [Reranking Answers of Large Language Models with Knowledge Graphs](https://arxiv.org/abs/2610.25185)

**<font color=#1a73e8>作者：</font>** Mikhail Salnikov, Hai Le, Olga Tsymboi 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Answering natural language questions over knowledge graph data is challenging due to the vast number of facts, which can be difficult to process and navigate. One potential solution for this issue is to use mined subgraphs related to the query, although this process still requires extracting these subgraphs. This research presents a solution for extracting subgraphs related to entity candidates from a question-and-answer set, which can be obtained by inferring a large language model by calculating the shortest paths between entities. The proposed approaches detail various features that can be extracted from the subgraphs and reranking models to select the most probable answers from a list of candidates. Experiments were conducted on Wikidata to evaluate the effectiveness of the proposed approaches. This involved enumerating all the main feature types that can be extracted from mined subgraphs and a detailed analysis of the proposed features and reranking method combinations. In addition, a public web application that provides a useful web tool for studying the graph space between question and answer entities has been developed to work with subgraphs. This includes visualization of the extracted subgraph and automatic generation of natural language text to describe it.

---


### 248. [Acharya 2.0: An AI Tutor for Self-Learning Subjects in Hindi](https://arxiv.org/abs/2610.25192)

**<font color=#1a73e8>作者：</font>** Shantipriya Parida, Debasish Dhal, Sonal Khosla 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Text processing is crucial for low-resource languages as it enables the development of tools and technologies that bridge the digital divide and provide equitable access to information and services. By empowering low-resource languages with robust text processing, we can preserve linguistic diversity, enhance education, improve communi- cation, and foster inclusivity in a rapidly digitizing world. Due to the lack of sufficient annotated datasets and lin- guistic resources, it is challenging to develop accurate and reliable language technologies for these low-resource languages. Large Language Models (LLMs) have attracted sig- nificant attention with their performance and the value they produce. However, with the ever-evolving language, adapting LLMs for a specific task is time-consuming and resource-intensive. Thus, Retrieval-Augmented Genera- tion (RAG) has overcome this limitation by augmenting LLMs with external knowledge, thereby improving their efficiency and extensive task-specific adaptation. Most applications of the RAG technique have been limited to English and has seen limited application in In- dic languages. This paper introduces the RAG-powered AI-Tutor application, Acharya 2.0, designed to produce academic assistance to Hindi-speaking students. The client-server-based web application integrates many fea- tures to support students in accessing and interacting with educational content.

---


### 249. [ViCoR: Estimating Visual Necessity via Counterfactual Residuals for Multimodal Medical Data Selection](https://arxiv.org/abs/2610.25202)

**<font color=#1a73e8>作者：</font>** Haotian Gan, Yudong Li, Xintian Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Medical vision-language models often exhibit hidden stratification, where high overall performance masks failures on subtle visual findings and overlapping clinical conditions. We trace this failure mode to modality imbalance during fine-tuning, where strong linguistic priors can suppress visually grounded learning and induce plausible but weakly grounded rationales. Existing data selection methods usually score image-text pairs as holistic units, without separating visually necessary samples from shortcut-solvable ones. To address this problem, we propose ViCoR, a counterfactual-residual-based data selection method for Med-VLM fine-tuning. ViCoR estimates visual necessity through image-dependent optimization residuals, calibrates the resulting scores with medical supervision compatibility, and constructs a diversity-aware fine-tuning subset. Across two backbones, four external generalization benchmarks, and one multi-disease robustness benchmark, ViCoR-selected 20\% subsets achieve the strongest average performance compared with full-data fine-tuning and selection baselines. Gradient-level analysis and perturbation audits further show that ViCoR enriches image-dependent training signals and strengthens image-level and evidence-region dependence. The code will be available at this https URL.

---


### 250. [BrandEval: A Two-Track Multi-Agent Benchmark for Risk-Sensitive LLM Crisis Communication](https://arxiv.org/abs/2610.25208)

**<font color=#1a73e8>作者：</font>** Haotian Gan, Weidong Tang, Hanbin Sun 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Evaluating LLMs for crisis communication requires more than judging isolated responses, because public feedback and competitor actions can reshape trust over time. Existing benchmarks remain largely static and single-turn, offering limited evidence about long-horizon risk-sensitive communication. We introduce \textbf{BrandEval}, a two-track benchmark for product-crisis communication, focusing on public brand responses to product-related safety, quality, service, and trust incidents. BrandEval-Static evaluates stakeholder-aware strategic analysis, while BrandEval-Dynamic stress-tests response policies in \textbf{BrandPolis}, a controlled multi-agent sandbox with consumer feedback, competitor responses, and trust-risk trajectories. We also construct \textbf{BrandSRD}, a Chinese crisis-response dataset, and instantiate a reference Strategic Agent using \textbf{Strategic Rationale (SR)}. Across proprietary and open-source models, we find that static strategic quality is informative but incomplete: it aligns with some end-state outcomes but does not reliably predict volatility and delayed recovery; dynamic stress tests further expose tail-risk failures under manipulative or weakly grounded policies. The code and dataset will be available at this https URL.

---


> [!TIP]
> 当前位于：**201-250**（第 5/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-548](./part-11.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
