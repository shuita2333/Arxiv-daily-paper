# 🧠 大模型相关研究 | 2026年05月19日

> 本类共 **127** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**101-127**（第 3/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-127**

---

### 101. [Reference-Free Reinforcement Learning Fine-Tuning for MT: A Seq2Seq Perspective](https://arxiv.org/abs/2605.15976)

**<font color=#1a73e8>作者：</font>** Ernesto Garcia-Estrada, Carlos Escolano, José A. R. Fonallosa  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Production machine translation relies overwhelmingly on encoder-decoder Seq2Seq models, yet reinforcement learning approaches to MT fine-tuning have largely targeted decoder-only LLMs at $\geq$7B parameters, with limited systematic study of encoder-decoder architectures. We apply Group Relative Policy Optimization to NLLB-200 (600M and 1.3B) using a hybrid reference-free reward (LaBSE and COMET-Kiwi) that requires no parallel data at fine-tuning time, evaluating across 13 typologically diverse languages. GRPO yields consistent improvements on all 13 languages, up to $+$5.03 chrF++ for Traditional Chinese, and, without any target-language data, competes with 3-epoch supervised fine-tuning on morphologically complex languages . We identify a consistent empirical pattern in which gains are largest where baseline performance is weakest and reward discriminability is highest, making this approach most effective precisely where parallel data is scarcest, and replicate this pattern across English and Spanish source languages.

---


### 102. [Flash-GRPO: Efficient Alignment for Video Diffusion via One-Step Policy Optimization](https://arxiv.org/abs/2605.15980)

**<font color=#1a73e8>作者：</font>** Xiaoxuan He, Siming Fu, Zeyue Xue 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Group Relative Policy Optimization has emerged as essential for aligning video diffusion models with human preferences, but faces a critical computational bottleneck: training a 14B parametered model typically demands hundreds of GPU days per experiment. Existing efficiency methods reduce costs through sliding window subsampling training timesteps, but fundamentally compromise optimization, exhibiting severe instability and failing to reach full trajectory performance. We present Flash-GRPO, a single-step training framework that outperforms full trajectory training in alignment quality under low computational budgets while substantially improving training efficiency. Flash-GRPO addresses two critical challenges: iso-temporal grouping eliminates timestep-confounded variance by enforcing prompt-wise temporal consistency, decoupling policy performance from timestep difficulty; temporal gradient rectification neutralizes the time-dependent scaling factor that causes vastly inconsistent gradient magnitudes across timesteps. Experiments on 1.3B to 14B parameter models validate Flash-GRPO's effectiveness, demonstrating substantial training acceleration with consistent stability and state-of-the-art alignment quality.

---


### 103. [Can Vision Language Models Be Adaptive in Mathematics Education? A Learner Model-based Rubric Study](https://arxiv.org/abs/2605.16011)

**<font color=#1a73e8>作者：</font>** Jie Gao, Yongan Yu, Junzhu Su 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Adaptive learning refers to educational technologies that track learners' learning progress and adapt the instructional process based on individual learners' learning performance. It is increasingly recognized as critical for developing an effective learning support tool. Vision language models (VLMs) have seen adoption in mathematics education, and students have been using them as learning aids for personalized instruction. However, it is unknown whether VLMs have the ability to adapt to different learner profiles when providing mathematical instructions. Current VLMs lack a systematic evaluation framework for this adaptivity to different learner profiles in mathematics tutoring tasks. To address this gap, we draw on the learner model from the adaptive learning framework (Shute and Towle, 2018) and propose a learner model-based rubric. Our rubric formalizes adaptivity assessment into three aspects: cognitive aspects, motivational aspects, and complexity. We also evaluate two additional dimensions of VLM responses: correctness (of answers and solutions) and quality (of the response itself). Our experimental results show measurable differences in adaptivity across models and also reveal that current VLMs struggle to consistently produce learner model-based instructional responses, especially when receiving limited learner information.

---


### 104. [EndoGSim: Physics-Aware 4D Dynamic Endoscopic Scene Simulations via MLLM-Guided Gaussian Splatting](https://arxiv.org/abs/2605.16022)

**<font color=#1a73e8>作者：</font>** Changjing Liu, Yiming Huang, Long Bai 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In robot-assisted minimally invasive surgery, high-fidelity dynamic endoscopic scene reconstruction and simulation are crucial to enhancing downstream tasks and advancing surgical outcomes. However, existing methods primarily focus on visual reconstruction, lacking physics-based descriptions of the scene required for realistic simulation. We propose a unified framework that achieves physics-aware reconstruction and physical simulation of endoscopic scenes through Multi-modal Large Language Models (MLLMs)-guided Gaussian Splatting. Our approach utilizes 4D Gaussian Splatting (4DGS) integrated with pre-trained segmentation and depth estimation to represent deformable tissues and tools. To achieve automatic inference of physical properties, we introduce an object-wise material field that initializes material parameters via MLLM and refines them through a differentiable Material Point Method (MPM) under joint supervision from rendered images and optical flow. Validated on both open-source and in-house datasets, our framework achieves superior simulation fidelity and physical accuracy compared to state-of-the-art methods, underscoring its potential to advance robot-assisted surgical applications.

