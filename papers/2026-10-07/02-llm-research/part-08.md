# 🧠 大模型相关研究 | 2026年10月07日

> 本类共 **505** 篇论文：已确认 **467** 篇，待复核 **38** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**351-400**（第 8/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | **351-400** | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-505](./part-11.md)

---

### 351. [From Transformation to Target State: Rethinking Query Representation for Zero-Shot Composed Image Retrieval](https://arxiv.org/abs/2610.05993)

**<font color=#1a73e8>作者：</font>** Yihe Zhao, Songhe Feng  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Composed image retrieval (CIR) aims to retrieve a desired target image from a query consisting of a reference image and a modification text. This task exhibits an unusual representational asymmetry: the modification text specifies a transition from the reference state, whereas retrieval candidates depict completed target states. This creates a representation mismatch for zero-shot methods that query pretrained vision-language spaces directly with transformation-oriented language. We study this mismatch and reformulate zero-shot composed image retrieval as target-state reconstruction followed by retrieval. We instantiate this formulation with ASAP-CIR, a training-free framework that reconstructs a static target representation using a frozen multimodal large language model (MLLM). The representation combines multiple holistic descriptions with a variable set of importance-weighted atomic semantics, thereby preserving both overall target identity and fine-grained visual constraints. Retrieval then integrates holistic state alignment, atomic constraint grounding, and calibrated target-state evidence aggregation. A controlled text-only diagnostic shows that target-side static query formulations achieve more reliable retrieval than dynamic composed query formulations, particularly when source-state semantics must be suppressed or transformed. Experiments on FashionIQ, CIRR, and CIRCO further characterize the effectiveness and limitations of this representation principle, with the clearest gains on the multi-target CIRCO benchmark. These results show that how composed intent is represented before retrieval is a consequential design choice, distinct from the choice of retrieval backbone itself.

---


### 352. [D-Loop: Looped Diffusion Drafting for Speculative Decoding](https://arxiv.org/abs/2610.06011)

**<font color=#1a73e8>作者：</font>** Kecheng Chen, Yuyang He, Cheng Gong 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Block diffusion accelerates speculative decoding by drafting multiple tokens in one forward pass. However, each position predicts a marginal distribution without observing earlier proposed tokens, limiting draft quality and acceptance length. We identify a concrete failure, the \emph{repetition trap}, in which neighboring positions produce redundant copies of the same token. We explain this tendency theoretically and empirically examine its association with shorter accepted drafts. Recent methods refine marginal predictions with an additional causal head or a separately trained drafter, increasing parameter storage and introducing separate training objectives. We instead propose D-Loop, which introduces \emph{intra-block causal conditioning} within the original diffusion drafter without additional model components. Inspired by semi-autoregressive generation and parameter sharing, D-Loop reuses the same backbone across looped passes. The first pass proposes a block, and the second conditions on a selected prefix to regenerate the suffix in parallel. A complementary prefix--suffix objective trains the shared drafter for both anchor-only prefix prediction and prefix-conditioned suffix prediction. Across eight math, code, and chat benchmarks, D-Loop can beat DFlash and DSpark on Qwen3-4B and Qwen3-8B with obvious gains.

---


### 353. [Differentiable Bit-Widths: Co-optimizing Pruning and Quantization via SVD for Ultra-Efficient LLM Compression](https://arxiv.org/abs/2610.06026)

**<font color=#1a73e8>作者：</font>** Hankyul Kang, Jongbin Ryu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> SVD-based pruning and quantization have recently emerged as a promising strategy for the ultra-efficient compression of large language models. In these methods, compression is performed in two stages: components are first truncated, and the remaining ones are subsequently quantized. Although this decoupled pipeline benefits from both pruning and quantization, it requires separate optimization for each stage and fails to fully exploit their balance, which can lead to suboptimal performance under aggressive compression. To address this limitation, we propose a new LLM compression method that co-optimizes pruning and quantization in a unified framework. Our key idea is a differentiable method for learning component-wise bit-widths, allowing less important components to be assigned 0-bit precision and pruned away. Notably, our method performs favorably against two-stage baselines, even when subjected to extreme quantization settings ($1.61$ bits) designed for ultra-efficiency. Code: this https URL.

---


### 354. [LightMTP: Lightweight Latent Multi-Token Prediction](https://arxiv.org/abs/2610.06031)

**<font color=#1a73e8>作者：</font>** Tamara Czinczoll, Julie Kallini, Gerard de Melo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Next-token prediction (NTP) is the standard pretraining objective for large language models, yet it provides an explicit training signal only for the immediate next token, which can lead models to exploit local patterns instead of capturing longer-range structure and ideas. Multi-token prediction (MTP) addresses this by training models to predict several future tokens. However, existing MTP methods often introduce a large number of new parameters with limited improvements in downstream performance. Latent MTP approaches address this efficiency issue by encoding future tokens into a vector representation. However, these approaches usually rely on external helper models for future token encoding. We propose LightMTP, a lightweight, i.e., parameter-efficient, latent MTP approach that bootstraps the future token representations from the model's own hidden states. Our two LightMTP variants extend supervision to more future tokens without requiring the additional computational overhead of conventional MTP nor the external supervision latent MTP normally relies on. LightMTP adds at most 1% extra parameters, retains better performance on general language modeling benchmarks, and achieves similar gains in planning, coding, and reasoning.

---


### 355. [RocketAgent: A Long-Horizon Engineering Agent for Multidisciplinary Design of Liquid-Rocket Thrust Chambers](https://arxiv.org/abs/2610.06044)

**<font color=#1a73e8>作者：</font>** Junxiang He, Runze Mao, Kun He 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Liquid-rocket thrust-chamber design involves interdependent analyses in which downstream constraints can require earlier design decisions to be revisited. Managing these dependencies across heterogeneous tools requires consistent design information and coordinated updates throughout the workflow. We present RocketAgent, a long-horizon engineering agent for multidisciplinary preliminary design of liquid-rocket thrust chambers. A single plan-owning Coding Agent coordinates engineering skills for performance sizing, subsystem optimization, geometry generation, and multiphysics assessment. A provenance-aware knowledge graph supports method selection, while a typed Design Intermediate Representation maintains shared parameters, artifacts, and decisions. Revision-aware checks invalidate affected results and block superseded inputs, with consequential changes subject to engineering approval. In a representative simulation-based design, RocketAgent continued from an infeasible cooling search through an engineer-authorized operating-point revision, identified feasible subsystem designs, and coordinated subsequent geometry generation and multiphysics assessment to support final configuration selection. Separate module tests assessed surrogate predictions and nozzle adaptation. A two-configuration comparison across three controlled scenarios verified the expected dependency invalidations and superseded-input blocking before solver execution. The representative case demonstrates sustained coordination across a multidisciplinary design workflow, while the controlled tests establish the behavior of the revision mechanisms supporting that execution.

---


### 356. [Backdooring Sparse Autoencoders](https://arxiv.org/abs/2610.06049)

**<font color=#1a73e8>作者：</font>** Enrico Ahlers, Daniel Passon, Tobias Kiecker 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Sparse autoencoders (SAEs) are increasingly used not only to interpret language models but also to intervene on their internal representations. We show that this creates a supply-chain attack surface: a maliciously modified SAE can induce attacker-chosen behavior when inserted into the forward pass of an otherwise unchanged language model. We introduce a decoder-only SAE backdoor that leaves both the underlying LLM and the SAE encoder frozen, restricting the attack to a single auxiliary component at a single insertion layer. Using code generation as a case study, we demonstrate high rates of unsolicited code insertion across three language models and a wide range of insertion layers, as well as trigger-dependent behavior conditioned on a prompt cue. We further evaluate the modified SAEs using HumanEval and selected SAEBench metrics. While attack effectiveness varies across models and layers, strong backdoor behavior can coexist with relatively small changes in several conventional SAE quality measures. These results establish that SAEs can carry behavioral backdoors without modifying the language model itself and should therefore be treated as security-sensitive components.

---


### 357. [ROT: Rotating Hidden States towards Contextual Vectors for Hallucination Mitigation in LVLMs](https://arxiv.org/abs/2610.06056)

