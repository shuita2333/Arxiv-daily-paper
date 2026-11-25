# 🧠 大模型相关研究 | 2026年11月26日

> 本类共 **299** 篇论文：已确认 **280** 篇，待复核 **19** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**251-299**（第 6/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-299**

---

### 251. [When Repair Accuracy Misleads: Training a VLM on Its Own Failures](https://arxiv.org/abs/2611.32982)

**<font color=#1a73e8>作者：</font>** Ang Qi, Yue Wang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Fine-tuning a vision-language model on its own failures is a direct way to repair it, but accuracy on held-out failures, the obvious measure of success, misleads. Many mined failures are not model errors: a human audit of 100 failures of Qwen3-VL-8B-Instruct on questions generated from COCO and GQA found label errors in 37. And mined failures share wording regularities: question-only classifiers get both answers right on 73.2% of held-out failure pairs. We study both traps with verified failure-driven repair (VFR): typed minimal-pair failure mining, verification by three LLM judges that answer without seeing the stored labels, answer-first corrective targets, and LoRA fine-tuning with replay. VFR repairs 82.8% of held-out failures (base model: 10.0%), and on independently labeled, unconditioned pairs it raises overall accuracy from 87.4% to 92.4% through spatial relations, whose accuracy rises from 66.7% to 96.8% even where the wording points to the wrong answer. Yet on negation, of which it repairs 88.9% of held-out failures, its accuracy on unconditioned pairs falls from 88.7% to 79.7%: it breaks negations about absent objects, rare in its training set. Without verification, accuracy on unconditioned pairs falls to 80.8%, below the base model's 87.4%, through a negation shortcut our development benchmarks miss; without failure selection, it stays at 92.0% (one seed) while repair falls to 73.4%. Training also lowers two-image relation accuracy (74.3% to 49.6%; replay data alone: 48.4%); multi-image replay partly and unevenly reverses this. Paraphrasing the spatial questions keeps most of the gain (87.3% vs. the base model's 62.0%), though rewording lowers spatial repair on held-out failures from 92.9% to 76.8%. On What'sUp's independent photos of objects under others, caption choice stays perfect while accuracy on our yes/no pairs falls from 84.5% to 26.4%.

---


### 252. [Modelling Billingual Learning Through LLM Training: A Critical-Period Exploration](https://arxiv.org/abs/2611.32997)

**<font color=#1a73e8>作者：</font>** Uriel Benymon, Tristan Whipps, Armita Ghobadi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Critical-period accounts of second-language (L2) acquisition suggest that the ability to learn a new language may depend on how easily previously acquired first-language (L1) knowledge can be modified. This exploratory computational study extends a neural language-model approach to critical period effects by examining internal representations rather than behavior. A small two-layer GPT-2 model was trained on English and then on German (a relatively related L2) or Finnish (a relatively distant L2) through either Sequential training or Elastic Weight Consolidation (EWC), which limits change in parameters important for English. Mean-pooled hidden states for 20 held-out probe sentences per language were compared with those of the English-only model using cosine similarity at the embedding layer and two transformer layers after one and two L2 epochs. English similarity remained high in the transformer layers but became negative in the embedding layer. L2 similarity increased in the transformer layers, and German and Finnish differed more in the second transformer layer than in the first. EWC reduced Fisher-weighted parameter drift by about 6% but changed transformer-layer similarity by less than .001. With one training run per condition, these findings are preliminary.

---


### 253. [LEGOSpec: A Composable and Efficient Framework for Speculative Draft Design and Training](https://arxiv.org/abs/2611.33004)

**<font color=#1a73e8>作者：</font>** Hanzhen Wang, Jiaming Xu, Guohao Dai  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Speculative decoding accelerates large language model (LLM) generation using a lightweight draft. Existing methods evaluate complete recipes under different training configurations, leaving component effects, interactions, and composition benefits unclear. Therefore, we present LEGOSpec, a composable framework for speculative draft design and training. LEGOSpec decomposes draft models into Context, Backbone, Proposal, and Objective components that share a unified training infrastructure. Using LEGOSpec, we systematically vary components and evaluate selected combinations under matched training conditions to isolate their effects and interactions. These experiments reveal three findings: (1) Different workloads favor different backbones, depending on context length and memory budget, with within-block dependency modeling particularly important for long contexts. (2) Proposal design must balance acceptance and latency. (3) The training objective should match token distributions locally and optimize acceptance length across the block. These findings guide workload-aware configurations and DFlux, a balanced general-purpose draft combining a convolution-equipped SWA--GQA hybrid backbone, Residual Corrector, and hierarchical supervision. Across Qwen and Gemma models, DFlux improves acceptance length over the strongest baseline by up to 13.7% on regular benchmarks and 34.7% on long-context workloads. To support efficient training, LEGOSpec integrates metadata-aware scheduling and asynchronous execution, increasing training throughput by up to 79% and accelerating offline supervision preparation by up to $3.11\times$ over SpecForge.

---


### 254. [Leto: Utility-Centric Agent Memory](https://arxiv.org/abs/2611.33005)

**<font color=#1a73e8>作者：</font>** Shuguang Chen, Salman Paracha  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents rely on external memory to retain and reuse information across interactions. Existing memory systems treat memory as a record of the past and evaluate it by fidelity to the conversation. However, the value of memory lies in whether it improves the agent's response. A memory system decides what to memorize and what to serve before that response exists, and fidelity checks neither decision against it. Faithful memory can therefore fail to improve the response. We instead view memory as a prediction problem and present \textbf{\emph{\leto{}}}, a memory system for LLM agents that focuses on the utility of memory to the future rather than on its fidelity to the past. Because future requests are unknown, \emph{\leto{}} preserves access to conversation details through memory indexing, allowing information to remain available through its sources. When a request arrives, memory replay draws on this index to anticipate and supply the context the agent needs beyond what the request explicitly states. The utility of the served context remains uncertain until the response is generated, motivating a utility loop that uses response outcomes to refine future memory selection. We evaluate our system against six memory systems on five benchmarks across three scenarios. In personalization, it outperforms the strongest compared memory system by 16.3 percentage points in accuracy on PrefEval and by 3.1 points in task completion on PERMA. For long-horizon tasks, it achieves the best overall performance on MemoryArena averaged over five environments with a gain that increases with the chain depth. In long-context understanding, it is on par with retrieval over the raw history while serving fewer context tokens.

---


### 255. [Embodied AI Fails the Mirror Test: How a Simple Mirror Breaks Robot Policies](https://arxiv.org/abs/2611.33010)

**<font color=#1a73e8>作者：</font>** Xuanchen Liu, Hejun Zhang, Boxuan Dong 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Can a simple mirror expose the limitations of today's robotic manipulation policies? Inspired by the mirror self-recognition test in animal cognition, we investigate whether robot policies can reliably manipulate physical objects in scenes containing their reflections. We introduce RoboDojo-Mirror, a benchmark built on RoboDojo that preserves task objectives, success criteria, and policy checkpoints while comparing a mirror-free baseline with single-mirror, dual-mirror, and mirrored-tabletop conditions. Across five policies spanning Vision-Language-Action models, World Action Models, and agentic policies, every mirror condition reduces aggregate success rates: averaged over the three conditions, the drop ranges from 10.8 to 56.7 percentage points across policies, and it reaches 62.5 points on the mirrored tabletop. Because a mirror is also a physical obstacle, we compare it against geometrically matched non-reflective panels; 50--88\% of mirror-specific failures occur without recorded robot--panel contact, so direct collisions alone do not explain the degradation. Trajectory and contact analyses instead reveal recurring behaviors consistent with phantom targeting of reflected objects and spatial mislocalization of real ones. Targeted diagnostics further characterize grasping near reflections, policy-dependent pushing progress, and physical-target interaction under main-camera occlusion. Real-robot experiments with $\pi_{0.5}$ and FastWAM also show lower overall success rates under the upright-mirror and mirrored-tabletop conditions. These findings reveal a shared vulnerability to reflective environments across diverse robot policies and motivate reflection-aware evaluation of embodied intelligence. Code is available at this https URL.

---


### 256. [Can LLM Judges Catch Unsafe Clinical Actions? A Fault-Injection Study](https://arxiv.org/abs/2611.33012)

