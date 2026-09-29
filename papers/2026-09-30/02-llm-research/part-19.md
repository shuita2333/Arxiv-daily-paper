# 🧠 大模型相关研究 | 2026年09月30日

> 本类共 **992** 篇论文：已确认 **928** 篇，待复核 **64** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**901-950**（第 19/20 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-700](./part-14.md) | [701-750](./part-15.md) | [751-800](./part-16.md) | [801-850](./part-17.md) | [851-900](./part-18.md) | **901-950** | [951-992](./part-20.md)

---

### 901. [Can LLMs Value the Right Evidence? Evidence-Value Misalignment in Dynamic Medical Diagnosis](https://arxiv.org/abs/2609.35627)

**<font color=#1a73e8>作者：</font>** Kehua Feng, Yunsheng Lu, Yitong Qiao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A correct diagnosis reached from insufficient or misleading evidence can pose a clinical hazard, yet outcome-based accuracy may reward such lucky guesses. We call this mismatch between diagnostic decisions and the value of available evidence Evidence-Value Misalignment (EVM). To disentangle evidential grounding independently from diagnostic accuracy, we introduce MedEVM, a dynamic benchmarking environment comprising 1,050 cases across 24 disease systems. Observations arrive turn by turn, requiring models to continuously calibrate its decision by deciding whether to wait for more evidence or submit a diagnosis. Across 9 LLMs, four interesting patterns are observed. (1) Miscalibrated evidence tracking. Making a diagnosis often fails to calibrate evidence sufficiency, even in more capable models, and even worsens in reasoning mode. (2) Misaligned diagnosis submission. Confidence in the correct diagnosis often fails to ensure timely submission despite sufficient evidence. (3) Evidence order matters. Reordering the same evidence changes diagnoses even when model confidence remains similar. (4) Misleading evidence remains influential. Added misleading evidence redirects diagnoses even after prior evidence becomes sufficient. We further verify that EVM predicts errors and that preventing premature submission improves accuracy. These findings motivate Evidence-Verified Diagnosis Harness (EVD-Harness). It decouples diagnosis generation from submission through an offline Contrastive Diagnostic Wiki and three online control stages, namely observation management, proposal and witness verification, and diagnosis submission control. Across five LLMs, EVD-Harness improves accuracy by 12.0--51.1 percentage points while mitigating EVM-related failures. Our results demonstrate that verifying evidential support before submission can make diagnostic decisions more reliable.

---


### 902. [SANTA++: Sampling Attention through Representative Keys](https://arxiv.org/abs/2609.35629)

**<font color=#1a73e8>作者：</font>** Kyle Lee, Christian Z. Pratt, Ruoyu Fang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Attention often concentrates on a small subset of tokens in the context, but which subset matters changes from one query to the next. To exploit this changing structure, we introduce SANTA++, a training-free stochastic attention method that uses representative keys for memory-efficient selection without scanning the entire key-value (KV) cache. Cached keys are organized into teams, and the query scores one representative from each team to decide which teams to sample. We compute exact attention scores within the sampled teams and reweight each team's contribution by the inverse of its inclusion probability. This importance sampling correction estimates attention over the full cache, with a sampling budget that lets us trade memory reads for accuracy. Remarkably, with 32 or 64 sampled teams, SANTA++ uses 16% to 22% of dense attention's KV reads and retains 94% to 99% of the dense-attention baseline's scores on LongBench v2 and HELMET's retrieval-augmented generation subset, and 85% to 91% on RULER, with Qwen2.5-7B-Instruct at 32K context. With 31 sampled teams, our GPU implementation delivers a $1.69\times$ attention speedup over the dense FlashAttention baseline at 32K context. By reducing the number of cache entries read, SANTA++ in principle complements architectures with compressed KV representations, such as multi-head latent attention. Our kernels are available at: this https URL.

---


### 903. [Verifiable Visual Rewards Transfer from Synthetic Scenes to Natural Prompts](https://arxiv.org/abs/2609.35641)

**<font color=#1a73e8>作者：</font>** Shuyue Stella Li, Xiaochuang Han, Yulia Tsvetkov 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Precise instruction following in image generation, such as satisfying object counts and spatial relations, remains an open challenge at least in part because it is learned using unreliable reward models such as object detectors and vision-language models. We introduce Verifiable Visual Rewards (VVR), the first framework for programmatically verifiable image rewards, and show that training on it generalizes to natural prompts. Each VVR task is a scene of geometric objects and relations among them, from which we derive both the prompt and a deterministic verifier, so tasks can be generated in any number and at any chosen complexity. We release VVRBench, with 10,000 tasks over 32 constraint types, and VVRBench-Challenge, with 720 more complex tasks; the strongest model we evaluate---GPT-Image-2.5---solves 21.4% of VVRBench-Challenge. Using VVR scores as rewards for reinforcement learning (RLVVR) raises the accuracy of Stable Diffusion 3.5 Medium on VVRBench from 2.8% to 28.3% and demonstrates consistent easy-to-hard generalization. These gains extend to out-of-domain benchmarks, and mixing VVR into existing objectives further improves overall performance and human preference, motivating the adoption of VVR into standard image generation post-training recipes.

---


### 904. [Not All Thinking is Created Equal: Latent Reasoning Discovers a Recurrent Search Algorithm for Depth Generalization](https://arxiv.org/abs/2609.35643)

**<font color=#1a73e8>作者：</font>** Huzi Cheng, Zhewei Zhang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models can perform multi-step reasoning and improve task performance through different forms of intermediate computation, from token-based traces to computation carried out in latent space. However, a question remains open: do these different forms of thinking rely on the same underlying mechanism? To address this, we train and compare five variants of the same GPTNeoX backbone from scratch on an extended multi-hop reasoning task (ProsQA-Ext): a vanilla model, a Chain-of-Thought (CoT) model, a Pause Token model, and two latent-reasoning models that are optimized end-to-end without intermediate reasoning traces. We find that, strong in-distribution (ID) performance does not guarantee depth generalization. Vanilla, CoT, and Pause Token models solve ID problems well, but rely largely on local graph features and generalize poorly to out-of-distribution (OOD) problems with longer hops. In contrast, latent variants generalize better and show internal dynamics consistent with forward reachability propagation on the graph. Causal interventions and circuit analysis localize this computation to a sparse recurrent search circuit in the bottleneck latent model: an attention head retrieves graph relations, an MLP and the residual stream update the reachability state across recurrent steps, while multiple attention heads together then do the candidate matching. Together, these results show that different thinking mechanisms can learn distinct computational solutions, even at similar ID performance. In this setting, latent recurrence supports a reusable forward-search algorithm that generalizes beyond the training depth.

---


### 905. [Rubric Rewards from Item Response Theory](https://arxiv.org/abs/2609.35646)

**<font color=#1a73e8>作者：</font>** Milad Yazdani, Yaser Souri, Xiren Zhou 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Many language tasks have no single answer that can be checked automatically. Rubrics provide criteria for judging responses to these tasks. For reinforcement learning, the resulting verdicts must be combined into a scalar reward. A common approach sums the points assigned to satisfied criteria. Distinct verdict patterns can thus receive the same reward, and the fixed points encode how much each criterion should count, not how strongly its verdict distinguishes the current rollouts. Beyond this aggregation problem, judging the full rubric needs more judge requests as the criterion count grows. To address these limitations, Rubric Response Theory (RRT) measures quality and selects criteria when rubric criteria are monotone indicators of a shared target. Rather than adding assigned points, RRT uses a two parameter item response model that treats the verdict pattern as evidence about scalar quality specific to the rubric. Under this model, its likelihood score maximizes the local signal-to-noise ratio for quality. Its Response Parameter Network (RPN) reads the prompt and criterion text to predict criterion difficulty and discrimination. As the policy distribution changes during training, RRT uses online expectation maximization to update the RPN from current rollout verdicts. With Qwen3.5-4B as the policy, RRT's macro criterion score across Medical, Science, Rubrics as Rewards Science, and RubricBench is 1.7 points above that of group relative policy optimization (GRPO). On hard and very hard criteria in Medical and Science, RRT gains 2.8 to 5.6 points over GRPO. At half the criterion budget, adaptive Fisher selection with a frozen RPN keeps the macro criterion score across four datasets within 0.1 points of GRPO with full judging. These results show RRT can reduce judge requests while remaining competitive with GRPO.

---


### 906. [Late Attention Layers Alone Can Copy Entity Tokens, but Not Without Attending to Their Context](https://arxiv.org/abs/2609.35663)