**<font color=#1a73e8>作者：</font>** Yijing Du, Xiangcheng Zhan, Shuo Yang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large Vision-Language Models (LVLMs) frequently suffer from object hallucination. Existing training-free interventions primarily manipulate attention weights, which indirectly affect the deep semantics reaching the final predictive layers. In this work, we shift our focus to the hidden state vectors extracted after self-attention and residual addition. Empirical analysis reveals that hallucinated tokens do not simply over-rely on linguistic priors; instead, they exhibit an anomalous contextual deviation, showing significantly lower similarities to both textual and visual contexts in intermediate layers. Motivated by this, we propose ROT, a layer-specific, training-free framework. ROT dynamically detects semantic deviation in the middle layers and applies a norm-preserving rotation to steer the hidden states back toward the local multimodal context plane spanned by the contexts. For subsequent layers, a representational smoothing mechanism is introduced to stabilize the calibrated trajectory. Extensive experiments on multiple benchmarks demonstrate that ROT consistently reduces hallucinations across various model architectures and scales, offering an efficient, geometry-driven solution for grounded generation.

---


### 358. [TrustMI: Causally controlling how assistants trust their users](https://arxiv.org/abs/2610.06064)

**<font color=#1a73e8>作者：</font>** Théo Lasnier, Romain Froger, Maxence Lasbordes 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Model (LLM) assistants routinely decide whether they can trust users and third parties whose competence, intentions, and integrity they cannot verify. This uncertainty matters for safety, as trusting the wrong party can lead an agent to comply with harmful requests or act on malicious instructions encountered during tool use. To study this problem, we define trust as an assistant's willingness to accept vulnerability to the actions of another party and ask whether such behavior can be causally controlled through model activations. We build 2,000 contrastive conversations spanning ability, benevolence, and integrity, where paired responses complete the same request but differ in whether the assistant trusts the user. From these pairs, we learn steering matrices while keeping the model parameters frozen and test them across six instruction-tuned models from three families, finding that steering changes trust decisions monotonically in both directions. We then ask whether this effect extends to several safety-related agent settings involving harmful requests, prompt injections, and insider threats, while using benign-task and reasoning as controls. Our findings provide evidence that trust in the user can be causally controlled along linear directions in model activations and provide a way to study how trust shapes safety-relevant behavior in language models.

---


### 359. [Attention Tax, Handoff Tax: A Stylised Model of When Multi-Agent LLM Systems Help](https://arxiv.org/abs/2610.06069)

**<font color=#1a73e8>作者：</font>** Akshit Anchan, Nayonika Sen  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Recent work on multi-agent LLM systems reaches sharply different conclusions: some results show that a single agent with the same information and compute should dominate a delegated system, others that multi-agent gains grow with task depth. We argue that much of the disagreement comes from modelling different bottlenecks, and introduce a stylised reliability model built around two trade-offs. Decomposition reduces the burden of long contexts but incurs a handoff tax when information is compressed or transferred between agents. Redundancy gains from multiple samples, but its benefit depends on how much their failures are shared. With reasoning budget, verification, and task structure added, the model yields two crossover conditions: decomposition becomes preferable once the attention cost avoided by resetting context exceeds the handoff cost, and parallel sampling at equal budget is eventually preferable when its shared-failure floor lies below the error floor of one agent thinking longer. We connect these regimes to recent theoretical and empirical results. On a ledger-reconciliation task we measure the context-degradation curve and the handoff tax from single-agent and handoff runs alone. From these the model places the crossover at depth 10 and predicts decomposition to win at depths 20, 50, and 100. It does, on step-level and final-balance accuracy, and the decomposed system's success, which the prediction never sees, lands within 9 percentage points of the predicted rate at every depth.

---


### 360. [Cross-Lingual Transferability of Training Data Extraction Attacks to Recover Memorized PII](https://arxiv.org/abs/2610.06093)

**<font color=#1a73e8>作者：</font>** Alexandru Nazare, Agnese Profico, Nicolò Vania 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The robustness of Personally Identifiable Information (PII) protection in Large Language Models (LLMs) is a critical concern, yet the risks associated with cross-lingual data extraction remain under-explored. This study evaluates the vulnerability of English-centric and multilingual models to Training Data Extraction (TDE) attacks when prompted in non-English languages.
We construct a multi-domain PII dataset comprising social media handles, email addresses, and phone numbers and translate the attack contexts into Italian, Spanish, French, and German. Our results show that TDE attacks against both English-centric and multilingual models transfer to different languages: the attacks are successful on translated prompts, even though only the original English prompt might have been included in the pre-training data. A web-presence check on a sample of the translations confirms that they are not available online. The share of English leaks recovered in other languages grows with the multilingual capability of the model, and it drops sharply when the original wording is lost, even without a change of language.
This suggests that native multilingual pre-training facilitates the emergence of latent cross-linguistic bridges that simplify the retrieval of personally identifiable information (PII). We analyze the activations of multilingual large language models (LLMs) and find that different translations of the same prompt are bridged in similar representations, with the strongest alignment in the middle layers.
Our results highlight a fundamental security gap in modern LLMs, necessitating more robust, language-agnostic sanitization strategies for future model alignment.

---


### 361. [From Traces to Agentic Worlds: Agentic Language World Models for Interactive Environment Simulation](https://arxiv.org/abs/2610.06100)

**<font color=#1a73e8>作者：</font>** Quanyu Long, Xiao Chen, Jianda Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Realistic environment replicas are increasingly valuable for training and evaluating LLM agents, yet the original systems may be inaccessible or impractical to reproduce. We explore agentic language world modeling: rather than rebuilding an executable environment, a world model agent serves as the environment for a task agent and supports faithful and stateful simulation. We instantiate this paradigm with Trace2Env, a learning-free framework for settings where the original system is unavailable but historical interaction traces remain accessible. Trace2Env reconstructs these traces into a reusable environment worldbook containing environment schemas, grounded evidence, and induced behavioral knowledge. At runtime, the world model agent actively consults the worldbook together with persistent episodic state to infer each action's observation and lasting state effects. Across nine environments, Trace2Env improves both next-observation fidelity and long-horizon interaction consistency over conventional prompt-based LWMs. In multi-turn interaction, task agent actions generated against Trace2Env remain valid more often when replayed in the real environment, indicating that its simulated dynamics better preserve the consequences of earlier actions across successive turns. These results establish agentic language world modeling as an alternative direction for building realistic environment replicas without reconstructing the original executable system.

---


### 362. [Flash-OPD: Fast On-Policy Distillation](https://arxiv.org/abs/2610.06105)

**<font color=#1a73e8>作者：</font>** Wei Chen, Junle Chen, Yitong Yang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) provides dense teacher supervision on student-generated trajectories, but generating and evaluating long rollouts incurs substantial training cost. Existing acceleration methods reduce this cost through open-loop rollout schedules or closed-loop horizon adaptation. However, supervision compatibility can vary substantially across trajectories, making a single rollout horizon difficult to match their heterogeneous reliable lengths: an overly short horizon may truncate useful supervision, while an overly long one wastes computation beyond reliable regions. Our key insight is that the trajectory-specific reliability boundary need not be predicted before generation. By viewing reliability as the first-passage of accumulated low teacher--student compatibility events, the boundary is inherently unknown before sampling, yet whether it has been reached can be determined exactly from the observed prefix. Building on this insight, we propose *Flash-OPD*, which shifts from rollout-horizon control to adaptive trajectory-level boundary verification. *Flash-OPD* interleaves cached generation with teacher verification and independently stops each trajectory according to its observed compatibility events. To reduce verification overhead, the recent event rate is used only to schedule the next verification point, while the actual stopping decision always relies on the exact cumulative count. This separation prevents estimation errors from causing premature termination while enabling efficient verification during generation. Extensive experiments across diverse datasets and teacher--student settings show that *Flash-OPD* achieves $2.2\times$--$7.5\times$ speedups over standard OPD while maintaining or improving accuracy.

---


### 363. [ORCA: The Annealed Spectral Conditioning Optimizer for Faster, Better LLM Training](https://arxiv.org/abs/2610.06116)

**<font color=#1a73e8>作者：</font>** Yuanshi Liu, Boyuan Jiang, Liang Hou 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern LLM optimizers such as Muon often produce weight matrices with higher effective rank than Adam, yet further spectral control has delivered only modest gains. We identify a tension behind this result: concentrated spectra can suppress gradient directions in coupled weight matrices and slow optimization, while constraints maintained throughout training can limit task-specific adaptation and raise the attainable loss floor. We introduce ORCA (Orthogonal Regularization, Cooled After), a minimal optimizer intervention that applies strong but temporary soft orthogonality regularization early in training, then removes it. This allows the weights to benefit from a broader spectrum early on and adapt freely afterward. Across LLaMA, Qwen3, and fine-grained mixture-of-experts models ranging from 130M to 8B parameters, ORCA achieves lower final validation loss than Muon. Its loss reduction relative to Muon matches or exceeds Muon's reduction relative to Adam. Ablations support the early-shaping, later-release design. Further, ORCA requires no architectural changes and adds minimal overhead.

---


