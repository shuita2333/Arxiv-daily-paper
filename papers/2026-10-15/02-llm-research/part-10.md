# 🧠 大模型相关研究 | 2026年10月15日

> 本类共 **810** 篇论文：已确认 **758** 篇，待复核 **52** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**451-500**（第 10/17 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | **451-500** | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-700](./part-14.md) | [701-750](./part-15.md) | [751-800](./part-16.md) | [801-810](./part-17.md)

---

### 451. [Rethinking LLM-Guided Visual Question Answering: Does Deeper Knowledge Integration Really Help?](https://arxiv.org/abs/2610.17079)

**<font color=#1a73e8>作者：</font>** Aneerban Saha, Vijay Kumar, Sameer Madhav D. 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Knowledge-based Visual Question Answering (VQA) requires reasoning that extends beyond visible image content, demanding external commonsense and factual knowledge. While recent work leverages Large Language Models (LLMs) as knowledge sources, the question of how deeply such guidance should be integrated into a vision language architecture remains underexplored. In this work, we generate structured reasoning guidance, visual focus concepts, distractor elements and external knowledge using Llama~3.3~70B and systematically compare two integration strategies within a unified frozen ViT + FLAN-T5 framework on the OK-VQA benchmark: decision level late fusion and attention-matrix injection. Contrary to the prevailing assumption that deeper integration is superior, we find that shallow late fusion achieves the strongest results (39.4% exact match, +10.0 over the no guidance baseline), outperforming deep attention modification (31.8%) under data scarce fine-tuning. We further contribute an LLM based augmentation pipeline that expands training data more than tenfold via question paraphrasing. Our findings indicate that integration depth must be matched to the data regime.

---


### 452. [SFT Leaves a Reproducible Signature in Activation Geometry: Calibrating Post-Training Interpretability Against Run-to-Run Noise](https://arxiv.org/abs/2610.17093)

**<font color=#1a73e8>作者：</font>** Xupeng Chen, Chenqian Le, Jiayi Cheng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A model diff credits post-training with whatever separates a base checkpoint from one post-trained descendant, presuming a rerun would land close by. On the sparse co-activation graph of Qwen3-1.7B it does not: two LoRA-SFT reruns sit over half as far apart as either sits from the base. We score each base-to-post contrast against the run-to-run band of its own recipe, and show that $k$ runs certify no better than $p=1/(k+1)$ under run exchangeability, however large the effect, so the band $z$-score is a descriptive scale. SFT leaves a large, reproducible signature: base $\to$ SFT displaces the graph by 17.8 pairwise-distance SDs beyond the mean distance between four independent LoRA-SFT runs, and the pre-registered estimator replicates on Llama-3.1-8B with Llama-Scope. At 29 steps each, four SFT and four DPO runs occupy disjoint displacement ranges, a gap $5.0\times$ and $5.6\times$ the spreads of the two arms, without any band. All bands use graphs built on one GPU architecture. Three other readings stop short of a verdict: DPO band counts (3/4, 1/4, 3/4 contrasts outside at 12, 29, 60 steps) show no consistent dose ordering while its displacement stays flat; light GRPO is a secondary non-detection, not an absence, and we run no equivalence test; and the graph concentration read as an RL signature is already in the zero-RL base. A pre-registered causal sweep at three edge budgets on 4,816 held-out prompts found the displaced sources load-bearing ($12\times$ a matched random control in mean, $3.5\times$ in median at 10,000 edges), but their stage-specificity interaction reversed at two budgets and the third failed its faithfulness gate, so we claim calibrated structural displacement, not a changed mechanism. Scope: one backbone, one SFT recipe and general-text probe states for the full protocol.

---


### 453. [Towards Universal Calibration for In-Context Classification](https://arxiv.org/abs/2610.17096)

**<font color=#1a73e8>作者：</font>** Awik Dhar, Sunita Sarawagi, Arpit Agarwal  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In-Context Learning (ICL) has received a lot of interest recently due to its ability to improve classification accuracy for new tasks without having to fine-tune the model over these tasks. However, the impact of ICL on calibration has been far less studied. Recent work has shown that ICL can have a negative impact on calibration due to biased selection of in-context examples. The existing methods for improving ICL calibration require additional task and model-specific training, detracting from the no-fine-tuning convenience of ICL. In this work, we introduce CALIBFORMER, a universal ICL calibrator for classification tasks, that generalizes to new models and tasks without further fine-tuning on these tasks. Specifically, we design a transformer-based calibrator which uses the model predictions on in-context examples to predict a confidence score for the test input. We show that the calibrator trained on three models and ten tasks, is able to generalize/calibrate ICL predictions on several new tasks and four LLMs unseen during training. Even for frontier models like Gemini, CALIBFORMER is able to obtain over 50% reduction in calibration error.

---


### 454. [When LLM Agents See a Conflict but Still Proceed: Cross-Domain Dependencies in Network Slicing](https://arxiv.org/abs/2610.17118)

**<font color=#1a73e8>作者：</font>** Marcos Lima Romero, Ricardo Suyama  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Future AI-native networks are being designed to apply autonomous agents built on large language models (LLMs) in network management through intents. When intents from different domains meet on the same resource, an agent must recognize the cross-domain dependency before taking an irreversible action. We investigate this problem through a smart-grid use case, in which a power utility holds an active intent on a backup slice for protection traffic. This slice appears idle by design, which is precisely the profile targeted by a cost-reduction intent. We built a tool-based environment in which the dependency must be either queried by the agent or read from an inventory annotation, together with a negative control, and evaluated ten models from four different providers in 600 runs. Most models acted against the dependency they had observed: seven of the ten models removed the protection slice at least once after receiving the cross-domain dependency, and in the high-harm tier the slice was removed in 76% of the exposed runs, while four models practically never did. Only one of ten models never removed the slice. We identify two failure modes, not querying the dependency and querying it but proceeding anyway, and show that agents often reported no conflict after observing it. These results indicate that, in AI-native networks, visibility of cross-domain dependencies is not a sufficient safeguard, and that dependency verification should be enforced by the management architecture before irreversible actions rather than delegated to the LLM's judgment.

---


### 455. [D2: High-Capability Full-Duplex Spoken Language Models from Half-Duplex Backbones](https://arxiv.org/abs/2610.17124)

**<font color=#1a73e8>作者：</font>** Cheng-Kuang Chang, Alexander H. Liu, Brian Kingsbury 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Full-duplex spoken language models (FD-SLMs) support simultaneous listening and speaking, but often lag behind half-duplex spoken language models (HD-SLMs) in general capabilities. We propose Dialogue-to-Duplex (D2), a framework that converts pretrained HD-SLMs into high-capability FD-SLMs at fine temporal granularity. D2 adapts the original audio encoder to streaming through decoder-free representation distillation and learns full-duplex interaction through supervised fine-tuning. We systematically study the effects of chunk size on full-duplex interaction, general capabilities, and inference computation. We apply D2 to two distinct HD-SLM architectures, Qwen3-Omni and LLaMA-Omni 2. At a 12.5Hz update rate, Qwen3-Omni-D2 achieves 99.2% turn-taking success with 521-ms latency, 99.5% interruption success, and a state-of-the-art VoiceBench score of 70.1.

---


### 456. [ToolHACE: A Dataset for Detecting Hallucinations in Tool-Based LLM Responses](https://arxiv.org/abs/2610.17125)

**<font color=#1a73e8>作者：</font>** Nikolay Ivanov, Sergey Pletenev, Elisei Rykov 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Tool-augmented language models ground their responses in external tool outputs, improving reliability beyond parametric knowledge alone. However, even when the correct tool is called and returns accurate information, models may still contradict such outputs, omit critical details, or generate unsupported claims. Existing hallucination benchmarks for tool-augmented dialogue primarily focus on the tool-calling stage, evaluating whether the correct tool and arguments are selected, while overlooking errors that arise during post-tool response generation. To address this gap, we introduce ToolHACE, a span-level benchmark for hallucination detection in tool-augmented LLM responses, covering five fine-grained hallucination categories. Through extensive experiments with modern hallucination detectors, we show that post-tool-call hallucinations are widespread and remain challenging to detect. Our results further demonstrate that effective detection requires training on specialized tool-augmented corpora, while transfer from tool-agnostic hallucination datasets performs poorly in this setting. These findings highlight the need for dedicated benchmarks and models for reliable hallucination detection in tool-augmented language systems.

---


### 457. [EvoQuantLab: Training-Free Dual-Loop Evolution for Auditable Quantitative Research](https://arxiv.org/abs/2610.17130)