**<font color=#1a73e8>作者：</font>** Neda Ghafouri  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As clinical AI agents begin to interact with electronic health records (EHRs), large language models (LLMs) are increasingly used to evaluate their actions. But how reliably can these judges recognize clinically dangerous mistakes, especially when an agent appears to have completed its task successfully? We investigate this question using MedAgentBench by introducing controlled clinical errors into verified agent trajectories. The experiments include 416 faulty trajectories, eight error categories, and six open-weight LLM judges. By comparing each faulty trajectory with its correct counterpart, we measure whether judges genuinely recognize errors rather than simply flagging more actions as unsafe. The findings show that access to clinical evidence significantly improves judge reliability. When shown only the final answer, judges cannot distinguish errors that leave it unchanged, while flagging 56% of correct trajectories. With full trajectory information, the ability to distinguish unsafe actions from correct ones reaches a score of 0.75, and providing actual EHR responses improves discrimination by 0.39. Surprisingly, including the agent's reasoning does not improve overall performance and reduces detection of incorrectly reported clinical values by 0.18, which remain the hardest errors to detect. MedGemma performed worse than the general-purpose model and was the only judge to miss potentially dangerous medication overdoses. We also find that the benchmark's original grader accepts all 38 trajectories with an intentionally skipped laboratory check, while combining LLM judges with a rule-based checker informed by the full EHR record detects 97% of injected faults.

---


### 257. [Training Lightweight Gaze Models without Target Gaze Annotation: What Makes a Good Teacher?](https://arxiv.org/abs/2611.33014)

**<font color=#1a73e8>作者：</font>** Scott J. Lewis, Di Fu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Model-generated labels offer a scalable route to training lightweight vision models, but what makes a model a good teacher, and can we tell before training a student? We study this in gaze target estimation, where interactive robots need models that are both accurate and efficient. In a controlled comparison of eleven supervision conditions, we vary only the source of gaze-point labels, keeping the student, training protocol and 361k training samples fixed, across three video datasets, two student sizes and three seeds; every student is evaluated against human annotation. Three findings emerge. First, imperfect model-generated labels can replace human annotation: Gaze-LLE, never trained on the target datasets' gaze annotation, trains students that match annotation-trained ones on ViT-Tiny and are significantly more accurate on ViT-Small (average distance error 0.187 vs 0.196), and the ViT-Tiny student runs 32$\times$ faster than its teacher on a laptop CPU. Second, apparent competence can conceal unreliable supervision: given another person's face centre in the prompt, InternVL3 and Qwen3-VL return it on 93.4% and 81.1% of test samples, and a copy-the-coordinate baseline matches InternVL3's labels and students. Without that coordinate, both models fall far behind the specialist. Third, good teachers can be identified before training: validation label error ranks student test error (Spearman's $\rho = 0.91$), and ten annotated clips single out the two specialist teachers in 95% of draws. These findings give practical principles for assessing supervision, exposing shortcuts and selecting teachers for lightweight models.

---


### 258. [PORTA: Systematic Discovery of Vulnerabilities in Identity Brokers](https://arxiv.org/abs/2611.33015)

**<font color=#1a73e8>作者：</font>** Zixu Zhou, Xiangyu Guo, Ilya Grishchenko 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Identity brokers such as Keycloak, Vault, and Dex translate authentication proofs from an upstream identity provider into sessions for downstream services. Due to their central role in authentication and trust mediation, a single vulnerability in a broker compromises every downstream service behind it. In fact, recent incidents have demonstrated that even widely adopted platforms are not immune to such issues, highlighting the critical need for systematic analysis. To build such an analysis, this work first defines invariants for broker operation. These invariants are not completely covered by existing authentication specifications, primarily because brokers are unique in their duality, i.e., acting simultaneously as a relying party and an identity provider. The invariants capture the properties that identity brokers must uphold throughout their workflows, as all 60 previous CVEs we consider violate at least one invariant. Within these workflows, we further define high-level action categories. Equipped with this information, our automated tool PORTA leverages a large language model (LLM) to generate API invocation sequences corresponding to the high-level action categories, and oracle assertions aligned with the specified invariants. PORTA identifies 33 previously unreported security vulnerabilities in seven popular open-source brokers. We study these novel vulnerabilities and trace them to eight recurring patterns. We responsibly disclosed all discovered vulnerabilities: 29 have been confirmed, 14 patched, and 19 assigned CVE numbers, with 10 CVEs rated as critical.

---


### 259. [GRAPE-Bench: When Vision Degrades, Does Video Reasoning Hold?](https://arxiv.org/abs/2611.33020)

**<font color=#1a73e8>作者：</font>** Ce Zhang, Junyi He, Tianshi Ming 等 18 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite strong performance on standard benchmarks, video reasoning models remain vulnerable to visual degradation, raising concerns about their reliability in safety-critical scenarios. Existing benchmarks address this concern in part by simulating visual degradation or probing model reasoning with challenging questions, leaving open how well models handle naturally degraded video and whether they can make the simpler judgments that matter for safe driving. To this end, we introduce GRAPE-Bench, which jointly evaluates video reasoning across visual degradation conditions and question difficulty. It combines a synthetic set spanning twelve corruption types across daily-life and driving videos with real-world footage of driving at night or in rain, snow, or fog. Each video is paired with three progressively challenging questions, from fundamental judgments with potential safety implications to demanding reasoning stress tests. Across open-weight and frontier models, we observe ranking reversals between synthetic and real-world conditions and level-specific weaknesses obscured by overall accuracy. Synthetic-data fine-tuning improves Qwen3.5-9B's real-world accuracy from 76.7% to 81.1%, while clean-privileged on-policy distillation reaches 80.4% in a separate reasoning-enabled setting. Through preference steering, we further demonstrate continuous control over a frozen model's trade-off between safety-relevant judgments and challenging reasoning, with little change in overall accuracy. Together, GRAPE-Bench provides a unified testbed for evaluating, improving, and controlling video reasoning under degraded visual conditions.

---


### 260. [RecordRoute: Auditing Agent Failures with Localization-Guided Diagnosis](https://arxiv.org/abs/2611.33022)

**<font color=#1a73e8>作者：</font>** Yifan Duan, Lihuan Li, Chao Xue 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Auditing failed agent executions requires identifying the responsible actor, the earliest decisive step, and the error mode. Representative supervised methods either focus on step localization or predict multiple attribution targets from shared trajectory representations. These methods do not use the localization result to select the text for mode diagnosis. To address this limitation, we propose RecordRoute, which couples comparative localization with local diagnosis. Specifically, it represents each record with word and character features and learns to rank records through comparisons within each trajectory. The selected record supplies the actor and step, while its text and metadata drive mode prediction. On controlled-injection Who&When Pro, RecordRoute outperforms StepFinder and ASCon on all four official metrics. With actor and step predictions fixed, local diagnosis reaches 77.47% pooled joint accuracy versus 69.28% for full-trace diagnosis. On natural failures from TraceElephant and CatchBench POST, it outperforms these baselines and three open LLMs in localization.

---


### 261. [Can a Frontier LLM Repair a Quantized Network by Tool-Free Weight-Space Programming?](https://arxiv.org/abs/2611.33031)

**<font color=#1a73e8>作者：</font>** Steffen Urban  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We give four large language models (LLMs) of the Claude family the complete weights of a 20k-parameter CIFAR-10 CNN as text and ask them to produce a 4-bit network without tools, data or the ability to run inference. Standard round-to-nearest (RTN) quantization to 4 bit lowers the test accuracy from 81.4% to 60.4%. We design four evaluation protocols that differ in the input and task description given to the LLMs and analyze their responses. In the first two protocols the LLMs are given the float and the 4-bit RTN network and are told that the accuracy has dropped significantly. In the last two they receive only the float network and the task to quantize it, which tests whether they apply an optimization on their own or fall back to plain RTN. Our analysis shows that a frontier LLM can recover most of the lost accuracy. Given one answer per layer, Opus 5.5 raises the accuracy of the 4-bit network to 77.95% by balancing the rounding errors within each 3x3 kernel, reasoning over the integer weights without tools. This is 3.5 pp below the float network and 2.8 pp below AdaRound, which learns the rounding from calibration data. Given only the float network, the LLMs name error-cancelling corrections but do not apply them and fall back to plain RTN, at most with mildly clipped scales, which still lifts Fable 5.2's quantized network to 70.0%. We analyze in detail what the LLMs did and why it works. Code and prompts can be found at this https URL

---


### 262. [Latent Merger: Latent-Space Composition of Hypernetwork-Generated LoRAs](https://arxiv.org/abs/2611.33048)

