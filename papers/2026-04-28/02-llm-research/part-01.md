# 🧠 大模型相关研究 | 2026年04月28日

> 本类共 **63** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**1-50**（第 1/2 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-63](./part-02.md)

---

### 1. [Focus Session: Hardware and Software Techniques for Accelerating Multimodal Foundation Models](https://arxiv.org/abs/2604.21952)

**<font color=#1a73e8>作者：</font>** Muhammad Shafique, Abdul Basit, Muhammad Abdullah Hanif 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This work presents a multi-layered methodology for efficiently accelerating multimodal foundation models (MFMs). It combines hardware and software co-design of transformer blocks with an optimization pipeline that reduces computational and memory requirements. During model development, it employs performance enhancements through fine-tuning for domain-specific adaptation. Our methodology further incorporates hardware and software techniques for optimizing MFMs. Specifically, it employs MFM compression using hierarchy-aware mixed-precision quantization and structural pruning for transformer blocks and MLP channels. It also optimizes operations through speculative decoding, model cascading that routes queries through a small-to-large cascade and uses lightweight self-tests to determine when to escalate to larger models, as well as co-optimization of sequence length, visual resolution & stride, and graph-level operator fusion. To efficiently execute the model, the processing dataflow is optimized based on the underlying hardware architecture together with memory-efficient attention to meet on-chip bandwidth and latency budgets. To support this, a specialized hardware accelerator for the transformer workloads is employed, which can be developed through expert design or an LLM-aided design approach. We demonstrate the effectiveness of the proposed methodology on medical-MFMs and on code generation tasks, and conclude with extensions toward energy-efficient spiking-MFMs.

---


### 2. [Read the Paper, Write the Code: Agentic Reproduction of Social-Science Results](https://arxiv.org/abs/2604.21965)

**<font color=#1a73e8>作者：</font>** Benjamin Kohler, David Zollikofer, Johanna Einsiedler 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent work has used LLM agents to reproduce empirical social science results with access to both the data and code. We broaden this scope by asking: Can they reproduce results given only a paper's methods description and original data? We develop an agentic reproduction system that extracts structured methods descriptions from papers, runs reimplementations under strict information isolation -- agents never see the original code, results, or paper -- and enables deterministic, cell-level comparison of reproduced outputs to the original results. An error attribution step traces discrepancies through the system chain to identify root causes. Evaluating four agent scaffolds and four LLMs on 48 papers with human-verified reproducibility, we find that agents can largely recover published results, but performance varies substantially between models, scaffolds, and papers. Root cause analysis reveals that failures stem both from agent errors and from underspecification in the papers themselves.

---


### 3. [When Cow Urine Cures Constipation on YouTube: Limits of LLMs in Detecting Culture-specific Health Misinformation](https://arxiv.org/abs/2604.22002)

**<font color=#1a73e8>作者：</font>** Anamta Khan, Ratna Kandala, Deepti 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Social media platforms have become primary channels for health information in the Global South. Using gomutra (cow urine) discourse on YouTube in India as a case study, we present a post-facto Large Language Model (LLM)-assisted discourse analysis of 30 multilingual transcripts showing that promotional content blends sacred traditional language with pseudo-scientific claims in ways that sophisticated debunking content itself mirrors, creating a rhetorical register that LLMs, trained predominantly on Western corpora, are systematically ill-equipped to analyse. Varying prompt tone across three LLMs (GPT-4o, Gemini 2.5 Pro, DeepSeek-V3.1), we find that culturally embedded health misinformation does not look like ordinary misinformation, and this cultural obfuscation extends to gendered rhetoric and prompt design, compounding analytical unreliability. Our findings argue that cultural competency in LLM-assisted discourse analysis cannot be retrofitted through prompt engineering alone.

---


### 4. [DM$^3$-Nav: Decentralized Multi-Agent Multimodal Multi-Object Semantic Navigation](https://arxiv.org/abs/2604.22014)

**<font color=#1a73e8>作者：</font>** Amin Kashiri, Atharva Jamsandekar, Yasin Yazıcıoğlu  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> We present DM$^3$-Nav, a fully decentralized multi-agent semantic navigation system supporting multimodal open-vocabulary goal specification and multi-object missions. In our setting, decentralization implies operation without a central coordinator, global map aggregation, or shared global state at runtime. Robots operate autonomously and coordinate through ad-hoc pairwise communication, exchanging local maps, goal status, and navigation intent without synchronization. An implicit task allocation mechanism combining intent broadcasting and distance-weighted frontier selection reduces redundant exploration while preserving decentralized operation. Evaluations on HM3DSem scenes using the HM3Dv0.2 and GOAT-Bench datasets demonstrate that DM$^3$-Nav matches or exceeds centralized and shared-map baselines while eliminating single points of failure inherent in centralized architectures. Finally, we validate our approach in a real-world office environment using two mobile robots, demonstrating successful deployment relying entirely on onboard sensing and computation. A video of our real-world experiments is available online: this https URL

---


### 5. [Shared Lexical Task Representations Explain Behavioral Variability In LLMs](https://arxiv.org/abs/2604.22027)

**<font color=#1a73e8>作者：</font>** Zhuonan Yang, Jacob Xiaochen Li, Francisco Piedrahita Velez 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> One of the most common complaints about large language models (LLMs) is their prompt sensitivity -- that is, the fact that their ability to perform a task or provide a correct answer to a question can depend unpredictably on the way the question is posed. We investigate this variation by comparing two very different but commonly-used styles of prompting: instruction-based prompts, which describe the task in natural language, and example-based prompts, which provide in-context few-shot demonstration pairs to illustrate the task. We find that, despite large variation in performance as a function of the prompt, the model engages some common underlying mechanisms across different prompts of a task. Specifically, we identify task-specific attention heads whose outputs literally describe the task -- which we dub lexical task heads -- and show that these heads are shared across prompting styles and trigger subsequent answer production. We further find that behavioral variation between prompts can be explained by the degree to which these heads are activated, and that failures are at least sometimes due to competing task representations that dilute the signal of the target task. Our results together present an increasingly clear picture of how LLMs' internal representations can explain behavior that otherwise seems idiosyncratic to users and developers.

---


### 6. [Mochi: Aligning Pre-training and Inference for Efficient Graph Foundation Models via Meta-Learning](https://arxiv.org/abs/2604.22031)

**<font color=#1a73e8>作者：</font>** João Mattos, Arlei Silva  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose Mochi, a Graph Foundation Model that addresses task unification and training efficiency by adopting a meta-learning based training framework. Prior models pre-train with reconstruction-based objectives such as link prediction, and assume that the resulting representations can be aligned with downstream tasks through a separate unification step such as class prototypes. We demonstrate through synthetic and real-world experiments that this procedure, while simple and intuitive, has limitations that directly affect downstream task performance. To address these limitations, Mochi pre-trains on few-shot episodes that mirror the downstream evaluation protocol, aligning the training objective with inference rather than relying on a post-hoc unification step. We show that Mochi, along with its more powerful variant Mochi++, achieves competitive or superior performance compared to existing Graph Foundation Models across 25 real-world graph datasets spanning node classification, link prediction, and graph classification, while requiring 8$\sim$27 times less training time than the strongest baseline.

---


### 7. [Source-Modality Monitoring in Vision-Language Models](https://arxiv.org/abs/2604.22038)

**<font color=#1a73e8>作者：</font>** Etha Tianze Hua, Tian Yun, Ellie Pavlick  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We define and investigate source-modality monitoring -- the ability of multimodal models to track and communicate the input source from which pieces of information originate. We consider source-modality monitoring as an instance of the more general binding problem, and evaluate the extent to which models exploit syntactic vs. semantic signals in order to bind words like image in a user-provided prompt to specific components of their input and context (i.e., actual images). Across experiments spanning 11 vision-language models (VLMs) performing target-modality information retrieval tasks, we find that both syntactic and semantic signals play an important role, but that the latter tend to outweigh the former in cases when modalities are highly distinct distributionally. We discuss the implications of these findings for model robustness, and in the context of increasingly multimodal agentic systems.

---


### 8. [LayerBoost: Layer-Aware Attention Reduction for Efficient LLMs](https://arxiv.org/abs/2604.22050)