**<font color=#1a73e8>作者：</font>** Haolin Yang, Zhiqiang Qian, Chutian Chen 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Automated alpha factor discovery is critical for modern quantitative research. While large language models (LLMs) have increasingly been integrated into quantitative workflows, existing agent-based approaches remain highly susceptible to severe backtest overfitting. To address this challenge, we propose EvoQuantLab, a training-free, dual-loop self-evolving framework for robust factor discovery. Instead of relying entirely on LLM generation, EvoQuantLab deploys an inner genetic-programming (GP) loop that dramatically improves token efficiency while evolving typed factor expressions under structural and diversity constraints. An outer diagnosis loop then systematically audits evidence across cycles to drive protocol-level improvements. Furthermore, our evaluation pipeline applies multi-metric validation to rigorously filter out spurious factors before deployment. Extensive out-of-sample experiments across both daily and hourly frequencies -- covering equities and cryptocurrency -- demonstrate the robustness of EvoQuantLab. Specifically, on daily CSI 500 and S&P 500 tasks, EvoQuantLab achieves leading annualized returns of 18.34% and 21.30%, consistently outperforming existing agent baselines. On high-turnover hourly cryptocurrency data, EvoQuantLab delivers a 37.91% annualized return while effectively avoiding execution collapse.

---


### 458. [OpenDGO: Benchmarking Multi-Agent Organizations Across Diverse Application Domains](https://arxiv.org/abs/2610.17143)

**<font color=#1a73e8>作者：</font>** Xunkai Li, Miao Zhang, Zekai Chen 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM)-based multi-agent systems are increasingly applied across diverse domains, yet different applications require different forms of agent organization. Existing studies typically adopt predefined organizations, such as Star, Chain, and Tree, or learn communication graphs to improve performance on specific tasks. However, these methods are largely designed and evaluated within a limited set of application domains, providing little understanding of whether an organization effective in one domain remains suitable for others with different collaboration requirements. We present \textbf{OpenDGO}, a controlled benchmark and analysis framework covering six real-world domains and three collaboration settings: Sequential Dependency, Parallel Decomposition, and Information Integration. Under matched tasks, agents, tools, and resource limits, OpenDGO compares fixed and learned organizations while separately examining communication graphs, role assignments, input assignments, resource budgets, and component failures. Our results show that there is no ``one-organization-for-all'' solution: preferred organizations vary across applications, and even the same communication graph can yield different outcomes under different role and input assignments. These findings highlight the need for application-dependent organization design, aiming to understand \emph{which organization is suitable for a given application, under what conditions, and why}.

---


### 459. [The Format is the Filter: Scoring Format Fixes What an LLM Judge Can Express](https://arxiv.org/abs/2610.17158)

**<font color=#1a73e8>作者：</font>** Lovedeep Gondara, Jekaterina Novikova, Sagarika Suresh 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> When an LLM judge filters instruction-tuning data, its scoring format (binary verdict, 1--5 rating, 0--100 score, or comparison) is rarely justified or ablated. Holding the candidate pool, judge prompt, decoding and selection budget fixed, we score 15,406 UltraFeedback candidates under five formats with three judges, curate, fine-tune 66 models, and evaluate them with four judges. A 0--100 scale is worth only 7--12 equally used levels, two to three times a 1--5 scale rather than twenty, and a binary verdict leaves the top score tied in 77--78\% of prompts, so most selections are made at random. These properties are set by the format almost independently of the judge. Kendall's $\tau_b$ hides them: it ranks binary best while $\tau_a$ and top-1 agreement rank it last, because it discounts the ties a selector must break at random. Both comparative formats inherit a slot bias whose sign differs across judges. Downstream, curated data beat random selection under every evaluation judge, robust to length and markdown adjustment, but no ordering among formats is detectable. We propose four quantities that judge-based curation pipelines should report.

---


### 460. [Learning Perceptual Geometry of Natural Odor Mixtures from LLM-Derived Descriptors](https://arxiv.org/abs/2610.17164)

**<font color=#1a73e8>作者：</font>** Farhad Pashakhanloo, Venkatesh N. Murthy  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The relationship between odor chemistry and perception remains incompletely understood. Many existing studies focus on the perception of single molecules, whereas natural odors contain tens to hundreds of components, adding extra layer of complexity to percept formation. Here, we explore the relationship between molecular composition and perceived similarity in natural odor objects. We study this using a database of more than 1,200 volatile-compound-in-food mixtures containing more than 8,000 molecular components, and use large language models (LLMs) as a scalable surrogate for deriving mixture-level perceptual descriptions. We find that language-derived representations provide useful supervision for predicting held-out mixture similarities from molecular composition. The prediction was consistently strongest when perceptual targets were derived from chemosensory prompts than from other sensory prompts. Further, during the mixture-level training, we learned low-rank molecular embeddings that enabled better prediction of held-out mixture similarities than component-overlap metrics, even for mixture pairs with no shared molecules. Although no single-molecule labels were used during training, the learned molecular geometry showed significant alignment with the independent human odor-descriptor space. Finally, we explored the use of external molecular features in our mixture-similarity prediction task. These features showed modest zero-shot alignment with mixture-level perceptual similarity. They improved prediction under limited supervision but offered little additional predictive benefit with the full training set. Together, these results show that language-derived descriptions can provide scalable supervision for predicting the perceptual organization of complex natural mixtures, contributing to a quantitative understanding of how molecular composition gives rise to odor perception.

---


### 461. [FunDM: Cheap & Label-Free Decision Models from Frozen Language Models](https://arxiv.org/abs/2610.17175)

**<font color=#1a73e8>作者：</font>** Ujjawal K. Panchal  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Decision models such as Jev score candidate answers or actions. A small decision head trained label-free can recover about 99% of a frozen language model's multiple-choice accuracy while using only two-thirds of its transformer layers. It learns the full model's answer probabilities with KL divergence, without correct-answer labels for training. One backbone pass reads the question and all options together; the head returns probabilities for every option. We call this model FunDM (Fun Decision Model). Using 24 of Qwen3-8B's 36 layers and skipping the LM head, its +1T variant reaches 75.0% mean accuracy over eight benchmarks, versus 75.7% for the full model. On MMLU-Pro, both heads achieve 1.56 to 1.57 times batched vLLM throughput with about one-third lower peak GPU allocator memory. Both heads score higher than released Contrastive Language Models (CLM), fine-tuned CLM, and CLM-shaped heads trained from scratch on the eight multiple-choice benchmarks and coding-agent selection. Separately trained agent heads learn judge probabilities without pass/fail labels and select passing runs for 74.4 to 74.6 of 100 held-out tasks on average, versus 74 for the full-model judge and 52.0 for a CLM-shaped action-trained head. Code is available at: this https URL

---


### 462. [ChemExplain: A Multimodal Benchmark for Explanatory Chemical Reasoning](https://arxiv.org/abs/2610.17183)

**<font color=#1a73e8>作者：</font>** Aotian Chen, Frazier N. Baker, Reza Averly 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Current chemistry benchmarks primarily evaluate outcome prediction or reaction pathway generation, but rarely test whether a model can explain why an observed chemical effect occurs. We introduce ChemExplain, a benchmark of 1,180 multiple-choice chemistry questions drawn from 383 peer-reviewed papers. Each question pairs a molecular or reaction image with an observed chemical effect and four candidate explanations, each associated with a different structural feature visible in the image. Answering requires the model to perceive the depicted structure, apply chemical knowledge, and identify which feature most directly explains the effect, a capability we term explanatory attribution. The correct feature-mechanism relation is derived from supporting evidence in the source paper rather than invented by the question-generation LLM. We construct the benchmark automatically with a multi-agent framework that applies progressive quality control at three stages and validate it with eight chemistry domain experts. The strongest evaluated model reaches 78.6% accuracy, leaving considerable room for improvement. On a 600-question expert-reviewed subset, reasoning-trace analysis classifies 71.4% of the strongest model's errors as attribution failures. Attribution is also the largest error category for the open-source and chemistry-specific models included in our analysis.

---


### 463. [DuoDiscover: Scaling Autonomous Discovery Beyond the Evaluation Bottleneck](https://arxiv.org/abs/2610.17184)

**<font color=#1a73e8>作者：</font>** Shubham Agarwal, Akshat Gupta, Mike Heddes 等 24 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Evaluation has been central to advances in AI, and it is equally critical to autonomous discovery. Yet scaling autonomous discovery to real-world engineering challenges faces a fundamental bottleneck: the cost of evaluating progress. In real settings, a single true evaluation, such as a full benchmark or serving trace, can take hours, so a search can afford only a handful of true evaluations. We present DuoDiscover, a search system that jointly discovers what to optimize and how to evaluate progress efficiently, through three mechanisms. First, each worker in a fleet of coding agents co-discovers an optimization target and a fast, tailored proxy evaluator, which we call a yardstick. The agent then hill-climbs the yardstick rather than the true evaluation. Second, since search can exploit gaps between a yardstick and the true objective, fidelity tests continually recheck each yardstick's ranking and invalidate any that drift. Third, the fleet is bottom-up, with no central decomposition of the problem. A lightweight orchestrator spawns and terminates agents, briefs running ones, and seeds new agents with others' confirmed work. DuoDiscover enables autonomous optimization from software to chip architecture. We demonstrate DuoDiscover on two repository-level benchmarks and four GPU and TPU kernel suites covering hundreds of kernels. On SWE-fficiency, it doubles the average speedup of human experts. On SOL-Exec, it ranks first on 121 of 235 kernels and in the top three on 212. On the heavily optimized vLLM and SQLite engines, DuoDiscover achieves 1.92$\times$ and 1.38$\times$ gains over the base code. On a CPU microarchitecture optimization task with evaluations of up to 28 hours, DuoDiscover surpasses both AlphaEvolve-based ArchAgent v2 and the best human design, with 1.65$\times$ ArchAgent v2's gain in 16.7 days versus more than 40 days, advancing the frontier of autonomous chip design.