**<font color=#1a73e8>作者：</font>** Yanlai Yang, Minki Kang, Divyam Madaan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent work proposes hypernetworks that convert a document into a low-rank parameter update (LoRA) in a single forward pass, enabling fast injection of new knowledge into a frozen LLM. However, storing separate LoRA adapters for each document can be unsustainable in streaming settings. In this paper, we study the problem of composing hypernetwork-generated LoRAs using two representative systems, Doc-to-LoRA and SHINE. We show that hypernetwork-generated LoRAs have a geometry sharply different from directly fine-tuned LoRAs. They exhibit greater spectral concentration and stronger cross-document alignment than next-token prediction and QA fine-tuned adapters, which are diffuse and nearly orthogonal across documents. Guided by this observation, we propose latent-space LoRA merging. We compose the intermediate hypernetwork latents and then decode the merged latent through the frozen LoRA-generation head. We show that latent-space merging techniques consistently improve over weight-space and factor-space baselines while preserving a single fixed-rank adapter. These results support latent-space composition as a promising mechanism for combining hypernetwork-generated LoRAs under a fixed output-rank budget.

---


### 263. [Worth the Wait? How Response Time and Streaming Shape Judgments of Generative AI Answers and Chatbot Engagement](https://arxiv.org/abs/2611.33050)

**<font color=#1a73e8>作者：</font>** Zihan Chen, Di Zhu, Lei Nico Zheng  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Answers from generative AI chatbots built on large language models (LLMs) now arrive at very different speeds: reasoning models deliberate before replying, while response caches can return a stored answer at once. Blind preference votes, which rank these models, are read as judgments of their text, and if delivery matters, faster answers are expected to gain. Research on the labor illusion and on how text appears on screen suggests instead that an answer which unfolds as it is written is credited over the same answer shown at once. We test these accounts with three sources of variation in natural use. First, compar:IA, a French government chatbot arena, answered repeated prompts, by a random draw, either with a fresh answer streamed as it was written or with a stored earlier answer from the same model, shown at once. Within the same prompt, a replay lowered an answer's chance of winning a decisive blind vote by 25.8 percentage points. The same stored text won 57% of its decisive votes when streamed and 29% when replayed, and voters called it less complete, more superficial and more often incorrect when replayed. Second, provider congestion slowed streamed answers. In 324,029 conversations, slower answers earned no detectable net credit in the vote, but a slower first exchange made visitors less likely to ask a follow-up question. Third, in 4,378,514 WildChat replies from everyday ChatGPT use, replies slowed by congestion made users less likely to continue. Delivery moved blind votes, in the direction opposite to the one the arena's designers expected, while waiting cost follow-up questions that a comparison between two answers cannot register when both are slow. The results bear on how AI services cache and stream answers, how they budget latency, and how preference leaderboards evaluate models.

---


### 264. [Understanding Clipping In Zeroth-Order Optimization](https://arxiv.org/abs/2611.33062)

**<font color=#1a73e8>作者：</font>** Saket Gollapudi, Elisa Bertino, Sewoong Oh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Zeroth-order optimization has emerged as a resource-efficient alternative to Stochastic Gradient Descent (SGD) when fine-tuning LLMs, thanks to the inherent low dimensionality of the loss landscape. It relies on a two-point estimate of the gradient that only accesses the function value and not the gradient, bypassing the resource-heavy backpropagation. Recently, it was accidentally discovered that per-sample clipping can improve the performance of the trained model, while running a differentially private version of zeroth-order optimization \cite{zhang2024dpzero} with a very large privacy parameter $\epsilon$ (corresponding to very little privacy). In this paper, we systematically investigate this phenomenon and demonstrate that ($i$) the optimal choice of learning rate $\eta$ is inversely proportional to the clipping threshold $c$, satisfying $\eta c =$ constant; ($ii$) clipping drives the zeroth-order optimization to a different solution with higher test accuracy; and ($iii$) this phenomenon is only observed with per-sample clipped zeroth-order optimization and not other zeroth-order alternatives that also provide robust estimates of the gradient. Further analyses with artificially injected label noise reveals that clipping leads to more robust predictions, which stems from the implicit down weighting of hard-to-fit training examples. Our code is available at this https URL

---


### 265. [U-Statistics-Powered LLM Reasoning](https://arxiv.org/abs/2611.33064)

**<font color=#1a73e8>作者：</font>** Shijin Gong, Kai Ye, Victor Chernozhukov 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Since its introduction by DeepSeek, group relative policy optimization (GRPO) has been widely adopted for training large reasoning models and agents, spurring a proliferation of its variants. Yet the group size, a crucial hyperparameter in these GRPO-type algorithms, remains largely chosen by trial and error. Exploiting the U-statistic structure of GRPO's policy gradient, we recast the selection of the group size as a classical statistical problem of variance ratio estimation. This problem is particularly challenging when the denominator of the ratio is small, rendering naive plug-in estimators unstable. To address this challenge, we propose a pessimistic ratio estimator that accounts for the denominator's estimation uncertainty. We characterise the statistical properties of this estimator across three sample-size regimes. Empirically, using %a jackknife-based pessimistic rule on synthetic tasks from Reasoning Gym and real-world benchmarks covering both mathematical reasoning and code generation, we show that our adaptive group size selection reduces the mean squared error of the resulting policy gradient and improves policy optimisation over fixed-group-size baselines, with modest additional computational cost.

---


### 266. [Auditing the Judge: Human-Derived Bias Discovery, Quantification, and Mitigation in LLM Judges](https://arxiv.org/abs/2611.33065)

**<font color=#1a73e8>作者：</font>** Hamin Koo, Chanjoo Jung, Fangzhao Wu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> While Large Language Models (LLMs) are increasingly deployed as automated evaluators in evaluation and training pipelines, their judgements are often affected by systematic biases that conflict with human preferences. Although prior work has identified various biases and proposed methods for detecting and mitigating them, less attention has been paid to using human preferences to inform bias identification and mitigation. Moreover, these approaches rely heavily on pre-discovered bias lists, overlook bias strength, and depend on costly interventions. In this work, we propose HUB-J, an integrated framework based on human-derived bias factors that detects, quantifies, and mitigates biases in LLM-as-a-Judge systems. Our approach leverages human-LLM judgement disagreement cases to automatically discover interpretable bias factors, and utilizes agreement cases to quantify bias strength through controlled input modifications and resulting shifts in model decisions. Finally, building on these quantified biases, we introduce a lightweight, training-free regression-based mitigation strategy that estimates the influence of each bias factor on model judgments and corrects bias-influenced decisions by removing its estimated effect. Empirical results show that HUB-J uncovers both known and novel bias factors, reveals meaningful differences in model susceptibility, and consistently reduces bias-driven decision flips while generalizing across models.

---


### 267. [FOL-Proof: Verifying LLM Text-to-Logic Translations via Deterministic Semantics](https://arxiv.org/abs/2611.33078)

**<font color=#1a73e8>作者：</font>** Yisrael Clark, Guy Katz  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are increasingly used to translate natural-language statements into first-order logic (FOL) to improve reasoning. However, LLMs are prone to errors, and so a semantically unfaithful FOL formula could corrupt downstream reasoning. We present FOL-Proof, a semantic firewall pipeline that validates LLM-generated FOL translations against independently derived linguistic interpretations. FOL-Proof operates by deterministically obtaining a pool of candidate translations via semantic analysis tools, such as the English Resource Grammar and Minimal Recursion Semantics; then applying an SMT solver to check each derived reading for logical equivalence to the LLM-generated formula. If the translation is faithful it is accepted; otherwise, it is rejected, or optionally repaired via repeated invocations to the LLM. The procedure is conservative: incomplete search, unsupported constructions, or inconclusive checks yield abstention rather than false rejection. We evaluated FOL-Proof on established benchmarks (ProofWriter, RuleTaker and PrOntoQA), and also on a new adversarial benchmark (LongFaithCheck). Our experiments show that FOL-Proof attains near perfect selective accuracy, while direct LLM judges and round-trip baselines show substantially worse performance.

---


### 268. [Shifter Quantization: Compact Representations for Native Integer Computation](https://arxiv.org/abs/2611.33080)

**<font color=#1a73e8>作者：</font>** Yufeng Huang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Groupwise quantization is used in LLM quantization to improve accuracy at low bit widths, but grouping weights keeps standard integer MMA from spanning the full dot product for efficient GPU inference. We develop a new quantization method, Shifter Quantization (SQ), that reconstructs native-width integer operands by appending and shifting shared bits. To further extend the efficiency, we develop a special variant of SQ, Shifter Integer (SHI), to use INT4 kernels. We show that SQ and SHI formats perform better than standard groupwise quantization in quality, as measured by projection error and KL divergence, and in inference speed, as measured during decoding and prefill. For low precision like 2-bit quantization, SQ2 and SHI2 achieve 2.71-3.77x the 4,096-token prefill throughput of this http URL on a Q2_K checkpoint and reduce WikiText-2 KL by 6.6-7.8%. For mid precision like 4-bit quantization, SQ4 achieves 1.43-2.47x the prefill throughput of NInfer's groupwise-integer baselines across the tested models and prompt lengths, with 24-40% lower KL than the NInfer baselines. For high precision like 8-bit quantization, SQ8 achieves 27.4% higher batch-one prefill throughput and 72.7% lower KL than vLLM's online FP8.

