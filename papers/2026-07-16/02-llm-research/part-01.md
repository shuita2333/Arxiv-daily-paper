# 🧠 大模型相关研究 | 2026年07月16日

> 本类共 **99** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**1-50**（第 1/2 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-99](./part-02.md)

---

### 1. [Scaling Point-in-Time Language Models](https://arxiv.org/abs/2607.11889)

**<font color=#1a73e8>作者：</font>** Bryan Kelly, Semyon Malamud, Johannes Schwab 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models trained on unrestricted internet corpora inevitably embed information from the future, introducing lookahead bias that compromises the validity of backtests and causal inference in finance and the social sciences. Point-in-time language models--trained exclusively on text available up to each calendar date--eliminate this leakage by construction, but existing efforts typically produce models that lag substantially behind their unconstrained counterparts. We show that this performance gap can be substantially narrowed through scale. Training decoder-only transformers with up to 4 billion parameters on 1 trillion chronologically filtered tokens from FineWeb, we construct a sequence of monthly model checkpoints spanning 2013-2024. Across a range of common-sense reasoning and language understanding benchmarks, our models approach the performance of leading open-weight models of comparable size (e.g., Gemma-3-4B and LLaMA-7B) trained on temporally unrestricted data, although a performance gap remains on several tasks. Instruction fine-tuning via LoRA further improves downstream usability. We release the complete pipeline--including dataset construction, training infrastructure, and evaluation code--to enable reproducible point-in-time language modeling and to support research applications that require strict temporal validity.

---


### 2. [CANDI: Contextual Alignment for Niche Domains Question Answering](https://arxiv.org/abs/2607.11891)

**<font color=#1a73e8>作者：</font>** Megha Chakraborty, Darssan L. Eswaramoorthi, Het Riteshkumar Shah 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The deployment of large language models (LLMs) in specialized domains like medical diagnostics and financial advisory necessitates evaluating capabilities beyond general knowledge. Traditional question-answering benchmarks often fail to capture the nuanced contextual grounding, user awareness, and domain understanding these fields require. To address this, we introduce CANDI-QA (Contextual Alignment for Niche Domains Question Answering), a novel dataset evaluating LLMs on delivering accurate, context-sensitive, and user-aligned answers in specialized settings. CANDI-QA features expert-curated question-answer pairs structured into two categories: (1) Information Assistance Questions, which are direct, factual queries requiring precise extraction, and (2) Applied Inference Questions, which are multi-hop reasoning tasks needing situational inference to generate actionable insights. We evaluate over ten diverse language models, from compact open-source to state-of-the-art proprietary systems. As a robust baseline, we present MTSS-Net, a lightweight neuro-symbolic framework combining neural retrieval with rule-based reasoning. Our findings highlight the profound challenges of achieving contextual alignment in niche domains, revealing the limitations of current LLMs without enhanced contextual or symbolic integration. Ultimately, CANDI-QA serves as a critical benchmark for advancing research in context-aware language models, stimulating the development of robust, trustworthy AI for high-stakes domains.

---


### 3. [I'm Sorry, but I Can't Help with Braille: Revealing Accessibility Failures in State-of-the-Art LLMs](https://arxiv.org/abs/2607.11893)

**<font color=#1a73e8>作者：</font>** Abdullah Abdullah  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) perform strongly on many language tasks, but their capability in structurally constrained, accessibility-critical modalities such as Braille remains unclear. We evaluate state-of-the-art LLMs on bidirectional Korean-Braille translation using a human-annotated dataset. Despite expectations that multilingual, instruction-tuned models can generalize to Braille via text representations, we find consistently poor, unstable outputs and substantial disagreement with human judgments. These results point to missing Braille-aware tokenization and weak alignment between Korean and Braille patterns. In contrast, supervised fine-tuning of a small model (T5-small) on the same data yields large and stable gains over zero-shot and prompted LLM baselines across standard metrics (SacreBLEU, ChrF++, CER, BLEU, ROUGE-L, METEOR, CIDEr). Our findings reveal a systematic limitation of current LLMs and demonstrate the effectiveness of modest task-specific supervision.

---


### 4. [Reading the Eyes in VR: Multimodal Modeling of Social Intelligence](https://arxiv.org/abs/2607.11931)

**<font color=#1a73e8>作者：</font>** Mohammad Fahim Abrar, Shayla Sharmin, Roghayeh Leila Barmaki  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Social intelligence, the ability to interpret others' emotions, beliefs, and intentions, is often assessed with the Reading the Mind in the Eyes Test (RMET), in which participants infer mental states from images of the eye region. Yet RMET is typically presented on paper or desktop displays, where viewing geometry can vary across participants, and it rarely includes immediate feedback. We investigated whether presentation medium and brief trial-level feedback influence RMET behavior. We implemented RMET in Unity for both desktop and Virtual Reality (VR), using VR to hold stimulus distance and field of view constant without changing the items. We conducted a 2x2 mixed study with 20 participants, with device (VR vs. desktop) manipulated between subjects and feedback (immediate correctness cue vs. none) manipulated within subjects. Eye-tracking and EEG data were recorded and synchronized with behavioral logs. We analyzed fixation-based gaze measures, EEG signals, response time, accuracy, and subjective measures. Immediate feedback was associated with longer fixation durations and higher EEG-based engagement, while no significant differences were observed in task completion time or total correct answers. Presentation medium did not produce reliable differences in the objective measures, but VR received higher usability ratings and was also rated as more effortful. These results provide initial evidence that RMET can be studied as a process-aware assessment task in controlled VR and desktop settings.

---


### 5. [Transforming LLMs into Efficient Cross-Encoders via Knowledge Distillation for RAG Reranking](https://arxiv.org/abs/2607.11933)

**<font color=#1a73e8>作者：</font>** Shreeya Dasa Lakshminath, Shubhan S  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Cross-encoders achieve high reranking accuracy in Retrieval-Augmented Generation (RAG) pipelines but impose quadratic inference costs that limit real-time deployment. We address this by fine-tuning LLaMA 3 (8B) as a drop-in reranker using a two-stage pipeline: supervised fine-tuning on a custom query-document relevance dataset via the Unsloth framework with LoRA adapters, followed by 4-bit quantization for efficient inference. The resulting model replaces the cross-encoder in a dual-retriever RAG pipeline combining BM25 and dense vector search. Evaluated on a domain-specific question-answering benchmark using the RAGAS framework, our fine-tuned LLaMA 3 reranker achieves gains of 14% in answer relevancy, 16% in context precision, 19% in answer similarity, and 21% in answer correctness over the cross-encoder baseline, while reducing inference overhead through 4-bit quantization. These results demonstrate that instruction-tuned LLMs can be adapted into accurate, efficient rerankers without the quadratic complexity of traditional cross-encoders.

---


### 6. [TSCA-Net: Temporal-Spatial Clique Attention for Interpretable Multimodal Pedestrian Trajectory Prediction](https://arxiv.org/abs/2607.11939)

**<font color=#1a73e8>作者：</font>** Md Mustafizur Rahman, Guangchao Yang, A F M Abdun Noor 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate pedestrian trajectory prediction in crowded environments remains challenging due to the multimodal uncertainty of human motion and the variable complexity of motion dynamics across different scene contexts. Existing goal-conditioned models rely on static displacement structures that assign equal weight to all historical time steps, standard graph attention mechanisms, and fixed-capacity motion decoders that cannot adapt to local prediction complexity. To address these limitations, we propose TSCA-Net, a trajectory prediction framework built upon three complementary modules. The Temporal-Spatial Clique Attention (TSCA) module introduces learnable temporal gating into clique-based goal-history interaction, enabling time-aware modulation of historical observations relative to each candidate goal. The Cross-Pedestrian Clique Potential (CPCP) module models asymmetric pairwise agent relationships through a dynamic clique potential framework with a time-varying social graph. The Adaptive KAN Grid Refinement (AKGR) mechanism dynamically adjusts the B-spline grid resolution of a Kolmogorov-Arnold Network-augmented LSTM decoder based on per-agent goal distribution entropy, balancing model expressiveness against overfitting across varying motion complexities. Extensive experiments on the ETH/UCY and Stanford Drone Dataset benchmarks demonstrate that TSCA-Net achieves state-of-the-art performance, with average ADE/FDE of 0.13/0.20 m on ETH/UCY and 6.95/10.43 pixels on SDD. Comprehensive ablation studies confirm the complementary contributions of all three proposed modules.

---


### 7. [Belief-reality separation lives in routing over a shared value slot in language models](https://arxiv.org/abs/2607.11945)