---


### 464. [Soft Teacher Forcing](https://arxiv.org/abs/2610.17189)

**<font color=#1a73e8>作者：</font>** Mohammad Fahes, Cordelia Schmid, Anurag Arnab  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Soft tokens have so far been used to replace discrete chain-of-thought in latent reasoning methods. These approaches typically require multi-stage training and, in some cases, auxiliary modules, yet they still underperform supervised fine-tuning (SFT) on <input, chain-of-thought, output> triples. In this paper, we ask whether soft tokens can be used to improve SFT itself, instead of as an avenue for latent reasoning. We introduce Soft Teacher Forcing (Soft-TF), a simple training algorithm that combines teacher-forced embeddings with soft tokens through random convex combinations. The soft tokens are computed in a single parallel forward pass over the ground-truth sequence. Soft-TF adds no parameters, no external model and no curriculum, and leaves inference unchanged. Experiments show that Soft-TF improves over SFT on GSM8K, MATH, MathQA and AQuA, by +2.1 to +4.1 points on GSM8K across seven Gemma, Llama and Mistral models.

---


### 465. [MLAfication: Efficiently Enabling High-Fidelity MLA for Modern LLMs](https://arxiv.org/abs/2610.17202)

**<font color=#1a73e8>作者：</font>** Zile Wang, Zhide Xie, Tao Ji  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-Head Latent Attention (MLA) compresses the KV cache into a latent representation, reducing inference memory and bandwidth. Existing MHA2MLA/TransMLA methods do not support QKNorm and require costly recovery on modern LLMs, especially MoE. We present MLAfication, a QKNorm-compatible, parameter-efficient extension of MHA2MLA. It combines calibrated KNorm, parameter-efficient distillation, contribution-aware Partial-RoPE, and activation-aware joint KV initialization. Across MHA and GQA models, including QKNorm- and MoE-equipped variants, MLAfication preserves performance under substantial KV-cache compression, surpasses the current SOTA on commonsense and long-context benchmarks, and extends MLA conversion to modern architectures. On Qwen3-30B-A3B, MLAfication delivers up to $5.35\times$ the serving throughput of BF16 GQA and, combined with 4-bit KV quantization, reduces the KV-cache footprint by $94.73\%$. Our code is available at this https URL.

---


### 466. [Online LLM Personalization from Pairwise Preferences Across Users](https://arxiv.org/abs/2610.17203)

**<font color=#1a73e8>作者：</font>** Romain Puech, Georgy Salakhutdinov, Dimitris Bertsimas  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models can answer the same question in different styles, but users' preferred styles are hidden and vary across users and questions. We study inference-time personalization through online selection from a fixed set of prompts, each representing a persona. Users arrive sequentially, each asks a short sequence of questions, and the system displays two responses per question and observes one pairwise choice. We formulate this interaction as a variant of the contextual dueling bandit problem in which the learner starts without preference data, adapts within each session, and exploits information shared across users. The objective is to minimize cumulative strong regret, summing the utility gaps of both displayed responses relative to the user's best response among the available options. We make two contributions. First, we introduce the problem and release a reproducible preference benchmark and dataset built around a tutoring case study, containing educational questions, LLM-generated answers in six teaching styles, and pairwise judgments from LLM-simulated students with hidden preference profiles. We fit Bradley-Terry models to these judgments to obtain reference utilities for regret evaluation. Second, we propose a baseline that learns a mixture prior over users from completed sessions and adapts to each new user within the session. On students and topics never used in development, it removes 44-48% of random pairs' excess regret and achieves over half the performance of a per-user linear oracle fitted in hindsight. We release code, prompts, and the benchmark.

---


### 467. [Releasing the Inner Jev: A Simple Recipe for Open Decision Models](https://arxiv.org/abs/2610.17205)

**<font color=#1a73e8>作者：</font>** Jonathan Geuter, Andrew Cheng, David Alvarez-Melis  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-based decision-making systems, also called System One models, have recently gained popularity, most notably through Jev (Almeida, 2026). Given a typed input state, a question, and a set of options, they return a probability for each option in a single forward pass, without text generation. We show that existing open instruction-tuned language models can achieve comparable performance \textit{without any additional training}, by reading out answers from letters (A, B, C, etc.) in the model's output logits at the last token position. Furthermore, we show how a simple supervised fine-tuning recipe can improve their performance further. We evaluate four open instruction-tuned language models: Gemma 4 31B, Gemma 4 12B, Qwen3.6-27B, and Qwen3.5-4B. We fine-tune each using LoRA and a decision head initialized from a slice of the language model head. Furthermore, we introduce OpenDecisions, a novel 2,352-question validation dataset designed to reflect the task composition of JevBench (JevBench main- tainers, 2026) and which computes a Capability score based on accuracy and calibration metrics. Without fine-tuning, Gemma 4 31B scores 79.6 on OpenDecisions, compared to Jev's 80.1. After undergoing our fine-tuning recipe, it scores 84.4 on OpenDecisions and 81.5 on JevBench v1.7, outperforming Jev by 4.3 and 4.4 Capability points respectively and setting a new state-of-the-art on OpenDecisions. On a suite of public decision datasets, our models achieve accuracy comparable to Jev, with lower calibration error. Our results show that open language models already possess System One capabilities, and with simple fine-tuning they outperform Jev on a wide range of decision tasks. We release our models, serving code, and OpenDecisions.

---


### 468. [AutoMARS: Automatic and Scalable Multi-Agent Large Language Model Framework for Supply Chain Risk Assessment](https://arxiv.org/abs/2610.17206)

**<font color=#1a73e8>作者：</font>** Yinzhu Quan, Zefang Liu, Frederick Benaben 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We propose AutoMARS (Automatic Multi-Agent Risk Assessment), an agentic framework for automatic and scalable comparative risk assessment in supply chain networks. The framework enables end-to-end execution of analytical workflows by automatically planning tasks, coordinating specialized agents, invoking external analytical tools, and synthesizing domain-specific results into integrated risk evaluations. AutoMARS further supports scalable risk comparison across multiple locations by parallelizing independent analytical tasks. The framework adopts a multi-domain, multi-agent, and multi-tool architecture that integrates heterogeneous risk factors from socioeconomic, disaster, environmental, and transportation domains. Through coordinated agent interactions and tool integration, AutoMARS enables structured, systematic, and interpretable comparative analysis to support supply chain risk-aware location evaluation.

---


### 469. [Density-Matrix Reinforcement Learning](https://arxiv.org/abs/2610.17214)

**<font color=#1a73e8>作者：</font>** Chiuman Ho  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> What information does a reinforcement learning policy omit? At each state, a standard policy stores one probability per action. It has no place to record how actions relate to each other, such as which pairs go together and which conflict. We ask when this missing structure matters, and we give exact answers. We store the policy at each state as a density matrix, a positive semidefinite, unit-trace matrix borrowed from quantum information theory. We use it here as a purely classical data structure, computed on ordinary classical hardware. The diagonal holds the usual action probabilities. The off-diagonal entries, called coherences, are new parameters. This gives density-matrix reinforcement learning (DMRL). Coherences change outcomes in two settings. First, suppose a policy is regularized toward a coherent reference policy using matrix relative entropy. The optimum then has coherences that no diagonal reference policy produces, and its action probabilities can depend on the reference policy's coherences. This is relevant to fine-tuning of large language models (LLMs) with a Kullback--Leibler penalty. Second, suppose the agent chooses a unit-vector action and the reward is a quadratic function of that vector. This could arise when an LLM judge scores a weighted consolidation of reasoning paths, or when coupled robotic sensors each respond to a mix of actions. Then some coherent policies earn strictly more expected reward than every classical policy with the same action probabilities, and we give the margin in closed form. In a two-action example, both policies assign probability $0.5$ to each action, yet the classical one earns expected reward $0$ while the coherent one earns $1$, the maximum. Outside these two settings, DMRL matches or transfers the classical results. This is a theory paper. All results are proved, and we report no empirical evaluation.

---


### 470. [When Left Is Right? Camera-Motion Understanding beyond Screen](https://arxiv.org/abs/2610.17242)