---


### 105. [Judge Circuits](https://arxiv.org/abs/2605.16023)

**<font color=#1a73e8>作者：</font>** Nils Feldhus, Tanja Baeumel, Elena Golimblevskaia 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM-as-a-judge has become the dominant paradigm for grading model outputs at scale, yet the same model assigns systematically different scores when its output format changes (e.g., a 1-5 rating vs. a True/False label). Existing diagnoses of these format-induced inconsistencies stop at the input-output level. Using Position-aware Edge Attribution Patching (PEAP), we causally investigate the internal mechanism in Gemma-3, Qwen2.5, and Llama-3. We find that judgments across structured understanding and open-ended preference tasks share a sparse, generalized Latent Evaluator sub-graph in the mid-to-late multi-layer perceptrons (MLPs); zero-ablating it collapses judgment while preserving world knowledge in architecturally modular models. By structurally decoupling abstract judging from output formatting, we provide a mechanistic account of format-induced inconsistency on the open-weight models we study: a continuous judgment signal computed in the shared trunk is mapped through fragile, format-specific terminal branches, enabling format-independent preference to be isolated downstream of the requested output format. Our findings imply that benchmark-level reliability comparisons across formats are partially measuring formatter geometry rather than evaluation quality.

---


### 106. [From Flat Language Labels to Typological Priors: Structured Language Conditioning for Multilingual Speech-to-Speech Translation](https://arxiv.org/abs/2605.16026)

**<font color=#1a73e8>作者：</font>** Yu Pan, Yang Hou, Xiongfei Wu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Compositional speech-to-speech translation (S2ST) systems built upon speech large language models (SpeechLLMs) have recently shown promising performance. However, existing S2ST systems often either neglect source-language information or encode it through a language-as-label paradigm, representing each source language as an independent flat embedding. Such a design overlooks systematic linguistic structure shared across languages, which may limit data-efficient multilingual adaptation when supervised S2ST data are scarce. To address this issue, we propose S2ST-Omni 2, a many-to-one compositional S2ST framework that systematically reformulates multilingual language conditioning from flat language labels to structured typological priors. Specifically, S2ST-Omni 2 revisits language conditioning at three levels: typology-informed hierarchical language encoding for structured source-language representation, dynamically-gated language-aware Dual-CTC for content-adaptive acoustic modulation, and typology-aware LLM prompting for decoder-side linguistic guidance. Experiments on CVSS-C show that S2ST-Omni 2 achieves superior average performance among representative S2ST approaches across BLEU, COMET, ASR-BLEU, and BLASER 2.0 under the adopted evaluation protocol. Ablation studies indicate that the proposed representation-level, acoustic-level, and decoding-level strategies provide complementary benefits. Moreover, controlled data-budget analyses and a Japanese-to-English evaluation using only approximately 3 hours of supervised training data suggest that explicit typological priors provide useful inductive biases for data-efficient multilingual S2ST.

---


### 107. [RecMem: Recurrence-based Memory Consolidation for Efficient and Effective Long-Running LLM Agents](https://arxiv.org/abs/2605.16045)

**<font color=#1a73e8>作者：</font>** Zijie Dai, Shiyuan Deng, Sheng Guan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Memory systems often organize user-agent interactions as retrievable external memory and are crucial for long-running agents by overcoming the limited context windows of LLMs. However, existing memory systems invoke LLMs to process every incoming interaction for memory extraction, and such an eager memory consolidation scheme leads to substantial token consumption. To tackle this problem, we propose RecMem by rethinking when memory consolidation should be conducted. RecMem stores incoming interactions in a subconscious memory layer and encode them using lightweight embedding models for retrieval. LLMs are only invoked to extract episodic and semantic memory when sustained recurrence are observed for semantically similar interactions. Such recurrence-based consolidation works because these interactions correspond to a semantic cluster with rich information and thus are worth extraction and summarization. To improve accuracy, RecMem also incorporates a semantic refinement mechanism that recovers the fine-grained facts omitted by memory extraction. Experiments show that RecMem reduces the memory construction token cost of three SOTA memory systems by up to 87% while exceeding their accuracy.

---


### 108. [ITGPT: Generative Pretraining on Irregular Timeseries](https://arxiv.org/abs/2605.16069)