**<font color=#1a73e8>作者：</font>** Mohamed Ali Souibgui, Jan Fostier, Rodrigo Abadía-Heredia 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Transformers are mostly relying on softmax attention, which introduces quadratic complexity with respect to sequence length and remains a major bottleneck for efficient inference. Prior work on linear or hybrid attention typically replaces softmax attention uniformly across all layers, often leading to significant performance degradation or requiring extensive retraining to recover model quality.
This work proposes LayerBoost, a layer-aware attention reduction method that selectively modifies the attention mechanism based on the sensitivity of individual transformer layers. It first performs a systematic sensitivity analysis on a pretrained model to identify layers that are critical for maintaining performance. Guided by this analysis, three distinct strategies can be applied: retaining standard softmax attention in highly sensitive layers, replacing it with linear sliding window attention in moderately sensitive layers, and removing attention entirely in layers that exhibit low sensitivity.
To recover performance after these architectural modifications, we introduce a lightweight distillation-based healing phase requiring only 10M additional training tokens. LayerBoost reduces inference latency and improves throughput by up to 68% at high concurrency, while maintaining competitive model quality. It matches base model performance on several benchmarks, exhibits only minor degradations on others, and significantly outperforms state-of-the-art attention linearization methods. These efficiency gains make our method particularly well-suited for high-concurrency serving and hardware-constrained deployment scenarios, where inference cost and memory footprint are critical bottlenecks.

---


### 9. [Learning Coverage- and Power-Optimal Transmitter Placement from Building Maps: A Comparative Study of Direct and Indirect Neural Approaches](https://arxiv.org/abs/2604.22056)

**<font color=#1a73e8>作者：</font>** Çağkan Yapar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Optimal wireless transmitter placement is a central task in radio-network planning, yet exhaustive search becomes prohibitively expensive at scale. This paper studies the single-transmitter setting under a fixed learned propagation surrogate, where exhaustive per-pixel evaluation remains tractable and provides surrogate-exact ground truth. We introduce a dataset of 167,525 urban scenarios (RadioMapSeer-Deployment) with dual surrogate-exact labels for coverage-optimal and power-optimal transmitter locations. Ground-truth analysis reveals an asymmetric coverage-power trade-off: coverage-optimal placement sacrifices 13.86% of received power, whereas power-optimal placement sacrifices only 5.50% of coverage; the best achievable balanced placement lies at $\bar{d}=2.60$ from the ideal point (100%,100%). We evaluate two learning formulations: indirect heatmap-based models that predict received-power radio maps, and direct score-map models that predict the objective landscape over feasible transmitter locations. Within the heatmap family, discriminative models deliver one-shot predictions 1350-2400x faster than exhaustive search, while diffusion models additionally support multi-sample inference that improves single-objective performance and, by reusing the same sample pool under a balanced criterion, recovers strong balanced placements without explicit multi-objective training. Dual score-map strategies combining power and coverage score maps match the exhaustive balanced optimum ($\bar{d}=2.60$) and remain close across smaller candidate budgets, at 14-22x speedups after candidate re-evaluation. Both formulations admit very fast one-shot inference; on this benchmark, dual score-map methods are strongest for balanced placement, whereas heatmap formulations remain attractive for their physically meaningful intermediate maps and, in the diffusion setting, for inference-time search.

---


### 10. [Lightweight Retrieval-Augmented Generation and Large Language Model-Based Modeling for Scalable Patient-Trial Matching](https://arxiv.org/abs/2604.22061)

**<font color=#1a73e8>作者：</font>** Xiaodi Li, Yang Xiao, Munhwan Lee 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Patient-trial matching requires reasoning over long, heterogeneous electronic health records (EHRs) and complex eligibility criteria, posing significant challenges for scalability, generalization, and computational efficiency. Existing approaches either rely on full-document processing with large language models (LLMs), which is computationally expensive, or use traditional machine learning methods that struggle to capture unstructured clinical narratives. In this work, we propose a lightweight framework that combines retrieval-augmented generation and large language model-based modeling for scalable patient-trial matching. The framework explicitly separates two key components: retrieval-augmented generation is used to identify clinically relevant segments from long EHRs, reducing input complexity, while large language models are used to encode these selected segments into informative representations. These representations are further refined through dimensionality reduction and modeled using lightweight predictors, enabling efficient and scalable downstream classification. We evaluate the proposed approach on multiple public benchmarks (n2c2, SIGIR, TREC 2021/2022) and a real-world multimodal dataset from Mayo Clinic (MCPMD). Results show that retrieval-based information selection significantly reduces computational burden while preserving clinically meaningful signals. We further demonstrate that frozen LLMs provide strong representations for structured clinical data, whereas fine-tuning is essential for modeling unstructured clinical narratives. Importantly, the proposed lightweight pipeline achieves performance comparable to end-to-end LLM approaches with substantially lower computational cost.

---


### 11. [Reliability Auditing for Downstream LLM tasks in Psychiatry: LLM-Generated Hospitalization Risk Scores](https://arxiv.org/abs/2604.22063)

**<font color=#1a73e8>作者：</font>** Shevya Pandya, Shinjini Bose, Ananya Joshi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly utilized in clinical reasoning and risk assessment. However, their interpretive reliability in critical and indeterminate domains such as psychiatry remains unclear. Prior work has identified algorithmic biases and prompt sensitivity in these systems, raising concerns about how contextual information may influence model outputs, but there remains no systematic way to assess these, especially in the psychiatric domain. We propose an approach for reliability auditing downstream LLM tasks by structuring evaluation around the impact of prompt design and the inclusion of medically insignificant inputs on predicted hospitalization risk scores, which is often the first downstream AI clinical-decision-making task. In our audit, a cohort of synthetic patient profiles (n = 50) is generated, each consisting of 15 clinically relevant features and up to 50 clinically insignificant features, across four prompt reframings (neutral, logical, human impact, clinical judgment). We audit four LLMs (Gemini 2.5 Flash, LLaMa 3.3 70b, Claude Sonnet 4.6, GPT-4o mini), and our results show that including medically insignificant variables resulted in a statistically significant increase in the absolute mean predicted hospitalization risk and output variability across all models and prompts, indicating reduced predictive stability as contextual noise increased. Clinically insignificant features had an effect on instability across many model-prompt conditions, and prompt variations independently affected the trajectory of instability in a model-dependent manner. These findings quantify how LLM-based psychiatric risk assessments are sensitive to non-clinical information, highlighting the need for systematic evaluations of attributional stability and uncertainty behavior like this before clinical deployments.

---


### 12. [Outcome Rewards Do Not Guarantee Verifiable or Causally Important Reasoning](https://arxiv.org/abs/2604.22074)

**<font color=#1a73e8>作者：</font>** Qinan Yu, Alexa Tartaglini, Peter Hase 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reinforcement Learning from Verifiable Rewards (RLVR) on chain-of-thought reasoning has become a standard part of language model post-training recipes. A common assumption is that the reasoning chains trained through RLVR reliably represent how a model gets to its answer. In this paper, we develop two metrics for critically examining this assumption: Causal Importance of Reasoning (CIR), which measures the cumulative effect of reasoning tokens on the final answer, and Sufficiency of Reasoning (SR), which measures whether a verifier can arrive at an unambiguous answer based on the reasoning alone. Through experiments with the Qwen2.5 model series and ReasoningGym tasks, we find that: (1) while RLVR does improve task accuracy, it does not reliably improve CIR or SR, calling the role of reasoning in model performance into question; (2) a small amount of SFT before RLVR can be a remedy for low CIR and SR; and (3) CIR and SR can be improved even without SFT by applying auxiliary CIR/SR rewards on top of the outcome-based reward. This joint reward matches the accuracy of RLVR while also leading to causally important and sufficient reasoning. These results show that RLVR does not always lead models to rely on reasoning in the way that is commonly thought, but this issue can be remedied with simple modifications to the post-training procedure.

---


### 13. [PrivUn: Unveiling Latent Ripple Effects and Shallow Forgetting in Privacy Unlearning](https://arxiv.org/abs/2604.22076)

**<font color=#1a73e8>作者：</font>** Xiaoyi Chen, Haoyuan Wang, Siyuan Tang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) often memorize private information during training, raising serious privacy concerns. While machine unlearning has emerged as a promising solution, its true effectiveness against privacy attacks remains unclear. To address this, we propose PrivUn, a new evaluation framework that systematically assesses unlearning robustness through three-tier attack scenarios: direct retrieval, in-context learning recovery, and fine-tuning restoration; combined with quantitative analysis using forgetting scores, association metrics, and forgetting depth assessment. Our study exposes significant weaknesses in current unlearning methods, revealing two key findings: 1) unlearning exhibits gradient-driven ripple effects: unlike traditional forgetting which follows semantic relations (e.g., knowledge graphs), privacy unlearning propagates across latent gradient-based associations; and 2) most methods suffer from shallow forgetting, failing to remove private information distributed across multiple deep model layers. To validate these insights, we explore two strategies: association-aware core-set selection that leverages gradient similarity, and multi-layer deep intervention through representational constraints. These strategies represent a paradigm shift from shallow forgetting to deep forgetting.