---


### 269. [AIChipBench: Benchmarking LLM Agents for Automated AI Accelerator Design](https://arxiv.org/abs/2611.33093)

**<font color=#1a73e8>作者：</font>** Guangyuan Wang, Chengran Li, Minchen Luo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A language-model decoder carries state between decoding steps, and in hardware a wrong state update can leave the current token correct and corrupt the output several tokens later, so a design can pass output tests and still be wrong. AIChipBench asks what LLM coding agents need to build such hardware correctly. Agents implement quantized Qwen3.5, Gemma 3, Gemma 4, and Llama 3.2 decoders in synthesizable register-transfer-level (RTL) code against an executable integer reference that specifies the outputs and the stored state at every decoding step. They debug against public tests under fixed budgets; their frozen designs are graded on held-out token sequences, resets, memory stalls, and synthesis, and a second track asks them to speed up a correct design at nearly fixed area. Across 9,136 attempts by four coding agents, the difficulty lies in stored state. Feedback that points to the first state mismatch raises acceptance over output-only feedback in all 12 agent--task cells of a matched study, by 25.0 to 46.9 percentage points, and halves the agent-hours per accepted design. Regraded on new sequences and conditions, 45 of 69 accepted designs fail within the 32 steps their tests required. More than a third of attempts to speed up a correct design end without one. An overall score ranks Sol 5.6 and Fable 5.1 above Astra 6 and Opus 5.5, and both halves of the instances give this order in all 200 random splits. Hardware agents therefore need debugging feedback that exposes stored state, and their benchmarks need final tests well beyond the development cases.

---


### 270. [Delegent: A Multi-Agent Harness That Reduces Cost without Sacrificing Performance](https://arxiv.org/abs/2611.33098)

**<font color=#1a73e8>作者：</font>** Lingwei Gu, Jimmy Lin  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agents built on frontier language models are expensive. At every step, the frontier model re-reads its entire context and executes every subtask regardless of its difficulty. This paper explores the simple thesis that much of this cost can be removed by delegating easy subtasks to a small language model, or SLM, that runs on hardware one already owns. To test it, we build Delegent, a simple and effective agent harness built on Claude Code, in which the frontier model stays in charge of every task but hands focused subtasks, such as investigating code, running tests, and searching a corpus, to SLM subagents. Existing approaches such as cascades and model routers usually choose which model executes the entire task, whereas in Delegent, the frontier model always leads the execution and delegates easy subtasks to the SLM. No router or model is trained, so either model can be swapped freely. With the help of a 27B FP8 SLM, Delegent reduces the frontier cost of long-horizon coding by 67% and of agentic search by 59%, with no loss in task performance, and even a 2B SLM that fits on a laptop reduces the coding cost by 66%. The savings grow with the legwork that the frontier model would otherwise do itself, and a short instruction, which leaves the main coding tasks to the frontier model, accounts for most of the saving and keeps the 2B SLM from losing tasks. Code: this https URL

---


### 271. [Draft Calibration for Speculative Decoding: Accelerating LLM Serving by Matching Draft and Target Distributions](https://arxiv.org/abs/2611.33111)

**<font color=#1a73e8>作者：</font>** Yuxing Liu, Wei Zuo, Walid Krichene 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Speculative decoding accelerates large language model (LLM) inference by employing a lightweight draft model to propose draft tokens and allowing the target model to verify the new tokens in parallel to improve inference-time compute utilization. The speedup relies on the acceptance probability of draft tokens in target verification, which is directly related to the gap $\|p-q\|_1$ between the target distribution $p$ and the draft distribution $q$. In this paper, we study draft calibration of speculative decoding to improve the speedup of speculative decoding, where we employ post-hoc methods to calibrate the draft distribution to mitigate the distribution gap. We observe that though current community open-source draft models may learn the top candidate token correctly, they are generally underconfident compared to the target model, suggesting a consistent distribution mismatch. To mitigate the effect of this mismatch on the acceptance rate of the draft models, we try various post-hoc calibration methods, including standard temperature scaling and token-wise calibration. Our results suggest that a standard temperature scaling applied to the draft distribution improves the acceptance length by up to approximately 10\% with almost no additional cost across different tasks. Throughput analysis further verifies that this improvement in serving efficiency. Analysis of more general calibration methods reveals further potential room for improvement.

---


### 272. [MetaFORGE: A Meta-Learning Framework for Harness Optimization in Automated Code Generation for Parallel Computing](https://arxiv.org/abs/2611.33119)

**<font color=#1a73e8>作者：</font>** Scott Piersall, Yang Gao, Shenyang Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) can generate parallel programs, but their correctness and performance depend strongly on the instructions that guide generation. We present \textsc{MetaFORGE}, an execution-grounded meta-learning framework that iteratively optimizes persistent natural-language skill specifications for MPI C code generation. \textsc{MetaFORGE} combines correctness testing, compiler diagnostics, static-analysis findings, runtime measurements, and rank-level load-imbalance profiles into a scalar reward that drives textual-gradient refinement, while an external memory distills and retrieves reward-supported optimization knowledge across runs.
Across six MPI tasks and three workload sizes, \textsc{MetaFORGE} improves static-analysis quality, runtime, and load balance relative to zero-shot generation and generally exceeds the evaluated \textsc{TextGrad} iterative baseline. A model-matched refinement ablation shows that the MetaFORGE advantage persists when its refinement model is reduced to \texttt{gpt-4o}. An expanded retrieval ablation across all 18 task--workload configurations shows consistent runtime benefit and broad static-analysis and load-balance benefit from retrieved context. Leakage-controlled held-out and zero-update experiments further provide evidence that optimization knowledge persists in both the transferred skill and external memory under the evaluated protocol.

---


### 273. [SAG-Mem-1.0 Technical Report](https://arxiv.org/abs/2611.33124)

**<font color=#1a73e8>作者：</font>** Yuchao Wu, XingCheng Liang, Xuanze Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-term conversational memory requires retrieving complementary facts scattered across dialogue sessions, including intermediate evidence with limited similarity to the original question. Existing approaches often rely on derived memory representations or persistent relational structures, introducing construction costs and potentially losing source details. We present SAG-Mem, a conversational memory framework that preserves complete dialogue messages in non-overlapping chunks and discovers complementary evidence through query-time lexical expansion. Memory construction requires no model inference, using a lexical index without LLM-based extraction, summarization, or semantic relation construction. At query time, BM25 retrieves initial candidates, an evidence evaluator identifies useful chunks, and lexical cues from selected evidence guide an additional retrieval round. Retrieved dialogue is further annotated with calendar interpretations of supported relative-time expressions, preserving the original wording and temporal granularity. We also introduce SAG-Mem-Lite, an alternative configuration that replaces evidence scoring with embedding-based candidate scoring, achieving lower operational cost than Full Context and all memory-based baselines across both benchmarks with low query latency. On LoCoMo and LongMemEval, SAG-Mem achieves overall scores of 83.08 and 80.20, respectively, the highest among the evaluated methods on both benchmarks. On LongMemEval, it exceeds the strongest compared baseline by 7.20 points. SAG-Mem-Lite achieves scores of 77.09 and 77.20, respectively. These results support dialogue preservation and evidence-guided retrieval expansion as an effective design for long-term conversational memory.

---


### 274. [A Bias in Disguise: Tiny Gradient Edits Stop a Small Language Model's Thinking Loops and Complement a Frontier Model's Weight Edit](https://arxiv.org/abs/2611.33133)