**<font color=#1a73e8>作者：</font>** Antoine Honoré, Ming Xiao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Timeseries regression models often struggle to leverage large volumes of labeled multimodal data, particularly when the data are irregularly sampled or contain missing values. This is common in domains like healthcare and predictive maintenance, where data are collected from unreliable sources, and labeling requires expert knowledge or costly equipments. Transformer-based large language models have proven effective on structured data such as text through self-supervised learning (SSL) and generative pretraining (GPT) frameworks. However, such models lack the flexibility to efficiently process irregularly sampled multimodal timeseries data. In this paper, we introduce ITGPT, an attention-based architecture designed for handling multimodal, irregularly sampled timeseries by allowing training with both SSL losses and GPT-like objectives. We evaluate its performance on a healthcare task with the TIHM dataset, and a predictive maintenance task with the CompX dataset. Our results demonstrate that ITGPT achieves state-of-the-art performance without requiring resampling, feature fusion or explicit data imputation. Furthermore, when labels are scarce, ITGPT effectively leverages unlabeled data through SSL and GPT training, outperforming the purely supervised approach. This represents an important step towards efficiently using large and unstructured timeseries datasets for practical inference tasks.

---


### 109. [Can Large Language Models Imitate Human Speech for Clinical Assessment? LLM-Driven Data Augmentation for Cognitive Score Prediction](https://arxiv.org/abs/2605.16077)

**<font color=#1a73e8>作者：</font>** Si-Belkacem Yamine Ketir, Lenard Paulo Tamayo, Shohei Hisada 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Accurate assessment of cognitive decline from spontaneous speech remains challenging due to limited dataset size and class imbalance. In this work, we propose a large language model (LLM)-driven data augmentation framework to improve the prediction of cognitive scores from speech. Experiments are conducted on a Japanese corpus in which each participant provides both a spontaneous oral narrative and a written response to the same clinical prompt. The written responses serve as semantic anchors to generate multiple oral-like monologues in different styles using GPT-5. We then predict Hasegawa Dementia Scale scores, a widely used cognitive screening tool in Japan, using a Partial Least Squares regression model trained on Sentence-BERT speech embeddings. We investigate two augmentation strategies: random class-balanced selection, which yields moderate but unstable improvements, and similarity-guided class-balanced selection. The latter prioritizes semantically close synthetic samples, leading to more consistent improvements and substantially reducing prediction error for minority low-score participants while maintaining performance for the majority group. Overall, our findings demonstrate the potential of semantically guided LLM-driven augmentation as a principled approach for addressing class imbalance and improving data efficiency in clinical speech analysis.

---


### 110. [VideoSeeker: Incentivizing Instance-level Video Understanding via Native Agentic Tool Invocation](https://arxiv.org/abs/2605.16079)

**<font color=#1a73e8>作者：</font>** Yiming Zhao, Yu Zeng, Wenxuan Huang 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large Vision-Language Models (LVLMs) have shown significant progress in video understanding, yet they face substantial challenges in tasks requiring precise spatiotemporal localization at the instance level. Existing methods primarily rely on text prompts for human-model interaction, but these prompts struggle to provide precise spatial and temporal references, resulting in poor user experience. Furthermore, current approaches typically decouple visual perception from language reasoning, centering reasoning around language rather than visual content, which limits the model's ability to proactively perceive fine-grained visual evidence. To address these challenges, we propose VideoSeeker, a novel paradigm for instance-level video understanding through visual prompts. VideoSeeker seamlessly integrates agentic reasoning with instance-level video understanding tasks, enabling the model to proactively perceive and retrieve relevant video segments on demand. We construct a four-stage fully automated data synthesis pipeline to efficiently generate large-scale, high-quality instance-level video data. We internalize tool-calling and proactive perception capabilities into the model via cold-start supervision and RL training, building a powerful video understanding model. Experiments demonstrate that our model achieves an average improvement of +13.7% over baselines on instance-level video understanding tasks, surpassing powerful closed-source models such as GPT-4o and Gemini-2.5-Pro, while also showing effective transferability on general video understanding benchmarks. The relevant datasets and code will be released publicly.

---


### 111. [DebiasRAG: A Tuning-Free Path to Fair Generation in Large Language Models through Retrieval-Augmented Generation](https://arxiv.org/abs/2605.16113)

**<font color=#1a73e8>作者：</font>** Rui Chu, Bingyin Zhao, Thanh Quoc Hung Le 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have achieved unprecedented success due to their exceptional generative capabilities. However, because they depend on knowledge encapsulated from training corpora, they may produce hallucinations, stereotypes, and socially biased content. In particular, LLMs are prone to prejudiced responses involving race, gender, and age, which are collectively referred to as social biases. Prior studies have used fine-tuning and prompt engineering to mitigate such biases in LLMs, but these methods require additional training resources or domain knowledge to design the framework. Moreover, they may degrade the original capabilities of LLMs and often overlook the need for dynamic debiasing contexts for fairer inference. In this paper, we propose DebiasRAG, a novel tuning-free and dynamic query-specific debiasing framework based on retrieval-augmented generation (RAG). DebiasRAG improves fairness while preserving the intrinsic properties of LLMs, such as representation ability. DebiasRAG consists of three stages: (1) query-specific debiasing candidate generation; (2) context candidate pool construction; and (3) gradient-updated debiasing-guided context piece reranking. First, DebiasRAG leverages self-diagnosed bias contexts relevant to the query through regular retrieval, where the bias contexts are prepared offline by the DebiasRAG provider. Given the query-specific bias contexts, DebiasRAG reversely produces debiasing contexts, which are provided as additional fairness constraints for LLM outputs. Second, a regular RAG retrieval process produces query-related contexts from the regular RAG document database, such as a chunked Wikipedia dataset.