**<font color=#1a73e8>作者：</font>** Oliver Steele, Jiangtao Wen, Yuxing Han  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Capable language models hold what a character believes apart from what is true: told "Anna believes the cup is blue; in reality it is red," they answer blue about Anna and red about the world. Where in the computation does that separation live? We show it rests on two separable mechanisms at two positions. A generic value slot binds the attributed value. A router at the query position selects which frame, the character's belief or reality, a query reads out. Two routes fill the slot: an asserted belief, whose value the text supplies, binds in directly; a derived belief, whose value must be inferred from what the character could see, arrives by a visibility-gated lookback. A subspace trained on either route steers the other, and only the derived route depends on described visibility. The slot itself carries no belief-reality tag: intervening on it moves a reality readout as strongly as a belief one. The separation lives instead in a dissociated pair of routing subspaces, which flip a query between frames without injecting the donor's value. These results hold across three architectures, on stimuli de-confounded against theory-of-mind-benchmark shortcuts; the behavior itself emerges between 3B and 7B across five model families. This paper develops the single belief-reality axis in depth; a companion paper shows the same slot-and-router format is shared across the other non-actual contexts a sentence can open (counterfactual, fictional, temporal).

---


### 8. [Ontology-Amplified Distillation and Contextuality Auditing for Sovereign Enterprise Language Models: A Combined Proof-of-Mechanism and Negative-Results Method Study](https://arxiv.org/abs/2607.11948)

**<font color=#1a73e8>作者：</font>** Thanh Luong Tuan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Regulated financial institutions operating under data-residency rules need tenant-owned language models that can run inside the institution's perimeter. This paper combines two related FAOS studies into one mechanism-and-control article. First, it reports a reduced-power proof-of-mechanism study of ontology-amplified distillation: a Qwen3.6-27B student is adapted to the Foundation AgenticOS ontology through supervised fine-tuning on frontier-teacher trajectories and ontology-grounded direct preference optimization (DPO), trained locally on a single Apple M5 Max from 47 synthetic, English-language, cross-domain preference pairs. On 40 held-out Vietnamese financial-domain tasks, the distilled student grounds 36 of 40 tasks (grounded rate 0.90; mean ontology term-coverage r_onto = 0.95 on a metric floored at 0.50), equal to the GPT-5 frontier baseline, which also grounds 36 of 40. The outcome is underpowered to establish equivalence: the paired-difference 95% confidence interval spans +/-4 tasks, and the run does not test or show the pre-registered amplification prediction that the student should exceed the frontier. Second, the paper consolidates a contextuality-audit method for enterprise-agent routing. In a separate negative-results pilot, the corrected canonical Contextuality-by-Default degree is zero for all Phase 1.3 groups in both the local-Qwen run and an explicitly labeled Gemma replication check; the useful signal is direct influence and construct coupling, not surviving residual contextuality. Together, the studies pair an ontology-grounded model-building mechanism with a governance diagnostic for deciding when apparent disagreement should trigger prompt standardization, multi-agent synthesis, or human review. The evidence supports neither deployability, safety, superiority, statistical equivalence, nor a contextuality-positive routing rule.

---


### 9. [Scalable Optimal Transport Algorithm for Network Alignment](https://arxiv.org/abs/2607.11952)

**<font color=#1a73e8>作者：</font>** Elaheh Hassani, Durga Mandarapu, Qi Yu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Network alignment identifies node correspondences across different networks and is a fundamental primitive in many data science applications, including social network analysis, fraud detection, and knowledge graph integration. However, state-of-the-art network alignment methods often achieve high accuracy by repeatedly constructing and updating dense matrices, sacrificing scalability in the process. To address this scalability limitation without compromising alignment accuracy, we present FastAlign, a scalable, sparsity-aware framework for optimal transport-based network alignment. Rather than introducing a new alignment model, FastAlign preserves the original OT formulation and reinterprets its computation as a set of recurring mixed sparse-dense operations. FastAlign combines sparsity-aware graph computation with domain-specific kernel fusion, including a custom SpMM kernel. Our results show that FastAlign achieves alignment quality comparable to state-of-the-art OT-based methods while substantially reducing end-to-end runtime up to 3.89x-9.45x on CPU and 2.24x-32.54x on GPU.

---


### 10. [Self-Evolving In-Context Learning for Direct Pilot-to-Beamformer Design in MU-MISO Systems](https://arxiv.org/abs/2607.11970)

**<font color=#1a73e8>作者：</font>** Yubo Zhang, Xiaodong Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We develop an enhanced in-context learning (ICL) framework to improve the performance of pilot-based beamforming in multi-user multiple-input single-output (MU-MISO) systems. The proposed scheme integrates the ICL-Transformer backbone with the pilot encoder-decoder network (EDN) and the beamformer EDN. A crucial feature of our ICL network is that it can handle multiple channel models without retraining, enabled by the construction of model-specific context datasets. To improve convergence and robustness, we introduce three key innovations: (a) a curriculum learning (CL) strategy that smoothly transitions from supervised LMMSE-labeled imitation to unsupervised sum-rate maximization, (b) a self-evolving mechanism that dynamically expands and refines the context datasets for all channel models during CL-based training, and (c) a mismatch-aware extension that incorporates several mismatches into the general ICL framework and bypasses explicit channel calibrations. Ablation studies validate the effectiveness of the in-context architecture and enhanced training strategies. Simulation results over diverse communication environments show that the proposed scheme is able to rapidly adapt to both seen and unseen channel models without gradient-based parameter updates, and can mitigate the mismatch issues via intelligent context constructions. Furthermore, our scheme consistently outperforms the existing beamforming schemes under pilot-based settings, including the WMMSE benchmark and the recent Transformer-based methods.

---


### 11. [Are we Merging the Right Models? Impact of Expert Training Duration on Model Merging for LLMs](https://arxiv.org/abs/2607.11997)

**<font color=#1a73e8>作者：</font>** Nikita Kozodoi, Zainab Afolabi, Jack Butler  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-task model merging combines separately trained expert models into a single model that handles all tasks without co-training. Standard practice merges experts at their optimal validation loss. We challenge this convention by systematically studying how training duration of domain experts affects the quality of the merged model. We fine-tune experts on five domains (Math, Code, Instruction Following, Multilingual, and Safety) across three model sizes (Qwen 3.5 0.8B, 2B, and 4B), saving checkpoints from 25\% to 500\% of the optimal training steps and evaluating five merging methods at each duration. Our findings reveal a striking method-dependent pattern: simple averaging degrades sharply with overfitting, while sparsification-based methods achieve their best performance well past the validation optimum. We formalize this through bias-variance decomposition analysis, drawing a parallel to random forests where averaging benefits from high-variance individual learners. These results suggest that training duration and merging method should be chosen jointly rather than independently.

---


### 12. [SymbOmni: Evolving Agentic Omni Models via Symbolic Concept Learning](https://arxiv.org/abs/2607.12042)

**<font color=#1a73e8>作者：</font>** Jinxiu Liu, Jianru Li, Tanqing Kuang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual generation is increasingly ubiquitous in diverse domains, from text-to-image/video synthesis to multimodal interactive creation. Yet prevailing monolithic models remain fundamentally constrained by their inability to learn cumulatively and evolve autonomously, which is a limitation we term the "perpetual novice" problem. They lack mechanisms for structuring experience into reusable knowledge and therefore rely on brittle, "from-scratch" reasoning for each task, resulting in poor compositional generalization and inefficient knowledge retention. Motivated by these limitations, we propose SymbOmni, an agentic omni-model designed for cumulative evolution through Symbolic Concept Learning. At its core is the Symbolic Concept Box, an optimizable memory module that abstracts low-level operations into reusable Symbolic Workflow Instructions. SymbOmni operates through an induction-transduction cycle: experiences are abstracted into symbolic concepts (induction), which are then adaptively composed to solve novel tasks (transduction). The training is done by verbalized backpropagation with language-based feedback to enable continuous self-improvement without gradient-based model fine-tuning. Comprehensive experiments validate that (I) SymbOmni significantly outperforms existing agent-based systems for iterative creation and also surpasses closed-source models (e.g., Nano Banana, GPT-Image-1) in both image quality and task success rates; (II) SymbOmni effectively reduces token consumption by over 40% while maintaining competitive generation quality; and (III) SymbOmni enables effective continual learning by achieving cumulative gains across multiple online-learning benchmarks and setting a new state of the art.

---


### 13. [Agentic systems for breast cancer treatment recommendations](https://arxiv.org/abs/2607.12051)

**<font color=#1a73e8>作者：</font>** Vinicius Anjos de Almeida, Nícolas Henrique Borges, Leonardo Vicenzi 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly being explored for clinical decision support, but their reliability in complex oncology treatment planning remains unclear. We evaluated agentic LLM systems for breast cancer treatment recommendation generation using 72 real clinical cases across stages I to IV and 1,147 case-specific rubrics generated through Asymmetric Information Rubric Generation (AIRG), in which the rubric generator had access to real clinical decisions unavailable to the evaluated models. Seven pipelines were compared, including single-LLM baselines, tool-augmented systems, and multi-agent architectures with fact checking and autonomous subagent spawning. The best-performing configuration, Claude Opus 4.8 with the D&C+SA pipeline, achieved a global score of 0.594 $\pm$ 0.025. Tool use and increased agent autonomy had mixed effects, improving performance in some settings but degrading it in others. Performance varied by clinical domain and disease stage, and oncologist-led error analysis revealed persistent clinically relevant failures, including incorrect or missing recommendations, flawed justifications, citation errors, outdated claims, and overconfidence. These findings suggest that agentic LLM systems can generate clinically relevant breast cancer recommendations, but remain insufficient for unsupervised clinical use.