**<font color=#1a73e8>作者：</font>** Muyu He, Yuchen Liu, Ran Tao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) reliably perform entity copying, in which a model copies tokens referring to an entity, termed entity tokens, from the prompt into its output to answer a question. Although entity copying is straightforward for most LLMs, existing research does not provide a systematic account of which layers specialize in this fundamental task or how other tokens in the same sequence, termed context tokens, influence the model's ability to copy the entity tokens. To address these questions, we conduct experiments on Qwen3-8B using two novel methods: genie-in-a-bottle, which controls exactly which layers can participate in an entity-copying task, and attention lobotomy, which cuts off specific tokens' attention to entity tokens without affecting the remaining attention distribution. We find that two distinct groups of layers in the second half of the model are both necessary and sufficient for entity copying. Moreover, in addition to the decoding position's attention to entity tokens, context tokens' attention to entity tokens also proves necessary for copying the exact tokens, even though context tokens do not store entity information themselves unless they satisfy particular semantic properties. Our findings establish the critical role of late layers in entity copying under the guidance of context tokens, calling for future work on how models propagate and consume entity information.

---


### 907. [PhoneCLI: From App Interfaces to Callable Commands for Mobile Agents](https://arxiv.org/abs/2609.35671)

**<font color=#1a73e8>作者：</font>** Yangqin Jiang, Lingrui Xu, Chao Huang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Mobile GUI agents operate through a perception--action loop: at each step they screenshot the device, invoke a vision--language model (VLM), and emit an action. It is slow, costly, and brittle, yet most of what it does is navigation---and everyday navigation is static, ordered, and endlessly repeated. We present PhoneCLI, which compiles an app's GUI navigation into callable commands, without any app-internal API, runtime instrumentation, or model training. Offline, PhoneCLI explores a target app from the outside and distills its screens, interactive elements, and navigation edges into a semantically annotated map; each screen yields one deterministic command: a replay sequence that reaches it. Online, the agent selects a command, verifies it before execution, and then executes it deterministically in sub-second time at zero VLM cost; open-ended interaction and every failure of the compiled path fall back to the embedded VLM interpreter, exactly the pure VLM agent, so compilation can only help. On AndroidLab, PhoneCLI improves the task success rate while reducing steps and token consumption, and it transfers to AndroidWorld's official M3A agent with consistent efficiency gains. What PhoneCLI compiles is the app's navigation rather than one run, so it serves new tasks, not only repeated ones.

---


### 908. [FlowTool: Controlling Tool Parameter in Image Retouching via Flow Matching](https://arxiv.org/abs/2609.35673)

**<font color=#1a73e8>作者：</font>** Thanh-Long V. Le, Steven Walton, Seunghyun Yoon 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Tool-based image editing (image retouching) is commonly formulated with autoregressive multimodal large language models (MLLMs) that sequentially generate reasoning, tool selections, and parameter values. In this work, we present a novel approach to tool-based image editing by framing the task as a flow matching problem. We introduce FlowTool, a framework that directly models the distribution of high-quality tool parameters conditioned on the input image and user instruction using conditional rectified flow. FlowTool combines a vision-language model backbone for multimodal understanding with a Diffusion Transformer parameter generator that transforms Gaussian noise into an editing plan. We train FlowTool with a two-stage supervised flow-matching curriculum, followed by reward-based post-training. Across MMArt-Bench, FlowTool-Eval, ArtEdit-Bench, and MIT-Adobe5K, FlowTool achieves significantly stronger reference-based performance than specialized MLLM editing agents and proprietary MLLMs, while remaining competitive with proprietary models under reference-free evaluation. Moreover, FlowTool significantly improves inference efficiency, reducing latency by at least $50\times$ while requiring nearly $2\times$ less memory than the compared baselines. These results demonstrate that tool-based image editing can be effectively modeled as conditional generation over structured continuous editing parameters, without autoregressive reasoning.

---


### 909. [Verifier Errors in RLVR: Reward Hacking, Limits of Feedback, and Selective Control](https://arxiv.org/abs/2609.35677)

**<font color=#1a73e8>作者：</font>** Christian Moya, Elliott Thornley, Guang Lin  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In reinforcement learning with verifiable rewards (RLVR), imperfect verifiers can reward incorrect responses, creating opportunities for reward hacking. Using gradient flow with a fixed verifier, we characterize the conditions under which reward rises while correctness falls. We then show that the observations available during RLVR are, in general, insufficient to detect or identify accepted errors, or to guarantee their reduction without sacrificing correct responses. To address this limit, we construct a correction using additional feedback about correctness from audits. This correction achieves \emph{selective control}: at the current policy, it lowers the probability of accepted errors and raises that of correct responses, provided it outweighs the pressure toward errors from verifier reward. Experiments with log linear and neural contextual bandits and with a language model support the analysis and show that selective control under partial auditing reduces accepted errors while increasing correctness.

---


### 910. [QuanReview: Offline, Auditable Reconciliation of Human and LLM Span Annotations](https://arxiv.org/abs/2609.35685)

**<font color=#1a73e8>作者：</font>** Matteo Musacchio, Juan Cruz Giner Pulero, Isabel Castañeda 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Structured span annotations, such as quantities with their units, uncertainty modifiers, and event classes, are expensive to create and hard to keep trustworthy once language models enter the loop. We present QuanReview, an open-source system for auditing and correcting such annotation layers. QuanReview aligns two annotation streams over the same documents at character level, resolves unambiguous cases by an explicit and logged policy, and routes candidate conflicts to a browser-based adjudication interface where reviewers accept either side, build field-level hybrids, or flag items for re-annotation. A campaign manager assigns documents to multiple annotators with configurable redundancy, computes agreement at document and span level, auto-merges unanimous documents, and exports the corrected layer in the original file format, so that it can replace the original annotation files directly. Applied to a 4,457-record humanitarian benchmark and an LLM extraction stream, the system fully auto-merged 8% of documents, applied automatic policy decisions to a further 1,513 records, and concentrated human attention on 3,131 candidate conflicts, a mean of 5.4 per reviewed document.

---


### 911. [Rethinking Circuit Evaluation: Do Circuits Explain Model Errors?](https://arxiv.org/abs/2609.35686)

**<font color=#1a73e8>作者：</font>** Li Zhang, Chuqin Geng, Mark Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mechanistic interpretability (MI) aims to explain a model's behaviour through analyzing its internal computations; circuit-based explanations aim to isolate these computations with compact subnetworks validated by ablating the rest of the model. We show that circuits validated this way may fail to recover the underlying mechanism of the model's behaviour by closely reproducing its successful decisions while failing to account for most of its errors. Such explanations should account for the model's particular errors as well as its successes. We evaluate this requirement by measuring exact answer agreement separately on model successes and failures, across circuit sizes and ablation settings, on IOI, Docstring, and six model-task settings from the Mechanistic Interpretability Benchmark. We discover that many tested circuits closely replicate correct behaviour while missing most of the model's errors. On indirect object identification (IOI) for GPT-2 small, under mean ablation, the manual circuit and tested automated circuits, including one trained against the model's full output distribution, agree with the model on 97.3-99.5% of prompts it answers correctly but only 11.4-41.7% of errors. An IOI case study shows that lost errors are recoverable by restoring omitted attention-heads which raise error reproduction from 14.2% to 75.1% on a separate held-out set with 0.41 percentage point decrease on correct agreement, exceeding matched random extensions and scalar-biased control. Intervention traces show how omitted computations produce specific wrong answers for a reproducible subset of errors. In all, these findings show circuits can preserve task success without adequately explaining model's failures, and support exact error reproduction as a necessary, but not sufficient, test of circuit-based explanations of model behaviour.

---


### 912. [Report: Progressive Disclosure of Agent Skills](https://arxiv.org/abs/2609.35692)

**<font color=#1a73e8>作者：</font>** Guilin Zhang, Kai Zhao, Priyanka Mudgal 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Users of Workday's deployed LLM-based agents often request features which can be addressed by defining named procedures, also known as skills, in the LLM context, effectively augmenting agents' capabilities. However, as an agent's skills library grows in size, so does the agent's operational cost. Progressive disclosure (lazy-loading) of skills as needed may reduce operational costs, but its impact on overall latency and skill-retrieval quality remains unclear. In this report, we investigate the impact empirically and find that progressive disclosure improves skill-retrieval quality but marginally degrades overall latency.

---


### 913. [Rethinking Personalized Generation: Test-Time Alignment via Factorized Ranking Models](https://arxiv.org/abs/2609.35695)