---


### 112. [SGR: A Stepwise Reasoning Framework for LLMs with External Subgraph Generation](https://arxiv.org/abs/2605.16117)

**<font color=#1a73e8>作者：</font>** Xin Zhang, Yang Cao, Baoxing Wu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have demonstrated strong capabilities across diverse NLP applications, such as translation, text generation, and question answering. Nevertheless, they remain limited in complex settings that demand deep reasoning and logical inference. Since these models are trained on large-scale text corpora, their generation process may still introduce irrelevant, noisy, or factually inconsistent content. To mitigate this problem, we introduce SGR, a stepwise framework that enhances LLM reasoning through external subgraph generation. SGR builds query-specific subgraphs from external knowledge bases and uses their semantic structure to support multi-step inference. By grounding intermediate reasoning steps in structured external knowledge, the framework helps the model concentrate on relevant entities, relations, and supporting evidence. In particular, SGR first constructs a subgraph tailored to the input question. It then guides the model to reason progressively over the generated structure and combines multiple reasoning trajectories to obtain the final prediction. Experimental results across several benchmark datasets show that SGR achieves consistent improvements over competitive baselines, highlighting its value for improving both reasoning accuracy and factual reliability.

---


### 113. [STABLE: Simulation-Ready Tabletop Layout Generation via a Semantics-Physics Dual System](https://arxiv.org/abs/2605.16137)

**<font color=#1a73e8>作者：</font>** Zhen Luo, Yixuan Yang, Xudong Xu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generating simulation-ready tabletop scenes from task instructions is an intriguing and promising research direction in the field of Embodied AI. However, existing task-to-scene generation methods rely exclusively on large language models (LLMs) to predict scene layouts, inevitably yielding object collisions or floating due to LLMs' inherent limitations in 3D spatial reasoning. In this paper, we present STABLE, a semantics-physics dual-system tailored for simulation-ready tabletop scene generation. STABLE consists of two complementary modules: (i) a Semantic Reasoner, a fine-tuned LLM trained on a structured tabletop scene dataset to generate coarse layouts from input task instructions, and (ii) a Physics Corrector, a physics-aware flow-based denoising model that outputs pose updates to refine layouts, which ensures the physical plausibility of scenes while preserves semantic alignment with task instructions. STABLE adopts a progressive generation paradigm: by alternating between the Semantic Reasoner and Physics Corrector, it incrementally expands the scene from task-critical objects to background objects. Experiments demonstrate that STABLE successfully generates simulation-ready tabletop scenes that strictly conform to task instructions and significantly enhances the physical validity of scenes over prior art.

---


### 114. [Property-Guided LLM Program Synthesis for Planning](https://arxiv.org/abs/2605.16142)

**<font color=#1a73e8>作者：</font>** Augusto B. Corrêa, André G. Pereira, Jendrik Seipp  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLMs have shown impressive success in program synthesis, discovering programs that surpass prior solutions. However, these approaches rely on simple numeric scores to signal program quality, such as the value of the solution or the number of passed tests. Because a score offers no guidance on why a program failed, the system must generate and evaluate many candidates hoping some succeed, increasing LLM inference and evaluation costs. We study a different approach: property-guided LLM program synthesis. Instead of scoring programs after evaluation, we check whether a candidate satisfies a formally defined property. When the property is violated, we stop the evaluation early and provide the LLM with a concrete counterexample showing exactly how the program failed. This feedback drastically reduces both the number of program generations and the evaluation cost, and can guide the LLM to generate stronger programs. We evaluate this approach on PDDL planning domains, asking the LLM to synthesize direct heuristic functions: every state reachable by strictly improving transitions has a strictly improving successor. A heuristic with this property leads hill-climbing algorithm directly to a goal state. A counterexample-guided repair loop generates one candidate program, checks the property over a training set, and returns the first case that violates the property. We evaluate our approach on ten planning domains with an out-of-distribution test set. The synthesized heuristics are effectively direct on virtually all test tasks, and compared to the best prior generation method our approach generates seven times fewer programs per domain on average, solves more tasks without using search, and requires several orders of magnitude less computation to evaluate candidates. Whenever a problem admits a verifiable property, property-guided LLM synthesis can reduce cost and improve program quality.

---


### 115. [Look Before You Leap: Autonomous Exploration for LLM Agents](https://arxiv.org/abs/2605.16143)

