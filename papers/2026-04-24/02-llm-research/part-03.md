# 🧠 大模型相关研究 | 2026年04月24日

> 本类共 **129** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**101-129**（第 3/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-129**

---

### 101. [Where Reasoning Breaks: Logic-Aware Path Selection by Controlling Logical Connectives in LLMs Reasoning Chains](https://arxiv.org/abs/2604.20564)

**<font color=#1a73e8>作者：</font>** Seunghyun Park, Yuanyuan Lei  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While LLMs demonstrate impressive reasoning capabilities, they remain fragile in multi-step logical deduction, where a single transition error can propagate through the entire reasoning chain, leading to unstable performance. In this work, we identify logical connectives as primary points of this structural fragility. Through empirical analysis, we show that connective tokens function as high entropy forking points, at which models frequently struggle to determine the correct logical direction. Motivated by this observation, we hypothesize that intervening in logical connective selection can guide LLMs toward more correct logical direction, thereby improving the overall reasoning chain. To validate this hypothesis, we propose a multi-layered framework that intervenes specifically at these logic-critical junctions in the reasoning process. Our framework includes (1) Gradient-based Logical Steering to guide LLMs internal representations towards valid reasoning subspaces, (2) Localized Branching to resolve ambiguity via targeted look-ahead search, and (3) Targeted Transition Preference Optimization, a surgical reinforcement learning objective that selectively optimizes single-token preferences at logical pivots. Crucially, by concentrating intervention solely on logic-critical transitions, our framework achieves a favorable accuracy--efficiency trade-off compared to global inference time scaling methods like beam search and self-consistency.

---


### 102. [The Effect of Idea Elaboration on the Automatic Assessment of Idea Originality](https://arxiv.org/abs/2604.20569)

**<font color=#1a73e8>作者：</font>** Umberto Domanti, Moritz Mock, Sergio Agnoli 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Automatic systems are increasingly used to assess the originality of responses in creative tasks. They offer a potential solution to key limitations of human assessment (cost, fatigue, and subjectivity), but there is preliminary evidence of a self-preference bias. Accordingly, automatic systems tend to prefer outcomes that are more closely related to their style, rather than to the human one. In this paper, we investigated how Large Language Models (LLMs) align with human raters in assessing the originality of responses in a divergent thinking task. We analysed 4,813 responses to the Alternate Uses Task produced by higher and lower creative humans and ChatGPT-4o. Human raters were two university students who underwent intensive training. Machine raters were two specialised systems fine-tuned on AUT responses and corresponding human ratings (OCSAI and CLAUS) and ChatGPT-4o, which was prompted with the same instructions as human raters. Results confirmed the presence of a self-preference bias in LLMs. Automatic systems tended to privilege artificial responses. However, this self-preference bias disappeared when the analyses controlled for the idea elaboration. We discuss theoretical and methodological implications of these findings by highlighting future directions for research on creativity assessment.

---


### 103. [Exploring Spatial Intelligence from a Generative Perspective](https://arxiv.org/abs/2604.20570)

**<font color=#1a73e8>作者：</font>** Muzhi Zhu, Shunyao Jiang, Huanyi Zheng 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Spatial intelligence is essential for multimodal large language models, yet current benchmarks largely assess it only from an understanding perspective. We ask whether modern generative or unified multimodal models also possess generative spatial intelligence (GSI), the ability to respect and manipulate 3D spatial constraints during image generation, and whether such capability can be measured or improved. We introduce GSI-Bench, the first benchmark designed to quantify GSI through spatially grounded image editing. It consists of two complementary components: GSI-Real, a high-quality real-world dataset built via a 3D-prior-guided generation and filtering pipeline, and GSI-Syn, a large-scale synthetic benchmark with controllable spatial operations and fully automated labeling. Together with a unified evaluation protocol, GSI-Bench enables scalable, model-agnostic assessment of spatial compliance and editing fidelity. Experiments show that fine-tuning unified multimodal models on GSI-Syn yields substantial gains on both synthetic and real tasks and, strikingly, also improves downstream spatial understanding. This provides the first clear evidence that generative training can tangibly strengthen spatial reasoning, establishing a new pathway for advancing spatial intelligence in multimodal models.

---


### 104. [Trust, Lies, and Long Memories: Emergent Social Dynamics and Reputation in Multi-Round Avalon with LLM Agents](https://arxiv.org/abs/2604.20582)

**<font color=#1a73e8>作者：</font>** Suveen Ellawela  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> We study emergent social dynamics in LLM agents playing The Resistance: Avalon, a hidden-role deception game. Unlike prior work on single-game performance, our agents play repeated games while retaining memory of previous interactions, including who played which roles and how they behaved, enabling us to study how social dynamics evolve. Across 188 games, two key phenomena emerge. First, reputation dynamics emerge organically when agents retain cross-game memory: agents reference past behavior in statements like "I am wary of repeating last game's mistake of over-trusting early success." These reputations are role-conditional: the same agent is described as "straightforward" when playing good but "subtle" when playing evil, and high-reputation players receive 46% more team inclusions. Second, higher reasoning effort supports more strategic deception: evil players more often pass early missions to build trust before sabotaging later ones, 75% in high-effort games vs 36% in low-effort games. Together, these findings show that repeated interaction with memory gives rise to measurable reputation and deception dynamics among LLM agents.