### 364. [Efficient Test-time Adaptation through Candidate Verification and Divergence Shifts](https://arxiv.org/abs/2610.06147)

**<font color=#1a73e8>作者：</font>** Seungmin Oh, Seunghun Kang, Jongbin Ryu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) achieve strong zero-shot transferability but remain vulnerable to target-domain shifts at inference time. Test-time adaptation (TTA) offers a practical remedy, yet most existing VLM-TTA methods follow a prediction-side adaptation paradigm. They use test samples to adjust logits, prototypes, caches, priors, or feature statistics, often incurring additional computational overhead. In this paper, we take a different perspective and reframe VLM-TTA as candidate verification rather than prediction adjustment. We propose Test-Time Correction (TTC), a hypothesis-based correction framework guided by a simple principle: hypothesize, reconstruct, correct. Given a test feature and its top-k candidate labels, TTC treats each candidate label as a hypothesis, reconstructs the feature within the corresponding latent subspace stored in a memory bank, and measures the resulting divergence shift. This shift quantifies how much the candidate subspace and its relations to other candidates change after the hypothetical insertion of the test feature. A correct candidate hypothesis induces only a small shift, whereas an incorrect one perturbs the subspace more strongly. TTC therefore corrects the prediction by selecting the candidate with the minimum aggregated divergence shift. This training-free candidate-verification mechanism avoids iterative optimization and provides a favorable accuracy-efficiency trade-off. Across five TTA settings and 15 benchmark datasets, including zero-shot classification, domain generalization, few-shot classification, base-to-novel generalization, and cross-dataset evaluation, TTC consistently improves accuracy over state-of-the-art VLM-TTA methods while achieving up to 2x speedup, over 3x lower CPU memory usage, and up to 1.4x lower GPU memory usage than the lowest-memory training-free baseline.

---


### 365. [TIGER: Time-Series Classification with In-Context-Learning Gated Ensemble of Representations](https://arxiv.org/abs/2610.06156)

**<font color=#1a73e8>作者：</font>** Johann Faouzi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A representation family is a distinct way of extracting features from time series. Ensemble algorithms that combine several representation families remain the most accurate approach to time series classification. Current state-of-the-art ensembles, most notably HIVE-COTE~2.0, pair a bespoke classification algorithm with each representation family and combine their predictions using a fixed, non-adaptive rule. We present TIGER (Time-series classification with In-context-learning Gated Ensemble of Representations), which instead applies the same small portfolio of three general-purpose classifiers (Ridge, Extra Trees, and Naive Bayes) to four representations from four distinct families, stacking the resulting twelve base learners' predictions into a meta-feature matrix. The final prediction is produced by an adaptive meta-classification rule that chooses, independently for each data set, between a weighted hard majority vote and TabICLv2, a pretrained tabular foundation model used in-context as a meta-classifier, based on the mean number of training samples available per class. On a 142-data-set benchmark drawn from the UCR time series classification archive, TIGER obtains the best mean accuracy, balanced accuracy, and F1-score among six compared algorithms, including HIVE-COTE~2.0, and significantly outperforms each of the other five individually. TIGER's adaptive rule also meaningfully outperforms either of its two constituent meta-classification methods used alone, and its single hyperparameter, tuned using only a twenty-data-set development subset, is shown to generalize to the full evaluation benchmark. We further characterize TIGER's design through an extensive set of ablation experiments and report the design alternatives that we investigated and ultimately discarded.

---


### 366. [Where Did the Repair First Go Wrong? Localizing the Origins of Silent Failures in Agentic Vulnerability Repair](https://arxiv.org/abs/2610.06163)

**<font color=#1a73e8>作者：</font>** Wenji Bai, Muhammad Waseem, Zeeshan Rasheed 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Localizing where an LLM-based agent first fails to uphold security during a repair can show which stage of its workflow needs an additional safeguard. This is difficult for silent failures, which are patches that pass syntactic and functional checks but still contain a security vulnerability. Because such patches give no observable failure signal, existing failure attribution methods, which rely on observed task failures and labelled failure steps, are less suited to them. We propose Security Awareness Gap Evaluation (SAGE), a trace-based method that combines an assessment of the security reasoning recorded at each turn with the reconstructed code history to identify the earliest turn at which a repair diverges from the task's security intent. We evaluate SAGE on 95 confirmed silent failures drawn from 3,684 repair traces produced by six agent frameworks and six base models on SecurityEval and CVEfixes. SAGE assigned an origin in 93 cases. Most origins were an unaddressed security requirement or an inadequate defence choice, and only five coincided with the code change itself. When the agent introduced the vulnerable code, the origin preceded the write in 14 of 19 cases. Repeated scoring and a second judge reproduced the origin type more consistently than the exact turn, and agreement was lowest for traces that kept only the final file.

---


### 367. [MS-Exam-Gen: Source-Grounded Benchmark Construction for Evaluating LLMs on Textual Multiple Sclerosis MRI Knowledge](https://arxiv.org/abs/2610.06170)

**<font color=#1a73e8>作者：</font>** Abdul Basit, Muhammad Abdullah Hanif, Muhammad Shafique  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Biomedical large language model (LLM) evaluation requires auditable assessment of narrow, evolving, source-grounded subspecialty knowledge. Multiple sclerosis MRI (MS-MRI) provides a high-stakes textual-knowledge test case because correct reasoning requires current diagnostic criteria, standardized acquisition and reporting knowledge, longitudinal monitoring concepts, lesion morphology, and recognition of difficult mimics. We present MS-Exam-Gen, a reproducible framework for constructing and auditing a text-based multiple-choice question (MCQ) benchmark for MS-MRI knowledge; it does not evaluate direct MRI image interpretation. MS-Exam-Gen targets source-grounded criteria, protocols, reporting, and differential diagnosis. The framework combines expert-source indexing, exam-oriented topic induction, evidence-grounded MCQ generation, automated quality audits, a same-family consistency screen, and empirical calibration. From a 66-source corpus indexed into 4,289 retrieval chunks, the pipeline produced a locked 3,058-item candidate benchmark spanning 16 topics and 53 subtopics. Evaluation across 12 primary LLM endpoints yielded 36,696 item-level predictions and separated performance over a 42.8-percentage-point accuracy range (89.7% to 46.9%). Across these endpoints, 25.5% of items were missed by at least four. Post-generation audits showed that refreshed construction reduced measurable answer cues, while option-order testing showed that absolute MCQ scores remain position-sensitive. Generated construction labels remain metadata rather than validated psychometric categories. Because expert adjudication and full option-order counterbalancing remain future work, MS-Exam-Gen is not a clinically certified examination. It should be interpreted as an automatically filtered, source-grounded candidate benchmark and reproducible audit workflow for item-level and topic-specific LLM evaluation.

---


### 368. [Anosognosia in LLMs: Probing Self-Awareness of Quantized Computational Substrate](https://arxiv.org/abs/2610.06174)

**<font color=#1a73e8>作者：</font>** Yoshihiro Izawa, Gouki Minegishi, Yoko Yamakata  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Can LLMs recognize degradation in their own computational substrate? Inspired by anosognosia, a neurological condition in which patients fail to recognize impairments in their own abilities, we investigate whether LLMs can recognize degradation in their computational substrate induced by quantization. We first show that existing models fail to self-report their quantization state, even when provided with their own generated text as an external cue. Linear probing reveals that, while generated text carries almost no trace of quantization, internal representations contain clear, method-specific fingerprints. Through training, models learn to identify severely degraded outputs such as those of 4-bit models by comparison, yet still fail to do so from a single output. A shared LoRA trained jointly across quantization levels succeeded in reading out internal fingerprints, but fails on unseen quantization methods, merely mapping method-specific fingerprints to labels. Whereas external self-observation can restore awareness in some cases of human anosognosia, our results suggest that the more promising route to enabling such awareness in LLMs may lie in their internal representations. Our results highlight fundamental limits of generalizability to LLM self-monitoring.

---


### 369. [Auditable Clinical Timeline Reconstruction with Provenance-Aware Evidence Graphs](https://arxiv.org/abs/2610.06177)