**<font color=#1a73e8>作者：</font>** Ziang Ye, Wentao Shi, Yuxin Liu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model based agents often fail in unfamiliar environments due to premature exploitation: a tendency to act on prior knowledge before acquiring sufficient environment-specific information. We identify autonomous exploration as a critical yet underexplored capability for building adaptive agents. To formalize and quantify this capability, we introduce Exploration Checkpoint Coverage, a verifiable metric that measures how broadly an agent discovers key states, objects, and affordances. Our systematic evaluation reveals that agents trained with standard task-oriented reinforcement learning consistently exhibit narrow and repetitive behaviors that impede downstream performance. To address this limitation, we develop a training strategy that interleaves task-execution rollouts and exploration rollouts, with each type of rollout optimized by its corresponding verifiable reward. Building on this training strategy, we propose the Explore-then-Act paradigm, which decouples information-gathering from task execution: agents first utilize an interaction budget to acquire grounded environmental knowledge, then leverage it for task resolution. Our results demonstrate that learning to systematically explore is imperative for building generalizable and real-world-ready agents.

---


### 116. [Learn Where Outcomes Diverge: Efficient VLA RL via Probabilistic Chunk Masking](https://arxiv.org/abs/2605.16154)

**<font color=#1a73e8>作者：</font>** Vaidehi Bagaria, Nikshep Grampurohit, Pulkit Verma  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) allows vision-language-action (VLA) policies to generalize beyond their training distribution by optimizing directly for task success, but post-training is computationally expensive. A natural response has been to speed rollout collection through faster simulators and world models. In GRPO-based VLA RL, we find that the dominant cost lies elsewhere: gradient computation accounts for approximately 78% of wall-clock time per step in our runs, while rollout collection accounts for only 21%. Gradient cost dominates because much of this computation is spent on phases that contribute little to learning. GRPO's learning signal is driven by advantage variance: only phases where successful and failed rollouts diverge produce learning signal. However, GRPO assigns the same advantage to every chunk in a rollout. As a result, actor-update compute is spent uniformly across the trajectory, including phases the policy already handles after pre-training and supervised fine-tuning. This paper presents Probabilistic Chunk Masking (PCM), a drop-in modification to GRPO that allocates gradient computation to a small, probabilistically selected subset of chunks per trajectory. PCM scores semantic phases using success-failure action variance, a rollout-derived proxy for per-phase gradient variance, and samples a fixed chunk budget with online-updated phase-level keep probabilities. We formalize per-phase gradient variance as the quantity determines where gradient computation is useful and show that success-failure action variance provides a measurable proxy for it. PCM requires no reward model or learned critic. On three LIBERO benchmarks, PCM matches the final success rate of standard GRPO while achieving 2.38 times wall-clock speedup, 4.8 times faster gradient updates, and 60% lower peak activation memory, while backpropagating through fewer than 20% of trajectory chunks.

---


### 117. [Second-Order Multi-Level Variance Correction for Modality Competition in Multimodal Models](https://arxiv.org/abs/2605.16165)

**<font color=#1a73e8>作者：</font>** Yishun Lu, Wes Armour  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autoregressive next-token training offers a unified formulation for image generation and text understanding, but it also creates strong modality competition that destabilizes optimization and limits large-batch scaling. We show that first-order optimizers such as AdamW are vulnerable to cross-modality gradient heterogeneity, while second-order preconditioning, particularly SOAP, provides a more stable basis for multimodal alignment. Building on this insight, we propose \emph{ML-FOP-SOAP}, a second-order optimization framework with Multi-Level Variance Correction. Our Fisher-Orthogonal Projection suppresses variance-induced modality conflicts, reducing the trade-off between visual generation and textual understanding. To make this practical under large gradient accumulation, we introduce a hierarchical folding strategy that captures fine-grained variance with low micro-step overhead. Experiments on Janus and Emu3 show consistent gains across both modalities and stable training at batch size 8192. Compared with AdamW, our method improves sample efficiency by up to $1.4\times$ and accelerates wall-clock training by up to $1.5\times$, offering a robust optimizer for scaling multimodal foundation models.

---


### 118. [Res$^2$CLIP: Few-Shot Generalist Anomaly Detection with Residual-to-Residual Alignment](https://arxiv.org/abs/2605.16171)

**<font color=#1a73e8>作者：</font>** Xinyue Liu, Jianyuan Wang, Biao Leng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Few-shot Generalist Anomaly Detection requires models to generalize to novel categories without retraining, posing significant challenges in real-world scenarios with scarce samples and rapidly changing categories. Existing CLIP-based methods face two major challenges: coarse-grained unified text prompts struggle to adapt to fine-grained foreground-background differences, causing cross-granularity mismatch; and fine-tuning on auxiliary datasets disrupts CLIP's inherent open-world generalization due to domain shift, leading to cross-category generalization degradation. To address these, we propose to shift multimodal alignment entirely into a unified residual space, where residual representations naturally eliminate fine-grained normal feature differences across regions and class-specific biases, simultaneously resolving both problems. Based on this insight, Res$^2$CLIP, the first residual-to-residual alignment framework that symmetrically bridges visual and text modalities within CLIP's residual space, is designed. The framework is developed from a residual perspective into three branches: a text prompt-based branch, a visual prompt-based branch, and a novel residual-to-residual alignment branch. All learnable optimizations are constrained within the residual domain, and the residual alignment optimization objectives are designed to force the model to focus on relative anomaly deviations rather than optimizing class-specific features. Experiments on multiple datasets demonstrate the effectiveness of our architecture. The code is available at this https URL.