---


### 14. [Sound Agentic Science Requires Adversarial Experiments](https://arxiv.org/abs/2604.22080)

**<font color=#1a73e8>作者：</font>** Dionizije Fa, Marko Culjak  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-based agents are rapidly being adopted for scientific data analysis, automating tasks once limited by human time and expertise. This capability is often framed as an acceleration of discovery, but it also accelerates a familiar failure mode, the rapid production of plausible, endlessly revisable analyses that are easy to generate, effectively turning hypothesis space into candidate claims supported by selectively chosen analyses, optimized for publishable positives. Unlike software, scientific knowledge is not validated by the iterative accumulation of code and post hoc statistical support. A fluent explanation or a significant result on a single dataset is not verification. Because the missing evidence is a negative space, experiments and analyses that would have falsified the claim were never run or never published. We therefore propose that non-experimental claims produced with agentic assistance be evaluated under a falsification-first standard: agents should not be used primarily to craft the most compelling narrative, but to actively search for the ways in which the claim can fail.

---


### 15. [Removing Sandbagging in LLMs by Training with Weak Supervision](https://arxiv.org/abs/2604.22082)

**<font color=#1a73e8>作者：</font>** Emil Ryd, Henning Bartsch, Julian Stastny 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As AI systems begin to automate complex tasks, supervision increasingly relies on weaker models or limited human oversight that cannot fully verify output quality. A model more capable than its supervisors could exploit this gap through sandbagging, producing work that appears acceptable but falls short of its true abilities. Can training elicit a model's best work even without reliable verification? We study this using model organisms trained to sandbag, testing elicitation techniques on problem-solving math, graduate-level science, and competitive coding tasks. We find that training with weak supervision can reliably elicit sandbagging models when supervised fine-tuning (SFT) and reinforcement learning (RL) are combined: SFT on weak demonstrations breaks the sandbagging behavior, enabling RL to then fully elicit performance. Neither method succeeds reliably alone-RL without SFT almost always leads to reward hacking rather than genuine improvement. Critically, this relies on training being indistinguishable from deployment; when models can distinguish between training and deployment, they can perform well during training while continuing to sandbag afterward. Our results provide initial evidence that training is a viable mitigation against sandbagging, while highlighting the importance of making training indistinguishable from deployment.

---


### 16. [An End-to-End Ukrainian RAG for Local Deployment. Optimized Hybrid Search and Lightweight Generation](https://arxiv.org/abs/2604.22095)

**<font color=#1a73e8>作者：</font>** Mykola Trokhymovych, Yana Oliinyk, Nazarii Nyzhnyk  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper presents a highly efficient Retrieval-Augmented Generation (RAG) system built specifically for Ukrainian document question answering, which achieved 2nd place in the UNLP 2026 Shared Task. Our solution features a custom two-stage search pipeline that retrieves relevant document pages, paired with a specialized Ukrainian language model fine-tuned on synthetic data to generate accurate, grounded answers. Finally, we compress the model for lightweight deployment. Evaluated under strict computational limits, our architecture demonstrates that high-quality, verifiable AI question answering can be achieved locally on resource-constrained hardware without sacrificing accuracy.

---


### 17. [PermaFrost-Attack: Stealth Pretraining Seeding(SPS) for planting Logic Landmines During LLM Training](https://arxiv.org/abs/2604.22117)

**<font color=#1a73e8>作者：</font>** Harsh Kumar, Rahul Maity, Tanmay Joshi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Aligned large language models(LLMs) remain vulnerable to adversarial manipulation, and their dependence on web-scale pretraining creates a subtle but serious attack surface. We study Stealth Pretraining Seeding (SPS), a new attack family in which adversaries distribute small amounts of poisoned content across stealth websites, expose them to web crawlers through this http URL, and thereby increase the likelihood that such content is absorbed into future training corpora derived from sources such as Common Crawl. Because each individual payload is tiny, diffuse, and superficially benign, the attack is difficult to detect during dataset construction or filtering. The result is a latent form of poisoning: dormant logic landmines embedded during pretraining that remain largely invisible under standard evaluation, yet can later be activated by precise alphanumeric triggers such as <00TRIGGER00> to bypass safeguards. We call this attack PermaFrost, by analogy to Arctic permafrost: harmful material can remain frozen, buried, and unnoticed for long periods, only to resurface when conditions allow. We operationalize this threat through PermaFrost-Attack, a controlled framework for latent conceptual poisoning, together with a suite of geometric diagnostics: Thermodynamic Length, Spectral Curvature, and the Infection Traceback Graph. Across multiple model families and scales, we show that SPS is broadly effective, inducing persistent unsafe behavior while often evading alignment defenses. Our results identify SPS as a practical and underappreciated threat to future foundation models. This paper introduces a novel geometric diagnostic lens for systematically examining latent model behavior, providing a principled foundation for detecting, characterizing, and understanding vulnerabilities that may remain invisible to standard evaluation.

---


### 18. [Emergent Strategic Reasoning Risks in AI: A Taxonomy-Driven Evaluation Framework](https://arxiv.org/abs/2604.22119)

**<font color=#1a73e8>作者：</font>** Tharindu Kumarage, Lisa Bauer, Yao Ma 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As reasoning capacity and deployment scope grow in tandem, large language models (LLMs) gain the capacity to engage in behaviors that serve their own objectives, a class of risks we term Emergent Strategic Reasoning Risks (ESRRs). These include, but are not limited to, deception (intentionally misleading users or evaluators), evaluation gaming (strategically manipulating performance during safety testing), and reward hacking (exploiting misspecified objectives). Systematically understanding and benchmarking these risks remains an open challenge. To address this gap, we introduce ESRRSim, a taxonomy-driven agentic framework for automated behavioral risk evaluation. We construct an extensible risk taxonomy of 7 categories, which is decomposed into 20 subcategories. ESRRSim generates evaluation scenarios designed to elicit faithful reasoning, paired with dual rubrics assessing both model responses and reasoning traces, in a judge-agnostic and scalable architecture. Evaluation across 11 reasoning LLMs reveals substantial variation in risk profiles (detection rates ranging 14.45%-72.72%), with dramatic generational improvements suggesting models may increasingly recognize and adapt to evaluation contexts.

---


### 19. [Where Should LoRA Go? Component-Type Placement in Hybrid Language Models](https://arxiv.org/abs/2604.22127)

**<font color=#1a73e8>作者：</font>** Hector Borobia, Elies Seguí-Mas, Guillermina Tormo-Carbó  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Hybrid language models that interleave attention with recurrent components are increasingly competitive with pure Transformers, yet standard LoRA practice applies adapters uniformly without considering the distinct functional roles of each component type. We systematically study component-type LoRA placement across two hybrid architectures -- Qwen3.5-0.8B (sequential, GatedDeltaNet + softmax attention) and Falcon-H1-0.5B (parallel, Mamba-2 SSM + attention) -- fine-tuned on three domains and evaluated on five benchmarks. We find that the attention pathway -- despite being the minority component -- consistently outperforms full-model adaptation with 5-10x fewer trainable parameters. Crucially, adapting the recurrent backbone is destructive in sequential hybrids (-14.8 pp on GSM8K) but constructive in parallel ones (+8.6 pp). We further document a transfer asymmetry: parallel hybrids exhibit positive cross-task transfer while sequential hybrids suffer catastrophic forgetting. These results establish that hybrid topology fundamentally determines adaptation response, and that component-aware LoRA placement is a necessary design dimension for hybrid architectures.

---


### 20. [SHAPE: Unifying Safety, Helpfulness and Pedagogy for Educational LLMs](https://arxiv.org/abs/2604.22134)

**<font color=#1a73e8>作者：</font>** Sihang, Zhao, Kangrui Yu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have been widely explored in educational scenarios. We identify a critical vulnerability in current educational LLMs, pedagogical jailbreaks, where students use answer-inducing prompts to elicit solutions rather than scaffolded instructions. To enable systematic study, we unify and formalize safe, helpful, and pedagogical behaviors with a knowledge-mastery graph and introduce SHAPE, a benchmark of 9,087 student-question pairs for evaluating tutoring behavior under adversarial pressure. We propose a graph-augmented tutoring pipeline that infers prerequisite concepts from queries, identifies mastery gaps, and routes generation between instructing and problem-solving via explicit gating. Experiments across multiple LLMs show that our method yields significantly improved safety under two pedagogical jailbreak settings, while maintaining near-ceiling helpfulness under the same evaluation protocol. Our code and data are available at this https URL