**<font color=#1a73e8>作者：</font>** Judith Jeyafreeda Andrew  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A patient-timeline reconstruction system is auditable only if it keeps the mentions behind each answer, records how facts were revised, and declines to answer when the evidence is not in the text. This study tests these three properties on a fully synthetic corpus (1,000 patients, 3,353 notes, 220 revision edges). Two provenance-aware Evidence Graph operators reduced the node-plus-edge count to 67% and 63% (77-78% of serialized size) while preserving every answer and mention link across 6,813 query points answerable by recency; a fixed-window baseline returned no value for 53.4% of points, unflagged. On evidence-unavailable controls that announce the omission, a BioClinicalBERT gate and a zero-shot LLM gate responded mainly to the announcement. On marker-free controls, BERT abstained on 0 of 81 notes while its accuracy fell from 93.8% to 59.3% across all three relation classes; the LLM's coverage fell from 75.6% to 27.7% on notes its own model family judged undeterminable. Against 482 regenerated gold spans, the LLM's cited evidence reached recall 0.850 and precision 0.864; BERT's span head, trained without span labels, did not localize evidence. A temporally versioned provenance graph stored abstentions as typed, queryable edges. The clean task admits a 0.651-accuracy shortcut, and results describe implementation behaviour on synthetic data, not clinical performance.

---


### 370. [Bridging the Evidence-to-Execution Gap:A Reflective Agent for Multi-Objective Peptide Design](https://arxiv.org/abs/2610.06190)

**<font color=#1a73e8>作者：</font>** Haosen Zhang, Yang Yang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) can reason over scientific literature to devise design strategies, yet fail to reliably implement them for biological sequences. While protein generative models learn sequence patterns, they lack the capacity to incorporate literature evidence for multi-step reflective reasoning, forming an evidence-to-execution gap between scientific reasoning and sequence manipulation. We present EASER (Evidence-Aware Sequence Engineering with Reflection), a reflective agent bridging reasoning and sequence generation via a learned property interface of offline-trained, fixed low-rank matrices. The agent steers a diffusion generator by combining these matrices, proposing intervention hypotheses (anchors, editable positions, control coefficients) grounded in retrieved evidence, sequence context and past results. A Probe-and-Steer mechanism validates interventions and allocates samples according to predicted property responses, with outcome reflection informing subsequent decisions. Evaluated on multi-objective antimicrobial peptide design (optimizing activity, non-hemolysis and non-toxicity), explicit hypothesis formulation delivers better multi-objective performance than direct action generation under identical decision conditions. Ablation studies verify the importance of evidence retrieval, episodic history, reflection and Probe-and-Steer. Over six repeated trials, EASER obtains the highest mean hypervolume and lowest mean IGD+ on screened candidates compared with competing baselines. Our work demonstrates how an executable property interface and iterative feedback link scientific reasoning to targeted peptide sequence generation.

---


### 371. [Judged Useless, Queried Anyway: Tool-Using Agents Rarely Turn Their Own Evidence Judgments into Stopping Decisions](https://arxiv.org/abs/2610.06191)

**<font color=#1a73e8>作者：</font>** Chubin Zhang, Zhenglin Wan, Xingrui Yu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> An agent whose tool keeps returning nothing useful should stop relying on it. In a retrieval environment with controlled source failures, we separate how agents judge results from what they do. We compare stopping at the same step after longer and shorter runs of results the agent judged useless; this contrast is zero for clock- or deadline-driven stopping. Where we record their judgments, the seven agents we test call a failing source's results useless 97-100% of the time, yet most of them rarely stop on that judgment. Prompt cues change when they stop but not what they stop on. Permission to answer from memory and a reasoning mode can bring early stops regardless of evidence, a stated budget moves the 7-8B models' stops to the deadline, and a stopping rule or call cost in the prompt is followed at most partly. Stopping follows the evidence only when the harness enforces an integration step that makes the agent answer after five consecutive results it judged useless. This step raises failing-source success for every model, keeps the stopping point fixed when the budget doubles, and needs no extra judgment call when the agent states its judgments. A pre-registered replication on 300 fresh questions confirms the dissociation and the rule's effect.

---


### 372. [Copies or Sources? Measuring How LLM Aggregators Count Restated Evidence in Multi-Agent Systems](https://arxiv.org/abs/2610.06192)

**<font color=#1a73e8>作者：</font>** Jianxin Gao, Runze Li, Tianyi Yu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-agent systems built on large language models (LLMs) restate observations as a matter of course: relays forward them, shared boards repeat them and discussion rounds echo them. An aggregator that pools such messages should count sources, not statements. We convert a reported probability into units of independent readings, which assigns every restatement a copy weight, 0 for an aggregator that counts sources and 1 for one that counts every statement, and yields the implied decision under any cost structure. Three testbeds hold the evidence fixed and vary how it is restated: message logs with an exact Bayesian oracle, web documents with appended copies, and logs written by LLM agent teams under four communication protocols. Across four models from three providers, a forwarded copy counts for 0.06 to 0.42 of a new reading, mostly because some replies count every statement. On 5% to 40% of logs that state one reading three times, the reported belief implies an early commitment that the oracle never makes. The models that count copies least and most on controlled logs do so on web copies and agent-written logs as well. A one-paragraph declaration of what a copy contributes brings the copy weight on controlled logs to 0.08 or less. A rule that has agents refer to readings instead of restating them cuts belief-implied early commitment from 11.2% to 1.1% and preserves genuine corroboration.

---


### 373. [EORestore-Agent: Fidelity-Guided Agentic Restoration of Remote Sensing Images with Composite Degradations](https://arxiv.org/abs/2610.06196)

**<font color=#1a73e8>作者：</font>** Heli Qi, Zeqi Zhou, Jingjun Yi 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Remote sensing images often carry composite degradations, in which haze, cloud, noise, blur, low light, and low resolution coexist. Restoring them requires deciding which tool to apply, in what order, and when to stop, yet no clean reference is available at inference time to verify these decisions. All-in-one models trained on single degradations converge to a narrow PSNR band as degradations accumulate. To formulate real-world remote sensing restoration as a traceable trajectory, we present EORestore-Agent, which replaces this unmeasurable objective with reference-free, verifiable per-step decisions. A fine-tuned vision-language model reports all residual degradation types, whose tool pools are scored together, so the restoration order emerges from step-wise selection. A relative quality scorer, trained with full-reference supervision on synthetic degradation chains, predicts the changes in PSNR, SSIM, and LPIPS from the current image to each candidate. A step is accepted only when no predicted change is negative and the predicted PSNR gain is positive. Otherwise, the agent keeps the current image. On a synthetic Landsat-8 benchmark with six degradation types, EORestore-Agent improves PSNR by 2.3 to 3.2 dB over the strongest retrained all-in-one baseline on composites of two to six degradations, whereas zero-shot natural-image agents fall below the degraded input in PSNR in 17 of 18 settings. Replacing the learned scorer with no-reference quality differences costs 1.1 to 4.6 dB. The remaining harmful steps are small and cluster near the acceptance threshold. Sentinel-2 examples illustrate transfer to real atmospheric degradation without retraining.

---


### 374. [Do Small Language Models Learn to Negotiate? A Controlled Scaling Study of RL-Trained Sellers](https://arxiv.org/abs/2610.06204)

**<font color=#1a73e8>作者：</font>** Pedro Tabacof, Sagar Joglekar  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents are starting to own the full customer experience. Soon, LLMs may be selling and buying on behalf of companies and customers respectively. Small models are more cost-efficient at scale, but can reinforcement learning train them into competent sellers? We train four Gemma 4 checkpoints (2.3B to 31B effective parameters) with GRPO on a programmatic utility reward for bilateral multi-issue bargaining, and evaluate every arm on the same 1,152 negotiations against two frontier buyers it never saw in training. With the same learning rate ($10^{-6}$) for every size, the gain of the RL model over its base rises from $+0.001$ at 2.3B to $+0.078$ at 31B. Each size was trained once and the two smallest checkpoints use a different architecture, so we fit no scaling law. Tripling the learning rate, with the same or fewer training steps, improves on the shared rate at every size by $+0.032$ (2.3B) to $+0.081$ (4.5B). In exploratory comparisons with two frontier models run as sellers, the 12B seller trained at the tripled rate scores above both, though its untrained base already scores as high as they do. The 4.5B seller at that rate shows no detectable difference from either and fits on one 48 GB GPU. A further 2.3B arm at ten times the shared rate raises pooled score, but its gain concentrates on the evaluation buyer that shares a model family with the training pool. These results suggest tuning the learning rate before concluding that a small model cannot learn to negotiate, and testing against buyers from more than one model family.

---


### 375. [AI-Decision Checkpoints for AI-Augmented Business Process Management: Framework and Educational Instantiation](https://arxiv.org/abs/2610.06207)