**<font color=#1a73e8>作者：</font>** Chong Cheng, Ran Zhang, Xinyuan Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Can a vision-language model tell left from right? Modern VLMs solve visual puzzles and follow hour-long videos, yet when asked whether the camera moved left or right, most do no better than a coin flip. Adding camera-motion data or geometric representations has been tried, separately, and neither closes the gap. We argue that camera-motion understanding needs two conditions at once: the representation must couple off-screen camera motion with on-screen flow dynamics, and it must be interpreted by the language model rather than trained as a standalone pose or depth estimator. We propose CameraVLM, which pairs a motion-state representation with state-language alignment. Camera tokens capture how the camera moves off screen, flow tokens capture how the subject and background move on screen, and a two-stage training strategy keeps language in the loop so that both are learned together with camera-motion semantics. With only 9B parameters, CameraVLM outperforms all open-source and camera-motion-specific models by a wide margin across three benchmarks and more than 20 baselines, and matches or surpasses GPT-6 Astra as well as human viewers in a 48-participant study. Project page: this https URL

---


### 471. [From Conceptual EneMonIE to an Executable Backend: A Modular Architecture for Energy Information Extractionand Grounded Question Answering](https://arxiv.org/abs/2610.17243)

**<font color=#1a73e8>作者：</font>** Janik Lesage, Khadim Lô, and Jean-Sébastien Dessureault  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The original EneMonIE proposal describes a Web-based semantic system for continuously monitoring energy trends through targeted information extraction from heterogeneous online media. This article presents EneMonIE-Backend, an implementation-derived redesign that converts that conceptual pipeline into a modular, executable, and application-independent backend. The architecture separates five concerns: data sources, acquisition and normalization, semantic processing, knowledge organization, and persistent storage. It operationalizes configurable connectors for RSS feeds, URL collections, arXiv, social-media JSON files, and open-data CSV files; it also introduces question-driven Web search and scraping. Relevant documents pass through energy categorization, named entity recognition, temporal and event extraction, source sensitive sentiment analysis, and extractive summarization. The resulting semantic representations support entity co-occurrence graphs, cross-document interlinking, cluster-level information fusion, and relational persistence in SQLite. Three grounded question-answering paths are exposed at the backend level: live Web evidence, the stored corpus, and selected configured resources. Answer generation uses a language model when configured and otherwise falls back to deterministic extractive output. Unlike the original proposal, the presented architecture deliberately excludes the user-interface and server-side application layers, allowing the semantic core to be embedded in different applications. A deterministic smoke validation confirms relevance filtering, persistence, clustering, evidence retrieval, and document deletion. The work provides a reproducible architectural basis for future evaluation on larger multilingual energy corpora.

---


### 472. [LLM-to-Flow Distillation: Teaching Natural Language Goals to Scientific Generators](https://arxiv.org/abs/2610.17246)

**<font color=#1a73e8>作者：</font>** Riccardo De Santi, Federico Di Gennaro, Angelo Gnazzo 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generative discovery in science requires coupling high-level scientific reasoning with the ability to generate samples respecting the structure of a design space. Yet these capabilities remain largely separated: foundation LLMs encode broad chemical and biological knowledge, while domain-specific flow- and diffusion-based generators capture the priors needed to produce valid sequences and geometries. We study how to align such scientific generators to high-level natural-language discovery goals without requiring an explicit proxy reward, which is often unavailable or poorly captured by learned predictors in experimental sciences. We introduce LLM-to-Flow Distillation (LFD), where a frozen LLM acts as an adaptive teacher for a domain-specific generator. Given a goal such as 'generate peptides with promising anticancer activity', the teacher constructs a curriculum of intermediate sub-goals aware of the flow's current capabilities, and progressively directs them toward the original discovery goal. At each round, the LLM judges sampled candidates under the current objective. These judgments induce preferences that are iteratively distilled into the generator through DPO. This procedure provides dense learning signals even when the initial model places negligible probability on designs satisfying the final goal, enabling adaptation toward poorly covered, out-of-distribution regions. Experiments on therapeutic peptides and small-molecule structure design demonstrate that LFD enables a new form of generative control: aligning arbitrary domain-specific scientific generators to scientific discovery tasks expressed via high-level natural-language goals.

---


### 473. [Does a Governed Confidence Score Know When a Text-to-SQL Answer Is Right? An Exploratory Study on BIRD and a Pre-registered Confirmation on Spider](https://arxiv.org/abs/2610.17256)

**<font color=#1a73e8>作者：</font>** Raghu Venkat, Tricha Anjali  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Conversational analytics lets people ask questions of records spread across many systems and get answers in plain language; it is useful only if each answer can be trusted and explained. A production system of this kind attaches a confidence score to every answer it writes over a database and uses it to show the answer, show it with a warning, or withhold it. The score's weights, caps and thresholds were set by design. This paper audits that design. On the 1,534 questions of BIRD dev, answered by GPT-5.1 with a benchmark-adapted production prompt and five samples per question, the designed score separates right from wrong answers weakly (AUROC 0.624, 95% CI 0.595-0.652) and withholds 35.7% of correct answers. Nearly all of its ranking signal comes from agreement among the samples, and most of it is lost where agreement is combined by a minimum with a checklist that drops to zero on any unsupported claim, including claims in commentary. We froze a rule in which agreement with the shown answer is the score and deterministic checks act as vetoes and caps, and pre-registered a test on Spider dev before any Spider answer existed. The primary hypothesis held: AUROC rose from 0.566 to 0.725 (paired difference +0.159, 95% CI +0.097 to +0.221), and correct answers withheld fell from 49.0% to 8.8% with PASS accuracy 95.7%. Under one matching policy the choice of agreement statistic matters little; the gain comes from how agreement enters the score. Whether added checks help depends on how correctness is defined, while they always cost unqualified coverage. A pre-registered empty-result check did not meet its effect-size criterion on Spider. Correctness here means the core answer; labels are model-judged, and a blinded two-person audit, not yet complete, will be reported in a revised version.

---


### 474. [RL Post-Training Diffusion Language Models Along Their Own Generation Paths](https://arxiv.org/abs/2610.17266)

**<font color=#1a73e8>作者：</font>** Vaibhav Singh, Eugene Belilovsky  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Diffusion language models are a promising and more efficient alternative to autoregressive models. However, most RL post-training techniques are not easily adapted to these models. One issue is that diffusion language models generate answers through many intermediate states, deciding at each step which masked positions to reveal and which tokens to place in them. Many existing RL methods used in this setting approximate intractable sequence likelihoods or weight every denoising step by the same advantage, without explicitly distinguishing how these intermediate states of the denoising trajectory affect the expected reward. To address this issue of trajectory blindness, we introduce PACT (Potential-Anchored Consistency of Transitions). Motivated by a reward-tilted reference distribution, PACT jointly learns the policy and a scalar potential that scores each intermediate state, anchored by terminal reward. For each sampled denoising transition, a consistency loss matches the policy-to-reference log-probability ratio of revealed tokens to the change in this potential. This formulation requires neither sequence-likelihood estimation nor importance-ratio clipping. On four tasks, PACT improves LLaDA-8B-Instruct by +9.9 points on GSM8K, +12.0 on MATH500, +55.7 on Countdown, and +72.6 on Sudoku, and reaches the best average accuracy across the four tasks reported for this model, +3.7 points over the next best method. Further compared to AGRPO, it reaches that baseline's best accuracy in about half the training compute on GSM8K.

---


### 475. [The Surprising Expressivity of a Single Neuron with Autoregressive Chain-of-Thought](https://arxiv.org/abs/2610.17283)

**<font color=#1a73e8>作者：</font>** Roey Magen, Nirmit Joshi, Gal Vardi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The success of autoregressive language models trained with Chain-of-Thought~(CoT) supervision raises a fundamental question: How simple can a next-token predictor be while still enabling the efficient simulation of general computation through its autoregressively generated CoT? Surprisingly, we show that a single neuron suffices. For a broad family of activations, including threshold and ReLU, a single autoregressive neuron can simulate any feedforward circuit with the same activation. Specifically, a size-$s$ circuit on $n$ inputs can be simulated by a neuron of dimension $O(ns+s^2)$ using $O(s^2)$ generation steps, with both bounds independent of circuit depth and tight under natural assumptions. For threshold activations, this improves upon the simulation of Joshi et al. (COLT 2025), whose bounds scale exponentially with circuit depth. Consequently, autoregressive threshold neurons can simulate polynomial-time Turing machines, while remaining efficiently learnable from CoT supervision. Our main expressivity result relies on a novel connection to Sidon sets from additive combinatorics. As an experimental illustration, we efficiently train a single autoregressive ReLU neuron to mimic a neural network teacher with nontrivial test accuracy on CIFAR-10.

---


### 476. [Which Geometry on Which Layer? Measured Sign-Spectral Assignment in Mixed-Optimizer Training](https://arxiv.org/abs/2610.17285)