---


### 105. [CHORUS: An Agentic Framework for Generating Realistic Deliberation Data](https://arxiv.org/abs/2604.20651)

**<font color=#1a73e8>作者：</font>** A. Koursaris, G. Domalis, A. Apostolopoulou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Understanding the intricate dynamics of online discourse depends on large-scale deliberation data, a resource that remains scarce across interactive web platforms due to restrictive accessibility policies, ethical concerns and inconsistent data quality. In this paper, we propose Chorus, an agentic framework, which orchestrates LLM-powered actors with behaviorally consistent personas to generate realistic deliberation discussions. Each actor is governed by an autonomous agent equipped with memory of the evolving discussion, while participation timing is governed by a principled Poisson process-based temporal model, which approximates the heterogeneous engagement patterns of real users. The framework is further supported by structured tool usage, enabling actors to access external resources and facilitating integration with interactive web platforms. The framework was deployed on the \textsc{Deliberate} platform and evaluated by 30 expert participants across three dimensions: content realism, discussion coherence and analytical utility, confirming Chorus as a practical tool for generating high-quality deliberation data suitable for online discourse analysis

---


### 106. [Large Language Models Outperform Humans in Fraud Detection and Resistance to Motivated Investor Pressure](https://arxiv.org/abs/2604.20652)

**<font color=#1a73e8>作者：</font>** Nattavudh Powdthavee  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models trained on human feedback may suppress fraud warnings when investors arrive already persuaded of a fraudulent opportunity. We tested this in a preregistered experiment across seven leading LLMs and twelve investment scenarios covering legitimate, high-risk, and objectively fraudulent opportunities, combining 3,360 AI advisory conversations with a 1,201-participant human benchmark. Contrary to predictions, motivated investor framing did not suppress AI fraud warnings; if anything, it marginally increased them. Endorsement reversal occurred in fewer than 3 in 1,000 observations. Human advisors endorsed fraudulent investments at baseline rates of 13-14%, versus 0% across all LLMs, and suppressed warnings under pressure at two to four times the AI rate. AI systems currently provide more consistent fraud warnings than lay humans in an identical advisory role.

---


### 107. [Cooperative Profiles Predict Multi-Agent LLM Team Performance in AI for Science Workflows](https://arxiv.org/abs/2604.20658)

**<font color=#1a73e8>作者：</font>** Shivani Kumar, Adarsh Bharathwaj, David Jurgens  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multi-agent systems built from teams of large language models (LLMs) are increasingly deployed for collaborative scientific reasoning and problem-solving. These systems require agents to coordinate under shared constraints, such as GPUs or credit balances, where cooperative behavior matters. Behavioral economics provides a rich toolkit of games that isolate distinct cooperation mechanisms, yet it remains unknown whether a model's behavior in these stylized settings predicts its performance in realistic collaborative tasks. Here, we benchmark 35 open-weight LLMs across six behavioral economics games and show that game-derived cooperative profiles robustly predict downstream performance in AI-for-Science tasks, where teams of LLM agents collaboratively analyze data, build models, and produce scientific reports under shared budget constraints. Models that effectively coordinate games and invest in multiplicative team production (rather than greedy strategies) produce better scientific reports across three outcomes, accuracy, quality, and completion. These associations hold after controlling for multiple factors, indicating that cooperative disposition is a distinct, measurable property of LLMs not reducible to general ability. Our behavioral games framework thus offers a fast and inexpensive diagnostic for screening cooperative fitness before costly multi-agent deployment.

---


### 108. [GRPO-VPS: Enhancing Group Relative Policy Optimization with Verifiable Process Supervision for Effective Reasoning](https://arxiv.org/abs/2604.20659)

**<font color=#1a73e8>作者：</font>** Jingyi Wang, Lei Zhu, Tengjin Weng 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement Learning with Verifiable Rewards (RLVR) has advanced the reasoning capabilities of Large Language Models (LLMs) by leveraging direct outcome verification instead of learned reward models. Building on this paradigm, Group Relative Policy Optimization (GRPO) eliminates the need for critic models but suffers from indiscriminate credit assignment for intermediate steps, which limits its ability to identify effective reasoning strategies and incurs overthinking. In this work, we introduce a model-free and verifiable process supervision via probing the model's belief in the correct answer throughout its reasoning trajectory. By segmenting the generation into discrete steps and tracking the conditional probability of the correct answer appended at each segment boundary, we efficiently compute interpretable segment-wise progress measurements to refine GRPO's trajectory-level feedback. This approach enables more targeted and sample-efficient policy updates, while avoiding the need for intermediate supervision derived from costly Monte Carlo rollouts or auxiliary models. Experiments on mathematical and general-domain benchmarks show consistent gains over GRPO across diverse models: up to 2.6-point accuracy improvements and 13.7% reasoning-length reductions on math tasks, and up to 2.4 points and 4% on general-domain tasks, demonstrating strong generalization.