**<font color=#1a73e8>作者：</font>** Amin Jalali  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs), Retrieval-Augmented Generation (RAG), and AI agents are increasingly embedded in operational business processes. Yet Business Process Management (BPM) curricula and frameworks still largely treat artificial intelligence (AI) as an add-on technology, leaving graduates (as potential future process developers) unprepared to reason about AI as a first-class design element of end-to-end processes. This paper addresses that gap by proposing \emph{AI-decision checkpoints}: explicit moments in a process development trajectory where process developers identify AI-candidate sub-processes, assess expected effects on time, cost, quality, and flexibility, consider legal and organisational constraints, and document a reasoned decision to adopt, constrain, or reject specific AI components. The checkpoints are instantiated through a fictitious customer onboarding process as a \textit{BPM Teaching Case}, embedded in a lifecycle-driven framework spanning six modules that combine process modeling, simulation, workflow execution with AI agents, and process mining, with each module's output serving as the next module's input. A preliminary formative reflection draws on instructor observations, submitted artifacts, and discovered process maps from learning-management-system logs. These exploratory observations suggest that the approach supported clearer distinctions between task-level automation and process-level value.

---


### 376. [Cross-lingual Calibration of Pre-Generation Success Probes for Multilingual LLM Routing](https://arxiv.org/abs/2610.06216)

**<font color=#1a73e8>作者：</font>** Andrea Paganelli, Stefano Civelli, Pietro Bernardelle 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Pre-generation success probes estimate response correctness from a language model's hidden activations before decoding, enabling cost-aware routing. While prior work has demonstrated their utility primarily on English inputs, we study their reliability across languages along three dimensions: (1) whether they preserve the ranking of likely successes and failures (DISCRIMINATION); (2) whether they retain probabilities that match observed success frequencies (CALIBRATION); and (3) whether they produce scores comparable enough across candidate models for cost-aware multilingual routing (UTILITY). Using 3,000 MATH problems in 10 languages and 8 open-weight model configurations, we compare cross-lingual transfer from English-trained probes and equal-budget pooled multilingual probes. English-trained probes retain useful cross-lingual discrimination but become less well calibrated after transfer. Pooled multilingual supervision improves both properties and yields more reliable estimates of success. In routing experiments, the pooled router achieves a 0.7% higher test success rate while reducing modeled cost by 13.0% relative to always selecting the model with the highest average success. These results show that multilingual routing requires success estimates that remain well calibrated and comparable across languages and models.

---


### 377. [DP-ES: Differentially Private Evolution Strategies for Prompt Optimization](https://arxiv.org/abs/2610.06236)

**<font color=#1a73e8>作者：</font>** Ziniu Liu, Aiping Li, Yue Han 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Token-level differentially private (DP) prompt optimization methods such as DP-OPT can become unstable under tight privacy budgets: on GSM8K, DP-OPT obtains $49.5\pm28.5\%$ across 30 runs, and a logged search trajectory reveals prompt-template drift and noise-sensitive irreversible choices. We diagnose these as structural consequences of greedy token-by-token construction over privately aggregated counts. We then propose DP-ES (Differentially Private Evolution Strategies), a structurally cleaner alternative that maintains a population of full prompts, mutates them via LLM calls that never access the private dataset, and spends privacy only on sampled-Gaussian evaluation; deterministic or Gumbel-smoothed selection is post-processing. Under a conservative $(\varepsilon\leq1.0,\delta=10^{-5})$ guarantee, DP-ES achieves 88.1% on GSM8K (+38.6 pp over DP-OPT, approximately 9 times lower standard deviation), 99.7% on MedQA, 73.5% on BANKING77, and 86.8% on Alpaca. It is also 2.5 times faster in wall-clock time and uses 3.3 times fewer logged private-data call groups than DP-OPT. Selection and population ablations, implementation-level noise checks, and a 200-profile exact-match memorization stress test complement the formal guarantee. Scope: Our experiments establish optimization robustness under DP noise, especially where prompt structure is critical; end-to-end validation on genuinely sensitive, non-saturated deployment data remains future work.

---


### 378. [Certification-Enhanced Generalization Bounds](https://arxiv.org/abs/2610.06238)

**<font color=#1a73e8>作者：</font>** Leo Elmecker-Plakolm, Matthew Wicker  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We investigate the use of formal methods to provide tight and sound generalization bounds for learning algorithms. By casting the traditional notion of algorithmic stability as a specification to be verified, we demonstrate that recent advances in reachability analysis can yield provable bounds on the generalization of a given model and algorithm on a sample dataset. As sample-specific algorithmic stability is insufficient to bound the usual distributional notion of generalization, we develop a novel concentration inequality to connect the sample-specific results of formal certification algorithms to the required distributional analysis for bounding the expected generalization gap. The resulting framework enables the analysis of prior generalization bounds to extend far beyond their original restrictive assumptions. Our approach computes sound bounds on the expected generalization gap in a constant number of algorithm runs without making any analytical assumptions on the algorithm; to achieve non-vacuous bounds we only require that the certified reachable parameter set is bounded --- a condition that we do not assume but formally verify. In practice, we demonstrate that our framework provides formal generalization guarantees that are orders of magnitude tighter than alternative sound computational approaches at scales ranging from toy datasets to fine-tuning classification heads on top of modern large language models. While we implement certification-enhanced versions of several well-known stability results, future extensions of our approach will enable tighter bounds and enhanced practical adoption across the spectrum of modern generalization bounds.

---


### 379. [RoSA: Rotational Sparse Adaptation for Memory-Efficient Fine-Tuning](https://arxiv.org/abs/2610.06243)

**<font color=#1a73e8>作者：</font>** Muhammad Azeem Lodhi, Chao Zhou, Rebekka Burkholz  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Parameter-efficient fine-tuning (PEFT) reduces the cost of adapting foundation models by focusing training on a small parameter subset. Complementary to this idea, we introduce RoSA (Rotational Sparse Adaptation), which narrows adaptation to a subset of layers at a time. RoSA freezes lower layers close to the input throughout training and rotates a trainable block over later layers, progressively increasing the number of frozen layers close to the input. This design reduces optimizer-state memory, shortens backpropagation, and even forward propagation if activations at the last frozen layer are cached. Because RoSA is orthogonal to the choice of trainable parameterization, it can be combined with PEFT methods or sparse optimizers within each active block. Experiments across multiple LLM architectures and tasks show that RoSA reduces peak memory while maintaining strong fine-tuning performance.

---


### 380. [From Papers to Mechanisms: An Evidence-Grounded Knowledge Substrate for Scientific Language Models](https://arxiv.org/abs/2610.06248)

**<font color=#1a73e8>作者：</font>** Qiuhui Chen, Yibo Liu, Tao Dai 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Scientific language models often access literature through untyped text chunks, which fragment the functional and evidential structure required for mechanism-rich questions. We introduce an evidence-grounded mechanism knowledge substrate that organizes scientific literature into provenance-linked evidence units, role-typed entities, and directed mechanism paths. We instantiate it as MS$^3$, a Material-Sensor-Signal-System schema for conductive-fiber flexible sensors, over 13,689 papers, 131,083 evidence items, and 26,648 mechanism objects. On in-domain and coverage-shift question-answering benchmarks, we compare closed-book generation, Web search, Raw-PDF RAG, and MS$^3$ retrieval across ten language models. MS$^3$ improves macro-averaged scientific correctness. It also improves citation entailment and answer completeness. These results support mechanism substrates as a reliable representation layer for scientific language models and motivate a source-repair workflow in which insufficient MS$^3$ evidence triggers targeted retrieval from its linked papers rather than assuming that a user has already supplied the correct PDFs.

---


### 381. [Shared Stopping Decisions Change Answers in HQQ Cache Quantization](https://arxiv.org/abs/2610.06251)

**<font color=#1a73e8>作者：</font>** Seunghui Jwa, Minsu Oh, Chanjun Park 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language-model systems batch questions for throughput, but unrelated questions should not change a target's answer when its input and numerical execution are fixed. We study compression of the key and value cache, which stores attention representations reused during generation. With request-local groups, Transformers' Half-Quadratic Quantization (HQQ) backend updates compression parameters separately but uses a shared average error to decide when all updates stop. Replacing only the question batched with the target changes four-bit HQQ answers in 170/384 test comparisons across two models. Replaying the other execution's update counts reproduces its complete answer and cache fingerprints in every changed pair, in both directions. Computing the stopping mean in FP32 reduces cache differences but leaves answer changes. Native HQQ also changes confirmed numerical correctness in eight arithmetic pairs. Fixed iterations and request-local stopping remove observed companion dependence under matched controls. Request-local stopping remains sensitive to synthetic padding changes at the tensor level. Fixing the original iteration budget removes this decision path without tuning. Neither repair has an established quality advantage, and natural rebatching still changes answers. Request-independence audits must cover stopping decisions as well as quantization groups.

---


### 382. [CentriQ: Calibration-Free Quantization of Diffusion Transformers via Exact Mean Centering](https://arxiv.org/abs/2610.06260)