**<font color=#1a73e8>作者：</font>** Hiroki Naganuma, Laura Gomezjurado, Mahdi Ghaznavi 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern neural-network training uses mixed recipes, assigning AdamW-like or sign-based updates to embedding and output layers and spectral updates to hidden matrices. These assignments are usually fixed by layer type, without a clear criterion for selecting the appropriate geometry. We turn sign-versus-spectral assignment into a measurable, layerwise decision problem. For ideal memoryless steps, we derive a finite-batch ratio of conservative descent-lemma lower bounds for spectral and sign updates. Its closed form separates signal efficiency from a geometry-dependent global curvature factor. In the positive-signal regime, the same smoothness assumption gives two-sided bounds that determine which step has the larger conditional expected decrease when the ratio crosses explicit noise-dependent thresholds. We then derive a local directional quadratic score from gradient alignments and Hessian-vector products and use it in Generalized-Scion (G-Scion) to control layerwise routing. In a controlled input-rank experiment, including directional curvature matches the measured same-iterate ordering in all seven aggregate settings, whereas the curvature-free proxy selects the opposite geometry. On 31M GPT-2, the output score routes the output layer from spectral warmup to sign, and G-Scion improves validation loss over fixed Scion in memoryless and matched-momentum comparisons. ViT-B/16 results further show that a spectral edge assignment can outperform fixed Scion outside language modelling. These results suggest that optimizer geometry need not be hard-coded by layer type and are a first step toward understanding how it should be assigned.

---


### 477. [PhysCodeGym: Benchmarking Coding Agents for Physically Verifiable 4D Reconstruction](https://arxiv.org/abs/2610.17288)

**<font color=#1a73e8>作者：</font>** Shuai Shao, Jinchen He, Cunxin Fan 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Building physical simulations from video requires coding agents to translate observations into executable models and refine them through tool use. We introduce PhysCodeGym, a benchmark for physically verifiable 4D reconstruction with $156$ tasks covering rigid-body, liquid, deformable, and wind-driven motion. Agents autonomously inspect videos, write and run Blender programs, and revise their scenes using simulation feedback. Six metrics combine rule-based measurements with rubric-based judgments to assess visual and physical reconstruction quality. Program inspection, scene measurements, and counterfactual interventions test physical consistency under original and modified conditions. Experiments with frontier coding agents reveal a tradeoff between artifact quality and completion across reasoning-effort settings, while harness comparisons and agent traces link verification behavior with reconstruction performance. Case studies show that matching visible objects and events can coexist with physical defects. Counterfactual tests further expose latent contact and support failures in reconstructions that pass ordinary physical checks, highlighting the gap between reproducing observations and building reliable physical models. Code is available at this https URL.

---


### 478. [The Agent Knew: Internal States Forecast Unauthorized Actions and Stop Them, and the Lies That Follow](https://arxiv.org/abs/2610.17301)

**<font color=#1a73e8>作者：</font>** Arya Fayyazi, Mehdi Kamal, Massoud Pedram  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Language-model agents sometimes act beyond their authorization and then misreport what they did. On CAPE-Bench, matched agent tasks in which one fact decides whether an action is authorized, frontier open-weight agents do both, and one behavior marks the lie: retroactive permission laundering, acting and then asking permission as if the action were pending, precedes a false report in 70% of 1081 fresh informed violations, against 8% otherwise (preregistered odds ratio 7.0); frontier agents on tau^2-bench instead fabricate the authorization before violating. A linear readout of the agent's residual stream forecasts the violation before the action (AUROC 0.94) and the false report before the report, and beats chain-of-thought monitors when the agent is pressured to hide its reasoning. Gating every proposed action on this forecast cuts violations over whole episodes in four model families, and sending repeated flags to an approver keeps authorized work (Gemma-4: violations 0.70 -> 0.09, completion 1.00; a model approver that escalates unclear cases keeps this gain with a person seeing 25% of asks), at about 10-8 of the agent's compute and 109 times less than a chain-of-thought monitor. On AgentDojo, an external prompt-injection benchmark, the same readout calibrated on 29 tasks, with the steering unchanged, cuts attack success on unseen tasks in two families (Gemma-4 11.7% -> 5.7%, gpt-oss 28.5% -> 17.5%) while keeping benign utility (Gemma-4 0.637 vs 0.637; gpt-oss 0.667 vs 0.681). Preventing the violation is also the most reliable way to prevent the lie (misreported violations 0.10 -> 0.01 pooled over three families, preregistered), whereas lie-specific fixes after a violation are weak. All tests are preregistered and hash-locked; code, data and the full record, including tests that did not pass, are at this https URL.

---


### 479. [Reliable Text-to-SQL in Resource-Constrained Settings with Small LLMs via Iterative Retry Workflows](https://arxiv.org/abs/2610.17305)

**<font color=#1a73e8>作者：</font>** Bilel Abderrahmane Benziane, Xavier Schepler  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have recently improved Text-to-SQL generation, but their computational cost can hinder deployment in resource-constrained settings. This paper evaluates the Text-to-SQL capabilities of small and medium open-source LLMs (1B-8B parameters) under a controlled inference budget, focusing on how model specialization and prompt formulation affect performance. Using the Spider benchmark, we compare multiple prompt representations and assess the accuracy of generated queries. Our results show that SQL-specialized models are consistently more reliable than general-purpose and chat-oriented models at small scales, and that performance can vary substantially depending on the prompt used. To reduce this variability without resorting to larger models, we introduce three lightweight inference workflows that automatically retry with alternative prompts and/or models when failures occur, including an optional syntax-correction step. These workflows significantly improve end-to-end success rates, with a trade-off in additional inference calls. These results demonstrate a practical path to stronger Text-to-SQL performance with small LLMs, by trading modest additional inference cost for higher reliability.

---


### 480. [Calibrating LLM Explanations to Human Decisions with Reinforcement Learning](https://arxiv.org/abs/2610.17306)

**<font color=#1a73e8>作者：</font>** Dong Shu, Ziyang Guo, Negar Kamali 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Explanations of LLM outputs are considered an important way to make model behavior legible, helping human users make good decisions on downstream tasks. However, default training approaches for improving explanations target model task performance or human preference rather than human decision quality. To bridge this gap, we introduce \textbf{HD-RL}, a reinforcement learning framework for optimizing LLM explanations for human decision making. Our approach calibrates a human decision simulator on observed human decisions, applying a proxy reward model to optimize the LLM to generate explanations that help people to make good decisions. We apply this framework to AI-generated text detection. In our initial data collection phase, we observed that while LLMs possess strong autonomous detection capabilities, the explanations they generate for users yield near-random human accuracy (51.3\%). By applying the HD-RL framework to the open-source Qwen 3.6 model, we generate optimized explanations that improve human performance, achieving a GLMM-estimated human accuracy of 63.7\% in a randomized between-subjects experiment with repeated measures and outperforming RLVR, RLAIF, and other baselines by over 8\%.

---


### 481. [Beyond Successful Play: Diagnosing Opponent Modeling in Large Language Models](https://arxiv.org/abs/2610.17310)

**<font color=#1a73e8>作者：</font>** Hanbo Xie, Yue Zhao, Robert C. Wilson  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Language-model agents are expected to adapt to others whose behavior changes through interaction. Yet adaptation may rely on learned behavioral patterns rather than theory of mind (ToM): the ability to infer others' mental states, including beliefs and intentions. We introduce a benchmark and diagnostic framework for repeated hide-and-seek against algorithmic opponents with explicitly defined recursive belief updates. Their ground-truth beliefs and action probabilities let us distinguish adaptive play, action prediction, and belief tracking through live interaction, fixed-history evaluation, and controlled information interventions. With structured elicitation and behavioral supervised fine-tuning (SFT), we find improved play in several tested settings, but diagnostics reveal limitations in opponent prediction and belief tracking. We test whether supervising opponent action probabilities can address this predictive deficit in Qwen2.5-7B-Instruct. Predictions improve when the model is told the opponent's type and parameter settings, but become less accurate when it must infer the opponent from history without this information. Training on examples that also omit these details reduces the gap, although improvements vary across opponents. Is this limitation specific to smaller open-weight models, or does it also appear in a frontier model? GPT-5.4 also benefits from correct opponent beliefs: supplying them improves its predictions and choices, whereas deeper explicit belief reports and self-generated memory do not consistently improve forecasting from interaction history. This contrast suggests that using useful belief information is easier than inferring it autonomously, even for a frontier model. Together, our findings distinguish improved play and action prediction from reliable belief tracking, providing a framework for evaluating mentalizing and testing targeted improvements.

---


### 482. [From Sampled Evidence to Radiology Reports: Objectives, Constraints, and Realization](https://arxiv.org/abs/2610.17318)