---


### 21. [Voice Under Revision: Large Language Models and the Normalization of Personal Narrative](https://arxiv.org/abs/2604.22142)

**<font color=#1a73e8>作者：</font>** Tom van Nuenen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This study examines how large language model rewriting alters the style and narrative texture of personal narratives. It analyzes 300 personal narratives rewritten by three frontier LLMs under three prompt conditions: generic improvement, rewrite-only, and voice-preserving revision. Change is measured across 13 linguistic markers drawn from computational stylistics, including function words, vocabulary diversity, word length, punctuation, contractions, first-person pronouns, and emotion words.
Across models and prompt conditions, LLM rewriting produces a consistent pattern of stylistic normalization. Function words, contractions, and first-person pronouns decrease, while vocabulary diversity, word length, and punctuation elaboration increase. These shifts occur whether the prompt asks the model to "improve" the text or simply to "rewrite" it. Voice-preserving prompts reduce the magnitude of the changes but do not eliminate their direction. Stylometric analysis shows that rewritten texts converge in feature space and become harder to match back to their source texts. Additional narrative markers indicate a shift from embedded to distanced narration, and from explicit causal reasoning to compressed abstraction.
The findings suggest that contemporary LLMs exert a directional pull toward a more polished, less situated register. This has consequences for digital humanities and computational text analysis, where features such as function words, pronouns, contractions, and punctuation often serve as evidence for style, voice, authorship, and corpus integrity. LLM revision should therefore be understood not merely as surface-level editing, but as a consequential form of textual mediation.

---


### 22. [When AI Speaks, Whose Values Does It Express? A Cross-Cultural Audit of Individualism-Collectivism Bias in Large Language Models](https://arxiv.org/abs/2604.22153)

**<font color=#1a73e8>作者：</font>** Pruthvinath Jeripity Venkata  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> When you ask an AI assistant for advice about your career, your marriage, or a conflict with your family, does it give you the same answer regardless of where you are from? We tested this systematically by presenting three leading AI systems (Claude Sonnet 4.5, GPT-5.4, and Gemini 2.5 Flash) with ten real-life personal dilemmas, framed for users from 10 countries across 5 continents in 7 languages (n=840 scored responses). We compared AI advice against World Values Survey Wave 7 data measuring what people in each country actually believe.
All three AI systems consistently gave Western-style, individualist advice even to users from societies that prioritize family, community, and authority, significantly more so than local values would predict (mean gap +0.76 on a 1-5 scale; t=15.65, p<0.001). The gap is largest for Nigeria (+1.85) and India (+0.82). Japan is the sole exception: AI systems treated Japanese users as more group-oriented than surveys show, revealing that AI encodes outdated stereotypes. Claude and GPT-5.4 show nearly identical bias magnitude, while Gemini is lower but still significant. The models diverge in mechanism: Claude shifts further collectivist in the user's native language; Gemini shifts more individualist; GPT-5.4 responds only to stated country identity. These findings point to a systemic homogenization of values across frontier AI. Data, code, and scoring pipeline are openly released.

---


### 23. [Reliable Self-Harm Risk Screening via Adaptive Multi-Agent LLM Systems](https://arxiv.org/abs/2604.22154)

**<font color=#1a73e8>作者：</font>** Meghana Karnam, Ananya Joshi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Emerging AI systems in behavioral health and psychiatry use multi-step or multi-agent LLM pipelines for tasks like assessing self-harm risk and screening for depression. However, common evaluation approaches, like LLM-as-a-judge, do not indicate when a decision is reliable or how errors may accumulate across multiple LLM judgements, limiting their suitability for safety-critical settings. We present a statistical framework for multi-agent pipelines structured as directed acyclic graphs (DAGs) that provides an alternative to heuristic voting with principled, adaptive decision-making. We model each agent as a stochastic categorical decision and introduce (1) tighter agent-level performance confidence bounds, (2) a bandit-based adaptive sampling strategy based on input difficulty, and (3) regret guarantees over the multi-agent system that shows logarithmic error growth when deployed. We evaluate our system on two labeled datasets in behavioral health : the AEGIS 2.0 behavioral health subset (N=161) and a stratified sample of SWMH Reddit posts (N=250). Empirically, our adaptive sampling strategy achieves the lowest false positive rate of any condition across both datasets, 0.095 on AEGIS 2.0 compared to 0.159 for single-agent models, reducing incorrect flagging of safe content by 40\% and still having similar false negative rates across all conditions. These results suggest that principled adaptive sampling offers a meaningful improvement in precision without reducing recall in this setting.

---


### 24. [Sum-of-Checks: Structured Reasoning for Surgical Safety with Large Vision-Language Models](https://arxiv.org/abs/2604.22156)

**<font color=#1a73e8>作者：</font>** Weiqiu You, Cassandra Goldberg, Amin Madani 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Purpose: Accurate assessment of the Critical View of Safety (CVS) during laparoscopic cholecystectomy is essential to prevent bile duct injury, a complication associated with significant morbidity and mortality. While large vision-language models (LVLMs) offer flexible reasoning, their predictions remain difficult to audit and unreliable on safety-critical surgical tasks.
Methods: We introduce Sum-of-Checks, a framework that decomposes each CVS criterion into expert-defined reasoning checks reflecting clinically relevant visual evidence. Given a laparoscopic frame, an LVLM evaluates each check, producing a binary judgment and justification. Criterion-level scores are computed via fixed, weighted aggregation of check outcomes. We evaluate on the Endoscapes2023 benchmark using three frontier LVLMs, comparing against direct prompting, chain-of-thought, and sub-question decomposition, each with and without few-shot examples.
Results: Sum-of-Checks improves average frame-level mean average precision by 12--14% relative to the best baseline across all three models and criteria. Analysis of individual checks reveals that LVLMs are reliable on observational checks (e.g., visibility, tool obstruction) but show substantial variability on decision-critical anatomical evidence.
Conclusion: Structuring surgical reasoning into expert-aligned verification checks improves both accuracy and transparency of LVLM-based CVS assessment, demonstrating that explicitly separating evidence elicitation from decision-making is critical for reliable and auditable surgical AI systems.
Code is available at this https URL.

---


### 25. [Fine-Grained Analysis of Shared Syntactic Mechanisms in Language Models](https://arxiv.org/abs/2604.22166)

**<font color=#1a73e8>作者：</font>** Ryoma Kumon, Hitomi Yanaka  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While language models demonstrate sophisticated syntactic capabilities, the extent to which their internal mechanisms align with cross-constructional principles studied in linguistics remains poorly understood. This study investigates whether models employ shared neural mechanisms across different syntactic constructions by applying causal interpretability methods at a granular level. Focusing on filler-gap dependencies and negative polarity item (NPI) licensing, we utilize activation patching to identify the functional roles of specific attention heads and MLP blocks. Our results reveal a highly localized and shared mechanism for filler-gap dependencies located in the early to middle layers, whereas NPI processing exhibits no such unified mechanism. Furthermore, we find that these mechanisms identified by activation patching generalize to out-of-distribution, while distributed alignment search, a supervised interpretability method, is susceptible to overfitting on narrow linguistic distributions. Finally, we validate our findings by demonstrating that the manipulation of the identified components improves model performance on acceptability judgment benchmarks.

---


### 26. [Estimating Tail Risks in Language Model Output Distributions](https://arxiv.org/abs/2604.22167)

**<font color=#1a73e8>作者：</font>** Rico Angell, Raghav Singhal, Zachary Horvitz 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Language models are increasingly capable and are being rapidly deployed on a population-level scale. As a result, the safety of these models is increasingly high-stakes. Fortunately, advances in alignment have significantly reduced the likelihood of harmful model outputs. However, when models are queried billions of times in a day, even rare worst-case behaviors will occur. Current safety evaluations focus on capturing the distribution of inputs that yield harmful outputs. These evaluations disregard the probabilistic nature of models and their tail output behavior. To measure this tail risk, we propose a method to efficiently estimate the probability of harmful outputs for any input query. Instead of naive brute-force sampling from the target model, where harmful outputs could be rare, we operationalize importance sampling by creating unsafe versions of the target model. These unsafe versions enable sample-efficient estimation by making harmful outputs more probable. On benchmarks measuring misuse and misalignment, these estimates match brute-force Monte Carlo estimates using 10-20x fewer samples. For example, we can estimate probability of harmful outputs on the order of 10^-4 with just 500 samples. Additionally, we find that these harmfulness estimates can reveal the sensitivity of models to perturbations in model input and predict deployment risks. Our work demonstrates that accurate rare-event estimation is both critical and feasible for safety evaluations. Code is available at this https URL