---


### 14. [The Capacity of Thought: Benchmarking Llama 3.2 in Semantic fMRI Neural Language Decoding and Improving the Huth Encoding-Model Baseline](https://arxiv.org/abs/2607.12079)

**<font color=#1a73e8>作者：</font>** Milos Suvakovic, Dom Marhoefer, Glenn Grant-Richards 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Decoding continuous language from fMRI signals remains a core challenge in non-invasive brain-computer interface research. We present two complementary investigations. First, we improve the Huth et al. ridge regression encoding pipeline through expanded voxel selection (10K->15K), substitution of GPT-2 medium for GPT-1 as the beam-search proposal model, and GPU-accelerated bootstrap training, achieving mean METEOR = 0.149 and BLEU-1 = 0.200 across three held-out narratives for subject UTS03 -- an 11% relative METEOR gain over our replication baseline. Second, we introduce fMRIFlamingo, which maps BOLD activity to a frozen Llama-3.2-1B with trainable gated cross-attention layers via a learned brain tokenizer and a Perceiver Resampler. Despite achieving 42.86% Top-1 accuracy on a 1-in-100 ranking task, well above chance, a blind control ablation with zeroed fMRI inputs yields near-identical scores, revealing that apparent decoding success is driven primarily by the frozen language prior rather than by neural input. These results demonstrate that high-capacity language models do not inherently improve fMRI decoding and can actively obscure failures without rigorous blind-control evaluation.

---


### 15. [CityBehavEx: A Scalable and Empirically Validated LLM-Assisted Urban Simulation Platform](https://arxiv.org/abs/2607.12086)

**<font color=#1a73e8>作者：</font>** Gustavo H. Santos, Aline Viana, Thiago H Silva  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent LLM-based multi-agent urban simulators can generate semantically rich city routines, but they remain costly to scale and are often weakly validated against empirical mobility patterns. We present CityBehavEx, an interactive LLM-assisted urban simulation platform that scales to city-size populations, exposes agent behavior for inspection, supports empirical validation, and generates mobility patterns that better match real-world spatial, temporal, and semantic distributions. Instead of invoking large language models for every agent action, CityBehavEx combines established human mobility models with fine-tuned cross-encoders that estimate semantic alignment between agent profiles, schedules, and activity transitions. This design enables large-scale simulations, as demonstrated in a case study of 100,000 agents over 75 days in under one hour on a single consumer GPU. The platform allows users to define simulation regions, launch experiments, inspect trajectories and activity traces, debug unrealistic behaviors, and validate generated routines against real-world mobility, time-use, and semantic metrics.

---


### 16. [PFAdapter: Hierarchical LoRA Decomposition for Personalized Federated MLLMs](https://arxiv.org/abs/2607.12111)

**<font color=#1a73e8>作者：</font>** Jing Liu, Kun Yang, Yan Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Agentic AI systems are reshaping communications and networking by deploying autonomous intelligent agents capable of collaborative learning while maintaining data privacy at network edges. Within distributed network environments, Multimodal Large Language Models (MLLMs) serve as cognitive engines for edge devices, yet federated fine-tuning faces substantial challenges in balancing global knowledge aggregation with local adaptation under heterogeneous network conditions. Conventional federated protocols typically rely on uniform parameter aggregation, which conflates domain-invariant features with client-specific nuances, thereby resulting in suboptimal personalization and excessive communication overhead. To address these challenges, we propose PFAdapter, a communication-efficient framework introducing hierarchical LoRA decomposition to explicitly separate adapter parameters into global-shared and local-private components. Query and key projections are assigned to global synchronization for capturing universal multimodal semantics across the network, while value and output projections remain localized for edge-specific adaptation. Additionally, orthogonality regularization based on the Frobenius norm enforces strict separation between these components, preventing redundant feature learning. Selective aggregation protocols synchronize only global-shared components across the federated network, preserving local expertise and reducing communication costs by nearly 50%. Extensive experiments on VQA-RAD, SLAKE, Hateful Memes, and CrisisMMD datasets demonstrate that PFAdapter consistently outperforms state-of-the-art baselines, achieving accuracy improvements ranging from 2.4% to 4.8% across diverse edge intelligence tasks. Consequently, our framework establishes an efficient solution for agentic AI deployment in resource-constrained communication networks.

---


### 17. [Continual Learning with Elastic Regularization and Synthetic Replay for Federated MLLM Fine-Tuning](https://arxiv.org/abs/2607.12112)

**<font color=#1a73e8>作者：</font>** Jing Liu, Chenxuanyin Zou, Jiayang Ren 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated fine-tuning of Multimodal Large Language Models (MLLMs) across distributed networks enables privacy-sensitive adaptation to evolving data streams, yet a fundamental obstacle prevents robust deployment in dynamic environments: catastrophic forgetting, wherein sequential task updates erase previously acquired knowledge across visual, linguistic, and cross-modal representations. Addressing this challenge is especially critical for autonomous networked AI operating in safety-sensitive domains, such as content moderation, where reliable retention of prior knowledge underpins system integrity. To overcome this, we propose Federated Continual Multimodal Learning (FedCMM), a framework that embeds continual-learning safeguards into the federated optimization loop at three complementary levels. At the parameter level, modality-aware elastic weight consolidation computes separate Fisher information matrices for the vision encoder, language backbone, and cross-modal projector, providing granular, asymmetry-aware protection against modality-specific forgetting. At the data level, each client trains a lightweight local generative replay module to synthesize raw-data-free embedding-level multimodal replay tuples without any raw data sharing. At the aggregation level, Task-similarity-aware gradient aggregation autonomously filters and reweights client updates by gradient cosine similarity, suppressing conflicting directions and stabilizing the global learning trajectory. Extensive experiments on two benchmarks demonstrate that FedCMM consistently outperforms recent baselines on accuracy and backward transfer, confirming that holistic, modality-aware optimization enables robust evolutive adaptation across heterogeneous networked AI deployments.

---


### 18. [An Agentic AI Scientific Community for Automated Neural Operator Discovery](https://arxiv.org/abs/2607.12122)

**<font color=#1a73e8>作者：</font>** Luis Loo, Ulisses Braga-Neto  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present an agentic approach to autonomous neural operator discovery based on an AI scientific community, which consists of a swarm of virtual laboratories that interact under a citation-based economy of influence. Highly-cited labs found new labs that follow their research direction and replace non-performing labs. Each virtual lab contains three agents: an LLM planner that proposes an architecture, a numerical worker that trains and measures it, and an LLM reviewer that participates in cross-lab peer review. All labs share a common vocabulary consisting of DeepONet (branch-trunk), Fourier, Transformer (attention), wavelet, and residual convolutional neural operator building blocks. We evaluate the neural operator AI scientific community on five problems, namely piecewise regression, the linear advection and Burgers 1D PDEs, and the Navier-Stokes and Darcy flow 2D PDEs, while repeating the simulation three times for each problem. The results show that the neural operator AI scientific community is capable of discovering high-accuracy, low-parameter-count neural operator architectures. All 9,623 LLM calls are logged and audited, which reveals that the virtual lab LLM planners choose to hybridize in 99.8% of their logged decisions, consistently returning multi-family hybrids. Moreover, we conducted an ablation study by replacing the LLM agents in each lab by rule-based alternatives, which caused the scientific community to collapse to non-hybridized single-family stacks in several cases, showing that LLM agency is needed to preserve diversity. The results suggest a no-free-lunch theorem for neural operators: there is no universal winner. The code, configurations, and the complete LLM transcripts are released at this https URL.

---


### 19. [A Calibrated Multimodal Ensemble for Ambivalence/Hesitancy Recognition: System Description and Private-Test Submission Strategy](https://arxiv.org/abs/2607.12176)

**<font color=#1a73e8>作者：</font>** Josep Cabacas-Maso, Ismael Benito-Altamirano, Carles Ventura  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Ambivalence and hesitancy (A/H) undermine digital behaviour-change interventions, and recognizing them automatically from video is the goal of the ABAW A/H challenge on the BAH dataset. We describe our system for the 11th edition of the challenge: a calibrated, equal-weight ensemble of three fusion models over frozen face, audio, text, and pose embeddings, which reaches 0.7358 macro-F1 on the public test set. This year's private test, released on a disjoint set of 30 new participants, is scored on five allowed submissions; we report the configuration and rationale of each of our five submissions, and, where already available, the private-test score obtained. Our first submission, an exact replica of the calibrated ensemble tuned only on public validation, scored 0.7361 macro-F1 on the private test, matching our public-test estimate almost exactly and confirming the pipeline generalizes to unseen participants without leakage.

---


### 20. [The Emerging Paradigm of Geospatial Foundation Models: From Pre-Training to Agentic Reasoning](https://arxiv.org/abs/2607.12177)