---


### 109. [The Expense of Seeing: Attaining Trustworthy Multimodal Reasoning Within the Monolithic Paradigm](https://arxiv.org/abs/2604.20665)

**<font color=#1a73e8>作者：</font>** Karan Goyal, Dikshant Kukreja  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The rapid proliferation of Vision-Language Models (VLMs) is widely celebrated as the dawn of unified multimodal knowledge discovery but its foundation operates on a dangerous, unquestioned axiom: that current VLMs faithfully synthesise multimodal data. We argue they do not. Instead, a profound crisis of trustworthiness underlies the dominant Vision Encoder-Projector-LLM paradigm. Rather than extracting grounded knowledge from visual inputs, state-of-the-art models frequently exhibit functional blindness, i.e., exploiting strong language priors to bypass severe visual representation bottlenecks. In this work, we challenge the conventional methodology of multimodal evaluation, which relies on data ablation or new dataset creation and therefore fatally conflates dataset biases with architectural incapacity. We propose a radical, information-theoretic departure: the Modality Translation Protocol, designed to quantifiably unmask the Expense of Seeing. By translating semantic payloads rather than ablating them, we formulate three novel metrics -- the Toll (ToS), Curse (CoS), and Fallacy (FoS) of Seeing -- culminating in the Semantic Sufficiency Criterion (SSC). Furthermore, we posit a provocative Divergence Law of Multimodal Scaling, hypothesising that as the underlying language engines scale to unprecedented reasoning capabilities, the mathematical penalty of the visual knowledge bottleneck paradoxically increases. We challenge the KDD community to abandon the illusory pursuit of "multimodal gain". By elevating the SSC from a passive diagnostic constraint to an active architectural blueprint, we provide the rigorous, trustworthy foundation required to force the next generation of AI systems to truly see the data, achieving true multimodal reasoning.

---


### 110. [Intersectional Fairness in Large Language Models](https://arxiv.org/abs/2604.20677)

**<font color=#1a73e8>作者：</font>** Chaima Boufaied, Ronnie De Souza Santos, Ann Barcomb  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are increasingly deployed in socially sensitive settings, raising concerns about fairness and biases, particularly across intersectional demographic attributes. In this paper, we systematically evaluate intersectional fairness in six LLMs using ambiguous and disambiguated contexts from two benchmark datasets. We assess LLM behavior using bias scores, subgroup fairness metrics, accuracy, and consistency through multi-run analysis across contexts and negative and non-negative question polarities. Our results show that while modern LLMs generally perform well in ambiguous contexts, this limits the informativeness of fairness metrics due to sparse non-unknown predictions. In disambiguated contexts, LLM accuracy is influenced by stereotype alignment, with models being more accurate when the correct answer reinforces a stereotype than when it contradicts it. This pattern is especially pronounced in race-gender intersections, where directional bias toward stereotypes is stronger. Subgroup fairness metrics further indicate that, despite low observed disparity in some cases, outcome distributions remain uneven across intersectional groups. Across repeated runs, responses also vary in consistency, including stereotype-aligned responses. Overall, our findings show that apparent model competence is partly associated with stereotype-consistent cues, and no evaluated LLM achieves consistently reliable or fair behavior across intersectional settings. These findings highlight the need for evaluation beyond accuracy, emphasizing the importance of combining bias, subgroup fairness, and consistency metrics across intersectional groups, contexts, and repeated runs.

---


### 111. [MGDA-Decoupled: Geometry-Aware Multi-Objective Optimisation for DPO-based LLM Alignment](https://arxiv.org/abs/2604.20685)

**<font color=#1a73e8>作者：</font>** Andor Vári-Kakas, Ji Won Park, Natasa Tagasovska  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Aligning large language models (LLMs) to desirable human values requires balancing multiple, potentially conflicting objectives such as helpfulness, truthfulness, and harmlessness, which presents a multi-objective optimisation challenge. Most alignment pipelines rely on a fixed scalarisation of these objectives, which can introduce procedural unfairness by systematically under-weighting harder-to-optimise or minority objectives. To promote more equitable trade-offs, we introduce MGDA-Decoupled, a geometry-based multi-objective optimisation algorithm that finds a shared descent direction while explicitly accounting for each objective's convergence dynamics. In contrast to prior methods that depend on reinforcement learning (e.g., GAPO) or explicit reward models (e.g., MODPO), our approach operates entirely within the lightweight Direct Preference Optimisation (DPO) paradigm. Experiments on the UltraFeedback dataset show that geometry-aware methods -- and MGDA-Decoupled in particular -- achieve the highest win rates against golden responses, both overall and per objective.