---


### 119. [MAgSeg: Segmentation of Agricultural Landscapes in High-Resolution Satellite Imagery using Multimodal Large Language Models](https://arxiv.org/abs/2605.16179)

**<font color=#1a73e8>作者：</font>** Piyush Tiwary, Utkarsh Ahuja, Depanshu Sani 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Agricultural landscape segmentation in the Global South is challenging as it is characterized by fragmented plots, high intra-class variance, and a scarcity of labeled training data. Recent advances in segmentation have been made by Multimodal Large Language Models (MLLMs). However, current approaches encounter critical context length bottlenecks and a domain alignment gap in understanding satellite features. We address these limitations through MAgSeg, a novel, decoder-free MLLM segmentation approach. MAgSeg is an architecturally efficient approach that enables standard MLLMs to perform segmentation of complex smallholder agricultural landscapes from high-resolution satellite imagery, without requiring auxiliary vision decoders. We introduce a novel instruction tuning data format designed to enable scalable fine-tuning and post-training on high resolution satellite imagery, which enables MAgSeg to learn from the global context of the image while generating text tokens for only a patch within the image. Extensive evaluations on datasets spanning three countries in the Global South demonstrate that MAgSeg significantly outperforms state-of-the-art MLLM baselines, offering a scalable solution to map smallholder agricultural environments.

---


### 120. [Optimized Three-Dimensional Photovoltaic Structures with LLM guided Tree Search](https://arxiv.org/abs/2605.16191)

**<font color=#1a73e8>作者：</font>** Michael P. Brenner, Lizzie Dorfman, John C. Platt  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present a case study for how AI coding systems can be used to generate novel scientific hypotheses. We combine a generic coding agent (Google's AntiGravity) with an LLM-driven tree search algorithm (Empirical Research Assistance / ERA) to autonomously generate high-efficiency three-dimensional photovoltaic (3DPV) structures that overcome losses limiting flat solar panels at mid-latitudes. These structures operate by presenting favorable angles to the sun throughout the day, and for illustrative purposes we focus on optimizing performance for a single solar day. Our workflow begins by using AntiGravity to reproduce calculations \cite{bernardi2012solar} showing that 3DPV can have energy densities much higher than stationary flat PV panels. We use these initial designs as the starting point for large scale tree search, where we seek improved solutions and score them for their diurnal yield. The initial tree search leads to nominally more efficient solutions, yet they are caused by algorithmic reward hacking, arising from non-physical design features such as structurally levitating disconnected tiers and exploitations of the discretizations in the optics solver. To counteract this, we develop a workflow where the coding agent iteratively patches the physics engine with constraints to eliminate reward hacking. With reward-hacking eliminated, ERA discovers a series of designs with various constraints and improved performance, including optimal designs with different fixed collector areas, optimizing zenith tracking and avoiding self shadowing.
Combining coding agents with tree search (ERA) provides a powerful platform for scientific discovery, for problems whose solutions can be empirically evaluated with a score function.

---


### 121. [Formal Methods Meet LLMs: Auditing, Monitoring, and Intervention for Compliance of Advanced AI Systems](https://arxiv.org/abs/2605.16198)

**<font color=#1a73e8>作者：</font>** Parand A. Alamdari, Toryn Q. Klassen, Sheila A. McIlraith  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We examine one particular dimension of AI governance: how to monitor and audit AI-enabled products and services throughout the AI development lifecycle, from pre-deployment testing to post-deployment auditing. Combining principles from formal methods with SoTA machine learning, we propose techniques that enable AI-enabled product and service developers, as well as third party AI developers and evaluators, to perform offline auditing and online (runtime) monitoring of product-specific (temporally extended) behavioral constraints such as safety constraints, norms, rules and regulations with respect to black-box advanced AI systems, notably LLMs. We further provide practical techniques for predictive monitoring, such as sampling-based methods, and we introduce intervening monitors that act at runtime to preempt and potentially mitigate predicted violations. Experimental results show that by exploiting the formal syntax and semantics of Linear Temporal Logic (LTL), our proposed auditing and monitoring techniques are superior to LLM baseline methods in detecting violations of temporally extended behavioral constraints; with our approach, even small-model labelers match or exceed frontier LLM judges. Our predictive and intervening monitors significantly reduce the violation rates of LLM-based agents while largely preserving task performance. We further show through controlled experiments that LLMs' temporal reasoning shows a pronounced degradation in accuracy with increasing event distance, number of constraints, and number of propositions.

---