**<font color=#1a73e8>作者：</font>** Shelley Cazares  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The analysis of satellite and aerial imagery has entered a new era with the advent of foundation models. This paper describes the concept of Geospatial Foundation Models (GeoFMs), which are artificial intelligence/machine learning (AI/ML) models pre-trained on massive geospatial datasets through varied methodologies. We first articulate the core paradigm shift that GeoFMs enable: a separation of duties, where large-scale model providers perform the computationally intensive pretraining, allowing domain experts to rapidly fine-tune or prompt these models for specific, mission-critical tasks. This approach democratizes access to state-of-the-art AI/ML while maintaining the security and confidentiality of the downstream task. We then explore the novel capabilities unlocked by different types of GeoFMs, distinguishing between the finetunable vision models produced by self-supervised techniques like masked auto-encoding, and the vision-language models produced by contrastive learning which enable zero-shot tasks like open-vocabulary image analysis. Next, we discuss the practical considerations for operationalizing GeoFMs, from performance-cost analysis to the broader MLOps ecosystem. To that end, we introduce a taxonomy of model adaptation strategies and propose a framework for domain experts to select the most cost-effective adaptation approach for their particular mission set. Finally, we present a forward-looking vision of Agentic Geospatial Reasoning, where Large Language Models act as intelligent orchestrators, leveraging GeoFMs as tools to answer high-level user queries in natural language and automate complex analytical workflows, moving the field from perception to cognition.

---


### 21. [Cost-Governed RAG: Unified Per-Tenant Cost Attribution Across Retrieval and Generation in Multi-Tenant LLM Systems](https://arxiv.org/abs/2607.12188)

**<font color=#1a73e8>作者：</font>** Navnit Shukla  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Enterprise Retrieval-Augmented Generation (RAG) deployments face a critical governance gap: while LLM generation cost is metered per token, the retrieval layer - vector memory, similarity compute, and embedding API calls - remains an unattributed shared cost, enabling invisible cross-subsidization among tenants. We present Cost-Governed RAG, an architecture that integrates a codebook-oblivious vector index (TurboVec) with a multi-tenant LLM governance gateway, creating a unified observability stack where embedding, retrieval, and generation costs are jointly attributable per tenant. The architecture exploits TurboVec's deterministic, closed-form memory formula to enable near-exact per-tenant retrieval cost calculation - a property unavailable in graph-based indexes with non-linear memory overhead. Deployed on Snowpark Container Services within a cloud data platform's governance boundary, the system achieves 99.96% end-to-end cost attribution accuracy across 100 simulated tenants (10M vectors, log-normal size distribution) with telemetry overhead below 0.04% of query latency. The architecture reduces retrieval infrastructure cost by 3.1-9.0x compared to managed vector database services under the pricing assumptions detailed in Section IV. We formalize a three-layer cost model and demonstrate that codebook-oblivious quantization enables deterministic per-tenant cost attribution while also removing the shared-codebook leakage surface present in trained quantizers - the latter observation being exploratory and subject to the limitations described in Section VII.

---


### 22. [Comparing Semantic Navigation in Humans and Large Language Models using Natural Language Processing](https://arxiv.org/abs/2607.12195)

**<font color=#1a73e8>作者：</font>** Gabriel Paris-Colombo, Rodrigo M. Cabral-Carvalho, Felipe D. Toro-Hernández  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Semantic memory retrieval can be conceptualized as navigation through conceptual space. We compared semantic search dynamics between humans and three large language models (GPT-4o, Gemini-2.5-Pro, Claude-Sonnet-4.5) using verbal fluency data. By applying trajectory-based NLP metrics to the items generated by 82 human participants and LLM output across eight temperature settings, we quantified three complementary dimensions: entropy (step size predictability), distance to next (successive semantic steps), and distance to centroid (global dispersion). Humans exhibited higher entropy, larger semantic steps and broader dispersion than all LLMs, indicating more variable and exploratory search. Temperature tuning produced only partial alignments, as individual metrics matched between humans and LLMs at specific settings, but no configuration reproduced the complete human profile (in all dimensions). These findings suggest that human semantic search implements a distinctive balance between local exploitation and global exploration that current model architectures fail to reproduce.

---


### 23. [A Threshold Exceedance Framework for CBRN Uplift Evaluation in Frontier Language Models](https://arxiv.org/abs/2607.12200)

**<font color=#1a73e8>作者：</font>** Rahul Gupta, Abhinav Mohanty, Payal Motwani 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As frontier language models advance, policymakers and model developers need methods for assessing whether model access materially increases a non-expert actor's ability to plan high-consequence Chemical, Biological, Radiological, or Nuclear (CBRN) misuse relative to public tools alone. Existing CBRN evaluations differ in non-expert definitions, threat scope, baselines, scoring rubrics, and decision rules, making results difficult to compare across studies. We introduce a Threshold Exceedance Criteria (TEC) framework that decomposes an uplift study into independently executable components: determining non-expert participant eligibility, defining the CBRN threat scope for the study, and statistically estimating material uplift. We then operationalize the TEC framework in a large-scale empirical study using a design that determines two forms of uplift: generative (where a model assists plan creation from scratch) and revisionist (where a model assists refinement of an existing plan). The study produced attack plans across the CBRN domains, which we evaluated through subject-matter-expert review to estimate generative and revisionist uplift. Applying the framework, our empirical study revealed domain heterogeneity: under this controlled pre-release evaluation, model-assisted plans sometimes received expert-equivalent instructional ratings, but confirmed material uplift was limited to the radiological domain. These findings informed mitigation and deployment-governance decisions rather than characterizing deployed model behavior. We conclude with methodological lessons for future CBRN uplift evaluations, emphasizing prespecified criteria, explicit baselines, separation of generative and revisionist estimates, and careful distinction between preliminary screening signals and confirmed risk determinations.

---


### 24. [RCWT: Measuring Task-Budget Displacement from Coordination Content in LLM Calls](https://arxiv.org/abs/2607.12216)

**<font color=#1a73e8>作者：</font>** Brenda Lelis, Rodrigo Cabral-Carvalho  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multi-agent and memory-augmented LLM systems often place coordination content, shared state, prior discussion, tool outputs, summaries, and role instructions, inside the same finite prompt used for the current task. This creates a practical allocation problem: every token spent on coordination is unavailable to task instructions or evidence when a call is assembled under a fixed context budget. We introduce the Roundtable Context Window Test (RCWT), a controlled protocol for measuring this task-budget displacement effect. RCWT varies coordination content while controlling total budget, position order, task family, and scoring. In the main context-dependent recall task at $W=4096$, three commercial models remain near baseline through moderate overhead and then degrade sharply once residual reference evidence falls to a few hundred tokens. Window-scaling summaries are consistent with a task-specific residual-budget interpretation rather than a fixed percentage threshold, but we treat this as descriptive evidence rather than a universal law. To test whether the fixed-budget cliff persists when task evidence remains intact, we add an intact-task ablation: the full task/reference block is kept present while coordination tokens increase by expanding total prompt length. In that setting, all tested calls return every scored field correctly across GPT-4.1-mini, Claude Haiku 4.5, and Gemini 2.5 Flash up to a 95\% coordination ratio. This ablation narrows the claim: the main RCWT cliff is best read as task-budget displacement, not as proof that coordination volume alone causes semantic interference in the original open-ended task. RCWT is therefore a measurement primitive for context-allocation budgeting, not a complete theory of multi-agent benefit or session-level coordination.

---


### 25. [Rethinking the Evaluation of Harness Evolution for Agents](https://arxiv.org/abs/2607.12227)

**<font color=#1a73e8>作者：</font>** Yike Wang, Huaisheng Zhu, Zhengyu Hu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We revisit the evaluation of automatic harness evolution for LLM agents. Existing harness evolution methods use unit test cases to search for harness configurations and then report final performance on the same public benchmark. This protocol raises two fundamental concerns. First, harness evolution is itself an iterative search procedure that repeatedly evaluates and revises candidate harnesses using task feedback. As in agentic test-time scaling, it should therefore be compared with simple task-level search baselines under matched feedback and inference budgets to determine whether its gains arise from improved harness design or from additional search alone. Second, because the search and the final evaluation share the same benchmark, the reported gains risk overfitting to that specific task set. To address these concerns, we conduct an extensive evaluation comparing harness evolution with simple test-time scaling and discovery baselines under comparable feedback and inference budgets, and also evaluate evolved harnesses on held-out tasks to assess whether the discovered improvements generalize. Experiments on Terminal-Bench 2.1 with GPT-5.4 and Claude Opus 4.6 show that automatic harness evolution does not consistently outperform simple test-time scaling methods and exhibits limited generalization. Our results raise important questions about the effectiveness of automatic harness evolution and highlight the need for fairer evaluation protocols and benchmarks for automatic harness design. Our code is available at this https URL.

---


### 26. [Fin-Analyst at FinMMEval 2026 Task 3: A Live Hybrid Trading Agent with LLM Specialists and Rule-Based Signals](https://arxiv.org/abs/2607.12233)