---


### 112. [R-CoV: Region-Aware Chain-of-Verification for Alleviating Object Hallucinations in LVLMs](https://arxiv.org/abs/2604.20696)

**<font color=#1a73e8>作者：</font>** Jiahao Xie, Alessio Tonioni, Nathalie Rauschmayr 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large vision-language models (LVLMs) have demonstrated impressive performance in various multimodal understanding and reasoning tasks. However, they still struggle with object hallucinations, i.e., the claim of nonexistent objects in the visual input. To address this challenge, we propose Region-aware Chain-of-Verification (R-CoV), a visual chain-of-verification method to alleviate object hallucinations in LVLMs in a post-hoc manner. Motivated by how humans comprehend intricate visual information -- often focusing on specific image regions or details within a given sample -- we elicit such region-level processing from LVLMs themselves and use it as a chaining cue to detect and alleviate their own object hallucinations. Specifically, our R-CoV consists of six steps: initial response generation, entity extraction, coordinate generation, region description, verification execution, and final response generation. As a simple yet effective method, R-CoV can be seamlessly integrated into various LVLMs in a training-free manner and without relying on external detection models. Extensive experiments on several widely used hallucination benchmarks across multiple LVLMs demonstrate that R-CoV can significantly alleviate object hallucinations in LVLMs. Project page: this https URL.

---


### 113. [SSL-R1: Self-Supervised Visual Reinforcement Post-Training for Multimodal Large Language Models](https://arxiv.org/abs/2604.20705)

**<font color=#1a73e8>作者：</font>** Jiahao Xie, Alessio Tonioni, Nathalie Rauschmayr 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) with verifiable rewards (RLVR) has demonstrated the great potential of enhancing the reasoning abilities in multimodal large language models (MLLMs). However, the reliance on language-centric priors and expensive manual annotations prevents MLLMs' intrinsic visual understanding and scalable reward designs. In this work, we introduce SSL-R1, a generic self-supervised RL framework that derives verifiable rewards directly from images. To this end, we revisit self-supervised learning (SSL) in visual domains and reformulate widely-used SSL tasks into a set of verifiable visual puzzles for RL post-training, requiring neither human nor external model supervision. Training MLLMs on these tasks substantially improves their performance on multimodal understanding and reasoning benchmarks, highlighting the potential of leveraging vision-centric self-supervised tasks for MLLM post-training. We think this work will provide useful experience in devising effective self-supervised verifiable rewards to enable RL at scale. Project page: this https URL.

---


### 114. [COMPASS: COntinual Multilingual PEFT with Adaptive Semantic Sampling](https://arxiv.org/abs/2604.20720)

**<font color=#1a73e8>作者：</font>** Noah Flynn  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) often exhibit performance disparities across languages, with naive multilingual fine-tuning frequently degrading performance due to negative cross-lingual interference. To address this, we introduce COMPASS (COntinual Multilingual PEFT with Adaptive Semantic Sampling), a novel data-centric framework for adapting LLMs to target languages. COMPASS leverages parameter-efficient fine-tuning (PEFT) by training lightweight, language-specific adapters on a judiciously selected subset of auxiliary multilingual data. The core of our method is a distribution-aware sampling strategy that uses multilingual embeddings and clustering to identify semantic gaps between existing training data and a target usage distribution. By prioritizing auxiliary data from under-represented semantic clusters, COMPASS maximizes positive cross-lingual transfer while minimizing interference. We extend this into a continual learning framework, COMPASS-ECDA, which monitors for data distribution shifts in production and dynamically updates adapters to prevent model staleness, balancing adaptation to new data with the preservation of existing knowledge. Across three different model architectures (Phi-4-Mini, Llama-3.1-8B, and Qwen2.5-7B) and multiple challenging multilingual benchmarks (Global-MMLU, MMLU-ProX), including unseen long-context tasks (OneRuler), we demonstrate that COMPASS consistently outperforms baseline methods guided by linguistic similarity, providing an effective, efficient, and sustainable solution for developing and maintaining high-performing multilingual models in dynamic environments.

---


### 115. [Exploiting LLM-as-a-Judge Disposition on Free Text Legal QA via Prompt Optimization](https://arxiv.org/abs/2604.20726)