**<font color=#1a73e8>作者：</font>** Kun Zhao, Haoteng Tang, Chenghua Lin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Sampling multiple reports creates an inference problem: how should sampled evidence be converted into a final decision, and does a better structured decision yield a better report? We study these questions through a framework that separates the decision signal, scoring objective, and feasible decision set, followed by text realization. On MIMIC-CXR and IU-Xray, controlled comparisons across 13 generator configurations per benchmark under grouped development/test evaluation reveal three findings. First, changing the objective under fixed evidence and rule capacity changes predictions and their held-out metric trade-offs. Second, relaxing candidate constraints has objective-dependent effects under shared signals and frozen scores. Diagnostics connect the IU macro-oriented assertion increase to near-zero label thresholds and show that limited candidate coverage coexists with selection headroom. Third, a controlled realization study with SFT-Qwen3-VL-8B shows that decision-level gains can be attenuated, amplified, or reversed. Change decomposition reveals that realization can remove incorrect assertions while losing correct findings, so target fidelity and reference accuracy need not improve together. Finding gains also do not consistently improve reference-based report quality. These results motivate separate evaluation of decision rules, candidate constraints, and realized reports.

---


### 483. [The Curse of Knowledge in Role-Playing Language Models](https://arxiv.org/abs/2610.17327)

**<font color=#1a73e8>作者：</font>** Xiao Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Role-playing language models speak as characters in games and agent simulations, where the system records what each character can hear, see and understand. We test whether characters respect these boundaries in 480 scenes, each with a counterfactual twin that changes only the hidden fact, so mentions of the twin's fact measure guessing. Across 11 open-weight models, characters use content from speech they cannot understand or hear at 67 and 72 percentage points (pp) above this baseline, although most models correctly state what the character perceives. This is a curse of knowledge. The leak extends to hidden actions and private messages and changes where characters search. Five of six proprietary models rarely leak, but compliance in strong models depends on input format. Changing only the scene layout or character description raises the rate in two otherwise compliant open-weight models from under 10 to over 60 pp, and combined changes raise two proprietary models from near zero to 13 and 21~pp. Writing the line as the scene's author leaks nearly as much as role-play, and thinking rarely helps. Giving models only what the character observes stops the leak without hiding what it may report.

---


### 484. [Do Theorem Provers Need Theorem-Proving Agents? mini-Lean-agent: A Coding-Agent Baseline for Lean](https://arxiv.org/abs/2610.17331)

**<font color=#1a73e8>作者：</font>** Tomas Ortega, Simon Park, Ayush Khaitan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> General-purpose coding agents use standard shell and file interactions, yet formal theorem-proving agents often rely on specialized, ad-hoc tooling. This makes it difficult to determine which components of theorem-proving agents provide benchmark gains: an improved base model, a specialized harness, a specific tool, or a combination of any of them. We introduce mini-Lean-agent, a deliberately minimal agent for Lean tasks whose only model-visible tool is bash. The model must use bash to inspect and edit the repository, search local libraries, invoke Lean, and manage its own intermediate work, while a separate trusted evaluator verifies the final artifact. We compare mini-Lean-agent against AxProverBase and Numina-Lean-Agent on the Putnam 2025 benchmark. Experiments with Gemini 3.8 Flash as the base model show that mini-Lean-agent solves 7/12 problems at \$2 per problem limit, compared with AxProverBase's 4/12. With Astra as the base model, mini-Lean-agent solves 12/12 problems at an average cost of \$1.28 per problem. This suggests that a generic coding agent with a minimal harness can already achieve strong performance on Lean benchmarks. Our results motivate using mini-Lean-agent as a standard baseline when evaluating theorem-proving infrastructure.

---


### 485. [Budgeted KV-Cache Repair for Evolving Contexts](https://arxiv.org/abs/2610.17338)

**<font color=#1a73e8>作者：</font>** Han Yu, Wenhui Zhu, Jincheng Cao 等 18 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Language-model agents revise their working context as information becomes obsolete, but deleting text does not erase its influence on cached computation. Later key-value (KV) states remain conditioned on the deleted content, while recomputing the entire retained suffix can be costly. We introduce budgeted KV-cache repair: recovering task performance by recomputing a user-chosen fraction of the retained suffix. Comparing repair allocations under identical relevance scores and token budgets, we find that refreshing coherent regions can substantially outperform refreshing isolated tokens. This finding motivates Semantic-Unit Refresh (SUR), which allocates the budget to query-relevant text regions using inexpensive embedding scores, without training or an auxiliary transformer forward. To execute these repairs efficiently, a layer-packed executor processes selected states together at each layer while preserving full causal cache access. Across five models, SUR achieves strong recovery in controlled deletion tasks while recomputing only 2-5% of the suffix. On four natural multi-hop QA datasets, it achieves near-full-recompute exact match at a 5% budget with lower post-edit latency. The executor accelerates fragmented refresh by up to 16.1x over interval-wise execution.

---


### 486. [WIRE: Weight Space Implicit Representation Encoding of Frozen Video LLMs](https://arxiv.org/abs/2610.17355)

**<font color=#1a73e8>作者：</font>** Ameen Ali, Tamim Zoabi, Lior Wolf 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video language models represent a video as a long sequence of visual embeddings in a decoder's input. Every visual embedding is processed by every decoder layer during prefill, stored in the key value cache, and attended by every generated token, so a long video raises prefill, memory, and generation cost at once. We present WIRE (Weight Space Implicit Representation Encoding), which reduces this recurring cost by moving part of the video conditioned computation of a frozen video language model from its input activations into a temporary low rank update of its weights. WIRE keeps a short explicit visual context, so the update acts as a correction rather than a replacement of the video. WIRE first compresses the full resolution embeddings of each frame into a small set of carrier tokens using a question conditioned bidirectional selective scan, and physically contracts the decoder input so every decoder layer, cache entry, and decoding step operates on the shorter sequence. Hypernetworks at selected decoder layers read the compressed forward pass together with a readout of the full resolution features removed by contraction and generate LoRA updates to the attention and feedforward projections. The updates are merged after prefill, so autoregressive decoding runs the unmodified frozen backbone. On Qwen3-VL-8B, WIRE with 16 carrier tokens per frame contracts the visual stream by $3.5\times$, reduces decoder prefill time by $3.35\times$ at 256 frames and $4.14\times$ at 1024 frames, shrinks the key value cache proportionally, and keeps per token decoding latency approximately constant. Across nine benchmark settings at 256 frames, it obtains the highest average accuracy among efficient video language models we evaluate under a common 256 frame budget.

---


### 487. [claimcheck: Measuring and Improving Specification Faithfulness](https://arxiv.org/abs/2610.17358)

**<font color=#1a73e8>作者：</font>** Martin Amster, One An, Holly Baker 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Formal verification proves that a program satisfies its specification, but says nothing about whether the specification captures what the author meant. As LLMs increasingly write both code and specifications, a gap between the author's natural-language requirement and the specification becomes a live risk. A machine-checked proof of a property narrower than the one requested is worthless but passes every check. Closing this gap is solving the spec formalization problem: given a natural-language requirement, produce a formal artifact whose meaning matches it. To measure the gap, we curate an end-to-end benchmark for spec formalization spanning four formal languages: Dafny contracts and Lean 4, Isabelle and Rocq theorem statements. Each of its 3,234 rows pairs a natural-language requirement with a formal artifact and a label established by execution, by proof, or by the benchmark it is drawn from. A third of the rows are meaning-preserving rewrites of the artifact that keep the faithful label, so a judge cannot score by detecting that a row was edited. We introduce claimcheck, a tool that detects incorrect formalizations: the formal artifact is translated back into plain English by a model that never sees the requirement, and a separate model, the judge, decides whether the informalization and the requirement express the same guarantee. On all four languages it gains 8.2 to 9.8 points of macro recall over a single call shown the requirement and the artifact, and 4.2 to 6.0 over that call handed the same list of meaning-preserving rewrites. Showing the judge the artifact as well costs 1.4 to 4.5 points. Across four judges that also see the artifact, the gain shrinks as the judge gets stronger, to within a point of the informed single call for the strongest.

---


### 488. [UMCR: Universal Medical Concept Recognition through Guideline Integration and Agentic Linking](https://arxiv.org/abs/2610.17363)

**<font color=#1a73e8>作者：</font>** Fabrice Lamarche, Amal Zouaq  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Medical Concept Recognition is the task of extracting and grounding spans in medical text to entries in a standard ontology. Current methods are generally developed towards a single ontology and source text type (clinical notes, drug labels, etc.) The central challenge is therefore to build methods that adapt to any target ontology without requiring ontology-specific retraining. More recent approaches like REAL and AutoPCR make direct use of Large Language Models and can theoretically adapt to any ontology choice but suffer from a lack of generalization. We propose UMCR, a pipeline that allows extraction and linking to any target ontology using any source text variety, utilizing direct guideline integration and an agentic linking module. We evaluate our method on the recent MedPath benchmark, covering a wide variety of medical text types and vocabularies, and show that our method achieves strong performance across these tasks. This ability unlocks interoperability in the healthcare domain, allowing for extraction and alignment between different medical standards. Our method also reduces dependence on parametric LLM memory, thanks to improved interaction with the target ontology compared to other proposed approaches.