**<font color=#1a73e8>作者：</font>** Mohotarema Rashid, Lingzi Hong, Junhua Ding 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) trading agents show promising performance in equity markets, yet remain narrowly focused on US equities with little evidence from live deployment. We present Fin-Analyst, a hybrid agent for FinMMEval 2026 Task 3: an eight-specialist LLM pipeline over news, SEC filings, fundamentals, analyst forecasts, technical indicators, and social sentiment, aggregated by a Meta-Agent for Tesla (TSLA), and a lightweight rule based three-signal vote for Bitcoin (BTC). On the final official leaderboard (accessed 2026-07-05), Fin-Analyst ranks first of all agents on TSLA with a +13.51% return, +28.33 points over Buy-and-Hold (Sharpe 4.10, 88% win rate), while the BTC vote ends flat yet well above a sharply falling baseline. Relative to the interim performance, the asset ranking reversed, indicating that short live windows yield volatility-sensitive rankings. Ablation identifies event-driven 8-K disclosures as the most influential TSLA signal. Error analysis shows that the memoryless agents repeat wrong calls for days at a time, and that the fixed-threshold BTC rules lost money by trading on noise in a sideways market while the LLM pipeline gained under similar conditions, motivating a memory-aware, LLM-based successor for both assets.

---


### 27. [Speculate with Memory: Lossless Acceleration for LLM Agents](https://arxiv.org/abs/2607.12236)

**<font color=#1a73e8>作者：</font>** Yu Li, Qinyuan Ye, Prafulla Kumar Choubey 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Speculative execution accelerates LLM agents by using a smaller, cheaper model to predict and pre-launch the next step while the environment is idle. However, existing speculators are stateless and discard all information between tasks, preventing prediction quality from improving with experience. We equip the speculator with three online memory systems that learn from past agent trajectories: a contrastive transition table tracking action-sequence statistics, an episodic memory retrieving contextually similar segments, and a confusion tracker suppressing recurring errors. We evaluate this approach on six benchmarks spanning three speculation types: action prediction, observation prediction, and chained prediction. Memory-augmented speculation yields a 19--39\% relative accuracy improvement on action prediction and up to a $2.5\times$ increase on observation prediction tasks with repetitive action spaces. These gains grow continuously as memory accumulates and generalize across speculator models of varying cost. All speculation is lossless because it runs during idle time at zero added wall-clock cost, and the actor's trajectory is identical to non-speculative execution.

---


### 28. [On-Device Deep Research at 4B: Exposure Bounds Faithfulness, Retrieval Bounds Coverage](https://arxiv.org/abs/2607.12257)

**<font color=#1a73e8>作者：</font>** Vinay Kumar Chaganti  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> On-device research agents search a corpus, read sources, and write a cited brief on a personal laptop. Whether their citations are faithful, and at what cost, is unmeasured for a deployable small model. This study fixes one 4B generator on a 24 GB laptop and asks what makes its citations faithful. It separates two quantities usually reported as one number. Cited claim faithfulness asks whether the cited source supports the claim. Trustworthy coverage asks whether the agent also cites the right sources. The study crosses how much of each source the generator sees, 400 against 1500 characters, with the quality of the sources supplied, gold papers against retrieved papers. Two levers fall out, and they act on different outcomes. Exposure sets faithfulness. More of each source lifts faithfulness from 0.45 to 0.58 on retrieved sources and from 0.37 to 0.58 on gold sources, and the two settings converge, so faithfulness is bound by exposure, not by whether the source is correct. The exposure lift is robust to a second, independent judge; the exact convergence is tight under the primary judge and only approximate under the second. Retrieval sets coverage. Trustworthy coverage stays near 0.22 on retrieved sources at any exposure, because recall is held near 0.40, so exposure cannot fix which sources are cited. The extra exposure costs about 235 output tokens. The practical recipe is to raise per source exposure first, cheaply, and then treat retrieval recall as the only remaining lever.

---


### 29. [From Many to Meaningful: Feature-Guided Zero-Shot Chronic Kidney Disease Screening Using Large Language Models](https://arxiv.org/abs/2607.12260)

**<font color=#1a73e8>作者：</font>** Muhammad Ashad Kabir, Sirajam Munira  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Early screening of chronic kidney disease (CKD) is essential for preventing irreversible progression; however, many machine learning (ML)-based screening methods remain difficult to deploy in community and resource-limited screening settings due to their reliance on large labeled datasets, resource-intensive pathology tests, or high-dimensional clinical features, and limited robustness to population and distributional shifts. This study examines the feasibility of using large language models (LLMs) for early-stage CKD screening in a zero-shot setting, without dataset-specific training. We propose a feature-guided zero-shot framework that evaluates LLM performance using a selected set of clinically meaningful, readily available community-based features, rather than exhaustive clinical inputs. Feature selection was guided by ML-based analysis to identify a compact, clinically relevant subset of variables. Tabular patient records were subsequently serialized into text using standardized prompt templates to enable zero-shot inference. The zero-shot performance of four LLMs (LLaMA-3, Qwen-3, Mistral, and GPT-4o-mini) was evaluated using both the full feature set and the selected subset. Generalizability was assessed across three heterogeneous CKD datasets spanning three countries. Across models and datasets, the selected feature set yielded consistent and statistically significant improvements in balanced accuracy and probability estimates, achieving performance levels suitable for screening purposes. These findings suggest that LLMs can support clinically meaningful, training-free CKD screening using minimal community-accessible patient features, offering a practical complement to conventional ML methods in real-world screening contexts.

---


### 30. [Saturation Makes Quantization Error Additive: A Coverage Model with a Certificate](https://arxiv.org/abs/2607.12266)

**<font color=#1a73e8>作者：</font>** Joshua Hill  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mixed-precision quantization must decide which parts of a model to keep at higher precision. A common premise, shared by sensitivity-based methods such as HAWQ and CoopQ, is that the loss from quantizing a set of layers can be reconstructed from per-layer or pairwise sensitivities measured in isolation. We test this premise at the 4-bit weight-and-activation precisions now being deployed, treating the change in loss $f(S)$ from quantizing a layer set $S$ as a set function on the Boolean cube and analyzing it through two classical changes of basis. This analysis yields two findings. First, across configurations drawn from the deployment distribution, 85--93\% of the variance of $f$ is explained by per-layer effects alone. Second, a monotone transform of a sum of per-layer terms reproduces $f$'s ranking of configurations, misordering at most 2\% of pairs.
We propose the coverage model $f(S)=c\bigl(1-\prod_{i\in S}(1-a_i)\bigr)$, which reproduces the measured variance profile of $f$ to within a few percent from its $L$ fitted break-rates. This structure supports two predictors of a configuration's loss, each with $L+1$ parameters. The additive model is the optimal first-order predictor. By Parseval's identity its mean-squared error equals the variance of $f$ left unexplained by per-layer effects, which we measure on full lattices, estimate out of sample at full-network scale, and report with every result as a certificate of how well any additive model can do. The coverage model itself is the second predictor.
As allocators at matched memory, they attain the lowest KL divergence among the compared allocators on models from 30B to 355B parameters. Below four bits, the resulting allocations continue to solve code and reasoning tasks at budgets where allocations from gradient sensitivities no longer produce terminating generations.

---


### 31. [Auditing Data Leakage in Whole-Slide Image Multimodal Benchmarks](https://arxiv.org/abs/2607.12278)

**<font color=#1a73e8>作者：</font>** Wenhao Zhang, Zhongliang Zhou, John Kang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent vision-language models (VLMs) for computational pathology report striking zero-shot performance on whole-slide image (WSI) visual question answering (VQA) benchmarks. We audit these claims and find them fundamentally compromised by data leakage at two hierarchical levels: patient-level leakage, where slides from the same case appear in both training and test folds, and institutional-level leakage, where different cases nonetheless share staining-batch and scanner signatures through a common Tissue Source Site (TSS). By tracing canonical slide, case, and TSS identifiers across major public resources, we document case level train test overlaps of 92.3~100% on TCGA-derived benchmarks, together with near-complete TSS overlap. We further demonstrate that both leakage levels are linearly decodable from foundation-model feature space, that they induce a measurable accuracy gap between leaked and audit-clean cases on a published checkpoint, and that across multiple published WSI VLMs, peak reported accuracies concentrate on the most heavily contaminated benchmarks. Therefore, the current WSI VQA evaluation cannot distinguish genuine multimodal reasoning from nearest-neighbor retrieval over memorized institutional and patient-specific artifacts. Finally, we outline concrete recommendations for contamination-free evaluation. By addressing benchmark construction, provenance disclosure, and automated overlap auditing, we aim to guide future research toward verifiable claims of progress.

---


### 32. [A Shared Subcircuit Lets LLMs Count Down Across Tasks](https://arxiv.org/abs/2607.12279)