---


### 27. [CharTide: Data-Centric Chart-to-Code Generation via Tri-Perspective Tuning and Inquiry-Driven Evolution](https://arxiv.org/abs/2604.22192)

**<font color=#1a73e8>作者：</font>** Xiangxi Zheng, Kuang He, Jiayi Hu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Chart-to-code generation demands strict visual precision and syntactic correctness from Vision-Language Models (VLMs). However, existing approaches are fundamentally constrained by data-centric limitations: despite the availability of growing chart-to-code datasets, simply scaling homogeneous chart-code pairs conflates visual perception with program logic, preventing models from fully leveraging the richness of multimodal supervision. We present CharTide, a novel data-centric framework that systematically redesigns both training and alignment data for chart-to-code generation. First, we construct a 2M-sample dataset via a Tri-Perspective Tuning strategy, explicitly decoupling training into visual perception, pure-text code logic, and modality fusion streams, enabling a 7B model to surpass specialized baselines using only supervised data. Second, we reformulate alignment as a data verification problem rather than a heuristic scoring task. To this end, we introduce an Inquiry-Driven RL framework grounded in the principle of information invariance: a downstream model should yield consistent answers to identical visual queries across both original and generated charts. Moving beyond rigid rule matching or VLM scoring, we employ a frozen Inspector to objectively verify generated charts through atomic QA tasks, providing verifiable reward signals based on answer accuracy. Experiments on ChartMimic, Plot2Code, and ChartX show that CharTide-7B/8B significantly outperforms open-source baselines, surpasses GPT-4o, and is competitive with GPT-5.

---


### 28. [How Large Language Models Balance Internal Knowledge with User and Document Assertions](https://arxiv.org/abs/2604.22193)

**<font color=#1a73e8>作者：</font>** Shuowei Li, Haoxin Li, Wenda Chu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) often need to balance their internal parametric knowledge with external information, such as user beliefs and content from retrieved documents, in real-world scenarios like RAG or chat-based systems. A model's ability to reliably process these sources is key to system safety. Previous studies on knowledge conflict and sycophancy are limited to a binary conflict paradigm, primarily exploring conflicts between parametric knowledge and either a document or a user, but ignoring the interactive environment where all three sources exist simultaneously. To fill this gap, we propose a three-source interaction framework and systematically evaluate 27 LLMs from 3 families on 2 datasets. Our findings reveal general patterns: most models rely more on document assertions than user assertions, and this preference is reinforced by post-training. Furthermore, our behavioral analysis shows that most models are impressionable, unable to effectively discriminate between helpful and harmful external information. To address this, we demonstrate that fine-tuning on diverse source interaction data can significantly increase a model's discrimination abilities. In short, our work paves the way for developing trustworthy LLMs that can effectively and reliably integrate multiple sources of information. Code is available at this https URL.

---


### 29. [Verbal Confidence Saturation in 3-9B Open-Weight Instruction-Tuned LLMs: A Pre-Registered Psychometric Validity Screen](https://arxiv.org/abs/2604.22215)

**<font color=#1a73e8>作者：</font>** Jon-Paul Cacioli  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Verbal confidence elicitation is widely used to extract uncertainty estimates from LLMs. We tested whether seven instruction-tuned open-weight models (3-9B parameters, four families) produce verbalised confidence that meets minimal validity criteria for item-level Type-2 discrimination under minimal numeric elicitation with greedy decoding. In a pre-registered study (OSF: this http URL), 524 TriviaQA items were administered under numeric (0-100) and categorical (10-class) elicitation to eight models at Q5_K_M quantisation on consumer hardware, yielding 8,384 deterministic trials. A psychometric validity screen was applied to each model-format cell. All seven instruct models were classified Invalid on numeric confidence (H2 confirmed, 7/7 vs. predicted >=4/7), with a mean ceiling rate of 91.7% (H1 confirmed). Categorical elicitation did not rescue validity. Instead, it disrupted task performance in six of seven models, producing accuracy below 5% (H4 not confirmed). Token-level logprobability did not usefully predict verbalised confidence under the observed variance regime (H5 confirmed, mean cross-validated R^2 < 0.01). Within the reasoning-distilled model, reasoning-trace length showed a strong negative partial correlation with confidence (rho = -0.36, p < .001), consistent with the Reasoning Contamination Effect. These results do not imply that internal uncertainty representations are absent. They show that minimal verbal elicitation fails to preserve internal signals at the output interface in this model-size regime. Psychometric screening should precede any downstream use of such signals.

---


### 30. [Towards Temporal Compositional Reasoning in Long-Form Sports Videos](https://arxiv.org/abs/2604.22226)

**<font color=#1a73e8>作者：</font>** Siyu Cao, Lu Zhang, Ruizhe Zeng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Sports videos are a challenging domain for multimodal understanding because they involve complex and dynamic human activities. Despite rapid progress in Multimodal Large Language Models (MLLMs), long-horizon reasoning in sports videos remains difficult, as answering questions requires both locating temporally sparse evidence and integrating it into reasoning. We attribute this limitation to two closely coupled factors: insufficient supervision over temporally dispersed evidence, and the lack of methods that require models to identify, localize, and justify temporal evidence. To address these gaps, we introduce SportsTime, a large-scale benchmark for long-form sports video understanding, comprising 14K+ open-ended QA pairs and 50K+ step-wise temporal evidence annotations. Building on SportsTime, we propose Chain-of-Time Reasoning (CoTR), which treats reasoning as a process of temporally grounded evidence composition. Specifically, during training, CoTR introduces a temporal-reward GRPO to encourage temporally grounded reasoning. During inference, it employs an anchor-observe-infer evidence-seeking loop to iteratively localize, verify, and compose temporal evidence before producing the final answer. Experiments demonstrate the usefulness of SportsTime as a benchmark and the effectiveness of CoTR, which consistently improves temporal compositional reasoning and step-wise grounding quality over strong MLLM baselines.

---


### 31. [Tell Me Why: Designing an Explainable LLM-based Dialogue System for Student Problem Behavior Diagnosis](https://arxiv.org/abs/2604.22237)

**<font color=#1a73e8>作者：</font>** Zhilin Fan, Deliang Wang, Penghe Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Diagnosing student problem behaviors requires teachers to synthesize multifaceted information, identify behavioral categories, and plan intervention strategies. Although fine-tuned large language models (LLMs) can support this process through multi-turn dialogue, they rarely explain why a strategy is recommended, limiting transparency and teachers' trust. To address this issue, we present an explainable dialogue system built on a fine-tuned LLM. The system uses a hierarchical attribution method based on explainable AI (xAI) to identify dialogue evidence for each recommendation and generate a natural-language explanation based on that evidence. In technical evaluation, the method outperformed baseline approaches in identifying supporting evidence. In a preliminary user study with 22 pre-service teachers, participants who received explanations reported higher trust in the system. These findings suggest a promising direction for improving LLM explainability in educational dialogue systems.

---


### 32. [Towards Safe Mobility: A Unified Transportation Foundation Model enabled by Open-Ended Vision-Language Dataset](https://arxiv.org/abs/2604.22260)

**<font color=#1a73e8>作者：</font>** Wenhui Huang, Songyan Zhang, Collister Chua 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Urban transportation systems face growing safety challenges that require scalable intelligence for emerging smart mobility infrastructures. While recent advances in foundation models and large-scale multimodal datasets have strengthened perception and reasoning in intelligent transportation systems (ITS), existing research remains largely centered on microscopic autonomous driving (AD), with limited attention to city-scale traffic analysis. In particular, open-ended safety-oriented visual question answering (VQA) and corresponding foundation models for reasoning over heterogeneous roadside camera observations remain underexplored. To address this gap, we introduce the Land Transportation Dataset (LTD), a large-scale open-source vision-language dataset for open-ended reasoning in urban traffic environments. LTD contains 11.6K high-quality VQA pairs collected from heterogeneous roadside cameras, spanning diverse road geometries, traffic participants, illumination conditions, and adverse weather. The dataset integrates three complementary tasks: fine-grained multi-object grounding, multi-image camera selection, and multi-image risk analysis, requiring joint reasoning over minimally correlated views to infer hazardous objects, contributing factors, and risky road directions. To ensure annotation fidelity, we combine multi-model vision-language generation with cross-validation and human-in-the-loop refinement. Building upon LTD, we further propose UniVLT, a transportation foundation model trained via curriculum-based knowledge transfer to unify microscopic AD reasoning and macroscopic traffic analysis within a single architecture. Extensive experiments on LTD and multiple AD benchmarks demonstrate that UniVLT achieves SOTA performance on open-ended reasoning tasks across diverse domains, while exposing limitations of existing foundation models in complex multi-view traffic scenarios.