### 122. [Context, Reasoning, and Hierarchy: A Cost-Performance Study of Compound LLM Agent Design in an Adversarial POMDP](https://arxiv.org/abs/2605.16205)

**<font color=#1a73e8>作者：</font>** Igor Bogdanov, Chung-Horng Lung, Thomas Kunz 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Deploying compound LLM agents in adversarial, partially observable sequential environments requires navigating several design dimensions: (1) what the agent sees, (2) how it reasons, and (3) how tasks are decomposed across components. Yet practitioners lack guidance on which design choices improve performance versus merely increase inference costs. We present a controlled study of compound LLM agent design in CybORG CAGE-2, a cyber defense environment modeled as a Partially Observable Markov Decision Process (POMDP). Reward is non-positive, so all configurations operate in a failure-mitigation mode. Our evaluation spans five model families, six models, and twelve configurations (3,475 episodes) with token-level cost accounting. We vary context representation (raw observations vs. a deterministic state-tracking layer with compressed history), deliberation (self-questioning, self-critique, and self-improvement tools, with optional chain-of-thought prompting), and hierarchical decomposition (monolithic ReAct vs. delegation to specialized sub-agents). We find that: (1) Programmatic state abstraction delivers the largest returns per token spent (RPTS), improving mean return by up to 76% over raw observations. (2) Distributing deliberation tools across a hierarchy degrades performance relative to hierarchy alone for all five model families, reaching up to 3.4$\times$ worse mean return while using 1.8-2.7$\times$ more tokens. We call this destructive pattern a deliberation cascade. (3) Hierarchical decomposition without deliberation achieves the best absolute performance for most models, and context engineering is generally more cost-effective than deliberation. These findings suggest a design principle for structured adversarial POMDPs: invest in programmatic infrastructure and clean task decomposition rather than deeper per-agent reasoning, as these strategies can interfere when combined.

---


### 123. [Confirming Correct, Missing the Rest: LLM Tutoring Agents Struggle Where Feedback Matters Most](https://arxiv.org/abs/2605.16207)

**<font color=#1a73e8>作者：</font>** Tahreem Yasir, Wenbo Li, Sam Gilson 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Effective tutoring requires distinguishing optimal, valid but suboptimal, and incorrect student solutions, a distinction central to intelligent tutoring systems (ITS) but untested for LLM-based tutors. As LLMs are increasingly explored as conversational complements to ITS, evaluating their diagnostic precision is essential. We present a benchmark of seven LLM feedback agents in propositional logic using knowledge-graph-derived ground truth across 10,836 solution--feedback pairs and three feedback conditions. Models achieved near-ceiling performance on optimal steps but systematically over-rejected valid but suboptimal reasoning and over-validated incorrect solutions, precisely where adaptive tutoring matters most. These failures persisted across models regardless of solution context, suggesting architectural rather than informational limits. Moreover, accurate diagnosis did not reliably produce pedagogically actionable feedback, revealing a gap between diagnostic judgment and instructional effectiveness. Our findings suggest that LLMs are better suited for hybrid architectures where KG-grounded models handle diagnosis while LLMs support open-ended scaffolding and dialogue.

---


### 124. [Fully Open Meditron: An Auditable Pipeline for Clinical LLMs](https://arxiv.org/abs/2605.16215)

**<font color=#1a73e8>作者：</font>** Xavier Theimer-Lienhard, Mushtaha El-Amin, Fay Elhassan 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Clinical decision support systems (CDSS) require scrutable, auditable pipelines that enable rigorous, reproducible validation. Yet current LLM-based CDSS remain largely opaque. Most "open" models are open-weight only, releasing parameters while withholding the data provenance, curation procedures, and generation pipelines that determine model behavior. Fully Open (FO) models, which expose the complete training stack end-to-end, do not currently exist in medicine. We introduce Fully Open Meditron, the first fully open pipeline for building LLM-CDSS, comprising a clinician-audited training corpus, a reproducible data construction and training framework, and a use-aligned evaluation protocol. The corpus unifies eight public medical QA datasets into a normalized conversational format and expands coverage with three clinician-vetted synthetic extensions: exam-style QA, guideline-grounded QA derived from 46,469 clinical practice guidelines, and clinical vignettes. The pipeline enforces system-wide decontamination, gold-label resampling of teacher generations, and end-to-end validation by a four-physician panel. We evaluate using an LLM-as-a-judge protocol over expert-written clinical vignettes, calibrated against 204 human raters. We apply the recipe to five FO base models (Apertus-70B/8B-Instruct, OLMo-2-32B-SFT, EuroLLM-22B/9B-Instruct). All MeditronFO variants are preferred over their bases. Apertus-70B-MeditronFO improves +6.6 points over its base (47.2% to 53.8%) on aggregate medical benchmarks, establishing a new FO SoTA. Gemma-3-27B-MeditronFO is preferred over MedGemma in 58.6% of LLM-as-a-judge comparisons and outperforms it on HealthBench (58% vs 55.9%). These results show that fully open pipelines can achieve state-of-the-art domain-specific performance without sacrificing auditability or reproducibility.