**<font color=#1a73e8>作者：</font>** Hussamuddin Syed  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Qwen3.5-0.8B rarely finishes reasoning in thinking mode: at a 4,096-token budget only 1 or 2 of 500 MATH-500 answers close their think block (two seeds), and accuracy is 15.4%. A recent demonstration had GPT-6 Astra edit 131,072 of the model's weights without gradients and reported MATH-500 rising from 7.9% to 48.1% at a 32,768-token budget. We provide the missing gradient baseline, then combine the two edits. Fine-tuning only the 140 to 139,750 weights with the largest gradient, on the model's own correct answers to MATH training problems, raises thinking-mode MATH-500 at 4k tokens to 39.0-45.5% after 2-9 minutes of training on one GPU; 50 training examples suffice, and 1,398 random positions give only 16.3%. The gradient concentrates the edit on the most nearly constant channel of each of the first three layers. Because the model has no bias terms, an edit confined to those channels acts as a constant vector added to the residual stream: adding three fixed vectors to the unedited model matches the accuracy of such an edit. Under the Astra protocol (32k tokens, presence penalty 1.5), the Astra edit scores 52.1% (finished and correct) in our reproduction and our full-strength edits reach 45.6-45.7%, but ours win at every budget up to 16k tokens (39.5% against 6.7% at 4k). The two edits are complementary. The Astra edit plus our 139,750-weight edit at half strength scores 62.2% at 32k, 10 points above the Astra edit alone (p = 3e-9), with half as many tokens; our half-strength edit alone scores 46.7%.

---


### 275. [BriConstrain: Geometrically Constrained Decoding for Autoregressive Brick Assembly Generation](https://arxiv.org/abs/2611.33135)

**<font color=#1a73e8>作者：</font>** Nadav Magar, Amir Hertz, Ariel Shamir 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Language models can generate LEGO$^\circledR$ assemblies from text, but their builds often contain parts that collide or attach to nothing. The usual approach of rejecting and resampling invalid placements discards decoded tokens without guaranteeing a valid build. We present BriConstrain, a constrained decoding method that restricts a pretrained language model's next-token probabilities before sampling, steering it towards valid placements. Because the validity of a brick placement depends on the non-predetermined build state, it cannot be compiled into a fixed grammar and must be checked dynamically. However, checking the validity of a brick before sampling is challenging as the space of valid placements is combinatorially large and cannot be enumerated exhaustively. Our key idea is to narrow the search space by constraining how parts attach rather than which parts attach to each other. Concretely, given the model's predictions of the currently placed part, and the previously placed parent it wants to connect to, we constrain the model's choice of how they attach. This allows us to span the space of part attachments, using a precomputed geometric oracle, and to effectively filter out colliding options. With valid attachment candidates in hand, we bias the model's next-token distribution towards the remaining valid candidates. We evaluate our method on two LEGO$^\circledR$ formats and models: BrickNet, which annotates connectivity explicitly, and our proposed Implicit Connectivity LDraw Format (ICLF), which uses numeric values for placements and leaves connectivity implicit. Our method raises collision-free builds from 31% to 91% on BrickNet and from 15% to 65% on ICLF, and outperforms rejection sampling on both formats at about 60% of its decoding cost.

---


### 276. [Physicl Scenes: An Artist-created 3D Dataset for Learning Perception and Action](https://arxiv.org/abs/2611.33137)

**<font color=#1a73e8>作者：</font>** Yueh-Cheng Liu, Snehal Jauhri, Matthias Nießner 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present Physicl Scenes, a high-quality artist-created and curated dataset of 6,499 3D scenes spanning household rooms, public interiors, and outdoor spaces. The dataset combines detailed geometry, physically based materials, and carefully composed environments with object- and part-level semantic annotations, providing rich, joint supervision for visual and embodied learning. We demonstrate its value as training data across inverse rendering, 3D reconstruction, scene understanding, and mobile manipulation. Across these tasks, training state-of-the-art methods with our scenes improves performance over alternative synthetic datasets. In addition, we introduce a mobile manipulation benchmark, evaluating vision-language-action models performing physical pick and place in diverse 3D scenes with realistic layouts, and using our part annotations to also score where each object is grasped. Our dataset will be released publicly to facilitate research in visual and embodied AI.

---


### 277. [Lost on Campus: Evaluating Embodied Spatial Reasoning of Vision-Language Models in the Wild](https://arxiv.org/abs/2611.33145)

**<font color=#1a73e8>作者：</font>** Zehan Zheng, Yanyuan Chen, Deming Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Embodied Spatial Reasoning (ESR) is central to deploying Vision-Language Models (VLMs) in real-world embodied tasks, yet remains inadequately evaluated. Existing benchmarks primarily assess spatial reasoning in static images or synthetic indoor environments, where semantic shortcuts often suffice, making it difficult to faithfully evaluate spatial reasoning capabilities in the wild. In light of this, we present Lost on Campus, a benchmark for evaluating ESR in large-scale real-world outdoor 3D environments reconstructed by 3D Gaussian Splatting. Our benchmark introduces a unified reasoning-action evaluation framework that seamlessly integrates diagnostic QA for isolated reasoning with closed-loop interactive navigation for active reasoning under multimodal instructions. To enable fine-grained diagnosis, we evaluate six capability aspects of ESR: action grounding, spatial foresight, metric awareness, goal-directed planning, ego-allocentric localization, and spatio-temporal consistency. Extensive experiments reveal that: (i) Compared to indoor settings, real-world outdoor environments impose substantially higher demands on spatial reasoning, where existing models exhibit poor performance; (ii) VLMs still struggle with fine-grained visual alignment, with failures in spatial foresight and ego-allocentric localization emerging as primary bottlenecks; (iii) Improving multimodal interaction capabilities and long-term spatial reasoning is crucial for advancing embodied intelligence. These findings highlight that faithful evaluation of ESR demands benchmarks tightly coupling perception, reasoning and action within realistic and continuous environments.

---


### 278. [CoT-Proxy: Cross-Format Transfer for Distilling Long-Horizon Policies](https://arxiv.org/abs/2611.33148)

**<font color=#1a73e8>作者：</font>** Dawid J. Kopiczko, Tijmen Blankevoort, Yuki M. Asano  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reasoning models become long-horizon agents through reinforcement learning or, more cheaply, through fine-tuning on a stronger teacher's trajectories, which contain the teacher's chain-of-thought as well as its actions. The standard fine-tuning approach imitates both, yet the strongest teachers are closed models whose chain-of-thought is hidden behind an API. We show that the chain-of-thought can be left out altogether and that the long-horizon policy can be distilled from the teacher's actions alone. The student is trained on these trajectories with its reasoning block left empty, while a KL loss on a replay buffer of its own generations limits drift from its initial model. Surprisingly, the policy learned from these trajectories with an empty reasoning block carries over to inference with thinking enabled, where the student reasons in its own style while acting like the teacher, an effect we call cross-format transfer. Distilling the actions of Qwen3.6-27B raises the task success of Qwen3-4B on AppWorld from 7% to 18% and that of Qwen3-32B from 12% to 25%. We further introduce CoT-proxies, short summaries of the teacher's reasoning placed after the empty reasoning block, which raise Qwen3-4B further, to 35%. Since neither actions nor CoT-proxies need the hidden chain-of-thought, the recipe applies unchanged to closed teachers. Distilling GPT-5.6 Luna from its visible outputs and the reasoning summaries its API returns raises Qwen3-4B from 7% to 48% on AppWorld and from 3% to 28% on SWE-bench Verified.

---


### 279. [BioLoom: Scaling Biomedical Vision-Language Models by Learning from the Structure of Scientific Articles](https://arxiv.org/abs/2611.33151)

**<font color=#1a73e8>作者：</font>** Yuwei Yang, Xiaoxiao Sun, Alejandro Lozano 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The development of biomedical vision-language models (VLMs) with contrastive image-text pretraining has been driven by scaling to increasingly large and diverse image-text datasets. Beyond scaling, further progress can come from learning richer representations from existing data. We hypothesize that the structure of scientific literature itself provides an additional source of supervision: figures, panels, captions, and accompanying article text encode rich relationships across modalities. Yet, treating these as independent image-text pairs overlooks their relationships. To address this limitation, we incorporate these structural relationships into contrastive image-text supervision. We preserve exact image-text matches while introducing weaker positive supervision for related pairs, such as a panel and the caption of a sibling panel. We upweight cross-article negatives of the same content type to encourage finer discrimination. We also enrich panel descriptions using visual content, original figure captions, and mentioning paragraphs. Pairing panels with these descriptions and whole figures with their original captions yields Loom52M, a dataset of 52.4 million image-text pairs spanning scientific charts and biomedical images. Using Loom52M, BioLoom (DFN-2B) achieves 56.82% domain-balanced mean accuracy across 67 zero-shot classification tasks from 43 datasets in 10 domains, compared with 48.77% for MedPMC-CLIP. On BioLoomBench with concise captions and BioMedFlickr, it achieves bidirectional mean Recall@1 of 63.20% and 10.59%, versus 46.37% and 7.55% for the respective strongest evaluated baselines, BiomedCLIP and MedPMC-CLIP. Code, datasets, benchmarks, and models are available at this https URL.