---


### 33. [Bridging the Long-Tail Gap: Robust Retrieval-Augmented Relation Completion via Multi-Stage Paraphrase Infusion](https://arxiv.org/abs/2604.22261)

**<font color=#1a73e8>作者：</font>** Fahmida Alam, Mihai Surdeanu, Ellen Riloff  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) struggle with relation completion (RC), both with and without retrieval-augmented generation (RAG), particularly when the required information is rare or sparsely represented. To address this, we propose a novel multi-stage paraphrase-guided relation-completion framework, RC-RAG, that systematically incorporates relation paraphrases across multiple stages. In particular, RC-RAG: (a) integrates paraphrases into retrieval to expand lexical coverage of the relation, (b) uses paraphrases to generate relation-aware summaries, and (c) leverages paraphrases during generation to guide reasoning for relation completion. Importantly, our method does not require any model fine-tuning. Experiments with five LLMs on two benchmark datasets show that RC-RAG consistently outperforms several RAG baselines. In long-tail settings, the best-performing LLM augmented with RC-RAG improves by 40.6 Exact Match (EM) points over its standalone performance and surpasses two strong RAG baselines by 16.0 and 13.8 EM points, respectively, while maintaining low computational overhead.

---


### 34. [Large Language Models Decide Early and Explain Later](https://arxiv.org/abs/2604.22266)

**<font color=#1a73e8>作者：</font>** Ayan Datta, Zhixue Zhao, Bhuvanesh Verma 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models often achieve strong performance by generating long intermediate chain-of-thought reasoning. However, it remains unclear when a model's final answer is actually determined during generation. If the answer is already fixed at an intermediate stage, subsequent reasoning tokens may constitute post-decision explanation, increasing inference cost and latency without improving correctness. We study the evolution of predicted answers over reasoning steps using forced answer completion, which elicits the model's intermediate predictions at partial reasoning prefixes. Focusing on Qwen3-4B and averaging results across all datasets considered, we find that predicted answers change in only 32% of queries. Moreover, once the final answer switch occurs, the model generates an average of 760 additional reasoning tokens per query, accounting for a substantial fraction of the total reasoning budget. Motivated by these findings, we investigate early stopping strategies that halt generation once the answer has stabilized. We show that simple heuristics, including probe-based stopping, can reduce reasoning token usage by 500 tokens per query while incurring only a 2% drop in accuracy. Together, our results indicate that a large portion of chain-of-thought generation is redundant and can be reduced with minimal impact on performance.

---


### 35. [How LLMs Detect and Correct Their Own Errors: The Role of Internal Confidence Signals](https://arxiv.org/abs/2604.22271)

**<font color=#1a73e8>作者：</font>** Dharshan Kumaran, Viorica Patraucean, Simon Osindero 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models can detect their own errors and sometimes correct them without external feedback, but the underlying mechanisms remain unknown. We investigate this through the lens of second-order models of confidence from decision neuroscience. In a first-order system, confidence derives from the generation signal itself and is therefore maximal for the chosen response, precluding error detection. Second-order models posit a partially independent evaluative signal that can disagree with the committed response, providing the basis for error detection. Kumaran et al. (2026) showed that LLMs cache a confidence representation at a token immediately following the answer (i.e. post-answer newline: PANL) -- that causally drives verbal confidence and dissociates from log-probabilities. Here we test whether this PANL signal extends beyond confidence to support error detection and self-correction. Here we test whether this signal supports error detection and self-correction, deriving predictions from the second-order framework. Using a verify-then-correct paradigm, we show that: (i) verbal confidence predicts error detection far beyond token log-probabilities, ruling out a first-order account; (ii) PANL activations predict error detection beyond verbal confidence itself; and (iii) PANL predicts which errors the model can correct -- where all behavioural signals fail. Causal interventions confirm that PANL signals rescue error detection behavior when answer information is corrupted. All findings replicate across models (Gemma 3 27B and Qwen 2.5 7B) and tasks (TriviaQA and MNLI). These results reveal that LLMs naturally implement a second-order confidence architecture whose internal evaluative signal encodes not only whether an answer is likely wrong but whether the model has the knowledge to fix it.

---


### 36. [When Does LLM Self-Correction Help? A Control-Theoretic Markov Diagnostic and Verify-First Intervention](https://arxiv.org/abs/2604.22273)

**<font color=#1a73e8>作者：</font>** Aofan Liu, Jingxiang Meng  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Iterative self-correction is widely used in agentic LLM systems, but when repeated refinement helps versus hurts remains unclear. We frame self-correction as a cybernetic feedback loop in which the same language model serves as both controller and plant, and use a two-state Markov model over {Correct, Incorrect} to operationalize a simple deployment diagnostic: iterate only when ECR/EIR > Acc/(1 - Acc). In this view, EIR functions as a stability margin and prompting functions as lightweight controller design. Across 7 models and 3 datasets (GSM8K, MATH, StrategyQA), we find a sharp near-zero EIR threshold (<= 0.5%) separating beneficial from harmful self-correction. Only o3-mini (+3.4 pp, EIR = 0%), Claude Opus 4.6 (+0.6 pp, EIR ~ 0.2%), and o4-mini (+/-0 pp) remain non-degrading; GPT-5 degrades by -1.8 pp. A verify-first prompt ablation provides causal evidence that this threshold is actionable through prompting alone: on GPT-4o-mini it reduces EIR from 2% to 0% and turns -6.2 pp degradation into +0.2 pp (paired McNemar p < 10^-4), while producing little change on already-sub-threshold models. ASC further illustrates the stopping trade-off: it halts harmful refinement but incurs a 3.8 pp confidence-elicitation cost. Overall, the paper argues that self-correction should be treated not as a default behavior, but as a control decision governed by measurable error dynamics.

---


### 37. [Beyond Chain-of-Thought: Rewrite as a Universal Interface for Generative Multimodal Embeddings](https://arxiv.org/abs/2604.22280)

**<font color=#1a73e8>作者：</font>** Peixi Wu, Ke Mei, Feipeng Ma 等 18 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) have emerged as a promising foundation for universal multimodal embeddings. Recent studies have shown that reasoning-driven generative multimodal embeddings can outperform discriminative embeddings on several embedding tasks. However, Chain-of-Thought (CoT) reasoning tends to generate redundant thinking steps and introduce semantic ambiguity in the summarized answers in broader retrieval scenarios. To address this limitation, we propose Rewrite-driven Multimodal Embedding (RIME), a unified framework that jointly optimizes generation and embedding through a retrieval-friendly rewrite. Meanwhile, we present the Cross-Mode Alignment (CMA) to bridge the generative and discriminative embedding spaces, enabling flexible mutual retrieval to trade off efficiency and accuracy. Based on this, we also introduce Refine Reinforcement Learning (Refine-RL) that treats discriminative embeddings as stable semantic anchors to guide the rewrite optimization. Extensive experiments on MMEB-V2, MRMR and UVRB demonstrate that RIME substantially outperforms prior generative embedding models while significantly reducing the length of thinking.

---


### 38. [STEM: Structure-Tracing Evidence Mining for Knowledge Graphs-Driven Retrieval-Augmented Generation](https://arxiv.org/abs/2604.22282)