---


### 125. [Artificial Aphasias in Lesioned Language Models](https://arxiv.org/abs/2605.16222)

**<font color=#1a73e8>作者：</font>** Nathan Roll, Jill Kries, Laura Gwilliams 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Aphasias, selective language impairments which can arise from brain damage, reveal the functional organization of human language by providing causal links between affected brain regions and specific symptom profiles. Drawing on this literature, we introduce an aphasia-inspired technique to characterize the emergent functional organization of language models (LMs). We ``lesion'' (zero-out) model parameters and measure the effects of this intervention against clinical aphasia symptoms, as diagnosed by the Text Aphasia Battery (TAB). When applied to 112,426 outputs from five 1B-scale LMs, the full range of evaluated symptoms surface, but in distributions largely distinct from those of humans. Our method uncovers broad symptom-profile differences between attention components (query, key, value, output) and feed-forward components (up, gate, down), with weaker evidence for differences among components within the same mechanism. We also find an effect of depth, where lesions in early layers disproportionately cause syntactic and semantic symptoms while late-middle layers yield higher rates of phonological and fluency deficits. Although some LM lesions induce quantitatively more similar profiles to some human aphasia types than others, qualitative differences in symptom patterns between LMs and humans suggest that aphasia syndromes are heavily influenced by the details of learning and processing rather than being a domain-invariant consequence of disrupted language processing.

---


### 126. [FORGE: Self-Evolving Agent Memory With No Weight Updates via Population Broadcast](https://arxiv.org/abs/2605.16233)

**<font color=#1a73e8>作者：</font>** Igor Bogdanov, Chung-Horng Lung, Thomas Kunz 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Can LLM agents improve decision-making through self-generated memory without gradient updates? We propose FORGE (Failure-Optimized Reflective Graduation and Evolution), a staged, population-based protocol that evolves prompt-injected natural-language memory for hierarchical ReAct agents. FORGE wraps a Reflexion-style inner loop, where a dedicated reflection agent (using the same underlying LLM, no distillation from a stronger model) converts failed trajectories into reusable knowledge artifacts: textual heuristics (Rules), few-shot demonstrations (Examples), or both (Mixed), with an outer loop that propagates the best-performing instance's memory to the population between stages and freezes converged instances via a graduation criterion. We evaluate on CybORG CAGE-2, a stochastic network-defense POMDP at a 30-step horizon against the B-line attacker, where all four tested LLM families (Gemini-2.5-Flash-Lite, Grok-4-Fast, Llama-4-Maverick, Qwen3-235B) exhibit strongly negative, heavy-tailed zero-shot rewards. Compared against both a zero-shot baseline and a Reflexion baseline (isolated single-stream learning), FORGE improves average evaluation return by 1.7-7.7$\times$ over zero-shot and by 29-72% over Reflexion in all 12 model-representation conditions, reducing major-failure rates (below $-100$) to as low as $\sim$1%. We find that (1) population broadcast is critical mechanism, with a no-graduation ablation confirming that broadcast carries the performance gains while graduation primarily saves compute; (2) Examples achieves the strongest returns for three of four models, Rules offers the best cost-reliability profile with $\sim$40% fewer tokens; and (3) weaker baseline models benefit disproportionately, suggesting FORGE may mitigate capability gaps rather than amplify strong models. All evidence is confined to CAGE-2 B-line; cross-family findings are directional evidence.

---


### 127. [Prospective multi-pathogen disease forecasting using autonomous LLM-guided tree search](https://arxiv.org/abs/2605.16238)

**<font color=#1a73e8>作者：</font>** Sarah Martinson, Michael P. Brenner, Martyna Plomecka 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Probabilistic forecasting of infectious diseases is crucial for public health but relies on labor-intensive manual model curation by expert modeling teams. This bespoke development bottlenecks scalability to granular geographic resolutions or emerging pathogens. Here, we present an autonomous system using Large Language Model (LLM)-guided tree search to iteratively generate, evaluate, and optimize executable forecasting software. In a fully prospective, real-time evaluation during the 2025-2026 US respiratory season, the system autonomously discovered methodologically diverse models for influenza, COVID-19, and respiratory syncytial virus (RSV). Aggregating these machine-generated models yielded an ensemble that consistently matched or outperformed the gold-standard, human-curated Centers for Disease Control and Prevention (CDC) hub ensembles out-of-sample. The system successfully navigated data-scarce "cold start" scenarios for RSV. Moreover, controlled retrospective ablations revealed that optimizing log-scale distance metrics prevents reward hacking, while an automated judge-in-the-loop ensures structural fidelity to complex scientific theories. By autonomously translating epidemiological theory into accurate, transparent code, this framework overcomes the modeling labor bottleneck, enabling rapid deployment of expert-level disease forecasting at unprecedented scales.

---


> [!TIP]
> 当前位于：**101-127**（第 3/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-127**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