---


### 489. [When Goals Leak Across Relationships: How Cached Goal Representations Shape Cross-Client Decisions](https://arxiv.org/abs/2610.17365)

**<font color=#1a73e8>作者：</font>** Saloni Gupta, Sébastien Krier, Glenn Matlin  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As LLM agents take on more autonomous roles, they may interact with multiple clients and counterparties whose goals and incentives conflict. If an agent maintains shared inference state across these interactions, information associated with one relationship may influence decisions made for another. We test OLMo-3-7B-Instruct in a controlled two-client environment with 20 market scenarios, where each client is assigned an opposing objective. With shared conversational memory, the model deviates from the current client's objective in 22% of eligible decisions. We then investigate how these goals are represented in the KV cache. Linear probes show that client-goal ownership becomes highly recoverable in middle layers and is concentrated in particular attention heads. We use these results to identify where to intervene in the cache and test whether these representations affect the model's decisions. Ablating the competitor's cached goal representations at these locations shifts the model toward the current client. The effect is larger for heads identified by probing than for randomly selected heads, and larger when ablating goal tokens than matched non-goal tokens from the same client. Our results show that client-specific goal representations persist in the KV cache and can causally influence decisions made for other clients, highlighting the importance of relationship-specific state isolation in persistent LLM agents.

---


### 490. [HarnessTTT: Learn to Optimize Harness at Test-Time for Scientific Discovery](https://arxiv.org/abs/2610.17370)

**<font color=#1a73e8>作者：</font>** Yingzi Ma, Yulong Cao, Nanxi Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Scientific discovery with language models requires finding the best valid solution within a finite computational budget. We study how feedback from this search can improve the procedure used to conduct it. We introduce HarnessTTT, a test-time learning framework that trains a harness proposer while keeping the executor frozen. The proposer generates executable harnesses comprising system prompts, reusable skills, tools, middleware, and execution controls. Each harness guides a budgeted discovery rollout, whose outcome provides feedback for updating the proposer. A discovery-oriented policy-gradient objective combines gap-normalized rewards, leave-one-out advantages (RLOO), and max-sharpening to favor high-performing proposals. Generated components are validated before execution, and the search retains the best valid solution and selected harnesses across rounds. Across fourteen discovery tasks in mathematics, systems, GPU kernels, heuristic programming, astrodynamics, and biology, HarnessTTT with a frozen 9B executor improves on OpenEvolve with the same executor on all eleven benchmark tasks (e.g., from 1.17 to 2.64 on circle packing), improves on the discovery-fine-tuned Finch-9B by up to 92%, holds the best open-weight sub-10B result on nine, and reaches 0.380919 on Erdős minimum overlap, better than the best human reference of 0.380927. Scaling the proposer and frozen executor to 27B improves on eleven of fourteen tasks, and transferring the learned harnesses to GPT-5.5 matches or exceeds the strongest reported system of any backbone on nine of fourteen tasks. Together, these results show that harness search can itself be learned at test time: a trained proposer lets a small frozen executor search effectively, and the harnesses it finds carry over to stronger executors.

---


### 491. [PIG: Parallel Inconsistency Guidance for Accelerating Diffusion Language Models](https://arxiv.org/abs/2610.17375)

**<font color=#1a73e8>作者：</font>** Quentin Fruytier, Anton Xue, Sanjay Shakkottai 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Diffusion language models accelerate generation by decoding multiple masked positions per forward pass. However, accuracy is known to drop when parallel decoding trajectories deviate from their sequential counterparts, which are slow and expensive "oracles" that adhere to the joint distribution of language. In this paper, we propose Parallel Inconsistency Guidance (PIG), a new paradigm that uses a trained auxiliary model to directly estimate the inconsistency between parallel and sequential generation from a single model forward pass. During inference, masked positions are traversed by decreasing confidence, and tokens are added to the parallel decode set one-at-a-time until the total estimated inconsistency between the parallel and sequential generation exceeds a threshold. Surprisingly, it suffices to train a lightweight ~2M parameter auxiliary model on a small mixture drawn from OpenCoder, GSM8K-train, MATH-train, and MBPP-train. For LLaDA-8B Instruct and NemotronDiffusion-3B Instruct, PIG extends the accuracy-TPF frontier on GSM8K, MATH500, MBPP, HumanEval, and MMLU, when compared to the industry standard Fast-dLLM and measures favorably on LLaDA-8B Instruct against DAPD, KLASS, EB-sampler, and other learned unmasking policies.

---


### 492. [EPOCH: Coverage-Aware Evolution with Experiential Preference Optimization for LLM-based Automated Heuristic Design](https://arxiv.org/abs/2610.17379)

**<font color=#1a73e8>作者：</font>** Oguzhan Gungordu, Ayse Tursucular, Siheng Xiong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-based automated heuristic design (AHD) discovers heuristics for combinatorial optimization problems (COPs), where an LLM generates candidates in an evolutionary search. Existing frameworks freeze the generator or fine-tune it on a scalar fitness signal hiding which instances each heuristic covers. Reflection-based frameworks improve heuristics with natural-language feedback, but it stays in the prompt and never reaches the generator's weights. We propose EPOCH, which makes instance coverage the objective of the evolutionary search and fine-tunes the generator to internalize reflection. Parent selection, operator allocation, and stagnation recovery all optimize how well the heuristics jointly cover the training instances, so the search returns a complementary heuristic ensemble. The generator learns from its own search by experiential preference optimization. A teacher LLM returns a natural-language insight on the generated heuristics, and the generator produces new heuristics with this insight. These improvements join the preference pairs for direct preference optimization (DPO). Since DPO only teaches the generator to rank these improvements, a reflective self-distillation (RSD) term makes it more likely to generate them on its own, and the gains accumulate over the long horizon of the search. Across COPs and open-source LLM backbones, EPOCH's heuristic ensembles outperform inference-only and fine-tuned baselines and generalize across problem scales.

---


### 493. [JustOPD: On-Policy Distillation from Autoregressive to Diffusion Language Models](https://arxiv.org/abs/2610.17397)

**<font color=#1a73e8>作者：</font>** Zikun Zhang, Jiayuan Sheng, David D. Yao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) is a post-training approach for large language models (LLMs) that enables a student model to learn a teacher model's distribution from sequences sampled from the student's own policy. Despite its promising capability, OPD for diffusion language models (DLMs) remains underexplored and existing studies primarily focuses on DLM-to-DLM distillation. The limited availability of strong teacher DLMs and the flexible generation order of DLMs impose additional technical challenges as well. However, it remains unclear how to effectively distill knowledge from a strong autoregressive language model (ARM) into a weaker DLM, given the mismatch between the left-to-right decoding of ARMs and the flexible decoding order of DLMs. Inspired by Ni et al. (2026), we propose JustOPD, an ARM-to-DLM on-policy distillation method that uses autoregressive rollouts during training to align the student's generation process with the ARM teacher's left-to-right decoding. This alignment enables effective distillation from ARM teachers while preserving the DLM's flexible generation-order capability at inference time. Experiments using Qwen3-14B as the teacher and Dream-7B as the student demonstrate that JustOPD consistently improves mathematical reasoning performance over the base DLM across multiple divergence choices.

---


### 494. [Learning to Detect Shifts in Unstructured Data Streams via Monitoring-by-Betting](https://arxiv.org/abs/2610.17399)

**<font color=#1a73e8>作者：</font>** Siyu Zhou, Jialin Ouyang, Fan Xia 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continuous monitoring of generative AI systems requires detecting distribution shifts in the unstructured data they ingest and generate. Existing monitoring methods typically control false alarms by requiring the discrepancy measure used to detect shifts to be *pre-specified*. However, for unstructured data, pre-specification creates a sensitivity--breadth trade-off: a narrowly defined measure is sensitive to the anticipated shift but may miss unexpected changes, whereas a broadly defined measure may detect a wider range of shifts but with reduced sensitivity. Although adaptively hypothesizing the shift direction can overcome this limitation, such data-dependent adaptation generally invalidates conventional false-alarm guarantees. We reconcile adaptivity with statistical validity through testing-by-betting, reframing sequential changepoint detection as a betting game in which the bettor continually updates its hypothesized shift direction, or witness function, as new observations arrive. We introduce *asymptotic e-detectors*, which approximate the pre-change distribution using a calibration set of size $m$, and prove that they asymptotically control the average run length to a false alarm as $m$ increases. Empirically, calibration sets as small as $m=30$ provide effective control. We then develop adaptive monitoring strategies ranging from black-box bettors that learn from embeddings to interpretable bettors based on LLM-proposed concepts. Across three real-world datasets, including data from a clinical AI scribe deployment, adaptive monitors detect shifts faster than fixed monitors at the same false-alarm level. Further, when the true shifts are sparse and interpretable, LLM-concept monitors provide the fastest and most interpretable detection, while also guiding root-cause diagnosis for complex shifts.