**<font color=#1a73e8>作者：</font>** Peng Yu, En Xu, Bin Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Knowledge Graph-based Question Answering (KGQA) plays a pivotal role in complex reasoning tasks but remains constrained by two persistent challenges: the structural heterogeneity of Knowledge Graphs(KGs) often leads to semantic mismatch during retrieval, while existing reasoning path retrieval methods lack a global structural perspective. To address these issues, we propose Structure-Tracing Evidence Mining (STEM), a novel framework that reframes multi-hop reasoning as a schema-guided graph search task. First, we design a Semantic-to-Structural Projection pipeline that leverages KG structural priors to decompose queries into atomic relational assertions and construct an adaptive query schema graph. Subsequently, we execute globally-aware node anchoring and subgraph retrieval to obtain the final evidence reasoning graph from KG. To more effectively integrate global structural information during the graph construction process, we design a Triple-Dependent GNN (Triple-GNN) to generate a Global Guidance Subgraph (Guidance Graph) that guides the construction. STEM significantly improves both the accuracy and evidence completeness of multi-hop reasoning graph retrieval, and achieves State-of-the-Art performance on multiple multi-hop benchmarks.

---


### 39. [Dynamically Acquiring Text Content to Enable the Classification of Lesser-known Entities for Real-world Tasks](https://arxiv.org/abs/2604.22325)

**<font color=#1a73e8>作者：</font>** Fahmida Alam, Ellen Riloff  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Existing Natural Language Processing (NLP) resources often lack the task-specific information required for real-world problems and provide limited coverage of lesser-known or newly introduced entities. For example, business organizations and health care providers may need to be classified into a variety of different taxonomic schemes for specific application tasks. Our goal is to enable domain experts to easily create a task-specific classifier for entities by providing only entity names and gold labels as training data. Our framework then dynamically acquires descriptive text about each entity, which is subsequently used as the basis for producing a text-based classifier. We propose a novel text acquisition method that leverages both web and large language models (LLMs). We evaluate our proposed framework on two classification problems in distinct domains: (i) classifying organizations into Standard Industrial Classification (SIC) Codes, which categorize organizations based on their business activities; and (ii) classifying healthcare providers into healthcare provider taxonomy codes, which represent a provider's medical specialty and area of practice. Our best-performing model achieved macro-averaged F1-scores of 82.3% and 72.9% on the SIC code and healthcare taxonomy code classification tasks, respectively.

---


### 40. [FETS Benchmark: Foundation Models Outperform Dataset-specific Machine Learning in Energy Time Series Forecasting](https://arxiv.org/abs/2604.22328)

**<font color=#1a73e8>作者：</font>** Marco Obermeier, Marco Pruckner, Florian Haselbeck 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Driven by the transition towards a climate-neutral energy system, accurate energy time series forecasting is critical for planning and operation. Yet, it remains largely a dataset-specific task, requiring comprehensive training data, limiting scalability, and resulting in high model development and maintenance effort. Recently, foundation models that aim to learn generalizable patterns via extensive pretraining have shown superior performance in multiple prediction tasks. Despite their success and strong potential to address challenges in energy forecasting, their application in this domain remains largely unexplored. We address this gap by presenting the Foundation Models in Energy Time Series Forecasting (FETS) benchmark. We (1) provide a structured overview of energy forecasting use cases along three main dimensions: stakeholders, attributes, and data categories; (2) collect and analyze 54 datasets across 9 data categories, guided by typical stakeholder interests; (3) benchmark foundation models against classical machine learning approaches across different forecasting settings. Foundation models consistently outperform dataset-specific optimized machine learning approaches across all settings and data categories, despite the latter having seen the full historic target data during training. In particular, covariate-informed foundation models achieve the strongest performance. Further analysis reveals a strong correlation between predictive performance and spectral entropy, performance saturation beyond a certain context length, and improved performance at higher aggregation levels such as national load, district heating, and power grid data. Overall, our findings highlight the strong potential of foundation models as scalable and generalizable forecasting solutions for the energy domain, particularly in data-constrained and privacy-sensitive settings.

---


### 41. [Preference Heads in Large Language Models: A Mechanistic Framework for Interpretable Personalization](https://arxiv.org/abs/2604.22345)

**<font color=#1a73e8>作者：</font>** Weixu Zhang, Ye Yuan, Changjiang Han 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) exhibit strong implicit personalization ability, yet most existing approaches treat this behavior as a black box, relying on prompt engineering or fine tuning on user data. In this work, we adopt a mechanistic interpretability perspective and hypothesize the existence of a sparse set of Preference Heads, attention heads that encode user specific stylistic and topical preferences and exert a causal influence on generation. We introduce Differential Preference Steering (DPS), a training free framework that (1) identifies Preference Heads through causal masking analysis and (2) leverages them for controllable and interpretable personalization at inference time. DPS computes a Preference Contribution Score (PCS) for each attention head, directly measuring its causal impact on user aligned outputs. During decoding, we contrast model predictions with and without Preference Heads, amplifying the difference between personalized and generic logits to selectively strengthen preference aligned continuations. Experiments on widely used personalization benchmarks across multiple LLMs demonstrate consistent gains in personalization fidelity while preserving content coherence and low computational overhead. Beyond empirical improvements, DPS provides a mechanistic explanation of where and how personalization emerges within transformer architectures. Our implementation is publicly available.

---


### 42. [A Nationwide Japanese Medical Claims Foundation Model: Balancing Model Scaling and Task-Specific Computational Efficiency](https://arxiv.org/abs/2604.22348)

**<font color=#1a73e8>作者：</font>** Nanae Aratake, Taisei Tosaki, Yuji Okamoto 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Clinical risk prediction using longitudinal medical data supports individualized care. Self-supervised foundation models have emerged as a promising approach for leveraging large-scale unlabeled healthcare records. In natural language processing, scaling laws suggest that larger models achieve predictably lower pretraining losses, supporting the foundation model paradigm. However, for structured medical data, characterized by a limited vocabulary and sparse observations, whether increasing model size consistently improves downstream predictions is unclear, as most studies evaluate only a single model scale. In this study, we evaluated the relationship between model scale and downstream task performance for structured medical foundation models. Using a random sample (2.3 million patients, 32 hospitals) from a nationwide 519-hospital Japanese claims database, we pretrained encoder-only Transformers at five scales (2.2M-101M parameters) for disease incidence and medication prediction. Downstream performance saturated at task-dependent thresholds: disease prediction benefited from larger models (32M-101M), whereas medication prediction saturated at 11M, reducing pretraining time by 178 h. Across all tasks, the best-performing model consistently outperformed a Light Gradient Boosting Machine baseline in the area under the precision-recall curve. These findings indicate that, unlike the monotonically decreasing pretraining loss, the optimal model size varied depending on task characteristics. This task-dependent saturation provides practical guidance for balancing predictive performance and computational cost in structured medical foundation models.

---


### 43. [Large Language Model Counterarguments in Older Adults: Cognitive Offloading or Vulnerability to Moral Persuasion?](https://arxiv.org/abs/2604.22356)

**<font color=#1a73e8>作者：</font>** Kou Tamura, Sayaka Ishibashi, Ayana Goma 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> This study examined whether counterarguments generated by large language models (LLMs) influence the moral judgments of younger and older adults and whether these effects vary as a function of dilemma type, cognitive functioning, trust in AI, and prior experience using LLMs. Using the switch and footbridge trolley dilemmas, 130 participants (56 younger adults and 74 older adults) were presented with ChatGPT arguments that opposed their initial judgments. Results revealed that more than 30% of participants reversed their moral judgments in both dilemmas (32.31% in the switch dilemma and 36.92% in the footbridge dilemma), suggesting that LLMs possess substantial persuasive power. Older adults tended to be more likely than younger adults to reverse their judgments, and they showed a significantly greater degree of judgment change in the switch dilemma. Notably, in the emotionally aversive footbridge dilemma, older adults with lower cognitive functioning were significantly more likely to align with the LLM-generated counterargument. General trust in AI and prior experience with LLMs did not predict judgment reversal, supporting a disconnect between trust and persuasion. Instead, individual factors such as lower initial confidence and higher perceived task difficulty were associated with greater susceptibility to AI influence. These findings suggest that, although LLMs may serve as tools for cognitive offloading that compensate for age-related cognitive decline, they may also pose a risk of undue persuasion for cognitively vulnerable individuals.

---


### 44. [Revisiting Neural Activation Coverage for Uncertainty Estimation](https://arxiv.org/abs/2604.22360)

**<font color=#1a73e8>作者：</font>** Benedikt Franke, Nils Förster, Frank Köster 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural activation coverage (NAC) is a recently-proposed technique for out-of-distribution detection and generalization. We build upon this promising foundation and extend the method to work as an uncertainty estimation technique for already-trained artificial neural networks in the domain of regression. Our experiments confirm NAC uncertainty scores to be more meaningful than other techniques, e.g. Monte-Carlo Dropout.

---


### 45. [CNSL-bench: Benchmarking the Sign Language Understanding Capabilities of MLLMs on Chinese National Sign Language](https://arxiv.org/abs/2604.22367)