**<font color=#1a73e8>作者：</font>** Mohamed Hesham Elganayni, Runsheng Chen, Sebastian Nagl 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This work explores the role of prompt design and judge selection in LLM-as-a-Judge evaluations of free text legal question answering. We examine whether automatic task prompt optimization improves over human-centered design, whether optimization effectiveness varies by judge feedback style, and whether optimized prompts transfer across judges. We systematically address these questions on the LEXam benchmark by optimizing task prompts using the ProTeGi method with feedback from two judges (Qwen3-32B, DeepSeek-V3) across four task models, and then testing cross-judge transfer. Automatic optimization consistently outperforms the baseline, with lenient judge feedback yielding higher and more consistent gains than strict judge feedback. Prompts optimized with lenient feedback transfer better to strict judges than the reverse direction. Analysis reveals that lenient judges provide permissive feedback, yielding prompts with broader applicability, whereas strict judges produce restrictive feedback, leading to judge-specific overfitting. Our findings demonstrate algorithmically optimizing prompts on training data can outperform human-centered prompt design and that judges' dispositions during optimization shape prompt generalizability. Code and optimized prompts are available at this https URL.

---


### 116. [Supplement Generation Training for Enhancing Agentic Task Performance](https://arxiv.org/abs/2604.20727)

**<font color=#1a73e8>作者：</font>** Young Min Cho, Daniele Bonadiman, Divya Bhargavi 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Training large foundation models for agentic tasks is increasingly impractical due to the high computational costs, long iteration cycles, and rapid obsolescence as new models are continuously released. Instead of post-training massive models for every new task or domain, we propose Supplement Generation Training (SGT), a more efficient and sustainable strategy. SGT trains a smaller LLM to generate useful supplemental text that, when appended to the original input, helps the larger LLM solve the task more effectively. These lightweight models can dynamically adapt supplements to task requirements, improving performance without modifying the underlying large models. This approach decouples task-specific optimization from large foundation models and enables more flexible, cost-effective deployment of LLM-powered agents in real-world applications.

---


### 117. [Render-in-the-Loop: Vector Graphics Generation via Visual Self-Feedback](https://arxiv.org/abs/2604.20730)

**<font color=#1a73e8>作者：</font>** Guotao Liang, Zhangcheng Wang, Juncheng Hu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) have shown promising capabilities in generating Scalable Vector Graphics (SVG) via direct code synthesis. However, existing paradigms typically adopt an open-loop "blind drawing" approach, where models generate symbolic code sequences without perceiving intermediate visual outcomes. This methodology severely underutilizes the powerful visual priors embedded in MLLMs vision encoders, treating SVG generation as a disjointed textual sequence modeling task rather than an integrated visuo-spatial one. Consequently, models struggle to reason about partial canvas states and implicit occlusion relationships, which are visually explicit but textually ambiguous. To bridge this gap, we propose Render-in-the-Loop, a novel generation paradigm that reformulates SVG synthesis as a step-wise, visual-context-aware process. By rendering intermediate code states into a cumulative canvas, the model explicitly observes the evolving visual context at each step, leveraging on-the-fly feedback to guide subsequent generation. However, we demonstrate that applying this visual loop naively to off-the-shelf models is suboptimal due to their inability to leverage incremental visual-code mappings. To address this, we first utilize fine-grained path decomposition to construct dense multi-step visual trajectories, and then introduce a Visual Self-Feedback (VSF) training strategy to condition the next primitive generation on intermediate visual states. Furthermore, a Render-and-Verify (RaV) inference mechanism is proposed to effectively filter degenerate and redundant primitives. Our framework, instantiated on a multimodal foundation model, outperforms strong open-weight baselines on the standard MMSVGBench. This result highlights the remarkable data efficiency and generalization capability of our Render-in-the-Loop paradigm for both Text-to-SVG and Image-to-SVG tasks.

---


### 118. [Anchor-and-Resume Concession Under Dynamic Pricing for LLM-Augmented Freight Negotiation](https://arxiv.org/abs/2604.20732)

**<font color=#1a73e8>作者：</font>** Hoang Nguyen, Lu Wang, Marta Gaia Bras  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Freight brokerages negotiate thousands of carrier rates daily under dynamic pricing conditions where models frequently revise targets mid-conversation. Classical time-dependent concession frameworks use a fixed shape parameter $\beta$ that cannot adapt to these updates. Deriving $\beta$ from the live spread enables adaptation but introduces a new problem: a pricing shift can cause the formula to retract a previous offer, violating monotonicity. LLM-powered brokers offer flexibility but require expensive reasoning models, produce non-deterministic pricing, and remain vulnerable to prompt injection.
We propose a two-index anchor-and-resume framework that addresses both limitations. A spread-derived $\beta$ maps each load's margin structure to the correct concession posture, while the anchor-and-resume mechanism guarantees monotonically non-decreasing offers under arbitrary pricing shifts. All pricing decisions remain in a deterministic formula; the LLM, when used, serves only as a natural-language translation layer. Empirical evaluation across 115,125 negotiations shows that the adaptive $\beta$ tailors behavior by regime: in narrow spreads, it concedes quickly to prioritize deal closure and load coverage; in medium and wide spreads, it matches or exceeds the best fixed-$\beta$ baselines in broker savings. Against an unconstrained 20-billion-parameter LLM broker, it achieves similar agreement rates and savings. Against LLM-powered carriers as more realistic stochastic counterparties, it maintains comparable savings and higher agreement rates than against rule-based opponents. By decoupling the LLM from pricing logic, the framework scales horizontally to thousands of concurrent negotiations with negligible inference cost and transparent decision-making.