**<font color=#1a73e8>作者：</font>** Qiyao Ma, Junshan Zhang, Zhe Zhao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Aligning large language models (LLMs) to diverse user preferences is fundamentally hindered by standard alignment paradigms that optimize for monolithic users. In this work, empirical studies are first used to reveal the existence of a massive, untapped performance headroom for personalized generation through test-time alignment. We demonstrate that personalized generation is uniquely suited for test-time scaling methods like Best-of-N (BoN) because it can be viewed primarily as a candidate matching problem rather than a generator capability bottleneck. While reward models could in principle exploit this headroom, they are poorly calibrated for personalization, and their billion-parameter scale makes scoring large candidate pools prohibitively expensive. To overcome this limitation, we propose a parameter-efficient framework utilizing million-parameter scale multi-layer perceptron (MLP) ranking models. Our personalized ranking model directly reuses the internal embeddings of the base generator with minimal overhead. By scaling train-time data to provide fine-grained personalized preferences, this million-parameter ranking model accurately scores large candidate pools and can seamlessly guide generation to reduce the cost of materializing N candidates. Extensive experiments on nine datasets spanning three personalized generation settings show that our personalized ranking model effectively exploits the discovered headroom, outperforming billion-parameter generalist reward models on every dataset, with under 0.4% of their parameters and four orders of magnitude lower scoring latency.

---


### 914. [Distillation Defenses Easily Break After Reinforcement Learning](https://arxiv.org/abs/2609.35699)

**<font color=#1a73e8>作者：</font>** Shidan Javaheri, Alexander Panfilov, Oliver Britton 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Distillation attacks copy the reasoning capabilities of closed-source large language models, allowing bad actors to replicate state-of-the-art performance at low cost. Attackers systematically collect a large volume of frontier model reasoning traces and then train (i.e., "distill") their own models on these traces. Existing defenses against distillation attacks are typically evaluated immediately after distillation, implicitly assuming attackers do not train their models any further. In this paper, we argue that a more realistic threat model includes further training with reinforcement learning after distillation. A misspecified threat model can give a false sense of security -- some defenses that seem effective after distillation can be broken after subsequent reinforcement learning. Practically, reinforcement learning lowers the bar for a distillation attack to be effective. We show that simple attacks can steal reasoning capabilities from existing closed-source language models using data easily obtainable from current APIs, yielding reasoning improvements equivalent to more sophisticated attacks that extract the full hidden traces. Results indicate that any distillation defense that leaks sufficient information to reconstruct approximate reasoning traces is likely ineffective. We conclude by discussing broader implications and batch-level distillation defenses which could be more effective.

---


### 915. [MeqMuon: Matrix-Equilibrating Muon for LLM Pretraining](https://arxiv.org/abs/2609.35701)

**<font color=#1a73e8>作者：</font>** Chang-Wei Shi, Xu Wang, Wu-Jun Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The success of large language models (LLMs) has been accompanied by continued growth in model size and pretraining costs. Muon offers high accuracy and training efficiency in LLM pretraining. Recent work introduces row-wise normalization into Muon to balance update magnitudes and improve pretraining performance. However, row-wise normalization alone cannot accommodate different imbalance patterns in update matrices. In this paper, we propose an improved Muon optimizer, called \underline{m}atrix-\underline{eq}uilibrating Muon~(MeqMuon), for LLM pretraining. MeqMuon balances both row and column magnitudes through normalization that can be automatically tailored to different imbalance patterns without manual intervention. Moreover, MeqMuon eliminates the need to store AdamW's second-moment estimates, reducing optimizer-state memory usage. Empirical results demonstrate that MeqMuon achieves better convergence performance than AdamW, Muon, and other baselines in LLM pretraining.

---


### 916. [Reinforcing Agentic Creativity in Scientific Ideation with Night Science](https://arxiv.org/abs/2609.35706)

**<font color=#1a73e8>作者：</font>** Priyanka Kargupta, Silviu Cucerzan, Shweti Mahajan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) excel at structured, verifiable tasks, but their low-entropy bias can produce homogeneous and predictable outputs, limiting their utility for open-ended scientific ideation. Effective discovery, however, spans a broader creative spectrum: from structured day science to loosely structured, serendipitous night science that reaches ideas beyond those typically considered. We introduce AI Night-Scientist, an agentic framework that uses reinforcement learning to teach models when and how to depart from predictable reasoning. Grounded in cognitive science, we model creativity along three axes: action (what to do and how creatively), process (when to explore versus exploit), and outcome (the novelty and usefulness of the resulting idea). We use these axes to train models with GRPO, exposing them to varying degrees and forms of creativity throughout training. This produces substantially more diverse scientific proposals, expanding the range of research directions by 27.8% and contribution types by 14.9% over the base model. It also improves predicted citation impact by up to 32.0 percentage points and originality by 66.2 points. These gains cannot be reproduced by simply increasing decoding temperature; instead, we find that semantic guidance specifying what kind of creativity to pursue is critical. Overall, our results suggest that creativity is a learnable, multi-level ability that can be shaped to help researchers reach ideas beyond those typically explored by LLMs.

---


### 917. [ScAn-Bench: Evaluating Scaling Analysis Methodology](https://arxiv.org/abs/2609.35707)

**<font color=#1a73e8>作者：</font>** Artin Sermaxhaj, Nastaran Alipour, Donat Sinani 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent progress in machine learning is driven by large-scale foundation models, where scaling laws and finding optimal scaling prescriptions for architecture, data, and hyperparameters are key in advancing the state-of-the-art. Therefore, it is surprising that no systematic study evaluates the methodology to obtain scaling laws and prescriptions across different model types. To shed light on this crucial blind spot and facilitate future research, we introduce the surrogate benchmarks ScAn-Bench-LLM and ScAn-Bench-VLM based on 4524 and 8024 checkpoints of language and vision-language model pipelines. On our benchmarks, we perform the first systematic evaluation of both data acquisition and extrapolation methodology for scaling analysis across different data modalities.

---


### 918. [Hard Vision, Easy Vision: What GPT-6 Astra Reveals Across Computer Vision](https://arxiv.org/abs/2609.35718)

**<font color=#1a73e8>作者：</font>** Hanoona Rasheed, Mohammed Irfan Kurpath, Bin Ren 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Frontier general-purpose systems are rapidly expanding beyond visual understanding into capabilities traditionally handled by dedicated computer-vision models. As these capabilities expand, a central question for the computer-vision community is how far this reach extends, and what remains hard. We evaluate GPT-6 Astra alongside five frontier general-purpose AI systems across 34 capabilities and 55 benchmarks spanning nine areas of computer vision. We compare their performance with dedicated models and humans where suitable references are available. Astra demonstrates broad visual capability, with substantial gains over other frontier systems in visual and spatial reasoning and several forms of structured prediction. Across the state-of-the-art systems, a consistent pattern emerges. Capabilities involving semantic interpretation, reasoning, and object-centric prediction increasingly approach or reach available reference levels. In contrast, larger gaps remain when tasks require metric geometric accuracy, faithful reconstruction, temporally consistent dense prediction, or specialized fine-grained visual knowledge. Additional reasoning and specialist tools close selected gaps, but their benefits vary across capabilities. These results map a changing landscape of computer vision in which increasingly sophisticated visual tasks are accessible through a general-purpose interface, while precise and fidelity-sensitive perception remains an important frontier.

---


### 919. [Failure-Transparent Agents: Benchmarking Post-Failure Reporting in Tool-Using Language Models](https://arxiv.org/abs/2609.35732)

**<font color=#1a73e8>作者：</font>** Junru Zhu, Shiming Xie, Aime Lu Fan Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Tool-using agents can fail twice: a required tool can fail, and the agent can then report success without the evidence needed to justify it. Existing benchmarks often entangle this reporting failure with tool selection, recovery, and environment dynamics. We introduce Failure-Transparent Agents (FTA), a controlled benchmark that fixes the failed observation and required evidence state before generation, making post-failure claims directly auditable. FTA contains 100 tasks with deterministic failure traces spanning five failure families, a neutral control, and four user-pressure conditions, and evaluates unsupported claims alongside useful recovery. Across six models, three response policies, and 3,600 human-annotated responses, false-success rates are 22.8% under the baseline policy, 9.3% with a transparency instruction, and 0.8% with a structured evidence contract. Fabricated-detail rates decrease from 28.3% to 14.3% and 0.8%, while useful responses increase from 74.9% to 89.2% and 98.8%, respectively. The tested evidence-contract policy is associated with substantially lower post-failure reporting errors while useful-response rates remain high within this blocked-task benchmark.

---


### 920. [Harness Learning Enables Generalizable Test-Time Adaptation](https://arxiv.org/abs/2609.35738)