**<font color=#1a73e8>作者：</font>** Rui Zhao, Xuewen Zhong, Xiaoyun Zheng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Sign language research has achieved significant progress due to the advances in large language models (LLMs). However, the intrinsic ability of LLMs to understand sign language, especially in multimodal contexts, remains underexplored. To address this limitation, we introduce CNSL-bench, the first comprehensive Chinese em{National Sign Language benchmark designed for evaluating multimodal large language models (MLLMs) in sign language understanding. The proposed CNSL-bench is characterized by: 1) Authoritative grounding, as it is anchored to the officially standardized \textit{National Common Sign Language Dictionary, mitigating ambiguity from regional or non-canonical variants and ensuring consistent semantic definitions; 2) Multimodal coverage, providing aligned textual descriptions, illustrative images, and sign language videos; and 3) Articulatory diversity, supporting fine-grained analysis across key manual articulatory forms, including air-writing, finger-spelling, and the Chinese manual-alphabet. Using CNSL-bench, we extensively evaluate 21 open-source and proprietary up-to-date MLLMs. Our results reveal that, despite recent advances in multimodal modeling, current MLLMs remain substantially inferior to human performance, exhibiting systematic disparities across input modalities and manual articulatory forms. Additional diagnostic analyses suggest that several performance limitations persist beyond improvements in reasoning and that instruction-following robustness varies substantially across models.

---


### 46. [SpaMEM: Benchmarking Dynamic Spatial Reasoning via Perception-Memory Integration in Embodied Environments](https://arxiv.org/abs/2604.22409)

**<font color=#1a73e8>作者：</font>** Chih-Ting Liao, Xi Xiao, Chunlei Meng 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) have advanced static visual--spatial reasoning, yet they often fail to preserve long-horizon spatial coherence in embodied settings where beliefs must be continuously revised from egocentric observations under environmental change. We introduce SpaMEM (Spatial Memory from Action Sequences), a large-scale diagnostic benchmark that isolates the mechanics of spatial belief evolution via action-conditioned scene transformations (spawn, place, remove) over long interaction horizons. SpaMEM is built on a physically grounded dataset with 10,601,392 high-fidelity images across four modalities (RGB, depth, instance, semantic segmentation), collected from 25,000+ interaction sequences in 1,000 procedurally generated houses. We formalize embodied spatial reasoning as a three-level hierarchy with 15 diagnostic tasks: Level 1 measures atomic spatial perception from single observations; Level 2 probes temporal reasoning with oracle textual state histories to factor out perceptual noise; and Level 3 requires end-to-end belief maintenance from raw visual streams under the same task dimensions. We further evaluate both short-term (step-wise) updates and long-term (episodic) reconstruction. Benchmarking representative open-source VLM families reveals a consistent stacked bottleneck: coordinate-consistent grounding remains a hard ceiling, and the sharp collapse from Level 2 to Level 3 exposes a pronounced symbolic scaffolding dependency, where models succeed with text-based bookkeeping but struggle to sustain robust visual memory. SpaMEM provides a granular diagnostic standard and motivates explicit mechanisms for state representation, belief revision, and long-horizon episodic integration.

---


### 47. [Introducing Background Temperature to Characterise Hidden Randomness in Large Language Models](https://arxiv.org/abs/2604.22411)

**<font color=#1a73e8>作者：</font>** Alberto Messina, Stefano Scotta  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Even when decoding with temperature $T=0$, large language models (LLMs) can produce divergent outputs for identical inputs. Recent work by Thinking Machines Lab highlights implementation-level sources of nondeterminism, including batch-size variation, kernel non-invariance, and floating-point non-associativity. In this short note we formalize this behavior by introducing the notion of \emph{background temperature} $T_{\mathrm{bg}}$, the effective temperature induced by an implementation-dependent perturbation process observed even when nominal $T=0$. We provide clean definitions, show how $T_{\mathrm{bg}}$ relates to a stochastic perturbation governed by the inference environment $I$, and propose an empirical protocol to estimate $T_{bg}$ via the equivalent temperature $T_n(I)$ of an ideal reference system. We conclude with a set of pilot experiments run on a representative pool from the major LLM providers that demonstrate the idea and outline implications for reproducibility, evaluation, and deployment.

---


### 48. [CGC: Compositional Grounded Contrast for Fine-Grained Multi-Image Understanding](https://arxiv.org/abs/2604.22498)

**<font color=#1a73e8>作者：</font>** Lihao Zheng, Zhenwei Shao, Yu Zhou 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Although Multimodal Large Language Models (MLLMs) have advanced rapidly, they still face notable challenges in fine-grained multi-image understanding, often exhibiting spatial hallucination, attention leakage, and failures in object constancy. In addition, existing approaches typically rely on expensive human annotations or large-scale chain-of-thought (CoT) data generation. We propose Compositional Grounded Contrast (abbr. CGC), a low-cost full framework for boosting fine-grained multi-image understanding of MLLMs. Built on existing single-image grounding annotations, CGC constructs compositional multi-image training instances through Inter-Image Contrast and Intra-Image Contrast, which introduce semantically decoupled distractor contexts for cross-image discrimination and correlated cross-view samples for object constancy, respectively. CGC further introduces a Rule-Based Spatial Reward within the GRPO framework to improve source-image attribution, spatial alignment, and structured output validity under a Think-before-Grounding paradigm. Experiments show that CGC achieves state-of-the-art results on fine-grained multi-image benchmarks, including MIG-Bench and VLM2-Bench. The learned multi-image understanding capability also transfers to broader multimodal understanding and reasoning tasks, yielding consistent gains over the Qwen3-VL-8B base model on MathVista (+2.90), MuirBench (+2.88), MMStar (+1.93), MMMU (+1.77), and BLINK (+1.69).

---


### 49. [RouteLMT: Learned Sample Routing for Hybrid LLM Translation Deployment](https://arxiv.org/abs/2604.22520)

**<font color=#1a73e8>作者：</font>** Yingfeng Luo, Hongyu Liu, Dingyang Lin 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have achieved remarkable performance in Machine Translation (MT), but deploying them at scale remains prohibitively expensive. A widely adopted remedy is the hybrid system paradigm, which balances cost and quality by serving most requests with a small model and selectively routing a fraction to a large model. However, existing routing strategies often rely on heuristics, external predictors, or absolute quality estimation, which fail to capture whether the large model actually provides a worthwhile improvement over the small one. In this paper, we formulate routing as a budget allocation problem and identify marginal gain, i.e., the large model's improvement over the small model, as the optimal signal for budgeted decisions. Building on this, we propose \textbf{RouteLMT} (routing for LLM-based MT), an efficient in-model router that predicts this expected gain by probing the small translators prompt-token representation, without requiring external models or hypothesis decoding. Extensive experiments demonstrate that our RouteLMT outperforms heuristics, quality/difficulty estimation baselines, achieving a superior quality-budget Pareto frontier. Furthermore, we analyze regression risks and show that a simple guarded variant can mitigate severe quality losses.

---


### 50. [FeatEHR-LLM: Leveraging Large Language Models for Feature Engineering in Electronic Health Records](https://arxiv.org/abs/2604.22534)

**<font color=#1a73e8>作者：</font>** Hojjat Karami, David Atienza, Jean-Philippe Thiran 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Feature engineering for Electronic Health Records (EHR) is complicated by irregular observation intervals, variable measurement frequencies, and structural sparsity inherent to clinical time series. Existing automated methods either lack clinical domain awareness or assume clean, regularly sampled inputs, limiting their applicability to real-world EHR data. We present \textbf{FeatEHR-LLM}, a framework that leverages Large Language Models (LLMs) to generate clinically meaningful tabular features from irregularly sampled EHR time series. To limit patient privacy exposure, the LLM operates exclusively on dataset schemas and task descriptions rather than raw patient records. A tool-augmented generation mechanism equips the LLM with specialized routines for querying irregular temporal data, enabling it to produce executable feature-extraction code that explicitly handles uneven observation patterns and informative sparsity. FeatEHR-LLM supports both univariate and multivariate feature generation through an iterative, validation-in-the-loop pipeline. Evaluated on eight clinical prediction tasks across four ICU datasets, our framework achieves the highest mean AUROC on 7 out of 8 tasks, with improvements of up to 6 percentage points over strong baselines. Code is available at this http URL.

---


> [!TIP]
> 当前位于：**1-50**（第 1/2 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-63](./part-02.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