---


### 119. [RespondeoQA: a Benchmark for Bilingual Latin-English Question Answering](https://arxiv.org/abs/2604.20738)

**<font color=#1a73e8>作者：</font>** Marisa Hudspeth, Patrick J. Burns, Brendan O'Connor  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We introduce a benchmark dataset for question answering and translation in bilingual Latin and English settings, containing about 7,800 question-answer pairs. The questions are drawn from Latin pedagogical sources, including exams, quizbowl-style trivia, and textbooks ranging from the 1800s to the present. After automated extraction, cleaning, and manual review, the dataset covers a diverse range of question types: knowledge- and skill-based, multihop reasoning, constrained translation, and mixed language pairs. To our knowledge, this is the first QA benchmark centered on Latin. As a case study, we evaluate three large language models -- LLaMa 3, Qwen QwQ, and OpenAI's o3-mini -- finding that all perform worse on skill-oriented questions. Although the reasoning models perform better on scansion and literary-device tasks, they offer limited improvement overall. QwQ performs slightly better on questions asked in Latin, but LLaMa3 and o3-mini are more task dependent. This dataset provides a new resource for assessing model capabilities in a specialized linguistic and cultural domain, and the creation process can be easily adapted for other languages. The dataset is available at: this https URL

---


### 120. [Where and What: Reasoning Dynamic and Implicit Preferences in Situated Conversational Recommendation](https://arxiv.org/abs/2604.20749)

**<font color=#1a73e8>作者：</font>** Dongding Lin, Jian Wang, Yongqi Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Situated conversational recommendation (SCR), which utilizes visual scenes grounded in specific environments and natural language dialogue to deliver contextually appropriate recommendations, has emerged as a promising research direction due to its close alignment with real-world scenarios. Compared to traditional recommendations, SCR requires a deeper understanding of dynamic and implicit user preferences, as the surrounding scene often influences users' underlying interests, while both may evolve across conversations. This complexity significantly impacts the timing and relevance of recommendations. To address this, we propose situated preference reasoning (SiPeR), a novel framework that integrates two core mechanisms: (1) Scene transition estimation, which estimates whether the current scene satisfies user needs, and guides the user toward a more suitable scene when necessary; and (2) Bayesian inverse inference, which leverages the likelihood of multimodal large language models (MLLMs) to predict user preferences about candidate items within the scene. Extensive experiments on two representative benchmarks demonstrate SiPeR's superiority in both recommendation accuracy and response generation quality. The code and data are available at this https URL.

---


### 121. [V-tableR1: Process-Supervised Multimodal Table Reasoning with Critic-Guided Policy Optimization](https://arxiv.org/abs/2604.20755)

**<font color=#1a73e8>作者：</font>** Yubo Jiang, Yitong An, Xin Yang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We introduce V-tableR1, a process-supervised reinforcement learning framework that elicits rigorous, verifiable reasoning from multimodal large language models (MLLMs). Current MLLMs trained solely on final outcomes often treat visual reasoning as a black box, relying on superficial pattern matching rather than performing rigorous multi-step inference. While Reinforcement Learning with Verifiable Rewards could enforce transparent reasoning trajectories, extending it to visual domains remains severely hindered by the ambiguity of grounding abstract logic into continuous pixel space. We solve this by leveraging the deterministic grid structure of tables as an ideal visual testbed. V-tableR1 employs a specialized critic VLM to provide dense, step-level feedback on the explicit visual chain-of-thought generated by a policy VLM. To optimize this system, we propose Process-Guided Direct Alignment Policy Optimization (PGPO), a novel RL algorithm integrating process rewards, decoupled policy constraints, and length-aware dynamic sampling. Extensive evaluations demonstrate that V-tableR1 explicitly penalizes visual hallucinations and shortcut guessing. By fundamentally shifting multimodal inference from black-box pattern matching to verifiable logical derivation, V-tableR1 4B establishes state-of-the-art accuracy among open-source models on complex tabular benchmarks, outperforming models up to 18x its size and improving over its SFT baseline

---


### 122. [Can "AI" Be a Doctor? A Study of Empathy, Readability, and Alignment in Clinical LLMs](https://arxiv.org/abs/2604.20791)