---


### 495. [Evaluating Temporal Reasoning in Large Language Models: Event Temporal Relation Extraction with Allen's Interval Algebra, Logical Consistency, and Relative Time in Narratives](https://arxiv.org/abs/2610.17402)

**<font color=#1a73e8>作者：</font>** Adib Sakhawat, Fardeen Sadab, Tamjid Hasan Fahim 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Understanding a narrative means knowing how every event relates in time to every other, yet large language models (LLMs) are mostly tested on isolated event pairs or coarse labels. We ask five LLMs to reconstruct the complete network of Allen's 13 interval relations for 360 English narratives whose events are placed relative to one another rather than by dates, and evaluate the outputs under a pre-registered protocol for agreement with our gold annotations, converse consistency and logical satisfiability. End to end, the best model clearly beats trivial baselines on macro-F1, our primary metric, yet under our pre-registered parser no model matches the accuracy of always answering "before", which the skewed labels inflate. Most of that accuracy gap is a parsing artifact: formatting errors in large matrices cost whole rows, and a post hoc parser that recovers the determined cells of malformed rows raises coverage from 0.60 to 0.84 and closes the gap to the baseline for the best model. On the cells they do answer, models recover precedence and containment but rarely overlap, and they fail most on flashbacks, where both the narration and the event list present the later event first. Logical consistency varies widely yet says little about agreement with gold: enforcing it raises accuracy mainly by filling empty cells, and is beaten there by the trivial control of guessing the majority label. Reliable structured output and robust handling of relative time are prerequisites for temporal reasoning over whole narratives.

---


### 496. [Reinforcement Learning In Partially Verifiable Environments for Colon Cancer Treatment Planning](https://arxiv.org/abs/2610.17426)

**<font color=#1a73e8>作者：</font>** Li-Ching Chen, Andrés Franco Valiente, Yuta Ishiyama 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Clinical decision-making is a sequential process of information collection, clinical inference, and forecasting under partial observability, often without a uniquely correct treatment decision. Large language models (LLMs) have demonstrated strong medical question-answering capabilities but extending these advances to clinical reasoning remains challenging because many clinical tasks are only partially verifiable. Recent clinical reinforcement learning (RL) work has therefore largely focused on diagnostic endpoints, where correctness can be more directly verified. Oncology treatment decision making is a particularly challenging instance of this problem that extends beyond medical question-answering in which multiple decision trajectories can be clinically defensible for the same partially observed patient state. We formulate oncology treatment planning as an interactive RL problem under partial observability and construct patient-specific, process-aware rewards from decision processes observed in real world clinical records. The agent must learn to sequentially acquire information from a structured patient representation before committing to a first-line treatment recommendation, and is evaluated on information gathering, treatment selection, and reasoning alignment. Using GRPO and GDPO to optimize Llama-3.1-8B-Instruct within this environment, RL substantially improves the base policy beyond frontier model capabilities. The GDPO-trained policy increases Mean@3 scalar clinical reward by $79.60\%$ over base Llama and exceeds GPT-5.2 by $18.82\%$ under the same interactive environment, while reducing query count during training. Overall, our results show that patient-specific, partially verifiable rewards can provide an effective learning signal for interactive clinical RL when both the patient state and the underlying clinical decision process are only partially observed.

---


### 497. [Monarch-Muon: Structure-Aware Muon for Fast and Memory-Efficient Pretraining](https://arxiv.org/abs/2610.17429)

**<font color=#1a73e8>作者：</font>** Alexander Miasnikov, Ruslan Kabirov, Gleb Molodtsov 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Training large language models is constrained by both wall-clock time and memory footprint, and recent matrix-aware optimizers sharpen this tradeoff: Muon can improve optimization but its dense polar update remains expensive. We propose Monarch-Muon, a structured matrix-aware optimizer for weights parameterized by Monarch factors. The resulting structure reduces weights, gradients, and optimizer state, and exposes small independent update subproblems in place of a single dense orthogonalization; we formalize this through a blockwise trust-region interpretation. In quality runs, Monarch-Muon improves over Monarch-AdamW at fixed structure: 3.06 vs. 3.09 in the dense 257M model and 2.68 vs. 2.77 in the 1B MoE model; the two-block MoE variant also matches dense AdamW while using 15% fewer active and 25.4% fewer total parameters. In 6.89B-parameter systems measurements, Monarch-Muon reduces peak memory from 68.9 to 52.9 GB, Muon optimizer state from 14.60 to 6.77 GB, and the Muon optimizer step from 1288 to 304 ms.

---


### 498. [VeriRouter: Towards Verifiable LLM Routing](https://arxiv.org/abs/2610.17431)

**<font color=#1a73e8>作者：</font>** Mengyu Yao, Ziqi Zhang, Shaofei Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) routers are increasingly deployed to optimize quality, latency, and cost through dynamic model selection and request rewriting. However, a compromised router can cause ineligible selection on the control plane, unendorsed rewriting or unfaithful relay on the data plane, undermining LLM routing integrity. We present VeriRouter, a verifiable LLM routing framework. Under an endorsed public context binding a private semantic index and rewrite banks, VeriRouter combines ZK proofs with a provider-issued serving certificate to establish integrity across both planes while keeping the router's private routing assets hidden from clients. For model selection, we design an efficient ZK proof for semantic search. For rewriting, local checks enforce message preservation and additions from committed banks. On real-world workloads, VeriRouter's model-selection and rewrite proofs average 21.92~s and 4.24~s, yielding 1,307$\times$ and 101$\times$ speedups over the fastest completing baselines. Relative to serving without verification, VeriRouter adds only 4.08 s under per-turn selection and 0.11 s under session-pinned selection.

---


### 499. [SchemaWeaver: Accelerating On-Device Mobile Agentic AI via Schema-Guided Parallel LLM Decoding](https://arxiv.org/abs/2610.17436)

**<font color=#1a73e8>作者：</font>** Boyuan Yang, Wei Gao  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) on mobile devices can act as agents that call external software tools to complete complex tasks, but the major challenge of supporting on-device mobile agentic AI with LLMs is the long latency of LLM tool calling on mobile devices. In particular, the decode phase is the main contributor of such long latency, but is hard to speed up on mobile processors as it is bound by memory bandwidth rather than compute power. To address this limitation, in this paper we present SchemaWeaver, a new on-device mobile agentic AI technique that enforces schema-guided parallel decoding in the decode phase of LLM tool calling, to reduce its latency by producing multiple tokens in each decode pass. SchemaWeaver can be generically applied to the LLM inference engine on mobile devices without involving any training efforts or changes on LLMs, and our experiment results on major mobile SoCs and LLM families show that SchemaWeaver can reduce the LLM tool calling latency by up to 3.9 times, compared to the competitive baselines.

---


### 500. [Large Language Models Extend Known Research But Do Not Create New Research Directions](https://arxiv.org/abs/2610.17439)

**<font color=#1a73e8>作者：</font>** Zhihua Liu, Kurt Butler, Damian Machlanski 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The success of autonomous research systems relies on the quality of the scientific hypotheses they generate. Recent studies report that human reviewers often rate LLM-generated ideas as more novel than those from human experts, raising hope that AI can accelerate scientific discovery. Yet it is unclear whether these models can do more than extend existing knowledge. Can LLMs drive genuine innovation by revealing new research directions, or are they limited to repeating and recombining what science already knows? This unresolved question lies at the heart of discussions about AI and the future of science. To address this, we distinguish two types of novelty: distance, which measures how far a hypothesis lies from existing work, and direction, which captures whether the hypothesis pursues new lines of inquiry beyond those already present. These two measures diverge sharply for LLM-generated work. We represent scientific papers in a shared conceptual space using a pretrained scientific-paper embedding model. Within this space, we embed 26.9 million human-authored papers across 1,325 research topics in six natural-science fields and 524,308 LLM-generated hypotheses from eight models. Distance is measured using existing metrics. To quantify direction, we introduce the orthogonal novelty score (ONS). LLMs consistently generate ideas more distant from existing work than human-authored papers, up to 16\% further when the LLM is given the papers farthest from the centre of the topic. However, LLM hypotheses have a 15--23\% lower median ONS than published papers from the same topic. Thus, LLMs move further from what is already known, but remain within established directions. This pattern persists across changes in various configurations. As a result, LLMs excel at extending the frontier but the creation of new directions is still led by human scientists.

---


> [!TIP]
> 当前位于：**451-500**（第 10/17 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | **451-500** | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-700](./part-14.md) | [701-750](./part-15.md) | [751-800](./part-16.md) | [801-810](./part-17.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