**<font color=#1a73e8>作者：</font>** Jacob Dunefsky, Wes Gurnee, Emmanuel Ameisen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Writing a sentence of exactly twelve words; ending a DNA sequence at the right codon; formatting an ASCII table. These are all tasks that language models can do that requires tracking how many tokens remain before a target. In this work, we identify in Llama-3.1-70B-Instruct a general mechanism for performing these tasks: a "countdown subcircuit" that compares the current position to a goal length and estimates the time remaining until then. We first isolate a countdown subcircuit in a controlled setting, in which the model is tasked with writing a fixed-length sentence ending in a specified word. We then investigate the geometry of the representations used by the subcircuit, and find that the subcircuit uses an identical motif previously identified in a frontier LLM on a separate task, thus suggesting that this motif is shared across models. Finally, we use unsupervised probing on a natural language dataset to find a variety of other tasks where this subcircuit is used, including tasks where the goal length is inferred from context rather than explicitly stated. Our work suggests that reverse-engineering subcircuits allows us to understand how behaviors generalize from a single example to many different tasks and even models.

---


### 33. [LakeQuest: A Three-Domain Benchmark for Grounded Question Answering across Data Lakes](https://arxiv.org/abs/2607.12310)

**<font color=#1a73e8>作者：</font>** Michael Solodko, Steven Gong, Guangwei Yu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While modern question answering (QA) systems excel on clean, schema-aligned corpora, real-world knowledge is rarely so neatly packaged. Answering questions over enterprise and scientific data lakes requires systems to navigate heterogeneous, weakly structured collections of tables, passages, and linked metadata. Current benchmarks abstract away this noisy discovery process, failing to evaluate end-to-end performance. To bridge this gap, we introduce LakeQuest, a human-validated benchmark of 9,846 QA pairs designed to evaluate the end-to-end retrieve-and-synthesize pipeline over realistic data lakes. LakeQuest spans three diverse domains (AI/ML metadata, retail banking, and multimodal biomedical drug information) and pairs every question with exact, modality-aware evidence pointers. By isolating source discovery from cross-modal synthesis, LakeQuest exposes critical failure modes in modern QA systems. Our baseline evaluations, including standard Retrieval-Augmented Generation (RAG) and agentic tool-use methods, reveal that high-quality retrieval does not guarantee correct reasoning. Systems consistently struggle with relation chaining in metadata graphs, policy grounding in bank ledgers, and joint tabular QA in biomedical contexts, highlighting the need for robust discovery and faithful cross-file composition mechanisms in future agentic QA systems.

---


### 34. [DM-KG: A Novel Method for Boosting Spatial Cognition of Vision-Language Models in Street View Imagery](https://arxiv.org/abs/2607.12319)

**<font color=#1a73e8>作者：</font>** Xinyue Xu, Zheng Zhang, Kunyang Ma 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> As vision-language models (VLMs) are increasingly deployed in geospatial question answering and visual scene understanding, improving their spatial cognition capability on street view imagery for complex logical reasoning has emerged as a key research priority. However, existing VLMs frequently suffer from "spatial semantic hallucinations" when perceiving object locations, distances, and directions in real-world street view scenes. Furthermore, such errors are often recalcitrant to tracing and calibration, posing a critical bottleneck for their practical deployment in geospatial tasks. To address this pressing challenge, this study proposes DM-KG (Direction-Metric Knowledge Graph), a structurally grounded spatial representation framework for street view imagery. By explicitly extracting directional and metric relationships between entities from a single 2D image, this framework enhances the spatial reasoning accuracy of VLMs through a structured knowledge graph. Specifically, we integrate panoptic segmentation with metric depth estimation to robustly compute entity-level 3D spatial coordinates. Subsequently, we encode the clock azimuths and Euclidean distances of entity pairs into a JSON-formatted knowledge graph, which is injected into the VLM as an explicit geometric prior to guide spatial reasoning. Experimental results on public spatial question-answering (QA) benchmarks demonstrate that DM-KG reduces the mean absolute error (MAE) in distance estimation by 31.1% and the mean angular error in direction judgment by 65.8%, while simultaneously maintaining a high QA success rate. By establishing a complete, augmented reasoning pipeline, this research significantly improves the spatial cognitive capabilities of VLMs in street view scenarios, thereby providing a flexible, generalized, and interpretable framework for geographic visual question answering (GeoVQA) in open environments.

---


### 35. [Evaluating Health Misinformation in Low-Resource Languages: Integrating Small Language Models with a Culturally-Sensitive Responsible NLP Framework (Bangla as a Case Study)](https://arxiv.org/abs/2607.12336)

**<font color=#1a73e8>作者：</font>** Farnaz Farid, Raihan Alam, Al Al-Areqi 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Artificial Intelligence (AI) technologies, while serving as a foundational enabler for modern social media and digital health services, exert a bivalent effect by simultaneously acting as a combatant against and a spread vector for misinformation. A prevalent challenge in mitigating this issue arises in non-English contexts and low socioeconomic classes, where limited data hinders the training of AI models for effective detection. Consequently, culturally and linguistically diverse (CALD) communities struggle to access trustworthy health information through AI-driven tools. Current AI tools underperform due to a lack of training data and are largely unable to consider language nuances and traditions in non-English contexts. This research addresses these gaps by proposing a CALD-friendly AI-based health misinformation detector and providing a dashboard for medical professionals to analyse this misinformation, a critical step toward mitigating a growing concern among CALD populations. To this end, we conduct a series of experiments using a Bangla-translated health misinformation dataset to evaluate the performance of various Small Language Models (SLMs). SLMs are particularly relevant in this context given the frequent underperformance of Large Language Models (LLMs), which often stems from insufficient domain-specific knowledge and the prohibitive costs of resource-intensive fine-tuning. The results demonstrate that Phi-4 is the superior model, achieving an ideal balance between precision and recall in claim extraction. Then, to mitigate the limitations of SLMs, we design and test a novel health misinformation detection framework grounded in Responsible Natural Language Processing (NLP), which incorporates cultural sensitivity, potential for harm, and communication quality, thereby providing a holistic lens for evaluating misinformation in low-resource languages.

---


### 36. [How Many Tasks Are Enough for Agent Benchmark Decisions? A Replay Analysis of Public LLM Agent Benchmarks](https://arxiv.org/abs/2607.12338)

**<font color=#1a73e8>作者：</font>** Wei-Jung Huang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agent benchmarks often compare two agents after all tasks have run, but costly evaluations make partial runs tempting. A task fraction alone does not show whether a partial run supports the same pairwise conclusion as the completed benchmark. We study this question by replaying completed public task-level records from SWE-bench, AppWorld, and tau-bench. A partial budget counts as enough only when it supports the completed benchmark's decision, covers required task groups, and leaves no more than a target fraction of comparisons unresolved. The required task fraction varies sharply. At the strict 0 percentage point threshold on a 5 percentage point budget grid, AppWorld first meets all targets at 15 percent, tau-bench at 25 percent, and SWE-bench Verified at 90 percent; SWE-bench Lite does not meet all targets by 95 percent under the primary coverage rule. Partial-evaluation reports should state how much one agent must outperform another, how tasks are selected, what coverage rule is required, what decision rule is used, and how many comparisons may remain unresolved.

---


### 37. [IQA-T1: Tool-based Visual Evidence Reasoning for Image Quality Assessment](https://arxiv.org/abs/2607.12375)

**<font color=#1a73e8>作者：</font>** Jinjian Wu, Jiaqi Tang, Wei Wei 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image Quality Assessment (IQA) in open-world environments remains challenging due to limited generalization and interpretability. Recent approaches based on multimodal large language models (MLLMs) introduce textual reasoning for quality prediction, yet their judgments rely heavily on semantically biased internal representations, making them insensitive to low-level perceptual degradations. We propose IQA-T1, a tool-based visual evidence reasoning framework that augments MLLM reasoning with explicit perceptual observations. During inference, the model autonomously invokes specialized analysis tools to generate structured visual evidence, such as noise residual maps, gradient statistics, and frequency spectra, which are progressively integrated into the reasoning process. To support this paradigm, we construct Q-Tool, a dataset containing 11k multimodal reasoning chains grounded in tool-generated evidence. Extensive experiments on seven IQA benchmarks show that IQA-T1 achieves the best overall performance across datasets while producing interpretable and evidence-grounded quality assessments. Code and dataset are available at this https URL.

---


### 38. [PM-Bench: Evaluating Prospective Memory in LLM Agents](https://arxiv.org/abs/2607.12385)

**<font color=#1a73e8>作者：</font>** Genglin Liu, Saadia Gabriel  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A significant challenge in agentic AI is prospective memory: the ability to execute an intention at a specific future cue or state while other activities are ongoing. We introduce PM-Bench, a text-based benchmark for measuring prospective memory capabilities in modern LLM agents. Inspired by the Virtual Week paradigm from cognitive science, PM-Bench evaluates how well LLM agents maintain user intentions, execute delayed intentions, and monitor latent environment changes. Over the course of a simulated seven-day week, agents must continue an ongoing activity while deciding whether any deferred task is due. We compare eight state-of-the-art LLMs on PM-Bench under eight different agent configurations. PM-Bench proves challenging across all settings: the best method, a GPT-5.4 agent, reaches only 65.1\% F1 score under our evaluation. Furthermore, no single strategy for improving prospective memory dominates across models. We release PM-Bench as a controlled testbed for diagnosing these failures and developing training or inference-time interventions that support reliable prospective behavior.