**<font color=#1a73e8>作者：</font>** Mariano Barone, Francesco Di Serio, Roberto Moio 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are increasingly deployed in healthcare, yet their communicative alignment with clinical standards remains insufficiently quantified. We conduct a multidimensional evaluation of general-purpose and domain-specialized LLMs across structured medical explanations and real-world physician-patient interactions, analyzing semantic fidelity, readability, and affective resonance. Baseline models amplify affective polarity relative to physicians (Very Negative: 43.14-45.10% vs. 37.25%) and, in larger architectures such as GPT-5 and Claude, produce substantially higher linguistic complexity (FKGL up to 16.91-17.60 vs. 11.47-12.50 in physician-authored responses). Empathy-oriented prompting reduces extreme negativity and lowers grade-level complexity (up to -6.87 FKGL points for GPT-5) but does not significantly increase semantic fidelity. Collaborative rewriting yields the strongest overall alignment. Rephrase configurations achieve the highest semantic similarity to physician answers (up to mean = 0.93) while consistently improving readability and reducing affective extremity. Dual stakeholder evaluation shows that no model surpasses physicians on epistemic criteria, whereas patients consistently prefer rewritten variants for clarity and emotional tone. These findings suggest that LLMs function most effectively as collaborative communication enhancers rather than replacements for clinical expertise.

---


### 123. [Automatic Ontology Construction Using LLMs as an External Layer of Memory, Verification, and Planning for Hybrid Intelligent Systems](https://arxiv.org/abs/2604.20795)

**<font color=#1a73e8>作者：</font>** Pavel Salovskii, Iuliia Gorshkova  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper presents a hybrid architecture for intelligent systems in which large language models (LLMs) are extended with an external ontological memory layer. Instead of relying solely on parametric knowledge and vector-based retrieval (RAG), the proposed approach constructs and maintains a structured knowledge graph using RDF/OWL representations, enabling persistent, verifiable, and semantically grounded reasoning.
The core contribution is an automated pipeline for ontology construction from heterogeneous data sources, including documents, APIs, and dialogue logs. The system performs entity recognition, relation extraction, normalization, and triple generation, followed by validation using SHACL and OWL constraints, and continuous graph updates. During inference, LLMs operate over a combined context that integrates vector-based retrieval with graph-based reasoning and external tool interaction.
Experimental observations on planning tasks, including the Tower of Hanoi benchmark, indicate that ontology augmentation improves performance in multi-step reasoning scenarios compared to baseline LLM systems. In addition, the ontology layer enables formal validation of generated outputs, transforming the system into a generation-verification-correction pipeline.
The proposed architecture addresses key limitations of current LLM-based systems, including lack of long-term memory, weak structural understanding, and limited reasoning capabilities. It provides a foundation for building agent-based systems, robotics applications, and enterprise AI solutions that require persistent knowledge, explainability, and reliable decision-making.

---


### 124. [LLaDA2.0-Uni: Unifying Multimodal Understanding and Generation with Diffusion Large Language Model](https://arxiv.org/abs/2604.20796)

**<font color=#1a73e8>作者：</font>** Inclusion AI, Tiwei Bie, Haoxing Chen 等 18 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present LLaDA2.0-Uni, a unified discrete diffusion large language model (dLLM) that supports multimodal understanding and generation within a natively integrated framework. Its architecture combines a fully semantic discrete tokenizer, a MoE-based dLLM backbone, and a diffusion decoder. By discretizing continuous visual inputs via SigLIP-VQ, the model enables block-level masked diffusion for both text and vision inputs within the backbone, while the decoder reconstructs visual tokens into high-fidelity images. Inference efficiency is enhanced beyond parallel decoding through prefix-aware optimizations in the backbone and few-step distillation in the decoder. Supported by carefully curated large-scale data and a tailored multi-stage training pipeline, LLaDA2.0-Uni matches specialized VLMs in multimodal understanding while delivering strong performance in image generation and editing. Its native support for interleaved generation and reasoning establishes a promising and scalable paradigm for next-generation unified foundation models. Codes and models are available at this https URL.

---


### 125. [OMIBench: Benchmarking Olympiad-Level Multi-Image Reasoning in Large Vision-Language Model](https://arxiv.org/abs/2604.20806)

**<font color=#1a73e8>作者：</font>** Qiguang Chen, Chengyu Luan, Jiajun Wu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large vision-language models (LVLMs) have made substantial advances in reasoning tasks at the Olympiad level. Nevertheless, current Olympiad-level multimodal reasoning benchmarks for these models often emphasize single-image analysis and fail to exploit contextual information across multiple images. We present OMIBench, a benchmark designed to evaluate Olympiad-level reasoning when the required evidence is distributed over multiple images. It contains problems from biology, chemistry, mathematics, and physics Olympiads, together with manually annotated rationales and evaluation protocols for both exact and semantic answer matching. Across extensive experiments on OMIBench, we observe meaningful performance gaps in existing models. Even the strongest LVLMs, such as Gemini-3-Pro, attain only about 50% on the benchmark. These results position OMIBench as a focused resources for studying and improving multi-image reasoning in LVLMs.

---


### 126. [Diagnosing CFG Interpretation in LLMs](https://arxiv.org/abs/2604.20811)