---


### 280. [DiaCap: Jointly Learning Who Speaks When for Audiovisual Dialogue Captioning](https://arxiv.org/abs/2611.33153)

**<font color=#1a73e8>作者：</font>** Binfei Ji, Zhiwen Cao, Anqi Yang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present DiaCap, an audiovisual LLM for comprehensive dialogue captioning, which produces the transcript, timestamps, and a visual description of the speaker for every utterance in a video. Considering that utterance timing and audiovisual diarization are tightly coupled, DiaCap unifies the tasks in a single model, trained in two complementary stages. First, we train DiaCap on 225K curated clips, using synthetic captions that densely label every utterance in detail. Second, we further refine the model via reinforcement learning on 2.9K human-corrected clips, using fine-grained feedback that directly evaluates utterance timing, speaker grouping, and speaker binding. On DiaDemBench, which we extend with utterance-level timestamps and subtitle redaction, both DiaCap with off-the-shelf transcripts and its end-to-end variant DiaCap-E2E achieve strong results. Specifically, DiaCap performs on par with Gemini 4 Argon in audiovisual diarization while clearly outperforming it in timestamp accuracy (76.59 vs. 42.76 TIME). It also maintains strong diarization on multilingual and minute-long videos, and transfers to audiovisual question answering.

---


## ⚠️ 待复核论文

> 以下论文保留内部待复核标记，并统一放在大模型章节末尾。

### 281. [Layer-Readout Interfaces in EEG Foundation Models: Predictive Accessibility and Cross-Dataset Transfer](https://arxiv.org/abs/2611.31320)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yanlin Fu, Wei Liu, Liming Zhao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Intermediate layers often outperform final layers when foundation models are used as frozen feature extractors, but the source of this advantage is unclear. We study this question in EEG foundation models by separating three factors: how representations are read out, whether intermediate layers provide predictive utility beyond the final-layer interface, and whether useful depth structure transfers across datasets. Across five models and three tasks, improving the final-layer readout consistently recovers substantial predictive performance, yet intermediate layers remain advantageous within frozen extraction. We also find that layers selected on one dataset remain useful on another across five dataset pairs and four task families, and that a compact set of source-derived task directions retains predictive value after transfer in sleep staging. Together, these results show that predictive utility varies across depth, and its usefulness depends on how representations are read out and transferred. More crucially, source-selected layers provide a reusable feature interface across datasets, reducing the need for target-side layer search while outperforming final-layer baselines on target datasets.

---


### 282. [GHC:Expanding Residual Interfaces in Hyper-Connections](https://arxiv.org/abs/2611.31350)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Tianyu Li, Hongtao Zhang, Dongchen Han 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hyper-Connections expand residual capacity across parallel streams, yet restrict every branch to narrow read and write interfaces: each branch still reads a single stream mixture and writes scaled copies of one output vector to all streams. To lift this bottleneck, we propose Grouped Hyper-Connections (GHC). By partitioning each branch into parallel groups along attention heads or FFN channels, GHC supplies each group with a distinct stream mixture and aggregates their separate outputs into each stream with learned weights. Extensive experiments across dense and Mixture-of-Experts (MoE) models show that GHC consistently improves upon Identity Hyper-Connections (IHC) with negligible parameter and memory-access overhead, increasing training efficiency by 35% over Pre-Norm and 10% over IHC. Moreover, expanding residual interfaces overcomes the diminishing returns of adding streams, allowing wider residual states to yield further gains.

---


### 283. [Which Way Is Up? Rotated Photos Silently Hurt Multi-View 3D Foundation Models](https://arxiv.org/abs/2611.31478)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yukun Shi, Minglun Gong  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-view 3D foundation models estimate camera poses and 3D points from a set of photos in one forward pass. Many cameras store a portrait shot sideways, with an orientation tag telling viewers how to turn it, and this tag can be ignored, lost or wrong. We measure how rotated photos affect five such models on three datasets. A few rotated photos lower camera pose accuracy for every model, and the sideways photos already in a standard benchmark do the same. Even the most robust model still loses accuracy. The failure is also silent: the models' confidence does not reliably flag it, and most official image loaders ignore the tag. The fixes we test each correct only part of the problem. These findings call for orientation checks in reconstruction pipelines and benchmarks.

---


### 284. [SwiftLoop: Selective Refinement for Adaptive Implicit Reasoning in Looped Transformers](https://arxiv.org/abs/2611.31481)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Tianyi Zhao, Ke Wan, Chen Chen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Looped Transformers advance implicit chain-of-thought reasoning through recurrent latent refinement. However, existing looped reasoners typically employ fixed-depth recurrence, updating all latent positions at every iteration and incurring redundancy when further refinement is unnecessary. We introduce \textsc{SwiftLoop}, an inference-time framework for selective recurrent refinement through position-wise freezing, enabling adaptive computation allocation across both recurrent depth and active width. SwiftLoop learns lightweight freezing policies through hindsight-guided supervision derived from two complementary criteria: K/V reusability at the internal representation level and functional impact at the output level. At inference time, these policies guide adaptive freezing based on observed hidden states. Extensive experiments demonstrate that SwiftLoop achieves favorable accuracy--computation trade-offs over fixed-loop inference and adaptive baselines, with measured inference acceleration. Beyond implicit reasoning, we further demonstrate its applicability to recurrent prompt prefilling in general looped models.

---


### 285. [ECLIPSE: Embedding-Centered Foundation-Model Federated Knowledge Transfer for Data-Free Edge Intelligence](https://arxiv.org/abs/2611.31527)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** S. Kawa Atapour, S. Jamal Seyedmohammadi, Maryam Hosseini 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Foundation Models (FMs) are envisioned to become an integral component of intelligent federated edge networks because of their strong representation and generalization capabilities. However, their integration into resource-constrained and privacy-sensitive edge environments remains challenging. This challenge is particularly pronounced in data-free settings, where no shared, public, or server-accessible reference dataset is available to establish a common reference space for aligning distributed knowledge. To address this challenge, we propose ECLIPSE, which is an embedding-centered FM-based federated knowledge transfer framework developed for data-free edge intelligence. ECLIPSE enables edge intelligence capitalizing on a server-hosted FM without sharing raw data, local models, or a public reference dataset. It establishes a shared embedding reference space through which edge devices encode their local task knowledge. Only the resulting embeddings are transmitted to the server for alignment and aggregation. Using the aggregated embeddings, the server constructs a task-aware surrogate dataset through an embedding-guided generative process. This surrogate dataset is then used to adapt the server-hosted FM to the downstream task. The adapted FM is subsequently distilled into a lightweight global model and distributed to the edge devices. This process allows edge devices to benefit from both distributed task knowledge and the generalization capabilities of the FM. Experimental results across diverse classification datasets show that ECLIPSE outperforms conventional Federated Learning (FL) and data-free Federated Knowledge-Transfer (FKT) baselines. It also achieves competitive performance compared with databased approaches. Furthermore, the framework remains robust under statistical and model heterogeneity across different data distributions and local architectures.

---


### 286. [Adapt, Label, Distill: Foundation-Model Supervision for Efficient Object Detection](https://arxiv.org/abs/2611.31604)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Zhengye Yang, Anthony Wang, Yuyang Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Object detectors often transfer poorly to specialized domains, where box annotations are scarce and deployment requires compact, real-time models. Large vision foundation models can provide offline supervision, but their zero-shot predictions may be poorly aligned with the target domain. We present an adapt-label-distill pipeline that uses limited target annotations to specialize a foundation teacher and transfer its supervision to compact detectors. We adapt SAM3 on the labeled subset, generate pseudo-labels for the remaining unlabeled images, and train YOLOv11 students with confidence-guided supervision. Teacher confidence weights pseudo-label losses, while zero-gating retains uncertain hypotheses during assignment without applying their associated training losses. Experiments across six target domains and three student capacities show substantial gains in several domains, while revealing limited or negative transfer in others. Teacher comparisons under a common hard-label training recipe support the choice of SAM3, and comparisons with an EfficientTeacher adaptation provide additional evidence against an online SSOD baseline. With YOLOv11m, our pipeline improves over STAC-style self-training by up to 15.3 AP and reaches 51.6 AP on Garbage, compared with 54.1 under full supervision. On NVIDIA Jetson AGX Orin, the deployed student achieves 188 FPS versus 2.9 FPS for SAM3, benefiting from foundation-model supervision without incurring the teacher's deployment cost. Code is available at this https URL.