---


### 39. [Critic Experience Bank: Self-Evolving Step-Level Confidence Estimation for LLM Agents](https://arxiv.org/abs/2607.12397)

**<font color=#1a73e8>作者：</font>** Yaopei Zeng, Congchao Wang, JianHang Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents act in external environments where each action changes the state that later decisions condition on, and where a single wrong step can waste interaction budget or trigger irreversible side effects long before the final failure is observed. Reliable deployment therefore requires \emph{step-level confidence estimation}: a calibrated probability that each proposed action is productive, available \emph{before} the action is executed. Existing LLM confidence estimators are designed to score a response from the given prompt, but agent confidence also depends on execution consequences: whether similar actions in similar situations actually advanced the task after the environment responded. We introduce the \method (\methodshort), a self-evolving critic framework in which an LLM critic accumulates evidence from its own past judgments and their observed consequences. After each trajectory, a hindsight LLM that sees the full execution feedback votes on whether each step was productive. The resulting pseudo-labels populate a memory bank from which related productive and unproductive experiences are retrieved into the critic's prompt whenever a similar step recurs. \methodshort requires no training and uses no ground truth step labels. Across three agent benchmarks and three critic backbones, \methodshort attains the best calibration (ECE and Brier) and ranking (AUC) in every dataset--critic combination, reducing ECE by up to $54\%$ relative to the strongest training-free baseline.

---


### 40. [Isolation as a First-Class Principle for LLM-Agent System Safety: Concepts, Taxonomy, Challenges and Future Directions](https://arxiv.org/abs/2607.12406)

**<font color=#1a73e8>作者：</font>** Huihao Jing, Wenbin Hu, Shaojin Chen 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The capability of LLM agents to function as the ``brain'' of a system fundamentally expands the scope of analysis beyond a standalone model. Consequently, safety is no longer only about input--output content alignment. It also concerns system behavior and real-world execution outcomes. However, the current literature is fragmented across attack types, applications, and benchmarks. This makes it hard to explain why failures such as prompt injection, tool misuse, and memory poisoning often share the same structural cause, and how they spread through an agent workflow. In this survey, we treat isolation as a first-class principle for LLM-agent system safety. By isolation, we refer to the separation of user inputs, tool access, execution channels, inter-agent communication, and environment-originated context. We organize the literature with a boundary-centric taxonomy of five boundaries: user-agent, agent-tool, agent-execution, agent-agent, and system-environment. This view helps identify where the loss of isolation first occurs, how compromise propagates across boundaries, and which defenses are most relevant at each interface. We also summarize cross-boundary failure paths, discuss open challenges, and outline a research agenda for isolation-by-construction in future agent systems.

---


### 41. [Virtual Chromoendscopy with Tunable Visibility Enhancement](https://arxiv.org/abs/2607.12416)

**<font color=#1a73e8>作者：</font>** Yuhi Kanno, Yusuke Monno, Sho Suzuki 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Chromoendoscopy (CE) is a common clinical practice that sprays indigo carmine blue dye onto the gastric surface to improve the visibility of gastric lesions, such as an early cancer. While CE is effective in detecting the lesions, preparing and spraying the dye needs additional cost and time, which is undesirable both for patients and medical practitioners. To overcome this issue, virtual chromoendoscopy (V-CE) was recently proposed, which applies a learned image translation model to virtually generate a CE image from a standard endoscopy (SE) image. In this paper, we propose virtual enhanced chromoendoscopy (V-ECE) that combines V-CE with image enhancement techniques to further improve the visibility of gastric lesions. Because a desired enhancement level depends on the inspected lesion and the practitioner's preference, we introduce a novel image translation model that can generate V-ECE images using an enhancement level tunable by a user. Experimental results demonstrate that our proposed model can plausibly generate V-ECE images with various enhancement levels using a unified model.

---


### 42. [MQAdapter: Multi-Modal Quantum Adapter for Coarse-to-Fine VLM Fine-tuning](https://arxiv.org/abs/2607.12418)

**<font color=#1a73e8>作者：</font>** Yumiao Zhao, Bo Jiang, Min Lu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large-scale Vision-Language Models have demonstrated impressive transfer learning capabilities across a wide range of tasks. For few-shot classification, we observe that VLMs exhibit a notable ability to filter candidate categories and thus achieve high Top-K accuracy. However, they often struggle with fine-grained discrimination among visually similar categories, resulting in unsatisfactory Top-1 performance, as shown in Figure 1. Existing studies on VLM adapters generally focus on global alignment between visual and textual representations in the feature space, but fail to exploit semantically similar categories to refine fine-grained visual representations. Based on these observations, we propose a novel coarse-to-fine VLM fine-tuning approach for few-shot learning that leverages quantum computation, termed the Multi-Modal Quantum Adapter (MQAdapter). Specifically, MQAdapter first retrieves the Top-K category candidates most similar to the input image and uses them as semantic anchors. It then employs a cross-modal quantum learning mechanism to refine visual features under the guidance of these anchors. The core of this mechanism is the encoding of visual and textual features into quantum states. By leveraging quantum entanglement and superposition in a high-dimensional Hilbert space, MQAdapter effectively models higher-order cross-modal interactions, producing more discriminative representations than traditional Euclidean adapters. MQAdapter is parameter-efficient and can be integrated with various existing fine-tuning algorithms to achieve further performance gains. Evaluations on 15 datasets demonstrate the effectiveness of MQAdapter while requiring fewer trainable parameters.

---


### 43. [The Computational Basis of Confidence in Large Language Models](https://arxiv.org/abs/2607.12447)

**<font color=#1a73e8>作者：</font>** Dharshan Kumaran, Viorica Patraucean, Maks Ovsanikov 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reliable confidence -- the probability that a model's own answer is correct -- is essential for the trustworthy deployment of language models. Existing work has largely evaluated confidence by how well it predicts correctness and whether it is calibrated, leaving open a more fundamental question: what does the confidence signal itself represent? Answer logits may reflect a latent decision variable sufficient to compute normative confidence, or instead a heuristic preference signal that combines the available evidence in a non-Bayesian manner. We address this using statistical decision confidence (SDC), a normative framework from computational neuroscience. Treating the answer-logit difference (LD) as a candidate readout of the latent decision variable, we test the qualitative signatures predicted by SDC. Across three perceptual discrimination tasks and a memory-based decision task, spanning three multimodal non-reasoning models and one reasoning model, LD satisfied these signatures -- including the diagnostic correct/error folded-X pattern -- showing that, in these settings, answer logits behave as monotonic readouts of a latent decision variable rather than heuristic preference scores. In complex visual reasoning, LD continued to predict correctness beyond objective task difficulty, but the full geometric signatures of SDC were absent, illustrating the current boundary of the framework when explicit normative process models are unavailable. These results provide a computational account of confidence in multimodal language models, delineate when answer logits behave as readouts of a latent decision variable, and establish SDC as a unifying framework for studying confidence across biological and artificial intelligence.

---


### 44. [Exploring Zero-Shot Foundation Models for Multivariate Time Series Anomaly Detection](https://arxiv.org/abs/2607.12454)

**<font color=#1a73e8>作者：</font>** Martin Uray, Saverio Messineo, Roland Kwitt 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multivariate Time Series Anomaly Detection (MTSAD) is essential for reliability and safety in domains such as industrial process monitoring and financial risk management, yet conventional approaches rely on application-specific models that are costly to train and hard to scale. Foundation Models (FMs), pre-trained on broad data with strong zero-shot generalization, have recently become available for univariate time series forecasting, raising the question of whether they can address MTSAD without task-specific training. We investigate the zero-shot application of a univariate forecasting FM, TimesFM, to industrial MTSAD on the Secure Water Treatment (SWaT) benchmark, evaluating two strategies: treating the FM as a per-feature forecaster with thresholded prediction errors, and as an embedder whose intermediate representations feed standard outlier detectors. Neither of our proposed setups is competitive with established baselines; embeddings reveal only partial separation between normal and anomalous segments, insufficient for reliable detection. The cause is that the FM is too effective at capturing temporal dynamics, yielding low error even within fully anomalous windows, so persistent anomalies become indistinguishable from normal behavior. However, these observations yield valuable insights: the error peaks at anomaly boundaries, indicating FMs reliably detect distribution changes. We conclude that the proposed naive zero-shot FMs are unsuitable for MTSAD but promising for change-point detection.

---


### 45. [EVOQUANT: Self-Evolving Verifier-Guided Strategy Optimization for Robust Quantitative Trading](https://arxiv.org/abs/2607.12455)