**<font color=#1a73e8>作者：</font>** Hanqi Li, Lu Chen, Kai Yu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As LLMs are increasingly integrated into agentic systems, they must adhere to dynamically defined, machine-interpretable interfaces. We evaluate LLMs as in-context interpreters: given a novel context-free grammar, can LLMs generate syntactically valid, behaviorally functional, and semantically faithful outputs? We introduce RoboGrid, a framework that disentangles syntax, behavior, and semantics through controlled stress-tests of recursion depth, expression complexity, and surface styles. Our experiments reveal a consistent hierarchical degradation: LLMs often maintain surface syntax but fail to preserve structural semantics. Despite the partial mitigation provided by CoT reasoning, performance collapses under structural density, specifically deep recursion and high branching, with semantic alignment vanishing at extreme depths. Furthermore, "Alien" lexicons reveal that LLMs rely on semantic bootstrapping from keywords rather than pure symbolic induction. These findings pinpoint critical gaps in hierarchical state-tracking required for reliable, grammar-agnostic agents.

---


### 127. [ParetoSlider: Diffusion Models Post-Training for Continuous Reward Control](https://arxiv.org/abs/2604.20816)

**<font color=#1a73e8>作者：</font>** Shelly Golan, Michael Finkelson, Ariel Bereslavsky 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement Learning (RL) post-training has become the standard for aligning generative models with human preferences, yet most methods rely on a single scalar reward. When multiple criteria matter, the prevailing practice of ``early scalarization'' collapses rewards into a fixed weighted sum. This commits the model to a single trade-off point at training time, providing no inference-time control over inherently conflicting goals -- such as prompt adherence versus source fidelity in image editing. We introduce ParetoSlider, a multi-objective RL (MORL) framework that trains a single diffusion model to approximate the entire Pareto front. By training the model with continuously varying preference weights as a conditioning signal, we enable users to navigate optimal trade-offs at inference time without retraining or maintaining multiple checkpoints. We evaluate ParetoSlider across three state-of-the-art flow-matching backbones: SD3.5, FluxKontext, and LTX-2. Our single preference-conditioned model matches or exceeds the performance of baselines trained separately for fixed reward trade-offs, while uniquely providing fine-grained control over competing generative goals.

---


### 128. [Convergent Evolution: How Different Language Models Learn Similar Number Representations](https://arxiv.org/abs/2604.20817)

**<font color=#1a73e8>作者：</font>** Deqing Fu, Tianyi Zhou, Mikhail Belkin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language models trained on natural text learn to represent numbers using periodic features with dominant periods at $T=2, 5, 10$. In this paper, we identify a two-tiered hierarchy of these features: while Transformers, Linear RNNs, LSTMs, and classical word embeddings trained in different ways all learn features that have period-$T$ spikes in the Fourier domain, only some learn geometrically separable features that can be used to linearly classify a number mod-$T$. To explain this incongruity, we prove that Fourier domain sparsity is necessary but not sufficient for mod-$T$ geometric separability. Empirically, we investigate when model training yields geometrically separable features, finding that the data, architecture, optimizer, and tokenizer all play key roles. In particular, we identify two different routes through which models can acquire geometrically separable features: they can learn them from complementary co-occurrence signals in general language data, including text-number co-occurrence and cross-number interaction, or from multi-token (but not single-token) addition problems. Overall, our results highlight the phenomenon of convergent evolution in feature learning: A diverse range of models learn similar features from different training signals.

---


### 129. [Parallel-SFT: Improving Zero-Shot Cross-Programming-Language Transfer for Code RL](https://arxiv.org/abs/2604.20835)

**<font color=#1a73e8>作者：</font>** Zhaofeng Wu, Shiqi Wang, Boya Peng 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Modern language models demonstrate impressive coding capabilities in common programming languages (PLs), such as C++ and Python, but their performance in lower-resource PLs is often limited by training data availability. In principle, however, most programming skills are universal across PLs, so the capability acquired in one PL should transfer to others. In this work, we propose the task of zero-shot cross-programming-language transfer for code RL. We find that, for Llama-3.1, RL training for code generation in a source PL fails to improve, and sometimes even degrades, the performance on other target PLs. To address this, we hypothesize that effective RL transfer requires a generalizable SFT initialization before RL. We thus propose **Parallel-SFT**, an SFT strategy that incorporates "parallel programs" -- functionally equivalent code implemented in multiple PLs -- into the data mixture. We demonstrate that this improves transferability: when we subsequently perform RL on our Parallel-SFT model, we observe better generalization to unseen PLs. Analysis of the model internal representations reveals that Parallel-SFT leads to a more functionality-centric latent space, where equivalent programs across PLs are more tightly clustered, which we hypothesize to contribute to the improved transferability.

---


> [!TIP]
> 当前位于：**101-129**（第 3/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-129**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