---


### 287. [Self-Improving Long-Horizon Reasoning by Learning Summaries from Local Continuations](https://arxiv.org/abs/2611.31621)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Haoqun Cao, Tengyang Xie  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reasoning models degrade as their context grows, so longer reasoning traces do not by themselves give longer effective horizons. One way to extend the horizon is to compress the reasoning history into a compact state from time to time and continue from the state. Existing methods train the state with the final-answer reward or distill it from a stronger model. Neither signal is tailored to measure the contribution of the state alone. We observe that a reasoning model that degrades over long trajectories still behaves reliably in short contexts. We aim to preserve this short-context behavior when compressing the reasoning history. Motivated by this, we train a separate summarizer with Delta-KL, a reward computed from the frozen reasoning model's token-level predictions on sampled continuations, and run inference by truncating the trace, summarizing it, and continuing from the summary (TruSuCo). Training uses a few thousand questions with 4k-token reasoning prefixes and does not need answers or external teachers. Under a fixed 32k-token budget, the trained summarizer improves on vanilla reasoning and on an untrained summarizer in all nine settings across mathematical benchmarks and Reasoning Gym puzzles, by up to 7.7 points and 12 points, respectively. The improvement over vanilla reasoning grows with the budget. At 128k tokens, our method outperforms it by 10 points on AIME 2024--2026. Analyses show that truncation prevents the collapse of vanilla reasoning and that the trained summaries retain more of the reasoning history.

---


### 288. [G0.7: Scaling Up a Fast World Action Model with Long Context](https://arxiv.org/abs/2611.31822)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Tianyuan Yuan, Baijun Ye, Shicheng Cao 等 25 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> World action models (WAMs) adapt pretrained video generators for robot control by jointly predicting future camera frames and actions, transferring physical priors learned from video into manipulation policies. However, generating future frames before every action makes test-time inference too slow for closed-loop control, while most existing policies remain restricted to short observation histories. Building on Fast-WAM, which showed that video prediction shapes policy representations during training so that future frame synthesis can be skipped at deployment, we present G0.7, a generalist world action model scaled along two axes: extending the context window from a single observation to up to five minutes of history, and scaling pretraining to a large-scale corpus of robot teleoperation and human egocentric (ego) video. Across public simulation suites and real-robot deployments, direct action decoding (Fast mode) matches imagine-then-act (IDM) inference from the same checkpoint while running in 60 ms per 16-step action chunk on a single RTX 5090 (7.6x faster than IDM) and supporting pause-free real-time chunking. Performance scales consistently with pretraining data, with human ego video driving the largest gains in out-of-distribution generalization: G0.7 achieves a 70.8 mean score across five simulation benchmark suites, 48% and 54% zero-shot pick-and-place success on Galaxea R1 Pro and R1 Lite, 96.7% in-distribution and 93.3% out-of-distribution success on video-conditioned in-context learning tasks, and 86.9% mean task progress across seven real-world post-training tasks including multi-minute box folding, drink preparation, and product bagging.

---


### 289. [Two-Stage Post-Training for Flow-Based Embodied Foundation Models](https://arxiv.org/abs/2611.31850)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Jiaming Zhang, Yao Lyu, Haoning Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large-scale pretraining provides embodied models with general capabilities, but reliable task execution still requires post training. In multitask settings, supervised fine-tuning (SFT) faces distribution mismatch between training and deployment, whereas reinforcement learning (RL) is limited by sparse rewards and uneven learning progress across tasks. Multi-teacher on policy distillation (MOPD) consolidates expert capabilities through dense supervision on the model's own trajectories, but achieving performance beyond the teachers remains challenging. We propose a two-stage post training framework for flow-based embodied models, constructing distillation objectives from the velocity regression formulation of conditional flow matching. Stage 1 efficiently consolidates expert capabilities through MOPD. Stage 2 combines RL with teacher distillation that weights velocity errors according to the sampling noise, where distillation is restricted to failed trajectories to supplement sparse rewards with dense guidance without directly constraining successful behaviors. Experiments across multiple models and benchmarks show that the framework outperforms joint SFT and exceeds the corresponding teachers' aggregate success rates. Sample efficiency comparisons show higher success rates than direct RL with fewer environment interactions.

---


### 290. [Loupe: Reinforcing Knowledge-Intensive Video Generation Agents](https://arxiv.org/abs/2611.31895)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Kai Zeng, Ruichuan An, Zhen Fang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Knowledge-intensive video generation remains challenging because prompts often omit the facts, appearances, and temporal relationships required for accurate generation. While search-based workflows can retrieve missing evidence, manually designed strategies limit adaptive planning, and conventional training suffers from costly video-level feedback and coarse trajectory-level credit assignment. In this paper, we present Loupe, a video generation agent that retrieves and verifies textual and visual evidence to construct evidence-grounded temporal video prompts with reference images. We further introduce Rubric-Based Credit (RBC), which leverages prompt-specific factual, visual, and temporal requirements to evaluate intermediate search and planning decisions before video rendering. Building on RBC, RBC-SFT reweights assistant-token learning by step quality, while RBC-GRPO incorporates step-level credits alongside a final planning reward, without rendering videos during RL. To address the lack of dedicated search-oriented evaluation, we construct Search-VBench, which contains 150 held-out prompts across seven categories. Experiments show that Loupe improves all four evaluation dimensions across three video generators, raising the overall score of MiniMax-H3 from 32.80 to 70.67 and outperforming an untrained search workflow. Ablation experiments show that full RBC training outperforms standard SFT followed by trajectory-level GRPO by 5.27 points. Human evaluations and results on Sci-VBench and KIVI-Bench further demonstrate improved generation quality, scientific grounding, factual precision, and helpfulness. Our project page is available at this https URL.

---


### 291. [Rethinking Universal Time Series Foundation Models from Unified Representations to Shared Dynamics (UniTFU)](https://arxiv.org/abs/2611.31921)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Shuxin Li, Yingjie Zhou, Le Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time series foundation models (TSFMs) have attracted increasing attention in cross-domain forecasting. Existing works mainly rely on large-scale pre-training and general modeling paradigms. However, the former heavily relies on the diversity and domain coverage of pre-training data. Meanwhile, the latter learns unified representations across heterogeneous domains without explicitly identifying the temporal regularities shared among them, limiting robust cross-domain generalization. This work explores cross-domain generalization by characterizing commonalities in recurring local dynamics across domains, rather than relying solely on implicitly learned temporal representations. To capture such cross-domain commonalities, we propose Time Series Foundation Units (TFUs) as reusable building blocks discovered from multi-scale temporal segments, each characterizing a recurring local dynamic pattern shared across domains. Building on TFUs, we develop a unified time series foundation model (UniTFU) that explicitly reuses and composes shared temporal regularities across domains for forecasting. Experiments on seven public datasets show that UniTFU substantially outperforms existing TSFMs in cross-domain forecasting and can efficiently adapt to target-domain dynamics by updating its reusable components with limited target data. UniTFU also achieves strong forecasting performance compared with state-of-the-art methods.

---


### 292. [DraftKV: Protecting Persistent Worlds through Hierarchical Streaming Retrieval](https://arxiv.org/abs/2611.31944)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Xiaoling Zhou, Haopeng Li, Yufa Zhou 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Interactive video world models enable action- and camera-controlled exploration, yet struggle to maintain consistent spatial geometry and appearance when revisiting previously explored locations. Historical KV caches help auto-regressive video diffusion models maintain long-term consistency, but their retrieval and attention computation introduce substantial latency as history grows. We propose DraftKV, a training-free framework that retrieves historical KV caches based on geometric grounding and query-conditioned relevance, while combining CPU offloading with tile-wise streaming attention to reduce GPU memory usage and inference latency. Theoretically, we show that draft relevance reproduces the mean branch of full-resolution block relevance exactly, so its deviation is confined to the $\beta$-weighted max branch, and we bound retrieval utility loss in terms of the measured Top-K selection overlap. We further show that draft relevance cannot distinguish blocks with similar pooled descriptors regardless of camera pose, motivating geometric grounding before refinement. Then, we introduce streaming CG-Attention, which overlaps CPU-to-GPU KV transfers with attention computation through tile-wise streaming, hiding transfer latency while maintaining bounded GPU memory usage. Experiments across diverse model families show that DraftKV achieves superior generation quality and consistency while achieving $3.27\times$ end-to-end speedup and 42.2% peak GPU memory reduction over other CPU-offloaded KV cache retrieval methods. Notably, DraftKV enables high-quality interactive world generation with historical KV retrieval on a single H100 GPU using SolarWM-33B.