**<font color=#1a73e8>作者：</font>** Nataša Jovanović, Mathieu Salzmann, Saqib Javed  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion transformers (DiTs) achieve state-of-the-art image generation, but their sampling cost limits deployment. Quantizing both weights and activations to 4 bits reduces this cost, yet existing methods fall short in one of two ways. Calibration-based methods are tied to a specific checkpoint and prompt distribution, whereas data-free Hadamard rotation, effective for LLMs, loses quality on DiTs. We show that this loss has a structural cause. Adaptive layer-norm conditioning adds a per-token mean to the activations, and at the widths of the evaluated DiTs, the Hadamard rotations used by data-free methods cannot spread this mean uniformly across coordinates. A single dominant direction therefore survives the rotation and sets the quantization range. We introduce CentriQ, a calibration-free quantizer that centers each token before rotation and restores the mean exactly through a rank-1 full-precision branch, so that per-token scales follow in closed form without data. Weights are fitted under a robust $\ell_p$ objective that tracks the dense mode of each group and discounts heavy tails. Across three DiTs, CentriQ matches the quality of calibrated SVDQuant at 4 bits, whereas calibration-free weight quantizers with plain per-token activation quantization collapse or degrade substantially. CentriQ outperforms the strongest calibration-free method reported to date at 2-bit weights. It is also the first calibration-free method to retain usable image quality at 2-bit activations.

---


### 383. [Evolving in Thought Space: Training a Small Model at Test Time Unlocks Better Discoveries](https://arxiv.org/abs/2610.06269)

**<font color=#1a73e8>作者：</font>** Chonghe Jiang, Ao Qu, Siyuan Liu 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Open-ended scientific discovery often requires repeatedly proposing and evaluating candidate solutions. LLM-based systems can support this process by generating and refining executable solutions from verifier feedback. Methods such as TTT-Discover use test-time training (TTT) to update the solution-generating LLM from verifier feedback, adapting its generation policy to improve subsequent proposals on the target problem. However, this becomes expensive when reliable execution requires a large model, since training must maintain gradients, optimizer states, and policy statistics while repeatedly generating long, structured outputs. It also complicates credit assignment: outcome-level verifier feedback must jointly evaluate the high-level strategy and its low-level implementation. In this work, we introduce Guidance-TTT, which separates these roles. A compact guidance model is trained at test time to propose high-level strategic changes, while a frozen execution model implements them as complete executable solutions. At each step, the system selects a promising previously discovered solution, proposes a change, executes and verifies it, and updates only the guidance model using an adaptive group-relative RL objective. This concentrates test-time learning on short strategic decisions while retaining the implementation capability of a substantially stronger model without adapting it. Without web access, Guidance-TTT produces strong solutions across four distinct domains: combinatorial optimization (Polyomino Packing), heuristic programming (AHC058), machine learning (Lasso), and GPU kernel optimization (TriMul). Across these tasks, it outperforms the best solutions reported in prior work while remaining competitive with state-of-the-art results on public online leaderboards. Code is available at this https URL.

---


### 384. [Probabilistic Race and Ethnicity Prediction Using Group-Specific Name Lists](https://arxiv.org/abs/2610.06273)

**<font color=#1a73e8>作者：</font>** Kyla Chasalow, Noah Dasanaike, Kosuke Imai  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Statistically valid estimation of racial and ethnic disparities often requires inferring the probability that an individual belongs to a particular racial or ethnic group given only their name and geographic location. The standard approach, Bayesian Improved Surname Geocoding (BISG), relies on group population frequencies for each name. Although the U.S. Census Bureau provides such information for common names and a limited set of racial categories, comparable data do not exist for many racial and ethnic groups and are rarely available outside the U.S. We propose the list-powered BISG ($\ell$BISG) method, which can be used to derive calibrated group probabilities from group-specific name lists. These lists may be compiled based on expert knowledge or generated synthetically using large language models (LLMs), and thus may be subject to unknown biases. Representing names as embeddings, we treat list membership as a proxy prediction task and apply a correction based on proximal inference to recover the target group probabilities. We validate the method on U.S. voter files with self-reported race, on the full-count 1900 U.S. Census, and on the Lebanese voter registry. We find that LLM-generated name lists yield accurate and well-calibrated probabilities as well as precise disparity estimates comparable to those obtained using methods that require name-race data. Thus, $\ell$BISG substantially broadens the applicability of probabilistic race and ethnicity prediction to settings where name-race data are unavailable.

---


### 385. [When Are Concept Bottleneck Model Explanations Faithful and Compact?](https://arxiv.org/abs/2610.06285)

**<font color=#1a73e8>作者：</font>** Stefano Teso, Emanuele Marconato, Steve Azzolin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Concept bottleneck models (CBMs) are neural classifiers that allow to explain their decisions via high-level concepts, potentially enabling understanding, steering and debugging. However, their explanations are often derived heuristically. Building on formal explainability, we argue they should also be faithful, i.e., not misreport which concepts actually matter. We show that, for widespread CBM architectures, including recent VLM-based variants, faithful explanations must include all concepts in the bottleneck, compromising interpretability when this is large. This result applies to both heuristic and faithful-by-construction formal explanations. To encourage the existence of compact faithful explanations, we suggest i) modeling concepts probabilistically as binary or categorical random variables (rather than logits), and ii) employing per-concept training-time sparsification via group lasso (rather than regular elastic net). We also extend algorithms from formal explainability to CBMs, and show they outperform natural heuristics in terms of guarantees and explanation size. Overall, our work warns against naive interpretability claims and provides formal conditions and practical strategies for ensuring CBMs are as interpretable as advertised.

---


### 386. [DeferKV: Rethinking Eviction Timing for One-Shot KV Cache Compression](https://arxiv.org/abs/2610.06286)

**<font color=#1a73e8>作者：</font>** Zhe Wang, Jiakai Li, Yujia Sun 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-context large language models (LLMs) have demonstrated strong capabilities across a wide range of tasks, but the growing KV cache introduces substantial memory and inference overhead. Existing one-shot KV cache compression methods typically commit to irreversible eviction immediately after prefill, before any signal from actual generation becomes available. Our quantitative analysis shows that early queries from the actual generation stage provide attention signals that are more consistent with subsequent decode attention, with the largest single-step gain occurring at the prefill-decode boundary. Based on this observation, we propose DeferKV, which moves the eviction decision from the end of prefill to the first real decoding step and temporally combines prompt-side and decode-side observations, thereby better aligning KV importance estimation with subsequent generation requirements. DeferKV requires no additional training, draft model, or future-query prediction module, making it simple and easy to deploy. Experiments on LongBench, RULER, and Needle-in-a-Haystack demonstrate that DeferKV consistently improves model performance under KV cache compression while maintaining low inference latency.

---


### 387. [VepAgent: Bridging Causal-Transition via Tool-Augmented Reinforcement Learning for Video Event Prediction](https://arxiv.org/abs/2610.06293)

**<font color=#1a73e8>作者：</font>** Qiutong Chen, Yuchan Guo, Zhenlong Yuan 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) have demonstrated remarkable potential in video understanding, yet their reliance on retrospective summarization and text-centric priors often limits their ability to bridge unobserved causal transitions when applied to Video Event Prediction (VEP). To address this, we propose VepAgent, an agentic framework that integrates causal-transition reasoning with tool-augmented reinforcement learning (RL) for robust VEP. Unlike prior methods that passively project future trajectories from historical dependencies, our approach explicitly models the logical progression from terminal observed states to future events. Specifically, we first construct futurebench-4K, a high-quality chain-of-thought dataset for supervised fine-tuning (SFT) that effectively bridges the causal-logic gap by structuring the deduction of unobserved intermediate states. Subsequently, we develop a diagnostic tool library integrating state tracking, frame retrieval, and region magnification, enabling the agent to dynamically augment reasoning with external tools to recover missing spatio-temporal evidence and resolve visual ambiguities during inference. Moreover, we propose a composite reward mechanism that jointly optimizes prediction accuracy, causal coherence, and reliable prior, compelling the agent to rely on genuine visual grounding rather than superficial textual similarities. Extensive evaluations on FutureBench and NEPBench datasets demonstrate that our method achieves state-of-the-art performance, significantly outperforming larger MLLMs and validating the empirical effectiveness of our agentic, future-oriented reasoning paradigm.

---


### 388. [Wiring Matters: Injection Topology and Initialization of Affordance Heads in Vision-Language-Action Policies](https://arxiv.org/abs/2610.06318)