**<font color=#1a73e8>作者：</font>** Alvin Zhang, Xuecheng Liu, Zixuan Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A language-model agent is jointly defined by its model and its harness, the executable program that organizes model calls, tool use, and information flow. Because different tasks call for different ways of organizing these operations, the harness needs to be adapted using feedback from the task at hand. We introduce harness learning, which trains a proposer model to revise a solver's harness using execution feedback. We formulate this process as meta-learning over executable programs, with harness revisions playing the role of weight updates in gradient-based adaptation. We train the proposer with reinforcement learning, using the task performance of revised harnesses as the reward. At test time, the proposer uses feedback from successive executions on a new task to refine the harness, without performing any parameter-space update. Experiments on reasoning and multi-hop question answering show that harness learning improves revision quality and that the ability to adapt at test time transfers to unseen tasks. Policies trained on individual revisions can continue improving harnesses over multiple rounds, while the benefits of training on revision sequences vary across settings. These findings suggest a path towards continually learning agents that turn accumulated experience into generalizable improvements.

---


### 921. [Shockingly Simple Self-retrospection Improves Agentic Models Without RL](https://arxiv.org/abs/2609.35741)

**<font color=#1a73e8>作者：</font>** Jonathan Light, Christopher Zhang Cui, Jeonghye Kim 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> People learn not only by repeating successful actions, but also by recounting and explaining their experiences, revising their understanding to guide future behavior. Can a language-model agent improve its future actions by training only on explanations of its own experience? We investigate this question by studying Retrospection-Only Fine-Tuning (ROFT), a minimal online procedure designed to isolate the effect of explanation-only training on subsequent behavior. The agent attempts a task, observes available feedback, generates a retrospective explanation, and is fine-tuned with a next-token prediction loss on the explanation tokens alone. The procedure uses neither an external teacher nor a reward-based policy update. In software-engineering experiments with Qwen3.5-4B, ROFT is trained on problems with mixed successful and unsuccessful base-model attempts. On held-out SWE-bench Verified and Pro, it reaches 49.2% and 26.8% solve rates after 20 updates without using a verifier, compared with GRPO's 48.0% and 25.3% after 40 updates in the evaluated runs, and makes faster early progress in training time and sampled attempts. It also learns to solve individual tasks on which all 64 sampled base-model attempts failed, showing that learning can begin without any initially successful trajectories. Behavioral analyses find that ROFT indirectly assigns credit to actions, encouraging good actions and discouraging incorrect ones. Moreover, prompting retrospections to emphasize more direct solutions yields shorter subsequent attempts even without an explicit length penalty. Together, these findings show that learning to explain can also improve learning to do, establishing self-generated retrospections as useful training targets and motivating further study of explanation-to-action transfer.

---


### 922. [Improving Test-Time Scaling with Adaptive Looped Transformers](https://arxiv.org/abs/2609.35748)

**<font color=#1a73e8>作者：</font>** Yichen You, Tianyu Fu, Aosong Feng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Looped transformers have demonstrated promising parameter efficiency by reusing layers for latent computation. Prior studies compare looped and non-looped models at matched parameters or per-token FLOPs. However, to the best of our knowledge, whether looping improves test-time scaling as outputs grow longer remains underexplored. Through post-training looped transformers, we study the accuracy-compute slope, measured as the accuracy gain per doubling of test-time decoding FLOPs. We find that existing looped transformers often yield steeper slopes than their non-looped baseline, yet underperform it at matched compute. While fixed-depth looping spends extra iterations on every token, our analysis shows that many tokens do not benefit from extra iterations. We therefore propose TaH2, which enables the model to focus extra iterations on the tokens that benefit from looping. It jointly post-trains the backbone and an iteration decider through lookahead depth supervision, which uses online labels indicating whether further iteration improves the prediction. TaH2 improves both the efficiency and attainable accuracy of test-time scaling. On challenging AIME benchmarks, TaH2 improves the accuracy-compute slope by 53% (2.74 vs. 1.79) over the non-looped baseline, exceeding the baseline's peak accuracy by about 3.4 points at matched test-time compute. As the maximum iteration depth increases, existing looped models largely plateau, while TaH2's gain over the non-looped baseline continues to grow from +2.8 points at depth 2 to +3.9 points at depth 8. Our code is available at this https URL.

---


### 923. [Towards Communication-Efficient Social Intelligence in Language Agents](https://arxiv.org/abs/2609.35749)

**<font color=#1a73e8>作者：</font>** Linxiao Gong, Yijie Xu, Tianfu Wang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Socially intelligent language agents must negotiate, coordinate, and resolve conflicting preferences while respecting the time and attention of both participants. Balancing these demands is challenging because agents must convey enough to address a partner's constraints and advance their goals without adding words that do not help the interaction. In this paper, we propose Teacher-Assisted Communication Training (TACT) to improve social goal attainment while reducing communication cost, making interactions with agents more productive and less demanding. We first characterize communication efficiency in terms of action strategy and expression, whose effects extend beyond the current utterance to the partner's response and subsequent exchanges. We design TACT to revise student-generated actions, test the revisions through partner responses, and distill useful feedback into the student. An expression specialist removes unnecessary detail while preserving the intended action, while a strategy specialist proposes alternatives that may better address the partner's constraints. To determine which revision helps, TACT samples a partner response for each candidate and selects a teacher reference by balancing local goal support against action-token cost. That reference guides on-policy distillation on the student's own generation prefixes, allowing the student to act independently at deployment. We evaluate TACT on SOTOPIA and AgentSense. On SOTOPIA, it achieves the highest Goal among the evaluated methods on All and Hard while using substantially fewer target tokens than SFT+SDPO. On AgentSense, it improves goal success over the initial student while reducing target tokens and interaction messages.

---


### 924. [KV-streams for Efficient Compaction in Agentic Reinforcement Learning](https://arxiv.org/abs/2609.35750)

**<font color=#1a73e8>作者：</font>** Emiliano Penaloza, Dane Malenfant, Dheeraj Vattikonda 等 18 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Scaling the horizon of agentic LLMs is bottlenecked by the need to fit ever longer context traces in GPU memory. Context compaction has been the most popular mechanism to alleviate this issue, keeping GPU memory constant for a given trace. Unfortunately, most compaction strategies rely on prefilling the LLM context many times over, hindering training throughput. To alleviate this bottleneck and enable efficient trainable compaction, we propose KV-streams, a plug-and-play strategy compatible with any compaction strategy that substantially increases throughput while showing no evidence of hindering performance. KV-streams enable scalable compaction by streaming the KV cache forward rather than flushing it after each compaction. We show that KV-streams enable three different compaction strategies, achieving a 2.6 to 5x wall-clock speedup in training. Beyond efficiency, we find that the streamed KV cache can act as a recurrent state, carrying forward information that has long since disappeared from the context. Specifically, in a controlled setting we show that, contrary to prior work, RL alone is all that is needed for this behavior to emerge. Overall, we show KV-streams to be an efficient and lightweight plug-and-play addition to any post-training pipeline.

---


### 925. [How to Loop MoE: Flatten the Experts, Untie the Attention](https://arxiv.org/abs/2609.35751)

**<font color=#1a73e8>作者：</font>** Shouren Wang, Chuang Ma, Mohsen Hariri 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Looped Transformers reuse one block of layers several times: by spending extra computation they push a model of fixed size further, and so use its parameters more fully; while sparse mixture-of-experts (MoE) models activate only a few of many experts for each token. Looped MoE bridges these two design philosophies and gives MoE models new potential for better expert usage, but it raises a question: how to loop a MoE? We answer it with Foil. With the expert parameters and the expert compute per token held fixed, Foil (1) flattens the experts, halving the expert layers, doubling the experts per layer and doubling the passes, so that every routing decision chooses from a larger pool, and (2) unties the attention, giving each pass its own attention parameters while the experts and routers stay shared. Experiments show that Foil clearly outperforms the unflattened looped baseline: at 20B tokens every Foil model has lower pretraining loss than the baseline; at 100B tokens the loss improves monotonically with the degree of flattening, the most flattened Foil ending 0.012 nat below the baseline at equal parameters and compute, with downstream accuracy on par or better; untying the attention also yields more balanced and more confident routing at equal shape. Our ablations analyse why Foil works and turn the findings into design guidance for looped MoE: the returns of looping and of widening the expert layers amplify each other, routing confidence tracks healthy expert use better than load balance, and a sparse looped MoE should therefore use more experts per layer and more passes. Code and configurations are available at this https URL.

---


### 926. [Scaling Long-Form Story Generation via Narrative State Tracking](https://arxiv.org/abs/2609.35759)