**<font color=#1a73e8>作者：</font>** Jie Mao, Changlun Li, Xiang Li 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Quantitative strategy optimization remains largely manual, requiring domain experts to identify weak signals, tune risk-control rules, and repeatedly validate iterative revisions. Large language models can accelerate this process, but directly relying on them to rewrite trading strategies often introduces hallucinated edits, strategy drift, and backtest overfitting. We propose EVOQUANT, a self-Evolving Verifier-guided framework for strategy Optimization in Quantitative trading. Our method utilizes LLMs to deeply diagnose performance bottlenecks, generates semantically controlled candidate edits, selects the best strategy through a multi-stage verification pipeline, and distills optimization experience into reusable knowledge for continual self-improvement. We evaluate our method using seven representative strategies: four from the A-share market and three from the Crypto market. Experimental results show that our method significantly improves the Sharpe ratio across all tested strategies: the average test Sharpe increases from -0.298 to 0.538, and the best-performing strategy achieves a 199% relative improvement. Ablation studies and stress tests under stricter conditions further validate the effectiveness and robustness of the framework. Overall, this work transforms quantitative strategy optimization from costly manual trial and error into an automated and verifiable iterative paradigm, offering a new path for applying large language models to financial strategy research.

---


### 46. [Function-Aware Fill-in-the-Middle as Mid-Training for Coding Agent Foundation Models](https://arxiv.org/abs/2607.12463)

**<font color=#1a73e8>作者：</font>** Yubo Wang, Jiarong Liang, Yuxuan Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Coding agents must integrate external tool returns into ongoing reasoning - a capability that standard left-to-right pretraining on code exposes only in its forward direction. We observe that the action-observation-continuation loop of a coding agent is structurally isomorphic to a function call site, where a caller binds arguments, a callee returns a value computed elsewhere, and downstream code consumes that value. This conditioning structure exists at internet scale in ordinary code. We exploit it through function-aware fill-in-the-middle (FIM) mid-training: a self-supervised objective that masks functions selected via program dependency graph analysis and a complexity-inferability double criterion. We mid-train Qwen2.5-Coder-Instruct (7B/14B) and Qwen3-8B on a 2.6B-token decontaminated corpus drawn from 968 GitHub repositories, then apply existing agentic post-training pipelines. Mid-training improves SWE-Bench-Verified by +2.8/+3.0 at 7B/14B and by +3.2 on Qwen3-8B; SWE-Bench-Lite gains are +3.7/+4.0/+5.4 on the same models. The improvement holds across two post-training pipelines (R2E-Gym, SWE-Smith) and on a non-Qwen2.5 base (Qwen3-8B with SWE-Lego). Beyond in-domain gains, mid-training also mitigates the capability erosion that agentic post-training otherwise inflicts on non-agent coding (e.g., LiveCodeBench) and non-coding tool-use benchmarks (tau-bench, BFCL): although the mid-training corpus contains Python code only, the function-call inductive bias survives post-training and yields consistent gains.

---


### 47. [From Observation to Insight: Mechanistic World Models and the Quest for Autonomous Discovery](https://arxiv.org/abs/2607.12474)

**<font color=#1a73e8>作者：</font>** Ingmar Posner, Anson Lei, Bernhard Schölkopf  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent advances in foundation models have transformed AI for Science, enabling remarkably accurate predictive performance across domains ranging from protein folding to weather forecasting. Yet prediction alone does not constitute scientific discovery. Scientific understanding depends on uncovering the reusable explanatory mechanisms that generate observations, whereas contemporary machine learning remains fundamentally organised around predictive mappings rather than explanatory structure. In this paper, we argue that scientific discovery is fundamentally a problem of knowledge organisation. To this end, we introduce Mechanistic World Models, a new design paradigm that places reusable mechanisms at the centre of representation, computation and learning. Drawing on insights from the philosophy of science, we derive the computational capabilities required for discovery, identify the design principles and inductive pressures that encourage explanatory knowledge to emerge, and formalise the anatomy of a mechanism-centric world model. Finally, we show how diverse research directions including mechanistic interpretability, causal representation learning, equation discovery and modular architectures capture complementary ingredients of this paradigm while lacking a unified framework. We propose Mechanistic World Models as a conceptual foundation and computational blueprint for moving AI beyond predictive forecasting towards autonomous scientific discovery.

---


### 48. [Self in Space: Benchmarking Self-Awareness and Spatial Cognition in UAV Embodied Intelligence](https://arxiv.org/abs/2607.12477)

**<font color=#1a73e8>作者：</font>** Zhishan Zou, Guoyan Sun, Zhiwei Wei 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autonomous UAV systems increasingly rely on multimodal large language models (MLLMs) to operate in complex real-world environments. Such embodied scenarios require not only understanding the surrounding space but also maintaining a coherent representation of the agent itself. However, existing UAV-oriented approaches and benchmarks remain largely environment-centric, primarily focusing on spatial understanding tasks, with the agent's self-awareness remaining implicit. To address this gap, we introduce SIS-Bench, a benchmark for evaluating embodied spatial intelligence in UAV scenarios under a unified self-in-space formulation. SIS-Bench organizes evaluation along two complementary dimensions, space and self, and a three-level hierarchy of perception, memory, and reasoning. It contains 4,856 question--answer pairs across 13 tasks derived from 1,646 real-world UAV videos through a task-conditioned construction pipeline with expert verification. Extensive evaluations reveal that current MLLMs exhibit fundamental limitations in modeling dynamic and agent-centered processes. In particular, we observe a clear imbalance between spatial cognition and self-awareness, as well as a progressive performance degradation across cognitive levels. Motivated by these findings, we further explore a motion-aware representation that incorporates self-related dynamics through optical flow and visual feature fusion. Experimental results show that modeling agent motion consistently improves perception and memory performance, not only in spatial cognition but also in self-awareness, and generalizes to downstream UAV decision-making tasks. Our results highlight the importance of self-awareness for advancing embodied spatial intelligence, and provide both a new benchmark and empirical evidence for motion-aware self-in-space modeling.

---


### 49. [TRACE: An Operational Reasoning Schema for Auditable Agentic Commitments](https://arxiv.org/abs/2607.12480)

**<font color=#1a73e8>作者：</font>** Edward Y. Chang, Emily J. Chang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper defines TRACE (Typed Reasoning And Commitment Evidence): a typed, versioned schema for recording reasoning traces, a reference procedure for writing records against it, and one operating discipline, no durable state change without a record. The paper argues in three layers that reasoning is not in the language model: the autoregressive mechanism natively computes association; chain-of-thought and reinforcement learning inherit its limits; and the formal constructs of reasoning theory, from Socratic procedure to Pearl's ladder, are absent as machinery. The schema answers the absence with fields and tests: the TraceRecord and its causal specialization, an eight-stage reference writer, a gate-first measurement regime, the TRACE-Bench protocol, and the consumers, memory admission, plan gating, temporal regret, and verdict reuse, whose more auditable decisions are the measure of the record. A record-consumer contract states what a record guarantees and what a consumer must honor in return, making the schema an operational interface rather than a passive document. Two worked examples run in the main text: a music-lessons argument traced from sentence to typed verdict, separating association, intervention, and prescription; and a flood search-and-rescue vignette in which a predictive world model reports confident plan success that its own support and out-of-distribution scores contradict, so the record defers the commitment, requests a bounded observation, revises append-only, and clears a different branch. The vignette is illustrative, not empirical; closed-loop evaluation is left to future work, so the contribution is the schema and its contract, not a performance claim. Appendices carry the full schema, writer algorithms and cost model, clinical and policy illustrations, the benchmark protocol, convergence metrics, and usage scenarios.

---


### 50. [TerraLogic: A Benchmark for Hierarchical Geospatial Reasoning in Earth Observation](https://arxiv.org/abs/2607.12497)

**<font color=#1a73e8>作者：</font>** Yuhang Yan, Linchao Mou, Bokang Yang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Beyond perception, reasoning is essential in remote sensing for advanced interpretation, inference, and decision-making. Recent advances in large language models (LLMs) have enabled tool-augmented agents that leverage external tools to perform complex analytical tasks. However, existing studies in remote sensing primarily focus on perception-oriented tasks, leaving cognitive geospatial reasoning largely underexplored. To address this gap, we introduce TerraLogic, a benchmark for geospatial reasoning. TerraLogic comprises 545 scenario-driven, hierarchy-aware tasks, such as hazard vulnerability assessment, urban heat island analysis, and forest fragmentation dynamics, spanning optical, Synthetic Aperture Radar (SAR), and infrared (IR) imagery. It advances evaluation beyond recognition and monitoring toward cognitive-level geospatial analysis. To facilitate evaluation on TerraLogic, we further propose HieraPlan, a tool-augmented agent that organizes toolkits into functional hierarchies and performs fault-tolerant reasoning. HieraPlan enables structured abstraction, robust recovery from tool failures, and stable long-horizon planning. Extensive experiments demonstrate that current approaches struggle with hierarchical geospatial reasoning, while HieraPlan provides a strong baseline with improved reasoning, cross-modal generalization, and error handling. The dataset and agent code are publicly available at this https URL.

---


> [!TIP]
> 当前位于：**1-50**（第 1/2 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-99](./part-02.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