**<font color=#1a73e8>作者：</font>** Zijian An, Linhan Wang, Jiayan Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Dense affordance supervision is an appealing auxiliary signal for vision-language-action (VLA) policies, yet naively co-training an affordance head can severely damage instruction following. We present a controlled study of how to wire such a head into a modern VLA on the LIBERO benchmark. Our recipe reads the backbone through a stop-gradient and re-injects an intermediate head feature into the action expert via a learned bridge. The stop-gradient is a precondition: letting affordance gradients reach the backbone drops the policy below the headless base (85.5% vs. 93.1%). With the backbone protected, a same-budget 2*2 ablation over injection topology (concatenation vs. residual) and bridge initialization (zero vs. random) shows initialization is the dominant lever. The best wiring, an actively initialized residual bridge, reaches 96.2%, matching the far more elaborate three-expert AffordanceVLA (95.8%) with under 1% extra parameters. Two probes explain the mechanism: ground-truth affordances fed as an input hurt, and inference-time zeroing shows a lazy bridge acts only as a training-time regularizer while an active bridge becomes load-bearing.

---


### 389. [Agentic schema-guided extraction of materials process knowledge from scientific literature](https://arxiv.org/abs/2610.06322)

**<font color=#1a73e8>作者：</font>** Sameer Sadruddin, Jennifer D'Souza  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Materials literature contains detailed experimental knowledge, but procedures, chemical entities and measurements remain difficult to aggregate because they are reported in heterogeneous forms and depend on process-specific context. We present SciKGExtract, a schema-guided framework that combines large-language-model extraction with chemical normalization and agent-based evaluation and refinement before knowledge-graph integration. We evaluate the framework on 176 atomic-layer-deposition papers describing zinc oxide (ZnO) and indium--gallium--zinc oxide (IGZO), together with an expert-annotated full-schema subset. PubChem normalization improves exact-match extraction F1 for every tested model. For ZnO, the best F1 increases from 0.591 for direct normalized extraction to 0.805 with agentic refinement, whereas the best IGZO result is 0.344, revealing the greater difficulty of multicomponent supercycle processes. Evaluation against a deeply nested schema containing 65 experimental properties and 155 quantitative measurement nodes further exposes errors in process segmentation and numerical assignment. These results show that chemical canonicalization and targeted agentic verification provide complementary controls for converting complex materials literature into reusable, machine-actionable experimental knowledge.

---


### 390. [Readout Blindness: VLM Scores Miss the Spatial Direction Their Frozen Encoders Retain](https://arxiv.org/abs/2610.06324)

**<font color=#1a73e8>作者：</font>** Guangyuan Li, Tianming Du, Yan Jiang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> CLIP-like vision-language models remain a cornerstone of multimodal systems, yet their scores stay near chance on directed spatial relations, such as whether one object is left of another. We call this failure readout blindness and analyze, theoretically and empirically, why deployed scores miss the direction: when scoring rules treat the subject and object symmetrically, direction cancels regardless of encoder training. Guided by this analysis, we introduce Antisymmetric Displacement Readout (ADR), which aligns caption words with image patches in the frozen features and scores each relation by the signed displacement between matched object centroids. Notably, ADR succeeds without additional training or learned parameters, thereby demonstrating that directional information remains in the frozen encoder. However, text and world priors can inflate accuracy, so we further introduce prior deflation, which measures the benefit of the image-text pairing as the grounded gain over a null that pairs each item with an unrelated image. Extensive experiments across encoder families show that ADR substantially improves over deployed scores, which remain near chance on most direction-balanced sets even for fine-tuned encoders. Compared with more complex readouts, ADR outperforms the evaluated MLLM likelihood readouts and is competitive with their chat inference at a small fraction of the computation. These results support our claim that directional information can be recovered from frozen features by an appropriate readout. Our implementation and evaluation kit will be publicly available.

---


### 391. [What Did the AI Take On? Characterizing Cognitive Delegation in LLM Reasoning](https://arxiv.org/abs/2610.06328)

**<font color=#1a73e8>作者：</font>** Yoonsu Kim, Sean Kim, Kihoon Son 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) often perform intermediate cognitive work while carrying out users' requests, yet it remains unclear which parts users intended to delegate and how they wanted to remain involved. This matters because consequential choices may go unnoticed, limiting users' ability to steer the process, while reviewing every step would make delegation burdensome. We examined this with 24 LLM users across three knowledge-work tasks, collecting 992 retrospective annotations of reasoning steps. From this, we developed taxonomies of LLM cognitive work, delegation enactment, and desired delegation protocols at the reasoning-step level. Our analysis revealed that participants viewed about half of all steps (48.6%) as AI-initiated, meaning the AI took on work they had not requested. Desired involvement varied with cognitive work and delegation enactment, even when contributions matched participants' intent. We propose design implications and sketches for supporting more deliberate cognitive delegation through flexible protocols and inspectable, revisable AI-initiated decisions.

---


### 392. [Dynamic Minimax Regret Optimization for Robust LLM Post-Training](https://arxiv.org/abs/2610.06329)

**<font color=#1a73e8>作者：</font>** Chengbo Zang, Haoyu Dong, Mehmet Kerem Turkcan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern LLM training increasingly relies on heterogeneous data sources spanning different domains, tasks, preference distributions, and difficulty levels. We study dynamic minimax regret for group-distributionally robust LLM post-training under instantaneous mini-batch-only bandit feedback. The framework views the training as a two-player sampler-optimizer process: a sampler adaptively selects among data sources using bandit feedback, while an optimizer updates the model parameters using stochastic gradients from the selected source. We focus on the practically restrictive setting where source losses evolve with model training but historical data are not re-evaluated, requiring the sampler to track instantaneous worst-sources from stale partial feedback. We propose DUCB-OGD, a simple and scalable algorithm that couples a Discounted Upper-Confidence-Bound sampler with an Online Gradient Descent optimizer. The sampler maintains exponential moving average loss estimates and confidence radii based on discounted effective sample sizes, avoiding costly re-evaluation of past data or intrusive changes to standard training pipelines. For $K$ data sources and $T$ training steps, we prove that DUCB-OGD achieves a dynamic minimax regret of $\tilde{O}(K^{1/4}T^{3/4})$, which is optimal up to logarithmic factors for the undiscounted objective under our feedback model. Extensive experiments across supervised fine-tuning, preference optimization, and reinforcement learning show that DUCB-OGD integrates seamlessly into modern LLM training pipelines and improves worst-group robustness with negligible computational overhead compared with standard sampling baselines.

---


### 393. [Breaking Bureaucracy: Evaluating open-source LLMs for legal document review](https://arxiv.org/abs/2610.06345)

**<font color=#1a73e8>作者：</font>** Farrukh Baratov, Niki van Stein, Suzan Verberne  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In this paper, we evaluate open-source generative LLMs on legal Natural Language Inference (NLI). Legal inspectorial processes take place in specific domains and often deal with confidential data. This creates a need for working with local models that do not require labeled training data. We evaluate our models on the ContractNLI benchmark and two NLI4Wills datasets. We successfully reproduce the baseline for the task (Span NLI BERT) and we evaluate multiple open-source LLMs on the same task. We analyze the invalid rate of the models, and their stability across temperature settings and domains. Among the generative models, Gemma-4 26B performs the best, reaching an accuracy of 81.2%, even outperforming the supervised model on one metric. On accuracy, it is not possible to beat the supervised model with zero-shot approaches. Qwen-3.6 35B performs well on both ContractNLI and additional datasets in the legal wills domain. Our findings indicate that zero-shot, open-source, generative LLMs are a viable alternative for real-world legal NLI when no supervised data is available. Our code is available at this https URL.

---


### 394. [ImproveAnyTask: An Autonomous Post-Training Harness for Iterative Model Self-Improvement](https://arxiv.org/abs/2610.06347)

**<font color=#1a73e8>作者：</font>** Xingbo Yao, Xiaoman Wang, Zhengwu Lei 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Adapting general-purpose large language models to specific tasks requires substantial human effort in designing data and training strategies. Sustaining improvement is especially challenging because model updates change the error distribution, requiring strategies to be continually refined. We introduce ImproveAnyTask, an autonomous post-training harness that improves task performance under a limited compute budget. Drawing inspiration from gradient-based parameter optimization, the harness organizes adaptation into error attribution, update-direction selection, and executable model updates. It combines metric-level and case-level analysis to identify a focal problem, then investigates research-backed strategies and compares their reported gains and reproduction difficulty. The selected strategy is translated into training data and a training configuration, with small-scale execution checks preceding full post-training. Subsequent evaluation guides model selection and further adaptation, while validated strategies and scripts are retained for reuse. Across 11 tasks, ImproveAnyTask achieves mean gains of 18.29 and 11.97 percentage points on the Base and Instruct models, respectively, with a maximum gain of 41.96 points, under a 24-hour budget with resources equivalent to eight H20 GPUs.