**<font color=#1a73e8>作者：</font>** Zhennan Wan, Jianfei Chen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLMs have demonstrated strong capabilities in creative writing. However, scaling them to full-length novels remains challenging, as maintaining narrative consistency becomes increasingly difficult. Existing story-generation methods typically focus on stories of up to about ten thousand words, leaving their ability to scale to full-length novels underexplored. In this work, we introduce Narrative State Tracking Agent (NstAgent), a training-free agentic framework that allows LLMs to track a structured narrative state including characters, past events and future requirements. We extend an existing benchmark to compare narrative consistency across lengths, and use it together with a writing-quality benchmark to systematically evaluate stories ranging from 10K to 100K words. We show that NstAgent achieves better narrative consistency and writing quality as stories grow longer, and neither of them degrades noticeably as length increases, suggesting that it provides an effective approach to scaling story generation toward full-length novels.

---


### 927. [TokenCast: Forecasting Token Consumption During LLM Agent Execution](https://arxiv.org/abs/2609.35760)

**<font color=#1a73e8>作者：</font>** Chaoqian Ouyang, Ling Yue, Libin Zheng 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> When a large language model (LLM) agent executes the same task, token consumption can vary by over an order of magnitude across runs. The agent chooses its next steps based on tool feedback and intermediate results, while the growing context steadily inflates the input size of every subsequent call. The total consumption of a task is therefore hard to predict before execution and the prediction must be revised as the run unfolds. In this paper, we propose TokenCast, which learns a composable cost representation for each execution segment, recording its own consumption and the context growth it introduces. Composing adjacent segments yields a cumulative estimate that captures the extra input cost incurred when context from earlier segments is re-read by every later call. As execution unfolds, newly observed evidence refreshes the forecast, requiring no additional LLM calls and incurring a mean cumulative prediction time of 32.8 ms per run on SWE-bench Verified. Across 4 task suites and 6 agent models, TokenCast's mean absolute error reduction against the strongest comparator averages 14.5% over 96 evaluated combinations. In offline budget-control replay, TokenCast uses 21.3% fewer tokens on average than a fixed-budget policy at matched trace completion. The code is available at this https URL.

---


### 928. [Telescopic Language Models](https://arxiv.org/abs/2609.35769)

**<font color=#1a73e8>作者：</font>** Zhilin Guo, Boqiao Zhang, Hakan Aktas 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> One deployed language model must often serve many compute budgets, yet serving each budget still means a separate training or compression run per point. We train a Telescopic Language Model (TLM) to be that continuum: a nested-capacity Transformer supervised by stochastic prefix supervision with a full anchor. At every step, one randomly truncated prefix of the capacity axis is trained against the full next-token target, alongside one full-capacity pass, so the trained artifact is a valid language model at every depth. Two forward-backward passes per step, no architectural change, nothing extra at inference. Fixed-exit suites such as Matryoshka Language Model Suites (MLMS) occupy one point in this design space, and the point has a cost: supervising only a few fixed exits leaves the nested model at chance level everywhere else (perplexity 10^2-10^5 in our baselines). On a 200M proxy suite (20B FineWeb-Edu tokens, identical data stream for all methods), a single TLM run is a valid language model at every one of its twenty layer prefixes, in perplexity and on perplexity-sensitive downstream tasks, reducing the area under the quality-budget curve by 43-44% relative to the fixed-exit suites while matching them at full capacity, at ~12% lower GPU cost per run. The prefix sampling density is a dial: concentrating it on a few depths recovers fixed-exit quality there at the price of the continuum, so the operating points become a training-time choice rather than an architectural one. These results indicate that the training objective, not the nesting itself, is what makes a model elastic.

---


## ⚠️ 待复核论文

> 以下论文保留内部待复核标记，并统一放在大模型章节末尾。

### 929. [Enhancing Foundation Models for Imbalanced SAR Ship Classification via Targeted Oversampling](https://arxiv.org/abs/2609.31657)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Ch Muhammad Awais, Marco Reggiannini, Davide Moroni  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Remote-sensing foundation models offer strong representations for SAR imagery, but their behavior under severe long-tail class imbalance is still not well characterized. We benchmark DOFA and SAR-JEPA on the imbalanced OpenSARShip dataset and compare them with ImageNet-pretrained baselines under a fixed, training-efficient protocol that keeps the backbone frozen. To mitigate imbalance without fine-tuning, we apply four oversampling methods in embedding space exclusively to minority classes and train a lightweight classifier head on the augmented embeddings. Across both foundation models, oversampling improves Macro-F1 and test accuracy relative to their respective baselines, with the largest Macro-F1 gains observed for DOFA using ADASYN (34.39 to 38.56) and for SAR-JEPA using SVM-SMOTE (25.89 to 32.30). We also report class-wise behavior, showing that aggregate improvements can coexist with persistent failures on specific rare classes. Code for embedding extraction and reproducible multi-seed evaluation is provided to support rapid experimentation on free-tier hardware.

---


### 930. [Medium-Term Multi-Resolution Electric Load Forecasting using Economic Data and Foundation Model](https://arxiv.org/abs/2609.31806)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Lindas Eloi, Goude Yannig, Ciais Philippe  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate medium-term, from a few months to a few years, electricity load forecasts are crucial for informed decision-making in power plant maintenance scheduling, load dispatch and price settlement. Being comprised between Long-Term Load Forecasting (LTLF) which uses mostly economic projections and appliances development scenarios, and Short-Term Load Forecasting (STLF) driven by weather, calendar and autoregressive patterns, Medium-Term Load Forecasting (MTLF) requires both extrapolation capabilities and variability modeling. Yet, it remains unclear if MTLF can benefit from economic indicators, and especially at which forecast horizon and resolution. To address these challenges we investigated the impact of socioeconomic data on predictions issued 1 month and up to 48 months in advance for France at monthly and daily resolution using a tabular Foundation Model (FM). A dataset covering 20 years of observations of electricity load, weather variables and economic features such as consumer price and production indices, electric vehicle counts or employment is created for the study. To avoid noisy data, we used a new feature selection pipeline, creating ensemble of expert models with diverse feature subsets, to demonstrate that selected economic covariates improve forecast skill by 20% over 2015-2025. This enhancement is steady across lead times and resolutions limiting the Mean Absolute Percentage Error to 4% for monthly granularity and 5% for daily granularity. Explainability of the models is investigated through feature and context importance. Results showed that the FM is limited in the context it leverages pointing towards potential computational savings with a reduced context, while feature importance of economic predictors grows with the forecast horizon. This suggests that including economic data in MTLF could bridge the gap with LTLF leading to seamless forecasts.

---


### 931. [A Surgical Foundation Model Reveals Task-Dependent Label Efficiency](https://arxiv.org/abs/2609.31821)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Florian Philipp Stilz, Lorenzo Arboit, Vinkle Srivastav 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Developing label-efficient models is a central challenge in surgical AI due to the high cost and scarcity of expert annotation. While self-supervised foundation models adapt well to new tasks with minimal data, how label efficiency varies across different surgical tasks remains largely unexplored.
Here, we introduce SURGE, a surgical foundation model trained on SurgSpectrum-30M+, the largest pretraining dataset comprising over 30 million frames, with checkpoints released to enable further research. We systematically evaluate label efficiency across 5 task categories and 15 benchmarks. These range from temporal and spatial scene understanding to fine-grained reasoning tied to instrument-anatomy interactions and safety-critical maneuvers.
SURGE outperforms prior state-of-the-art on all benchmarks, even surpassing task-specific models on complex reasoning tasks. Crucially, we reveal a task-dependent scaling behavior: while scene understanding tasks saturate with minimal supervision, fine-grained reasoning tasks continue improving with substantially larger annotation budgets, providing a blueprint for allocating expert effort in complex domains.
Code: this https URL

---


### 932. [Memory as Middleware for Self-Improving AI Agents](https://arxiv.org/abs/2609.32091)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** K. R. Jayaram, Vatche Isahagian, Vinod Muthusamy 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI agents are stateless across sessions by default and therefore operationally amnesic: each session begins with little durable knowledge of prior failures, repairs, preferences, or successful strategies. As a result, agents repeat the same mistakes and discard hard-won experience. The dominant fix is \emph{bespoke memory}---retrieval, persistence, and learning logic hand-wired into one agent and bound to one storage engine. This creates a fragmented landscape where memory cannot be swapped, shared, isolated, or reasoned about independently of the agent that owns it. We argue that this is a middleware problem: agent memory deserves a first-class, pluggable layer, just as data access, messaging, and persistence each became middleware concerns.
We develop this vision through six systems challenges: two-sided pluggability, host-native interposition, multi-tenant isolation, write-path consistency, federated sharing with provenance, and lifecycle governance. We present ALTK-Evolve, a reference implementation of memory middleware for self-improving agents, and use it to motivate a broader research agenda for future memory middleware.

---