---


### 293. [EffectWAM: Learning Action-Grounded Effects for Robot Manipulation](https://arxiv.org/abs/2611.32053)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yuan Zhang, Hao Cui, Jingfei Ni 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> World-action models connect visual prediction with executable robot control. We present EffectWAM, which develops this connection through three complementary components: Effect, camera positional encoding (CaPE), and Action Grounding. Effect represents visual change as the difference between independently encoded future observations and a shared current-observation anchor. CaPE conditions endpoint pooling on relative camera pose when reliable extrinsics are available, while sharing the same learned parameters with pose-free pooling for uncalibrated trajectories. Action Grounding trains the visual representation to retain measured changes in end-effector pose and gripper state. An exponential moving average of the observation encoder supplies Effect targets. A shared generation expert learns to jointly predict Effect and an executable action chunk through flow matching, and reuses the sampled pair to generate future video on demand. This allows the controller to execute actions without waiting for video synthesis. We train on more than 20,000 hours of heterogeneous embodied data, excluding unused chain-of-thought data, and accommodate dataset-specific joint, end-effector, and hand-pose representations. Our evaluation uses the Small (8B) configuration on all five benchmarks and additionally evaluates the Large (26B) configuration on RoboDojo. Experiments examine closed-loop manipulation across complementary benchmarks, and comparisons across multiple baseline policies show consistent improvements from Action Grounding.

---


### 294. [ThinkMorph-SSL: Scaling Interleaved Multimodal Reasoning with Pretext Tasks](https://arxiv.org/abs/2611.32183)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Jiawei Gu, Linjie Li, Yiming Liu 等 22 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> People reason with pictures as well as words. Interleaved multimodal reasoning gives models a similar way to solve problems by creating intermediate images and using them to guide further reasoning. Training models with this ability usually relies on task-specific demonstrations, which are difficult to collect. We introduce ThinkMorph-SSL, a two-stage training recipe that uses images themselves as a source of supervision. The first stage, pretext reasoning, converts visual pretext tasks, such as image colorization and denoising, into instruction-free interleaved traces. Models describe a corrupted or transformed image, generate a restored or canonical image, and interpret the result. The second stage uses automatically constructed demonstrations for question-driven instruction tuning. At the same instruction-tuning budget, models trained with pretext reasoning outperform those trained with instruction tuning alone. The full recipe improves over the base model by an average of 11.33 accuracy points across twelve benchmarks. These results show that supervision derived from images can build the visual skills needed for interleaved reasoning and improve learning from task-specific demonstrations.

---


### 295. [Refining and Aligning Clinical Reasoning with Health Guidelines via Formal Constraints](https://arxiv.org/abs/2611.32247)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Xiaoyang Fan, Yufan Cai, Zhe Hou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Clinical reasoning from incomplete or conflicting patient evidence must account for low-probability but high-risk concerns while remaining grounded in health guidelines. We introduce VerClin, an explainable framework that extracts guideline conditions, exclusions, recommendations, and priorities into executable knowledge and represents patient conversations as scoped cases. A deterministic four-valued reasoner produces traceable guideline matches while preserving uncertainty and enforcing exclusions. Multiple specialty agents then screen matched guidelines for case applicability, and a consultation model synthesizes accepted guidance through specialty recommendations and a sentence-preserving formal-constraint channel. We present accepted guidance in ascending order of the sum of its priority and trigger-strength ranks, which can surface high-risk guidance with weaker triggers. VerClin outperforms direct generation and Top-5 RAG on HealthBench Hard and HealthBench Professional. On the LLMEval-Med subset, it outperforms direct generation and ties Top-5 RAG. Component analyses further examine semantic closure, example-guided refinement, specialty screening, and constraint-conditioned delivery.

---


### 296. [InducedTFMs: A Family of Sub-Quadratic Tabular Foundation Models Using Induced Attention](https://arxiv.org/abs/2611.32504)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Salome Gobbi, Nicolas Atienza, Nicola Cancedda 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tabular foundation models (TFMs) have emerged as a serious competitor to gradient-boosted trees, predicting on a new table in a single forward pass by in-context learning. However, their attention is quadratic in the number of samples and features, which caps pretraining at small synthetic tables and forces inference on large ones to rely on chunking or subsampling. Row-compression models reduce the feature-wise cost, but only by discarding the cell-level representation, and remain quadratic in the number of samples. We introduce InducedTFM, which replaces both attention stages of a bidimensional TFM with the induced attention of the Set Transformer, preserving cell-level representations while making its cost linear in both samples and features. Under a training budget matched to a full-attention TabICLv2 reimplementation, InducedTFM matches its accuracy on TabArena and on a benchmark of larger datasets, and clearly outperforms a kernel linear-attention baseline of the same asymptotic cost. It overtakes TabICLv2 in inference time on narrow tables, reaching a 30x speed-up at 640K rows, although row compression remains preferable on wide tables.

---


### 297. [PtychoFM: A Foundation Model for Ptychographic Imaging](https://arxiv.org/abs/2611.32830)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Aileen Luo, Emon Dey, Ming Du 等 53 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Ptychography provides high-resolution lensless imaging across X-ray, electron, and optical microscopy, but reconstructing images from diffraction measurements generally requires computationally intensity iterative phase retrieval. These methods often require experiment-specific analysis, limiting real-time feedback as data acquisition rates increase. Here, we demonstrate PtychoFM, a physics-aware foundation model for ptychographic imaging that combines large-scale pre-training with experiment-specific fine-tuning to reconstruct complex object images directly from individual diffraction patterns. Trained using a differentiable forward model without object-space labels, PtychoFM transfers from step-scan training data on one sample to fly-scan measurements of other samples with different feature sizes, morphologies, and refraction indices. At a synchrotron beamline, diffraction frames were streamed from the detector to a single GPU for inference at up to 200 frames per second and returned for real-time visualization. PtychoFM provides a practical route to rapid, transferable ptychographic reconstruction and live experimental feedback under nonideal conditions.

---


### 298. [On Potentiality and Actuality Of Foundation Models](https://arxiv.org/abs/2611.32991)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Fabian Gröger, Shuo Wen, Maria Brbić  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Foundation models are built through large-scale pretraining, often followed by post-training, and are then adapted to specific tasks and behaviors. But, does the adaptation add truly new capabilities, or the base model already holds it? We decompose the update induced by different adaptations into a component shared across all inputs and a residual that varies with the input. We find that the shared component suffices for most of the adaptation gain and can be learned directly: a shift adapter that learns a constant vector per layer, identical for every input, reproduces the behavior of LoRA and full fine-tuning. We call this the potentiality principle of foundation models: the base model already contains the capacity needed for task-specific expertise. To adapt to a new task, the model just needs to be actualized, i.e., pushed in a certain direction via a constant, input-independent shift. We show the implications of this principle on parameter-efficient adaptation, steering, and convergence across models, and how it explains the neural thickets phenomenon.

---


### 299. [PAVE: Preference-Aligned Visual Egocentric Learning for the Blind and Low-Vision Users](https://arxiv.org/abs/2611.32996)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Nan Li, Shaofeng Liang, Shiyun Zhao 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Egocentric video question answering enables blind and low-vision (BLV) users to query their immediate surroundings through natural language. However, existing benchmarks and models primarily optimize for semantic agreement with reference answers, reducing visual assistance to a purely factual matching task. In real-world scenarios, a factually correct response remains practically unhelpful if it lacks the spatial orientation, actionable detail, or conciseness required by the immediate task of the user. Drawing upon real BLV egocentric videos and authentic user queries from EgoBlind, we construct the PA-EgoQA, a preference-aligned dataset that reconstructs reference answers according to empirical BLV communication criteria. Based on this dataset, we introduce Preference-Aligned Visual Egocentric Learning (PAVE), a unified learning and inference framework that couples structured answer-policy fine-tuning with deterministic question-conditioned routing to adapt response formulation directly to the surface form of the query at inference time. We further align the model via Filter-GRPO, which pairs a hierarchical correctness-quality reward with contrast-based candidate-group filtering to extract learning signals from both factual accuracy contrasts and fine-grained quality variations among correct answers. Extensive experiments across three vision-language backbones demonstrate consistent improvements in factual accuracy alongside substantial gains in assistive response quality. These results establish a concrete paradigm for translating human-centered response requirements into egocentric supervision, generation policies, and post-training objectives. Code will be provided at this https URL.

---


> [!TIP]
> 当前位于：**251-299**（第 6/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-299**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