---


### 395. [GraphDecide: Benchmarking System One Models on Graph Tasks](https://arxiv.org/abs/2610.06354)

**<font color=#1a73e8>作者：</font>** Xianliang Yang, Yapu Zhang, Li Zhao  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly explored for graph understanding and decision-making, while System One models such as Jev select directly from supplied options. However, the capabilities of System One models on graph-related tasks remain unclear. We introduce GraphDecide, a model-independent benchmark that combines structural task profiles, matched graph-text input contrasts and heuristic-proposal controls to diagnose graph decision performance. We evaluate Jev and related choice-based models alongside language-model baselines, covering fourteen model-interface configurations. Jev's results illustrate the benchmark's central distinctions: accurate adjacency recognition does not guarantee broader structural correctness, joint graph-text input does not consistently improve prediction, and feasible construction does not establish high solution quality. Its task contracts, candidate interfaces and scoring rules support comparison across native selectors and language-model adapters. Code and aggregate results are available at this https URL.

---


### 396. [Ontology Concept Overlap as a Training Signal: Knowledge-Grounded Reinforcement Learning for Clinical Question Answering](https://arxiv.org/abs/2610.06360)

**<font color=#1a73e8>作者：</font>** Aditya Tanna, Abhishek Jindal  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning post-training for language models relies on two reward designs: human preferences (RLHF, DPO) and binary verifiers (RLVR). Clinical question answering fits neither. Near-correct answers differ by a single substituted entity, and no executable check decides clinical correctness. We instantiate a soft verifier from a maintained controlled vocabulary: UMLS Concept Unique Identifier overlap (via scispaCy, set-level F1) gives a graded, externally specified reward computed without a model in the loop. We combine it inside GRPO with an entropy-normalised LLM judge, which covers the safety and evidence axes overlap cannot see, and a small consistency penalty on padding and repetition that keeps early-training samples scorable. This three-term composite improves over SFT on Phi-3-mini (3.8B) over MedQA by 2.9% on EM (0.700 vs 0.680) and 39% on Token-F1 (0.202 vs 0.145); on Llama-3.2-3B the corresponding gains are 14% on EM and 35% on Token-F1. We report Token-F1 as the primary metric because it credits partially-correct clinical content that EM discards at this open-generation scale. Main-table results are means over 3 seeds with standard deviations below 0.005. The method transfers to PubMedQA, where training on the PubMedQA train set with the same composite reward improves Token-F1 over SFT by 22% on Phi-3-mini and 17% on Llama-3.2-3B without retuning. A reward ablation on Phi-3, varying the judge-ontology split at a fixed consistency weight, attributes 3 EM points to the ontology term, the contribution that catches entity substitutions the judge cannot. Three negative findings constrain the design: DPO under random negatives underperforms SFT for strong-prior models but helps the weakest-prior one; PPO under a sparse neural reward diverges; GRPO with KL-in-loss collapses at 7B.

---


### 397. [Capability-Driven Self-Evolution of Agent Memory](https://arxiv.org/abs/2610.06361)

**<font color=#1a73e8>作者：</font>** Yaoqi Chen, Yuru Feng, Qianxi Zhang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Memory self-evolution uses task feedback to iteratively improve executable memory programs that store and retrieve information from past interactions. Existing approaches typically adopt holistic evolution, deriving revision directions from mixed feedback and judging progress by overall performance. This can obscure optimization directions and hide capability-specific gains offset by regressions elsewhere, leaving promising directions underexplored. We introduce capability-driven evolution, which extends search guidance from overall performance to individual capability dimensions, preserving promising revisions and expanding exploration beyond the boundaries of holistic evolution. We propose PrisMem, which uses dependency-aware capability selection to prioritize targets with potential cross-capability benefits and history-guided diagnosis to refine capability specialists. Trace-guided integration compares evaluated programs on paired differential cases, using their behavioral differences to consolidate complementary gains into a unified memory program. Experiments show that PrisMem outperforms the strongest baselines by 10.54 and 7.83 percentage points on BEAM-1M and LongMemEval-M, respectively, demonstrating its effectiveness on million-token histories.

---


### 398. [Correct Verdicts, Flawed Reasoning: Structured Auditing of LLM-based Vulnerability Reasoning](https://arxiv.org/abs/2610.06366)

**<font color=#1a73e8>作者：</font>** Boyue Caroline Hu, Kaivalya Ahir, Ronghao Ni 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are increasingly deployed for automated software vulnerability analysis. Binary classification alone is insufficient; practitioners need explanations to triage bugs and engineer patches. Standard practice relies on Chain-of-Thought (CoT) prompting, but free-form reasoning allows models to obscure logical leaps, hallucinated execution steps, and internal inconsistencies behind plausible prose. Our manual audit reveals that approximately 60% of correct vulnerability verdicts are accompanied by fabricated or unverifiable claims, and free-form explanations allow reasoning errors to evade LLM-as-a-judge evaluation.
We present Vulnerability Explanation Reasoning Auditor (VERA), an automated framework for auditing LLM vulnerability reasoning. Rather than accepting free-form text, VERA asks models to output a Structured Reasoning Record (SRR) encoding tracked pointers, memory operations, and state transitions in machine-readable fields. A multi-stage judge audits each SRR against eight reasoning failure modes using deterministic checks, with LLM calls reserved for semantic interpretation. The standardized SRR schema also enables automated mutation testing to benchmark judges at scale without human annotation. Our evaluation shows reasoning flaws occur in correct verdicts just as frequently as incorrect ones, and VERA exposes 87% of reasoning errors that free-form LLM-as-judge systematically miss.

---


### 399. [Steering by Influence: Curvature Aware Data Weighting for Activation Steering](https://arxiv.org/abs/2610.06383)

**<font color=#1a73e8>作者：</font>** James A. E. Dixon, Stephen J. Roberts, Francesco Quinzan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Inference-time steering offers cheap, fine-grained control over a language model's outputs by estimating a concept's representation in activation space and shifting activations towards it. Existing methods build these representations from activation averages over contrastive datasets. These averages incorporate unrelated concepts and noise, and are dominated by a few tokens, meaning the activation transport encodes token-level rather than thematic concepts. In this work, we steer towards examples that most express a concept thematically, rather than towards an expectation over all. We identify these examples using influence functions, which estimate how much each data point contributes to a model's representation of a concept. Unlike simple model activation similarity, they incorporate the curvature of the model's loss landscape, allowing them to capture concept-relevant relationships beyond superficial token-level similarity. We then propose influence-weighted activation transport, which uses optimal transport to steer activations of non-concept text towards those of concept text, weighting concept examples by their influence scores. We evaluate on toxicity suppression (Jigsaw), object-based concept induction (OneSec) and truthfulness induction (TruthfulQA), outperforming existing activation-transport baselines. We track capability after steering using perplexity and MMLU accuracy, finding that our method improves steering while largely preserving model quality. We further show that influence functions capture concept-relevant information that activation-based methods miss with the two approaches ranking data points significantly differently. Together, these results demonstrate the value of curvature-aware influence information for activation steering.

---


### 400. [Scaling Down the Scaling Laws: Parameter Efficiency and Compute-Optimal Training in Resource-Constrained Large Language Models](https://arxiv.org/abs/2610.06387)

**<font color=#1a73e8>作者：</font>** Joe Dwyer  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have achieved substantial performance gains through increases in model size, training data, and computational resources. However, traditional scaling approaches produce diminishing returns, rising financial and environmental costs, and barriers to participation for researchers operating outside large industrial laboratories. This review examines the evolution of LLM scaling theory from empirical scaling laws to compute-optimal training, with particular emphasis on parameter efficiency, token utilization, data efficiency, and resource-constrained environments. Foundational work on scaling laws is synthesized alongside later research on compute-optimal training, data pruning, efficient architectures, quantization, low-rank adaptation, and edge-oriented optimization. The literature indicates a shift from scale maximization toward more deliberate allocation of parameters, tokens, compute, and hardware resources. At the same time, important empirical, theoretical, and methodological gaps remain regarding whether scaling principles established on enterprise-grade infrastructure generalize to smaller models and constrained computing environments. This review organizes these developments into a unified framework for resource-efficient LLM training and argues that future progress should evaluate efficiency not solely through model performance, but through the relationship among performance, parameter count, computational cost, token allocation, and hardware constraints.

---


> [!TIP]
> 当前位于：**351-400**（第 8/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | **351-400** | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-505](./part-11.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