### 933. [Scalable In-Domain Self-Supervised Foundation Model for Dense Representation Transfer in High-Resolution Plant Imaging](https://arxiv.org/abs/2609.32183)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Junlin Guo, Sharmin Majumder, Isaac Lyngaas 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> High-resolution plant imaging enables detailed characterization of plant morphology, but dense scientific analysis remains limited by costly pixel-level annotations, large image pixel dimensions, and substantial variation in imaging conditions. This work proposes a scalable in-domain self-supervised pretrained foundation model for high-resolution, high-pixel-dimension multi-species plant imagery. A masked autoencoder with a ViT backbone is pretrained on more than 10 million multi-view plant image tiles using distributed training. Following scalable pretraining, the learned foundation-model representations are comprehensively benchmarked across fine-grained dense prediction and coarse global feature recognition, with particular emphasis on limited supervision and realistic downstream imaging conditions. This work focuses on the domain gap of existing foundation models in dense feature representation and transfer. Through extensive experiments involving limited annotations, cross-view variation, and resolution degradation, the in-domain FM achieves a Mean Dice of 0.8686 and a Pooled Dice of 0.8959, outperforming an MAE counterpart pretrained on large-scale natural-image data by 0.0694 and 0.0613, respectively. The results further indicate that increasing pretraining scale produces consistent improvements in dense feature transfer. Overall, these findings suggest that scaling in-domain self-supervised pretraining can reduce the domain gap and improve transferable dense representations for high-pixel-dimension scientific imaging.

---


### 934. [AI Harness: Certification under Proposal-Conditioned Information for Foundation-Model Agents](https://arxiv.org/abs/2609.32184)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Hailin Zhong, Shengxin Zhu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Foundation-model agents are often modeled as policies over an observed state. In deployed systems, however, a runtime may intervene only after the model has emitted a semantic proposal, making the proposal both an action candidate and a decision-time observation generated by a history-conditioned process. We show that collapsing this structure into a state-only proposal envelope can preserve proposal coverage while destroying certifiability. In a finite robust interface, the viability kernel of the collapsed model is contained in the physical projection of the history-augmented kernel, and the collapse is lossless exactly when every proposal-conditioned collapsed fiber retains a common robust-safe intervention. This gap can be maximal even with constant-size proposal and history alphabets. The same common-action condition yields a dual result: observing the current proposal can restore robust feasibility when it separates latent modes requiring incompatible interventions. We extend these one-step results over time using exact finite beliefs and standard safety and reachability fixed points, separating indefinite operational viability from finite worst-case verified progress. Controlled model-in-the-loop tests reproduce the predicted obstructions when telemetry or effect verification is removed or intervention authority is restricted. Thus, our contribution is not a new fixed-point calculus, but a characterization of when proposal--history correlation at the model--tool boundary is necessary for certification.

---


### 935. [Fracast-0: Fractal Weight Sharing for a Time Series Foundation Model with Only 85K Parameters](https://arxiv.org/abs/2609.32209)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Tianxiang Zhan, Huanyao Zhang, Yuanpeng He  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Time series foundation models must preserve multi-domain breadth, probabilistic output, and multiple temporal scales, but parameter count grows when each scale receives a separate representation. We introduce Fracast-0, a probabilistic forecasting foundation model that exploits temporal self-similarity to reuse one operator across scales. A parameter-free detector extracts significant seasonal structure. The encoder applies a shared local block along a geometric dilation ladder with scale conditioning, while the decoder combines context-gathered states with an explicit seasonal future state and reuses a second block along another ladder before emitting nine quantiles. Pretraining across six corpora preserves multi-domain breadth within 85,001 parameters. On 97 GIFT-Eval configurations without per-dataset fine-tuning, Fracast-0 is the smallest of 28 evaluated checkpoints and remains non-dominated in the aggregate parameter-accuracy plane with MASE 0.808 and WQL 0.564. It uses 42.0% fewer parameters than TinyCast, whose MASE and WQL are 4.2% and 3.3% lower. These results support cross-scale weight reuse as a practical route to further time series foundation model compression.

---


### 936. [When Does a Skill Add Value? Task-Conditional Gain Prediction for Selective Skill Use](https://arxiv.org/abs/2609.32274)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Anjie Xu, Zhiyu Zhang, Ruiqing Ding 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agent skills are expected to improve task performance. Yet we find that they often provide no benefit, and can even hurt performance while incurring additional token costs. Can we predict whether a skill will help before the agent acts? We introduce SkillDelta, a framework for predicting task-conditional skill gains from paired executions of the same agent with and without the skill. A local predictor transfers these historical gains to new tasks without retraining the agent. Under explicit transfer assumptions, our analysis links support coverage, representation mismatch, and execution noise to prediction error and decision regret. Across five benchmarks and three target agents, paired history improves observed-gain ranking over skill-assisted outcomes alone in 12 of 15 settings. At matched expected skill-use rates, SkillDelta improves success over random activation in all 15 settings, with an average absolute gain of 4.3%. Most of this advantage comes from allocation across task groups. Evidence for additional within-group selection value is strongest on ToolQA and weaker elsewhere. Code is available at this https URL.

---


### 937. [A Solvable Theory of Pre-training Data Poisoning: Regime-Dependent Scaling Exponents](https://arxiv.org/abs/2609.32288)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Indranil Halder, Rastri Dey, Cengiz Pehlevan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Pre-training data poisoning of large language models is usually studied using targeted backdoors and their survival through safety post-training, which leaves open a more basic question: how does a model's clean data performance degrade as the poison rate $\varepsilon$ grows? Motivated by our controlled pre-training runs of OLMo-style models, in which the relative clean data validation perplexity increase $\Delta$ between poisoned and clean models matched in architecture, token budget, and optimization schedule is well fit by a power law $\Delta\approx C\varepsilon^{a}$ with a non-integer exponent, we ask what such a law requires theoretically. We first prove an analyticity barrier: whenever the contaminated objective depends analytically on $\varepsilon$ around a nondegenerate clean data optimum, $\Delta$ is generically quadratic in $\varepsilon$, so a generic non-integer exponent is a signature of genuinely singular structure. We then supply that structure in solvable truncated ridge regression with heavy-tailed covariates, controlled by $q_\star$, and a label-shift poisoning. Our central result is that the excess risk scaling exponent depending on the order of limits: in the higher dimensional proportional regime it is $\epsilon^{q_\star/(q_\star+2)}$, whereas taking the ample-data limit first gives $\epsilon^{2-2/q_\star}$, and the limits do not commute. We confirm this prediction through several numerical simulations. Finally, we argue that finite training time plays the role of truncation on the curvature spectrum in local LLM pre-training, deriving the observed scaling law under heavy tailed inverse curvature spectrum as a modeling hypothesis.

---


### 938. [Phase Space Attention:A Hairer Lift Circumvents the Single-Layer Induction Obstruction](https://arxiv.org/abs/2609.32319)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Kingsuk Maitra, Shagun Sood Morteza Hosseini, Suman Gunnala 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We circumvent the Sanford-Hsu-Telgarsky (SHT) single-layer induction obstruction within a linear, one-step, causal, bilinear, symplectically consistent design class on the post-RoPE substrate, by lifting attention onto a symplectic phase space, mirroring Hairer's lift of Stormer-Verlet. The lift exits the premise of the SHT counting argument rather than the bound itself. The reframing exhibits the obstruction as a filter-order gap: a one-layer bilinear score realises a $z$-transform of joint order $(0,0)$, whereas the induction discriminator requires key-side order $\geq 1$. Applying the symplectic upper shear $M_\gamma:(q,p)\mapsto(q+\gamma p,p)$ to the post-RoPE query and key streams closes it. We prove this lift is unique within the factorised subclass, exactly symplectic at operator level, and requires post-RoPE placement; and in an explicit $T_4$-only Gaussian reduction we derive a closed-form two-branch induction phase transition, held out at $r=0.9876$ with zero fitted parameters. That law is an analytically solvable limit, not a robust prediction: restoring the $T_3$ channel moves $\gamma_c$ at $d_k=64$ from 1.030 to 0.569 and removes the crossover.
Deployability follows by exact derivation: the KV cache is unchanged, prefix reuse and speculative decoding are preserved, overhead is $6d$ FLOPs per token per layer, INT8 headroom grows by at most $\log_2(1+2\gamma)$ bits, fused kernels are unmodified, and no parameters are added.
At 91.3M parameters a supercritical sweep locates an emergence band: induction forms 3/3 seeds at $\gamma=0.80$ in a mean of 717 steps, against 2/3 seeds and 2700 steps at $\gamma=0$. Adverse results are reported as directly: a key-only half-lift reaches 0.949 against 0.811 for the symmetric operator, so if induction accuracy is the objective, the half-lift is the better construction. Forty-one notebooks and result files ship as ancillary material.

---


### 939. [FoundDSR: A Generalizable Foundation Model with Guided 2D Gaussian Splatting for Depth Super-Resolution](https://arxiv.org/abs/2609.32323)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Zhengxue Wang, Zhiqiang Yan, Yuan Wu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce FoundDSR, a generalizable foundation model for robust depth reconstruction across unseen data distributions using RGB-D pairs. FoundDSR begins with a guided 2D Gaussian Splatting strategy to model depth representations with Gaussian primitives. This strategy employs high-resolution RGB as prompts to optimize the Gaussian parameters, thereby encouraging each Gaussian primitive to anisotropically deform along high-frequency structural directions. The resulting Gaussian-upsampled representations are then mapped to high-resolution depth through an effective depth reconstruction branch. Furthermore, to mitigate training instability and bias toward dominant sources caused by distribution gaps in large-scale heterogeneous data, we introduce heterogeneous federated learning that allocates each data source to an independent client for local optimization and global aggregation. This design effectively endows FoundDSR with stable scalability to diverse and large-scale training data. Extensive zero-shot evaluations on synthetic, real-world, arbitrary-scale, and noisy conditions demonstrate that FoundDSR consistently outperforms existing state-of-the-art approaches, confirming its strong robustness and generalization to unknown scenes.

---


### 940. [Memory as a cache: Exact context reuse and deletion by construction](https://arxiv.org/abs/2609.32395)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Shengyao Wang, Jiang Liu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The KV cache of a transformer entangles every token's representation with its entire prefix: a passage encoded once cannot be reused under a different prefix or removed without recomputing everything after it, so exact cache reuse is limited to shared prefixes. We present SMem, an architecture whose context representation is a cache by construction. A block-local encoder maps each block to memory rows independently of other blocks, and a reader conditions generation on their union through cross-attention. For every parameter setting, memory composes exactly at fixed block indices, deleting a block is an exact $O(b)$ update for $b$-token blocks, and the memory state is independent of the edit path. At $4\times$ the training context, under the shared recipe, SMem retrieves planted needles beyond any trained-length window (exact match 0.14-0.28 at distances of 31 and 63 blocks), where learned-position, RoPE, and Block-Attention-style transformers all score at most 0.02. A fully cached context is served by computing one block alone at a near-constant 3.1-6.2 ms, whereas cold prefill grows with context; batched decode stores 34-38% fewer KV rows and runs 1.4-1.7$\times$ faster when bandwidth-bound; and deletion beats suffix recomputation by 8.5$\times$ at 512 blocks and 452$\times$ at 4096 blocks (32-256$\times$ the trained length, probing the cost model rather than a served regime). The cost is a perplexity gap of -4.7% to +2.8% (negative favors SMem) against a parameter-matched transformer with the same positional scheme, at 160M-1.5B on FineWeb-Edu across two recipes and a learning-rate search. SMem also composes with RoPE: at 160M and 410M the composite matches or leads the matched transformer and closes 29-59% of SMem's gap to a RoPE transformer. Dropping prefix entanglement thus keeps perplexity comparable while making the cache exactly composable and editable.

---


### 941. [PULSE: Identifying Demonstration-Utility Features with Sparse Autoencoders](https://arxiv.org/abs/2609.32469)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Chenduo Hao, Chuanbao Gao, Pinjun Zeng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In-context learning is highly sensitive to demonstration choice, yet most methods select demonstrations using external query-demonstration similarity. Such criteria can miss model-specific signals: Similar demonstrations may activate different internal features and downstream behaviors. We introduce PULSE (Paired Utility Localization over Sparse Encodings), an SAE-based framework for identifying model-internal features associated with demonstration utility and using them for demonstration selection. Using a small labeled discovery set, PULSE samples candidate demonstration sets, measures their zero-shot-relative utility under the target model, and scores SAE features by how their activation differences align with utility differences. The top positive and negative coordinates form a sparse utility-localization vector. We use this vector in two complementary ways: as a signed score for controlled complete-set ranking, and as PULSE-Retriever, which converts its magnitude into a feature-relevance mask for scalable pool-scale retrieval. Across classification, generation, and reasoning benchmarks, PULSE-Retriever improves over the strongest baseline by 2-3 accuracy points, 0.6-0.9 BLEU-4, and 3.2 exact-match points, respectively, while controlled ranking validates the identified features encode a predictive set-level utility signal. Feature inspection and cross-dataset experiments suggest that the identified features capture task-relevant, dataset-conditioned patterns, yet retain utility signals that partially transfer across datasets. Our code is available at this https URL.

---


### 942. [From Outcomes to Strategies: Learning Strategy Utility for Mathematical Reasoning](https://arxiv.org/abs/2609.32482)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Ruikang Zhang, Xiao An, Xuli Shen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards has substantially improved mathematical reasoning. However, terminal correctness alone provides limited insight into the quality of high-level strategies, such as theorem selection and subgoal decomposition, when considered separately from their subsequent execution. This paper studies strategy utility, which is defined as the likelihood that a strategy supports a correct downstream solution under a given executor. We introduce SURE, a framework for learning and leveraging relative strategy utility. In this framework, high-level strategies are separated from their detailed reasoning. Based on the pairwise preferences constructed from strategy-conditioned rollouts and teacher-generated contrasts, a Strategy Reward Model is learned to estimate relative strategy utility. During reinforcement learning, the frozen reward model reads only the extracted strategy, whose score is combined with the correctness and format rewards in a sequence-level GRPO objective. Compared with outcome-and-format GRPO baselines, experiments show that SURE improves average pass@1 by 1.87%, 2.64%, and 2.93% across three policy backbones. Our method also achieves competitive or better accuracy than stronger reward baselines while requiring substantially lower GRPO-stage compute.

---


### 943. [UnStep: Training-Free Acceleration of Causal Video Diffusion with Fewer Steps Than Distillation](https://arxiv.org/abs/2609.32518)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Youssef Mansour, Enis Simsar, Fadime Sener 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Distilling bidirectional multi-step video diffusion transformers into few-step causal models has become a common approach for streaming video generation. While these few-step students are significantly faster than the teachers they are distilled from, they remain slow for real-time generation. In this work we present UnStep, a training-free wrapper that accelerates few-step causal video models at inference by running them with fewer diffusion transformer (DiT) steps than during distillation and limiting the temporal window retained in the attention KV cache. We propose two inference-only mechanisms to recover quality lost by step reduction and attention windowing: renoising the generated latent frames to a near-clean level and reusing the existing clean-cache pass to refine them, and applying truncated SVD to the DiT attention value and output projections. We also accelerate inference with a quality-preserving runtime stack for the DiT and VAE decoder, including more efficient attention calls and KV indexing, fused Triton RoPE with cached coefficients, and VAE decoding with optimized memory layout, precision, and convolution kernels. By reducing computation and optimizing the runtime stack, UnStep sets a new throughput regime for causal video diffusion, by running substantially faster than current methods, reaching 50 FPS on a single H100 without quality loss, and 77 FPS on GB200, all without retraining.

---


### 944. [Beyond Dyadic Memory: Interaction-Aware Multimodal Memory with Adaptive Agentic Retrieval for Multi-Party Spoken Conversations](https://arxiv.org/abs/2609.32522)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Wenxu Jia, Xize Cheng, Zihan Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-term memory enables agents to accumulate information and reason across sessions, yet existing research primarily focuses on dyadic text or image-text conversations, leaving long-term memory for multi-party spoken conversations underexplored. This setting requires preserving conversational content, identifying participants across sessions, and retaining who speaks to whom. To this end, we propose VoxPolyMem, an interaction-aware multimodal memory framework combining incremental speaker identification with a memory hierarchy comprising interaction memory, fact memory, and participant profiles. We formulate retrieval as sequential decision-making, where an agent rewrites queries and selects retrieval tools and memory layers based on accumulated evidence to address information gaps. We further introduce Evidence-Gain GRPO (EG-GRPO), which uses round-wise credit assignment to encourage complementary evidence acquisition. We also construct VoxPolyBench to evaluate memory evolution, personalized answering, memory retrieval and reasoning, and interaction reasoning and attribution in multi-party spoken conversations. VoxPolyMem achieves an overall score of 85.0 on VoxPolyBench, surpassing the strongest evaluated baseline by 23.6 points. On Mem-Gallery and H2HMem-Multi, it scores 89.6 and 74.4, respectively, exceeding the strongest evaluated public memory baselines by over 8 points each. These results highlight its potential for persistent, personalized assistance in multi-party multimodal interactions. Code and datasets are available at this https URL

---


### 945. [Groupwise Agentic Grading and Advantage Redistribution for Code Agent RL](https://arxiv.org/abs/2609.32577)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Jinhao Dong, Liang Zhao, Zihao Yue 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) for code agents often uses executable tests to provide binary rewards. With these rewards, Group Relative Policy Optimization (GRPO) assigns identical advantages to test-passing trajectories within each rollout group, overlooking differences in implementation quality and adherence to task requirements. This leaves the policy without a learning signal that favors clean, targeted implementations over those containing unnecessary or out-of-scope changes. We introduce GAGAR, a framework for quality-aware credit redistribution in code agent RL. Built on dynamic sampling that retains groups containing both passing and failing trajectories, GAGAR places all trajectories from each group in a shared workspace, where an SFT-trained agentic grader jointly inspects them and ranks the test-passing candidates. Based on this ranking, we downweight lower-ranked trajectories and proportionally rescale the advantages of all test-passing trajectories to restore their original sum. This sum-preserving redistribution retains the relative weights established by quality-based downweighting while shifting credit toward higher-quality implementations. We evaluate GAGAR at industrial scale using pre-RL SFT checkpoints of MiMo-V2.6-Flash (310B total parameters) and MiMo-V2.6-Pro (1.02T total parameters). Controlled code-only Flash experiments show improved code agent performance, reduced trajectory-length growth, and more stable training. We further apply GAGAR in large-scale mixed-task RL with both Flash and Pro. Our results support combining test-based verification with groupwise agentic grading to improve the quality and stability of code agent RL.

---


### 946. [Expected Reasoning-Step Return Unifies On-Policy Learning from Rewards and Teachers](https://arxiv.org/abs/2609.32674)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Qiangqiang He, Jin Li  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> On-policy reasoning models can learn from task rewards or teacher signals, but these sources differ in form and can favor conflicting updates, leaving unclear which should guide a given reasoning action. We introduce \textbf{Expected Reasoning-Step Return (ERSR)}, which treats semantic reasoning steps as macro-actions and uses Monte Carlo student-policy rollouts to estimate the expected final task reward of student-generated and teacher-proposed actions in a common return space for step-level comparison. ERSR analysis reveals an outcome-dependent asymmetry: student actions are more beneficial than teacher replacements on successful trajectories, whereas teacher replacements become more beneficial on failed trajectories. We further show that student answer-probe gains track student-step ERSR utility and distinguish beneficial from harmful reasoning steps. Based on these findings, we propose \textbf{Return-Referenced On-Policy Learning (R$^2$OPL)}, which reinforces student reasoning on successful trajectories and distills teacher signals on failed ones, while using group success rate for difficulty scaling and student-probe gains for step-level modulation. Experiments across reasoning benchmarks and teacher--student configurations show that R$^2$OPL consistently outperforms strong baselines. ERSR training dynamics further show that R$^2$OPL jointly exploits substantial utility from both reward- and teacher-side signals, whereas existing hybrids often leave substantial residual utility in one branch.

---


### 947. [SIFT: Enhancing Time Series Foundation Models via Semantic Invariance and Structural Fidelity Fine-Tuning](https://arxiv.org/abs/2609.32676)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yi Tang, Tengxue Zhang, Yang Shu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time Series Foundation Models (TSFMs) have achieved remarkable zero-shot performance through extensive pre-training on massive time series datasets. Nevertheless, due to the low-dimensional properties and diverse structural patterns of time series data, performing naive fine-tuning on TSFMs often leads to overfitting and falling into the mean-prediction trap. To address these challenges, we propose SIFT, a robust adaptation method that enhances time series foundation models by preserving Semantic Invariance and structural Fidelity throughout the fine-Tuning process. We employ semantic-invariant adversarial augmentation, which utilizes semantic spectrum decomposition to partition the semantic space and then generates perturbations within the non-core semantic subspace to bolster the model's robustness against these perturbations, mitigating overfitting. We implement a component-based structural fidelity enhancement, which facilitates component-wise mixup and imposes a reconstruction objective to improve the model's ability to preserve structural fidelity, alleviating the mean-prediction trap. Extensive experiments on representative TSFMs covering 10 real-world datasets demonstrate that SIFT can significantly enhance the performance of TSFMs.

---


### 948. [IGSD: Environment-Verified Hindsight Self-Distillation for Search Agents](https://arxiv.org/abs/2609.32694)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Angqing Jiang, Gaoming Zhang, Chaoqun Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> On-policy self-distillation densifies agent training without external teachers: a policy conditioned on privileged hindsight provides step-level guidance for its own unprivileged rollouts. For search agents, however, hindsight can make the teacher prefer a query that does not improve retrieval from the student's state. Existing methods either distill this preference directly or filter it with model-internal scores, but neither strategy verifies the query's executed retrieval consequence. We propose Information-Gain-Gated Self-Distillation (IGSD), which verifies on-policy token proposals with environment feedback before distilling them. Treating each query token as a micro-action, IGSD completes the teacher's token proposal and the student's sampled token into matched queries and executes both from the same failed state with the same retriever. Shared counterfactual controls account for query-conditioned shifts in answer likelihood, so their difference, the executed paired information gain, provides a relative utility contrast for the retrieved documents. IGSD uses this contrast as a positive-only soft weight for candidate-pair distillation, while leaving the GRPO objective unchanged and confining verification to training. Across seven single-hop and multi-hop QA benchmarks, IGSD reaches macro-average exact-match accuracies of 42.8% and 47.0% with 3B and 7B policies, respectively, without inference-time verification. These results support environment-verified hindsight as an effective approach to reliable action-level supervision for search agents.

---


### 949. [Benchmarking EEG Foundation Models at Scale: Lessons from 20,000 Evaluations](https://arxiv.org/abs/2609.32743)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Zhige Chen, Shu Peng, Chengxuan Qin 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Electroencephalography (EEG) foundation models (FMs) promise transferable neural representations, yet their advantages over strong supervised baselines and their prospects for further scaling remain unclear. To address these questions, we introduce EEG-Arena, an open-source benchmark covering 30 EEG FMs and 25 supervised baselines evaluated on 57 downstream tasks from 23 public datasets. Through more than 20,000 evaluations across five experimental protocols, we assess downstream performance, pretraining benefits, model size scaling, pretraining data scaling, and robustness to channel configuration. We find that (1) EEG FMs outperform strong task-specific supervised baselines on most evaluated tasks, particularly under non-bipolar settings; (2) compared with architecture-matched supervised training from scratch, pretraining improves both early optimization and final downstream performance, with larger and more consistent gains as more labeled downstream data become available; (3) existing EEG FMs do not exhibit a consistent positive relationship between parameter count and downstream performance; (4) under a fixed architecture, increasing the pretraining data scale yields sustained downstream gains; and (5) channel-flexible FMs achieve higher absolute performance than channel-constrained models across most evaluated channel configurations. Together, these findings demonstrate the downstream value of EEG FMs and identify pretraining data expansion as a promising direction for further progress. To support continued research, we release EEG-Arena as an open-source evaluation framework that provides shared infrastructure for reproducible benchmarking, model comparison, and community-driven development.

---


### 950. [Reuse or Relearn? A Spectral View of Earth Observation Foundation Models](https://arxiv.org/abs/2609.32756)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Mehmet Ozgur Turkoglu, Valerio Marsocci, Dominik J. Mühlematter 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Foundation models are rarely used as generic, frozen feature extractors; instead, they are fine-tuned for the target downstream application. This practice is particularly prevalent in Earth observation (EO), and it raises a question that downstream accuracy alone cannot answer: does fine-tuning reuse the pretrained representation, or does it relearn a new one? We study this with spectral diagnostics that compare a model before and after adaptation, quantifying how well its dominant singular subspaces are preserved, how broadly the weight update is distributed, and how large it is. Using natural image models such as CLIP and DINO as a reference, we find that, under the evaluated fine-tuning settings, EO models undergo far larger, higher-rank updates and retain much less of their pretrained structure, so their downstream performance is often obtained with substantial changes to the pretrained weight structure. The diagnostics further provide insight into how cheaply a model can be adapted: where the pretrained subspaces are preserved, adapting a small fraction of the parameters can match full fine-tuning, and where they are not, it can fall behind. More broadly, foundation models, and EO foundation models in particular, should be assessed not only by benchmark accuracy, but also by how reusable their pretrained representation is.

---


> [!TIP]
> 当前位于：**901-950**（第 19/20 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-700](./part-14.md) | [701-750](./part-15.md) | [751-800](./part-16.md) | [801-850](./part-17.md) | [851-900](./part-18.md) | **901-950** | [951-992](./part-20.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
