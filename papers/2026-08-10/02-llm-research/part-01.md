# 🧠 大模型相关研究 | 2026年08月10日

> 本类共 **170** 篇论文：已确认 **159** 篇，待复核 **11** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**1-50**（第 1/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-170](./part-04.md)

---

### 1. [Preventive Care Recommendations by Large Language Models](https://arxiv.org/abs/2608.06379)

**<font color=#1a73e8>作者：</font>** Eden Avnat, Elia Yanko, Ori Yoran 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Preventive care services (PCS) extend life, yet physicians often underprioritize highly effective interventions such as lifestyle modifications (Zhang et al., JAMA Network Open 2020). We evaluated whether large language models (LLMs) replicate and augment physician prioritization of PCS under time constraints. Using Zhang et al.'s validated survey with two patients assessed during long and short visits, we compared seven LLMs with historical physicians. We generated 137 simulated physician personas matching cohort demographics and tested three prompts per model. Primary outcomes were concordance with physician rankings, measured by Spearman correlation, and Consensus-Stratified Agreement (CSA), the proportion of LLM selections rated 4 or higher that matched physician consensus across agreement strata. Secondary outcomes included life-years gained per prioritized choice (LYGPC), consistency, and selectiveness. Augmentation was assessed by having models revise physician rankings under three informative prompts, with delta LYGPC quantifying impact. LLMs closely mirrored physicians (mean Spearman = 0.83, SD = 0.11), with high CSA at extreme agreement ranges (94%, 197/210) but low CSA in moderate ranges (21%, 30/140), where they underprioritized lifestyle services (8.8% vs. 38% rated 4 or higher; P < .001). Several models exceeded physicians in LYGPC and consistency while being more selective. Time constraints affected physicians and LLMs similarly, increasing LYGPC and selectiveness but reducing consistency. Augmentation effects varied by model. Current LLMs reproduced physicians' time-sensitivity and base-rate prioritization while exacerbating underprioritized lifestyle interventions. Some models improved prioritization performance, but consistent augmentation will require value-aligned training, explicit time-constraint representation, and prospective real-world validation.

---


### 2. [TEXAS: Task-Expert-Aware Supervision for Downstream Mixture-of-Experts LLM Adaptation](https://arxiv.org/abs/2608.06396)

**<font color=#1a73e8>作者：</font>** Guanzhi Deng, Haibo Wang, Kuan Wu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Mixture-of-Experts (MoE) language models route each token through a small subset of experts, making routing patterns useful for identifying task-relevant experts during downstream adaptation. Yet current approaches have two limitations: task experts are typically identified from aggregate routing statistics that reflect usage rather than association with successful task completion, and task-expert activations remain underexplored as signals for supervision allocation. We introduce Task-Expert-Aware Supervision (TEXAS), which combines correctness-conditioned task expert discovery with token-level supervision allocation. TEXAS compares expert activations on instances that the base model solves successfully and those it fails to solve, and retains experts more strongly activated on successful instances. During fine-tuning, it upweights answer tokens in failed instances when they activate these experts. TEXAS therefore leverages existing routing behavior without restricting adaptation to a fixed expert subset or imposing an explicit target routing distribution. Across three MoE models and six benchmarks, TEXAS achieves the best or tied-best performance in 17 of 18 settings and improves over the strongest baseline by 1.3--1.5 points on average. Ablations and further analyses validate both the discovered experts and the resulting supervision strategy.

---


### 3. [EntropyMoE: Entropy-Aware Sparse Expert Routing for Tokenizer-Free LLMs](https://arxiv.org/abs/2608.06398)

**<font color=#1a73e8>作者：</font>** Bo Liu, Muxuab Yu, Yu Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent byte-level large language models (LLMs) have made tokenizer-free modeling increasingly competitive by grouping bytes into dynamically sized patches. However, existing byte-patch architectures still apply the same dense feed-forward computation to every patch. This uniform computation cannot adapt model capacity to variations in patch semantics and granularity. We address this limitation with EntropyMoE, a Mixture-of-Experts (MoE) architecture designed for dynamic byte patches. EntropyMoE replaces the dense feed-forward modules in the global patch Transformer with Top-K expert layers. Each dynamic patch serves as the basic unit of expert routing, and its byte coverage determines its contribution to workload accounting. The router selects experts directly from patch entropy, using the same granularity signal that underlies dynamic patch construction to organize sparse computation. Patch entropy and length jointly define the feature space for regulating expert specialization. Experiments show that EntropyMoE achieves the lowest held-out bits-per-byte among matched dense and sparse baselines while maintaining comparable downstream accuracy. These results establish patch entropy as an effective routing coordinate for sparse conditional computation and extend Mixture-of-Experts modeling beyond tokenizer-based representations.

---


### 4. [Beyond Routing Weights: Faithful Response-Level Interpretation of Mixture-of-Experts Reward Models via Contribution Contrast](https://arxiv.org/abs/2608.06400)

**<font color=#1a73e8>作者：</font>** Yifan Wang, Jinyi Mu, Mayank Jobanputra 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reward models are central to learning from human preferences, yet identifying what drives their predictions remains challenging. Recent sparse Mixture-of-Experts (MoE) reward models seek to improve interpretability by routing prompts to specialized experts and characterizing experts through examples with high routing weights. However, routing weights only reveal which prompts an expert $\textit{receives}$, not how it $\textit{judges}$ responses, providing only a partial account of expert behavior. We therefore propose $\textbf{Co}$ntribution-$\textbf{Co}$ntrast ($\textbf{CoCo}$) response-level interpretation, which faithfully characterizes experts' roles using chosen-rejected response pairs with the largest contribution contrasts, jointly capturing routing and preference behavior. Across automatic and human evaluations, CoCo yields more coherent, faithful, and specialized interpretations than router-based, score-based, and sparse autoencoder-based alternatives while maintaining competitive reward modeling accuracy. To the best of our knowledge, this is the first systematic study of interpretation methods for MoE reward models.

---


### 5. [Interpretable Unsupervised Community Detection with LLM-Symbolized Structured Processes](https://arxiv.org/abs/2608.06402)

**<font color=#1a73e8>作者：</font>** Aoting Zeng, Kai Wang, Jianwei Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Community detection is a fundamental task in graph analytics that aims to identify cohesive groups of entities with similar behaviors or interests. Classic objective-driven methods struggle with complex graph structures, while deep-learning approaches improve performance at the expense of interpretability and rely on labeled data and training. Large language models (LLMs), with strong reasoning capabilities and world knowledge, are promising for interpretable, label-free community detection. To leverage these strengths, we propose LUCID, an LLM-guided, interpretable, training-free, and unsupervised community detection method. Inspired by phase-transition kinetics in natural systems, where complex structures emerge through initialization, merging, refinement, and selection, LUCID is designed as a four-stage pipeline. Within this pipeline, the LLM induces formal rules that translate implicit knowledge into explicit and interpretable logical structures. Specifically, (1) the Local-View Community Initialization stage encodes local graph structures using k-ego contexts and unsupervised node roles; (2) the Multi-factor Community Merge stage uses LLM-induced rules to iteratively merge local communities; (3) the Multi-grain Community Refinement stage applies LLM-induced coarse-to-fine rules in parallel to reduce boundary noise; and (4) the Global-view Community Selection stage identifies high-quality communities based on topological compactness and boundary clarity. Extensive experiments on real-world datasets demonstrate that LUCID, as an unsupervised approach, achieves state-of-the-art performance and consistently outperforms leading unsupervised and semi-supervised baselines.

---


### 6. [Separating Decision-Rule Misalignment from Readout-Coverage Limitations in Speech Language Models](https://arxiv.org/abs/2608.06409)

**<font color=#1a73e8>作者：</font>** Linkai Peng, Baorian Nuchged  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Speech language models are increasingly evaluated on paralinguistic tasks by the accuracy of prompted answers, but answer accuracy combines failures at different stages of the audio-to-answer computation. We introduce a generation-aligned diagnostic ladder that compares the emitted answer, the option logits, an affine readout of those logits, and a linear readout of the hidden state at the same answer token. Successive differences separate endpoint, decision-rule, and readout-coverage gaps. Across five systems and two emotion corpora, state decoding exceeds generation by 27.8 accuracy points on average, and both the decision-rule and readout-coverage gaps are positive in all ten conditions. A label-free logit correction improves generated accuracy in every condition, showing that part of the decision-rule gap is actionable. In rank-matched comparisons, emotion information outside the native readout generalizes to held-out speakers and survives controls for measured acoustic descriptors, but replacing the selected readout-external directions usually has little effect on emitted answers. These results distinguish information availability from behavioral use and localize performance losses across the decision rule and the state-to-answer readout.

---


### 7. [ADIAS: Automated Design of Interactive Agentic Systems](https://arxiv.org/abs/2608.06410)

**<font color=#1a73e8>作者：</font>** Lekang Jiang, Bohan Tang, Stephan Goetz 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Automated agent design improves agent harnesses through iterative revision, evaluation, and feedback summarization. Existing methods are largely candidate-centric: cross-round experience is organized around candidate agents, which leaves the repair progress implicit. This causes inefficient repair targeting, slow consolidation of partial progress, and propagation of ineffective interventions across rounds. Therefore, we formulate issue-centric agent optimization, in which repair progress is carried forward as an explicit persistent issue state to guide optimization, rather than re-derived from candidate history in each round. We instantiate the formulation in ADIAS, a framework for automated full-code agent design with two mechanisms. A persistent issue state maintains stable issue identities, lifecycle status, supporting evidence, and intervention-outcome histories. Issue-guided optimization uses this state to jointly propose repair targets and revision directions for subsequent focused full-code modification. Across five interactive benchmarks, ADIAS outperforms the strongest baseline by 25.2% on average and achieves consistent gains across four backbone models. Controlled ablations further show that removing persistent issue state or replacing issue-centric revision with candidate-centric policies leads to performance drops of up to 40.7%.

---


### 8. [Learning to Predict Middle-Layer Attention in MLLMs for Visual Token Prunin](https://arxiv.org/abs/2608.06411)

**<font color=#1a73e8>作者：</font>** Yuyao Sun, Tao Deng, Shuang Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) achieve strong performance across diverse vision-language tasks, but their efficiency is limited by the cost of processing numerous visual tokens. Visual token pruning can reduce this cost, but requires accurate token importance estimates. Recent studies have demonstrated that text-to-vision attention from middle language model layers can effectively guide visual token pruning, typically using attention from a predefined middle layer to select the visual tokens to retain. Two problems therefore remain. First, our analysis shows that the layer whose attention is most responsive to the question varies substantially across samples, making a fixed layer suboptimal. Second, obtaining attention from the appropriate middle layer requires processing numerous visual tokens through several language model layers, by which point considerable computation has already been spent. To address both problems, we propose Middle-layer Attention Prediction (MAP), which uses Question Contrastive Teacher Selection to identify a sample-specific teacher layer by contrasting attention under the original and reference questions, and distills attention from the selected layer into a lightweight predictor that estimates visual token importance from multi-modal input features. During inference, MAP combines the predicted importance scores with a diversity criterion to prune visual tokens before the first language model layer. Thus, MAP requires no attention maps for pruning and remains compatible with existing inference acceleration techniques. Across ten benchmarks on LLaVA-NeXT-7B, MAP retains 97.5% of the unpruned model performance with only 5.56% of the visual tokens, yielding a 3.09x end-to-end speedup.

---


### 9. [Latent Fact-Checking: Detecting Misinformation through Activation Engineering](https://arxiv.org/abs/2608.06417)

**<font color=#1a73e8>作者：</font>** Pedro Barcelos, Otávio Parraga, Marcelo M. Mussi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The proliferation of misinformation online has driven demand for scalable detection systems. While most existing approaches rely on surface-level linguistic features or external knowledge retrieval, we examine truthfulness as a geometric property of a language model's representation space. We introduce a misinformation detection framework grounded in activation engineering, which leverages the latent geometry of transformer models. Our approach elicits a misinformation direction in the residual stream by contrasting activations from paired truthful and false statements, following the difference-in-means principle of Contrastive Activation Addition (CAA). At inference time, the last-token activation of an unseen claim is projected onto this direction, and the projected representation is fed to an Multilayer Perceptron (MLP) for classification. The procedure requires no fine-tuning of the backbone model, no external evidence retrieval, and no task-specific supervision beyond the contrastive pairs used to estimate the direction. We evaluate the method across 11 models from the Gemma, Llama, and Qwen families, ranging from 270M to 12B parameters, on three fact-checking benchmarks: AVeriTeC, LIAR, and FACTors. The falsehood direction is recoverable across model scales and architectural families, and last-token projection matches or surpasses zero-shot and few-shot prompting baselines on LIAR and FACTors, with the largest gains observed for smaller models. Performance on AVeriTeC is more limited, which we attribute to its evidence-grounded labeling scheme. These findings provide evidence that truthfulness is a structured, linearly separable concept in the latent space of pretrained language models, and point toward interpretability-driven misinformation detection as a practical complement to retrieval-based pipelines. The code is available on this https URL.

---


### 10. [Sharding Prevents LLM Oversight Failures and Adversarial Exploitation](https://arxiv.org/abs/2608.06422)

**<font color=#1a73e8>作者：</font>** Victor Akinwande, J. Zico Kolter, Aran Nayebi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Giving an LLM judge more compute does not necessarily make it check more requirements. When one call must return many verdicts, some decisions become weakly grounded in the evidence, even when that call receives the same token or tool budget as a panel of separate calls. Across expert-graded research replications, legal work, and clinical-trial assessments, agreement with experts falls as the number of verdicts per call grows. We identify sharding as the intervention that mitigates this failure in model-based oversight. Sharding partitions the requirements into smaller groups, assigns each group to a separate call, and aggregates the verdicts. Against a single call with the panel's full budget, sharding improves agreement while holding the model, evidence, total budget, and per-decision budget fixed. Overall, we find that a sharded weaker judge can outperform a more capable holistic judge and match that judge even when the latter receives the panel's full budget. Additionally, we find that sharding exhibits robustness against adversaries. A best-of-N adversary can hold the underlying work fixed, vary only its presentation, and increase an overloaded judge's acceptance of genuinely unmet criteria severalfold. Wherever sharding reduces baseline error, it removes this adversarial advantage, keeping over-acceptance low even as the adversary's search widens. Sharding does not address attacks that persuade the judge separately on each criterion rather than exploiting overload. In that setting, we find that debate-style opposition on top of sharding withstands such adaptive re-optimization.

---


### 11. [NTDH: Complex Reasoning for Comprehensive Affective Analysis](https://arxiv.org/abs/2608.06425)

**<font color=#1a73e8>作者：</font>** Tianlei Zhu, Zhiwei Liu, Yuyan Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Comprehensive affective analysis is challenging for two reasons: it spans heterogeneous prediction tasks with continuous, ordinal, and multi-label outputs, and affective meaning is context-dependent, requiring conflicting cues to be reconciled rather than mapped directly to labels. Existing methods learn this mapping directly and do not model the reconciliation explicitly. We recast the task as a complex-reasoning problem, which yields one output interface across heterogeneous label spaces and a trajectory over which a verifiable reward can be optimised; to our knowledge, this is the first such treatment covering both sentiment and emotion. The obstacle is on the data side: affective reasoning traces must be synthesised, and generic synthesis is misaligned with the targets, tolerances, and phenomena of affect, and discards or leaks its failure cases. We propose NTDH, which addresses these four failures. Naturalisation sets the training answer to the gold label, so it is correct by construction. A Tolerance-aware gate checks each answer against the task's own scoring margin. Domain-aware strategies refine the reasoning using ideas from affective science. Directional Hints report only the type and direction of an error, without exposing the target. We train Qwen3-8B with SFT and then GRPO under the same tolerance used for verification (up to a more permissive construction gate on the multi-label subtask), and a component ablation quantifies the data-quality effect of each part. Using 16,302 training records, about 14x fewer than comparable instruction-tuned systems, the final policy improves over its SFT checkpoint on five of six official-test metrics and achieves the strongest EI-reg result among the compared systems, at a Pearson correlation of 0.862.

---


### 12. [Recovering Lesion Parameters from Aphasic Picture Naming Error Profiles in Large Language Models](https://arxiv.org/abs/2608.06429)

**<font color=#1a73e8>作者：</font>** Yong Yang, Roger Newman-Norlund, Xiang Guan 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Interpretability methods for large language models (LLMs) describe internal state but do not directly test whether that state is causally sufficient to produce the observed behavior. In earlier work, we lesioned LLMs to produce error profiles in picture naming, a central task for assessing aphasia, and found that specific lesions produced errors resembling those of individual stroke survivors. Here we ask the inverse question: given an error profile, can the lesion parameters that produced it be recovered, and what does this inverse problem reveal about transformer computation? Lesions in LLaVA-Vicuna 13B were parameterized by layer index, modification percentage, and noise sigma across 4,840 configurations, and error profiles were characterized by a seven-category clinical taxonomy (correct, semantic, unrelated, formal, mixed, neologism, no-response). We trained a multi-task neural network to map error profiles back to perturbation parameters. The problem admitted a partial solution: across 10 independently trained inverse models, modification percentage and noise sigma were recoverable, whereas layer index was recoverable only within a neighborhood. In counterfactual validation, a fresh model instance perturbed with the recovered parameters reproduced the target behavior in 81.4% of cases. This dissociation between low layer recovery and high counterfactual fidelity is consistent with functional redundancy across transformer layers, a property not captured by standard interpretability methods. As an out-of-distribution test, we applied the trained model to picture-naming error profiles from 278 stroke survivors; recovered parameters were syndrome-discriminative, most strongly for perturbation intensity, indicating generalization beyond the training distribution. Counterfactual validation provides a general framework for LLM interpretability claims beyond inverse mapping.

---


### 13. [Test-Time Adaptation with Online Personalized Energy-Based Cache for Fine-Grained Video Expression Recognition](https://arxiv.org/abs/2608.06467)

**<font color=#1a73e8>作者：</font>** Masoumeh Sharafi, Muhammad Osama Zeeshan, Soufiane Belharbi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Facial expression recognition (FER) in videos is challenging because models must identify subtle, temporally evolving affective states that vary across individuals. Although vision-language models provide transferable visual-semantic representations, models trained on subject-independent data often degrade under subject-specific distribution shifts at inference time. Existing test-time adaptation (TTA) methods commonly update model parameters during inference, increasing computational cost and latency. Cache-based methods avoid parameter updates, but they usually require enough target samples to form reliable class prototypes, which is difficult early in adaptation and for rarely observed classes. We introduce Energy-Based Cache Personalization (EB-CaP), a subject-based online TTA method for video FER that generates class-specific prototypes personalized to each target video. EB-CaP uses a lightweight energy-based model to sample prototypes from the current unlabeled video and populate a personalized cache online, without accumulating large amounts of target data or storing diverse source prototypes. Its energy function relies only on pretrained CLIP: similarities between the target video embedding and class text embeddings guide prototype sampling. In parallel, positive and negative caches store reliable and uncertain target embeddings. An adaptive entropy gate controls cache updates according to the evolving confidence distribution, while a diversity gate limits redundant samples. Final predictions combine cache-derived scores with the current CLIP scores. Experiments on BioVid, StressID, and BAH show that EB-CaP outperforms state-of-the-art TTA methods while maintaining low computational and memory overhead. Code is available at this https URL.

---


### 14. [CyberForge: Verified Vulnerability Injection at Repository Level for Cybersecurity Agent Training](https://arxiv.org/abs/2608.06471)

**<font color=#1a73e8>作者：</font>** Amine Lbath, Manan Suri, Aurelien Delaitre 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Despite recent advances, frontier large language model (LLM) agents remain limited in discovering and patching complex vulnerabilities in real-world software. Generally available agents can already aid attackers, who only need to find one exploitable weakness, while defenders must continuously identify and patch all vulnerabilities across fast-growing codebases. Stronger defensive agents would help close this gap, yet the scarcity of security training data with reproducible build and execution environments remains a bottleneck.
We present CyberForge, a framework that synthesizes executable, repository-level security training data by injecting vulnerabilities into real C/C++ projects. It validates each instance dynamically: the injected build must pass the project's unit tests, and generated proof-of-vulnerability (PoV) must trigger on the injected build and not on the clean one. CyberForge is not limited by the availability of disclosed vulnerabilities, therefore it can scale in comparison to data augmentation techniques which rely on historic CVE data. The resulting corpus holds 1034 validated vulnerabilities across 80 projects and 63 weakness categories, with edit locality similar to real CVE patches under a real-versus-real noise floor. Fine-tuning on trajectories collected over this corpus improves SEC-bench patch repair by +3.3 to +14.7 points, in all six configurations of three model scales and two teachers, with the 31B student reaching its GPT-5.4-mini teacher, 72.7% against 74.0%. These gains generalize out of distribution to PatchEval, a corpus containing other programming languages, where every configuration also improves and the 31B student passes its teacher.

---


### 15. [WebGrader: Training LLMs for Web Development with Self-Evolving Programmatic Grader](https://arxiv.org/abs/2608.06474)

**<font color=#1a73e8>作者：</font>** Boshui Chen, Huiping Liu, Shaolei Zhang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models increasingly generate complete websites from natural-language descriptions, and reinforcement learning has become a central approach to closing their remaining functional gap. This training regime is bottlenecked by reward design. Hand-authored browser scripts are executable yet costly to write for open-ended requirements, while VLM and GUI-agent graders scale but may issue verdicts before observing the decisive state. We propose WebGrader, a self-evolving programmatic grader that autonomously derives the required interaction flows from each website request, represents each flow as an executable Flow Contract, and uses its execution outcome as an RL reward. WebGrader materializes the generated project in a live browser, grounds target actions against the source code and live DOM, and collects visual, DOM, response, and persistent-state evidence along the same browser trajectory. A residual-driven offline loop then discovers reusable verifier skills, screens them on disjoint validation pages, and freezes the promoted skill graph before policy training. By separating test planning, action grounding, evidence collection, and semantic judgment, WebGrader issues a Pass verdict only after observing the requested transition. On WebGen-Bench, WebGrader trains an 8B policy to a 52.01% functional success rate, outperforming a matched appearance-plus-script reward by 7.88 points and surpassing o4-mini and DeepSeek-v4-flash. On WG-core-250, the policy reaches a Full Score of 44.953 and surpasses Qwen3-Coder-480B.

---


### 16. [Do AI Personas Grow? Analyzing and Benchmarking Personality Evolution in LLM Agents After Life Events](https://arxiv.org/abs/2608.06485)

**<font color=#1a73e8>作者：</font>** Ming Wang, Peidong Wang, Xiaocui Yang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Personality-conditioned LLM agents (PC-Agents) are increasingly used in emotional support, social simulation, and role-playing, motivating the development of lifelong agents that remain coherent over extended interactions. A key component of such coherence is personality evolution: agents should undergo plausible, psychology-grounded changes as they experience life events in different contexts. Although prior work shows that LLM personalities can shift under contextual perturbations, how these shifts vary across traits, events, personas, and models remains poorly understood. We study event-induced personality change after 11 major life events, using the Big Five traits as a psychometric anchor and interpreting the resulting trajectories against longitudinal evidence from human personality psychology. Across four diagnostic axes, PC-Agents exhibit measurable trait shifts at similar rates for event-trait pairs with and without documented human change directions. Even when shifts follow the expected direction, their magnitudes usually fall below human effect-size ranges. Gender and cultural-region prompts show little moderating effect, while persona-level dispersion is compressed three- to four-fold relative to human samples. To enable systematic comparison, we introduce BFI-Adapt, a reusable benchmark for scoring the directional fidelity of event-induced personality change, and use it to rank 14 models. A validation suite shows that the measured shifts exceed no-event retest noise, remain stable under independently paraphrased prompts, exhibit limited and model-dependent convergence with scenario-based behavioral choices, and persist across intervening unrelated dialogue. Together, these checks establish the measured trajectories as robust event-conditioned response patterns. Our results suggest that current PC-Agents simulate the mean of human personality dynamics, but not its shape.

---


### 17. [ConstructCIE: A Dataset for Extracting Causal Information from Construction Accident Narratives](https://arxiv.org/abs/2608.06495)

**<font color=#1a73e8>作者：</font>** Hung Nguyen, Jaehoon Lee, Namgyun Kim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Construction accident narratives contain rich causal information, but the evidence is often implicit, long-span, and distributed. We introduce ConstructCIE, a manually annotated dataset for Causal Information Extraction from OSHA construction accident reports. The dataset uses a hierarchical schema for accident types, causal factors, sub-causal factors, and supporting evidence spans. We evaluate supervised sequence taggers and instruction-tuned LLMs in an end-to-end hierarchical extraction setting. Results show that most evaluated models achieve strong accident-type prediction and recover broad causal meaning but remain limited in precise span-level extraction. JHE generally achieves stronger exact and soft matching, while IHE sometimes achieves higher keyword F1. Error distributions vary by extraction strategy, but evidence-selection and span-boundary errors remain common. These findings show that reliable Causal Information Extraction for construction accidents requires stronger domain grounding and more accurate evidence extraction.

---


### 18. [Can MLLMs Decode the Creative Leap? Introducing C4 for Cross-Concept Understanding](https://arxiv.org/abs/2608.06501)

**<font color=#1a73e8>作者：</font>** Ming Wang, Yuqing Zhang, Tingna Xie 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Creative capabilities of MLLMs matter in design, communication, education, and human--AI collaboration, yet remain difficult to evaluate because explicit targets and reward signals are scarce compared with accuracy-oriented tasks. Cross-concept understanding is a core cognitive capacity underlying receptive creativity. It enables a perceiver to recover intended meaning from non-obvious but meaningful conceptual relations. We operationalize item construction as cross-concept encoding and model inference as cross-concept decoding. We introduce C4, a cognition-inspired evaluation framework for Chengyu (Chinese idiom)-based Cross-Concept Creativity. Its encoding component maps target slots to imageable substitute concepts along bridge paths in a manually annotated and third-party-reviewed cross-concept network, enabling batch generation with explicit structure, difficulty indexed by bridge count and depth, and exact answers. Using this framework, we instantiate the C4 Evaluation Set (C4-Eval), comprising 184 synthetic items and 37 human-created cross-concept chengyu figures collected from online sources. We manually construct and review cross-concept relations, bridge paths, and reasoning processes for the collected figures. Each C4-Eval item is instantiated in five task settings, yielding 884 primary answer-recovery cases. Across ten evaluated MLLMs, the strongest closed models reach 50.7% and 48.0% primary accuracy, while open-source models remain substantially lower. Candidate constraints improve accuracy sharply, but bridge hints and explanation requests provide only modest gains. These results expose a substantial gap in how current MLLMs decode creatively encoded meaning through cross-concept relations. The code is in the supplementary material.

---


### 19. [Toward Reliable Context Compression for Long-Horizon Agents: An Empirical Study of Execution Instability](https://arxiv.org/abs/2608.06503)

**<font color=#1a73e8>作者：</font>** Guanghui Min, Liang Wu, Mayank Darbari 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recurrent context compression controls context growth in long-horizon agents, but its behavioral effects remain poorly understood. In this preliminary empirical study, we show that compression can weaken the influence of recent interactions, increasing blocked actions, repeated exploration, and instability across runs. Motivated by these observations, we introduce TRACE, a verifier-guided framework that evaluates individual compaction events through paired closed-loop continuations from the same environment state and uses summary preferences to optimize a natural-language compression prompt while keeping all models frozen. Initial results on AppWorld show improvements over existing compression baselines in task performance, multi-run reliability, and context--execution efficiency. These findings provide early evidence for boundary-local evaluation as a promising direction for reliable agent context compression.

---


### 20. [Measuring the Cross-Lingual Comprehension Gap: How the language of the evidence shapes what language models understand](https://arxiv.org/abs/2608.06506)

**<font color=#1a73e8>作者：</font>** Rafael da Silva, Jeff Eicher  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language models are often evaluated as though capabilities demonstrated in English remain equally available when the same content is presented in other languages. Traditional multilingual benchmarks rarely isolate language while holding content, question, reference answer, model, and evaluation unit constant. We define the Cross-Lingual Comprehension Gap (CLCG) as the reduction in response quality when the same content and question are presented in a target language rather than in English.
Using ParallelQA-18, a professionally human-translated parallel corpus, we evaluate five models from five laboratories on a stratified sample of 150 articles across 18 languages (English reference; Portuguese high-resource baseline; 16 targets spanning Joshi et al. 2020 classes 0-4). A within-item design varies only passage language. The primary estimator contrasts English versus pooled target-language Token-F1 micro-means on higher-complexity open-ended questions, with article-cluster bootstrap intervals.
The primary pooled CLCG is 0.078 (95% CI 0.072-0.084), about a 17% reduction relative to the English score; the equal-language macro summary is 0.077. Net of Portuguese, the macro gap is 0.016 (95% CI 0.013-0.020). Language-level CLCG is negatively associated with Joshi resource class (rho = -0.594, p = 0.015, n = 16). In blinded paired human evaluations, higher-resource responses are preferred in 61.6% of decisive judgments (estimated preference probability 0.655, 95% CI 0.558-0.741).
Capabilities shown in English should not be assumed to transfer equally to other languages; English-centered evaluations may overestimate quality for users of low-resource languages.

---


### 21. [GRASP: Reinforcing Language Model Anonymizers with Group Relative Policy Optimization](https://arxiv.org/abs/2608.06526)

**<font color=#1a73e8>作者：</font>** Sajjad Ghiasvand, Nader Sehatbakhsh  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models can infer sensitive personal attributes, such as age, location, and occupation, from ordinary text, turning everyday writing into a privacy risk. Adversarial anonymization defends against this by rewriting a text with a capable language model that also plays the attacker, but it needs a powerful model at inference time and thus sends private text to a third party, the very exposure anonymization should prevent. Recent work distills this behavior into a small on-device model using supervised fine-tuning and direct preference optimization (DPO), but DPO only imitates the teacher's offline choices and never directly optimizes the privacy--utility objective we care about. We introduce \textbf{GRASP} (\textbf{G}roup-\textbf{R}elative \textbf{A}nonymization via \textbf{S}elf-refinement \textbf{P}olicy-optimization), which reinforces the local anonymizer online with Group Relative Policy Optimization. A single small model acts as anonymizer, adversary, and utility judge, trained against a self-generated reward that hides attributes while preserving meaning, with a design that guards against reward hacking. Trained on Llama-3.1-8B, \ours{} improves the privacy--utility trade-off over the DPO-distilled baseline, consistently across three independent LLM judges. Against adversarial anonymization driven by frontier models such as Gemini~2.5~Flash and Claude, it achieves a comparable or better overall trade-off while removing substantially more private information, and it runs entirely on-device at roughly $1\%$ of the GPT-4o teacher's cost.

---


### 22. [Lost in Interpolation: Why Predictive Feedback Fails in Diffusion Language Models](https://arxiv.org/abs/2608.06529)

**<font color=#1a73e8>作者：</font>** Lavanya Nigam, Ishaan Bansal, Aryan Sood 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Soft-masking accelerates the convergence of Masked Diffusion Language Models (MDLMs). Existing formulations build this blend with linear interpolation (LERP) in the raw embedding space, which implicitly treats that space as Euclidean. We analyze the embedding space of MDLMs and find that the mask and predicted-token embeddings maintain a near-constant angle of (\approx 73^\circ) throughout training, while embedding norms remain essentially flat across vocabulary-frequency rank. These indicate a hyperspherical geometry, for which LERP is the wrong interpolation primitive. We introduce Spherical Soft-Masking (S-SM), a drop-in replacement that aggregates the top-(k) predictions with a Fr'echet mean on the hypersphere and blends this mean with the mask direction using spherical linear interpolation (SLERP), then restores the native mask norm. We evaluate S-SM on continued pre-training of a released 169M-parameter MDLM checkpoint across a wide range of inference-time step budgets, SLERP feedback avoids the training degradation that LERP feedback induces and delivers MAUVE gains of up to 2x over the vanilla MDLM baseline and 27.5-56.1% over TopK/LERP at various sampling budgets, alongside consistently lower generative perplexity (16.9-19.6% over the baseline), while leaving output entropy and convergence essentially unchanged.

---


### 23. [Confidence Estimation for Financial Vision-Language Models in Chart and Document Understanding](https://arxiv.org/abs/2608.06532)

**<font color=#1a73e8>作者：</font>** Reza Khanmohammadi, Simerjot Kaur, Charese H. Smiley 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LVLMs are increasingly used to read financial charts, tables, and documents, where a single misread figure can move a decision and the most authoritative-looking answer is sometimes one the model produced without reading the exhibit. The operational question is therefore trust, not accuracy: which answers can be acted on, and which escalated to a reviewer. We evaluate seven confidence estimators, three inference-only and four trained internal probes, across five open-weight LVLMs and four conditions from three financial visual question-answering benchmarks, one bilingual; every probe is trained only on natural images and applied to finance without adaptation, so the results measure out-of-distribution transfer. Three findings hold. First, the scarce property is calibration, not ranking: the inference baselines rank correct above incorrect answers competitively but are badly overconfident, calibration error far above what a threshold can tolerate, and only the trained probes produce a thresholdable score. Second, reliability is structured rather than global, along two axes a practitioner can read directly: the best estimator shifts with both model and task, none leading more than eight of twenty (model, condition) cells, and a controlled bilingual contrast exposes an apparent language robustness as a composition artifact that dissolves once models are read one at a time. Third, cast as deferral under an error budget, how much can be safely automated is set first by the model's competence and only narrowed by its confidence, so deferral clears a real share of the easiest condition and almost none of the hardest, near zero at a strict 5% budget. Two trained probes carry the calibration a deferral policy needs, and among them only the grounding-aware one lowers its confidence on answers a model gives without using the figure, separating detected non-grounding from a fluent guess.

---


### 24. [Don't `Well, Actually' Me Unless You Know What You're Talking About: Weak Presupposition Verification Degrades General QA Performance](https://arxiv.org/abs/2608.06539)

**<font color=#1a73e8>作者：</font>** Shenran Wang, Vered Shwartz, Hila Gonen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> False-presupposition QA (FPQA) tests LLMs on their ability to identify false presuppositions in questions and abstain or correct them rather than reinforcing false assumptions. The common approach reduces the task to prompting LLMs to extract presuppositions and fact checking each presupposition. While the performance on dedicated benchmarks keeps improving, evaluation largely focuses on questions with false presuppositions (FPQs) while ignoring the performance on ``normal'' questions (TPQs). Since many benchmarks over-represent FPQs compared to their natural occurrence, the result is that performance on these benchmarks doesn't reflect real-world QA performance. Through extensive experiments across various model families, sizes, and benchmarks, we show that methods that perform better on FPQs tend to perform worse on TPQs. Our analysis reveals this is the result of weak fact checking modules that reject also true presuppositions. We hope our findings will help guide future work toward FPQA methods that generalize well to realistic settings.

---


### 25. [TradeVerse: A Longitudinal Benchmark of Political Negotiation in International Trade](https://arxiv.org/abs/2608.06549)

**<font color=#1a73e8>作者：</font>** Debodeep Banerjee, Amitangshu Dasgupta  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLMs are increasingly being applied to tasks involving institutional and political texts, but existing benchmarks evaluate them on isolated documents or single tasks. In realpolitik, negotiations are longitudinal data, where participating parties can align or argue over multiple iterations and each turn is an outcome of the previous turns, hence, understanding one turn requires tracking everything before it. We introduce TradeVerse, a benchmark built from the World Trade Organisation (WTO) specific trade concerns, where member states challenge one another and exchange arguments over multiple rounds, sometimes for years. We, in TradeVerse, reconstruct minutes of $1170$ meetings, spanning across 5 groups and $89$ product groups and define three tasks: first, the system has to analyze the longitudinal meeting records and predict the harmonized system codes (HS chapters) of the products under discussion in the particular meeting, second, we examine whether the system, upon analyzing the anonymized content of the meeting, can guess the name of the responding country and third, we ask the system to play the role of the responding country and provide the statement for the very last round. All labels are recovered directly from the proceedings, requiring no manual annotation. Our experiments highlight the challenges these tasks pose for current LLMs. To the best of our knowledge, TradeVerseis the first benchmark to investigate potential of LLMs in understanding longitudinal political trade negotiations.

---


### 26. [Quantization Damage Is Multiplicative, Not Additive](https://arxiv.org/abs/2608.06564)

**<font color=#1a73e8>作者：</font>** Zekun Wu, Swati Dhiman, Adriano Koshiyama  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Quantization is how large language models are actually deployed, and below four bits it is known to hurt. What nobody can say is which of the model's decisions will change at a given bit-width. The damage is silent: a compressed agent stops calling its tools, then loses half its safety refusals, yet benchmark scores barely move. Prior work assumes quantization adds noise of a roughly fixed size, which would make confident decisions safe. We measure the decision itself instead. The margin of a two-way decision is the model's score for the option it picks minus the score of its best alternative; we track it before and after quantization across 16 models from 8 model families, three quantization methods, and bit-widths from 8 down to 2. Quantization does not add fixed-size noise to the margin. It multiplies the margin by a factor that collapses with bit-width (median 0.86 at 4 bits, 0.33 at 3, 0.00 at 2); we call this margin shrinkage. This contraction reduces the protection a large margin affords; the model's own small biases pick the direction of failure: at 3 bits the decision to call a tool collapses toward inaction while the choice of which tool is untouched. In fitted statistical comparison, additive-noise accounts never win on the damaged tool and safety decisions. The fitted relation predicts flip rates within a median of 1.8 percentage points on held-out decisions, though no flip was used in the fit; per decision, the predicted flip probabilities are calibrated uncertainty estimates (expected calibration error 0.004 over 131,758 predictions). The same form holds in every model we measure, but the constants are each model's own and do not transfer. A small paired margin set, measured per model and bit-width, estimates which decisions break without full generative evaluation; under our cost-matched tests, nothing repairs damage more cheaply than one more bit.

---


### 27. [Divergent Response Modes in Frontier Language Models Under Steering Pressure](https://arxiv.org/abs/2608.06578)

**<font color=#1a73e8>作者：</font>** Ali Jalal-Kamali  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Frontier language models are trained using distinct data, objectives, and safety pipelines. Whether these differences produce measurably different behaviors under explicit steering pressure remains underexplored. This study evaluates behavioral steerability across six frontier models from six developers using 300 paired base and steered items over three categories: values-conflict, reasoning-elicitation, and reasoning-suppression (plus 40 validation items). All six models act as blind peer judges and classify every response based on fixed behavioral rubrics. The resulting 24,480 judgments are scored by leave-one-out consensus. We find that models differ not just in how much steering shifts their behavior but in what kind (mode) of response they give, and some response modes appear in only one or two of them. GPT-5 deflects requests to disclose its reasoning while leaving its answer intact (99% vs. 0% for all other models). Claude Opus 4.7 and GPT-5 resist explicit suppression instructions and in different ways. Using Llama as the open-weight model, we trace the largest behavioral split to its internals. A linear probe decodes the behavior from the residual stream at 0.87 held-out accuracy while injecting that direction during generation drives the behavior from 0% to 86% across an intervention sweep. Every finding holds under both a token-budget remediation and a control experiment with a hypothesis-blind judgment prompt.

---


### 28. [Beyond "AI Language": The case for the idiolectal nature of LLM output](https://arxiv.org/abs/2608.06589)

**<font color=#1a73e8>作者：</font>** Karolina Rudnicka, Thomas Stephan Juzek  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While large language model outputs are frequently analysed as a collective super variety termed "AI language," this chapter argues that this perspective coexists with distinct, model-specific linguistic signatures akin to human idiolects. We analyse two datasets of LLM-generated texts on societal topics: a 2024 corpus of six models (Improta et al. 2024) and a newly generated 2026 corpus using the same prompts featuring six contemporary models. Our findings, utilising computational descriptors and stylometric principal component analysis reveal a generational shift between the style of the 2024 and 2026 cohorts, while demonstrating that each individual model maintains a unique linguistic profile. This multi-layered interplay is illustrated by contraction frequencies, which vary from over 1,200 to over 30,000 per million words within the same cohort of models (2026). Ultimately, we conclude that treating LLM output as idiolectal in nature provides a valuable framework with potential implications for research on variation and change, LLM-generated text detection, forensic linguistics and usage-based approaches to language.

---


### 29. [Automated item evaluation: Predicting item acceptance and rejection using LLM-generated critiques](https://arxiv.org/abs/2608.06609)

**<font color=#1a73e8>作者：</font>** Hotaka Maeda, Yikai Lu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Automated item evaluation (AIE) refers to the use of computational methods to assess item quality without requiring manual expert review or field testing of the items under evaluation. We aimed to build a near-comprehensive AIE model by predicting item acceptance and rejection from item text using historical rejection data from a large-scale standardized testing program. The dataset contained 52,759 English language arts (ELA) and mathematics items with 34% permanently rejected from future operational use. Rejection reasons included poor psychometric properties, content issues, bias and sensitivity concerns, and non-content issues. We fine-tuned a DeBERTaV3-large classifier on raw item text, a second DeBERTa classifier on Qwen3-generated item critiques, and a fusion model combining representations from both. The fusion model achieved the strongest overall performance (Accuracy = .75, F1 = .64, AUC = .80, Sensitivity = .64, Specificity = .81). Prediction for math (F1 = .73, AUC = .86) was considerably more accurate than ELA (F1 = .51, AUC = .72). Lowering the decision threshold from .5 to .25 raised average sensitivity for ELA and math to .88 and .91, while reducing specificity to .31 and .56, respectively, which may be preferable in automated item generation contexts where generating items is cheaper than evaluating them. Incorporating item critiques alongside raw item text improved performance across most rejection reasons. The model assigned higher rejection probabilities to more difficult items. However, the fusion model struggled to identify items flagged for bias, sensitivity, fairness, or accessibility, especially for ELA. These findings suggest that text-based AIE is feasible in some areas and may offer a practical tool for reducing the burden of manual review and field testing, while also underscoring the importance of human review for items with fairness concerns.

---


### 30. [NxN E-valuation: Hypothesis Certification via a Conformal CRT Null](https://arxiv.org/abs/2608.06621)

**<font color=#1a73e8>作者：</font>** Bin Wang, Yan Zhong  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We propose NxN E-valuation, a handy, e-value-based hypothesis-certification algorithm that lets a hypothesis be verified without building any case-specific certification procedure---such as constructing a dedicated null hypothesis---as long as a large enough dataset is available. The method is especially suited to LLM-based exploration systems, where LLMs are remarkably good at proposing hypotheses but suffer badly from hallucination; this hallucination prevents us from harvesting LLM outputs directly, and existing remedies each fall short. The most common solutions include letting the LLM verify or correct itself circular verification and held-out testing (where false hypotheses can still pass via spurious correlations), among other remedies detailed in the introduction. To resolve this, NxN E-valuation exploits the naturally existing large training set and lets different samples serve as null hypotheses for one another. This design directly realizes a conditional randomization test (CRT) that certifies each hypothesis. The approach can be a universally better replacement for at least LLM circular verification and held-out-data testing, provided the LLM's generations are hypotheses that apply to each individual sample.

---


### 31. [Retrofitting Linear Attention into Diffusion Language Models](https://arxiv.org/abs/2608.06628)

**<font color=#1a73e8>作者：</font>** Jinha Kim, Younghun Roh, Jaeyeon Kim  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion language models (dLLMs) offer a promising alternative to autoregressive models by accelerating inference through parallel decoding. Recent dLLMs commonly use blockwise semi-autoregressive decoding, generating blocks autoregressively while denoising tokens within each active block in parallel. However, despite KV caching, each denoising step still attends to all previous blocks, repeatedly incurring prefix-attention cost. Motivated by this bottleneck, we ask whether dLLM inference can be further accelerated by linearizing attention over previous blocks. We introduce block-hybrid attention, which retains exact softmax attention within the active denoising block while applying linear attention over previous blocks. We show that this hybrid attention can be retrofitted into a pretrained dLLM with minimal post-training: LLaDA-Hybrid replaces 6 of the 20 attention layers in LLaDA~2.1, a 16B open-source dLLM, largely following LoLCAT (Zhang et al, 2024). The conversion takes only approximately 60 hours while preserving benchmark performance: 72.0% vs. 75.6% on HumanEval, 63.0% vs. 57.7% on MBPP+, and 86.7% vs. 88.3% on CMATH. With a Triton implementation, LLaDA-Hybrid achieves up to $1.7\times$ higher decoding throughput and supports more concurrent requests before exhausting memory, showing that pretrained dLLMs can be efficiently linearized for faster inference. Our code is available at: this https URL.

---


### 32. [The Sparsity Whisperer](https://arxiv.org/abs/2608.06630)

**<font color=#1a73e8>作者：</font>** Linghao Kong, Inimai Subramanian, Micah Adler 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Pruning reduces the inference cost of large language models, but existing criteria primarily preserve large activations or reconstruct layer outputs. We argue that this overlooks a key computation performed by particularly sparsity-sensitive neurons in the MLP up and gate projections: separating similar inputs into dissimilar outputs. This suggests that effective pruning should preserve not only activations, but also the differences between outputs more broadly. We introduce a family of difference-informed pruning methods built upon this principle. Wisp is a first-order, update-free method that scores weights using input-difference norms, and Wisp+ refines this score neuronwise using the input pairs each neuron separates most strongly. Finally, Whisper is a second-order method that uses a lightly regularized difference Hessian as its reconstruction objective. Across Llama 2 and 3.1 models from 7B to 405B parameters, our second-order variant consistently improves over strong reconstruction-based baselines, while our update-free variants improve over activation-aware baselines, especially in constrained settings. The improvements over Wanda and SparseGPT extend to structured sparsity, downstream evaluations, and other model families. Augmenting stronger techniques such as RIA and ALPS with our difference-informed criteria yields further improvements, shifting the overall accuracy-runtime frontier outward at negligible additional cost. These results suggest that preserving output differences is a broadly useful and composable signal for post-training LLM sparsification.

---


### 33. [Cryptanalytic Extraction of Isolated Bias-Free GLU Feed-Forward Blocks by Antipodal Separation](https://arxiv.org/abs/2608.06631)

**<font color=#1a73e8>作者：</font>** Chunhui Shi, Xinwen Fu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Cryptanalytic extraction has been demonstrated for ReLU networks, for networks using componentwise activations such as GELU or SiLU, and for a Transformer's final projection matrix. These methods do not recover the bias-free Gated Linear Unit (GLU) feed-forward blocks used in many modern language models. Such a block multiplies an activated linear projection by a second learned linear projection within each hidden unit, a two-branch structure absent from the network classes and final-layer setting addressed by those methods. We give a constructive, multi-stage forward-query recovery primitive for isolated bias-free GLU blocks. Finite-difference curvature supplies gate-direction candidates, and paired observations at x and -x separate gate magnitude, orientation, and value-branch coupling. Across high-precision targets, six Qwen layers, an 8,192-unit Llama subproblem, and a full-dimensional Gemma block all reach sub-percent median validation error. Four finite-precision configurations remain below 5 percent median error, but none reproduces every stored weight. These isolated-block experiments are not an end-to-end model-API attack: deriving the required internal block responses from final model outputs remains unsolved.

---


### 34. [Shape Your Feed: An LLM-based Agentic System for Conversational Recommendation](https://arxiv.org/abs/2608.06632)

**<font color=#1a73e8>作者：</font>** Ziyun Xu, Bosen Ding, Yue Zhang 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Industrial recommendation systems predominantly adopt a passive ranking paradigm that infers user preferences from implicit behavioral signals (e.g., clicks, dwell time) rather than explicit, natural language inputs. As a result, users experience a persistent discrepancy between their explicit interests and what passive behavioral algorithms deliver, limiting their ability to express nuanced preferences or steer their feed in real time. To address this growing gap between how recommendations are optimized and how users wish to articulate their interests, we present Shape Your Feed (SYF), an LLM-based agentic recommendation framework that enables real-time, multimodal co-curation of content. SYF employs a three-tier architecture: (i) a Perception Flow that captures fine-grained user intent from text prompts, voice commands, and UI interactions; (ii) a Serving Flow that performs real-time agentic re-ranking and pruning of candidate items, grounded in a persistent Semantic Profile encoding evolving user preferences; and (iii) a Self-Evolution Flow that aligns system behavior with human judgments via Direct Preference Optimization (DPO) and an LLM-as-a-Judge ensemble. Offline evaluations show that SYF's alignment scoring module achieves 98.85% accuracy, substantially improving over strong few-shot baselines. Large-scale online A/B experiments on production traffic further demonstrate that SYF improves feed relevance and user sentiment, indicating a practical and scalable path toward interactive, user-steerable recommendation in industrial settings.

---


### 35. [From Documentation to Zero-day Vulnerabilities: LLM-Driven Fuzzing of JavaScript Engines in PDF Readers](https://arxiv.org/abs/2608.06641)

**<font color=#1a73e8>作者：</font>** Suyue Guo, Stijn Pletinckx, Tianle Yu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Existing fuzzers for PDF readers rely on simple test cases that involve only individual API calls, leading to limited coverage and potentially missing vulnerabilities that require sequences of API calls. To address these limitations, we propose PDFuzzer, a novel PDF engine fuzzer that automatically generates complex and meaningful API call sequences. PDFuzzer first uses a Large Language Model (LLM) to construct context-free grammars and infer the relationships between individual API calls from specifications extracted from JavaScript API manuals and execution traces. Based on the grammars and relationships, PDFuzzer employs a constraint solver to generate concrete API call sequences for fuzzing. Our experiments show that PDFuzzer significantly outperforms state-of-the-art PDF fuzzers (TypeOracle, Favocado, and Cooper) and LLM-based fuzzers (Fuzz4All, naive LLM) on three mainstream PDF readers: Adobe Acrobat Reader, Foxit PDF Reader, and PDF-XChange Editor. PDFuzzer achieves up to 48% higher coverage than existing tools and identifies 31 zero-day vulnerabilities in these readers, from information leakage to arbitrary code execution. Our ablation study validates the necessity of each component, including LLMs, which achieve high accuracy across all pipeline stages (93-98%). We disclosed all vulnerabilities to the vendors via a coordinated vulnerability disclosure process and received bug bounties.

---


### 36. [CyberLLM: A Multi-Agent LLM Framework for Autonomous Detection and Guarded Response in Automotive Cybersecurity](https://arxiv.org/abs/2608.06651)

**<font color=#1a73e8>作者：</font>** Nenad Petrovic, Oussama Jeddou, Feres Ben Fraj 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Software-Defined Vehicles (SDVs) expand the automotive attack surface across source code, runtime logs, and deployment topologies, while safety constraints forbid autonomous agents from acting without oversight. This paper presents CyberLLM, a multi-agent, LLM-orchestrated framework that autonomously detects vulnerabilities and executes remediations under a formal, runtime safety guard. Detection combines a deterministic layer (regex rules, AST analyzers, and topology graph checks) with an LLM refinement pass, so a high-recall floor is complemented by high-precision reasoning. A decision agent aggregates findings, tags them with a human-centric asset taxonomy, and selects a tiered response, ratcheting its confidence with signed cross-session memory and re-planning feedback. Every action is validated against four contextual security properties and an independent action-alignment oracle before it is allowed to run, and refused actions trigger escalation and re-planning. A symmetric attack pipeline generates and replays exploits so both sides can be exercised on the same scenarios. On an independent, ground-truthed benchmark of nine original automotive ECU modules in C, C++, and Rust seeding 47 layered vulnerabilities plus clean controls, the always-on deterministic layer covers 34\% of the labeled vulnerabilities at perfect precision, and adding the grounded LLM refinement and completeness passes roughly doubles coverage to about 70\% (F1 $0.83$) while producing zero false positives on the clean controls. The results indicate that LLM agents can perform useful autonomous cyber-defense when wrapped in a deterministic, auditable safety envelope.

---


### 37. [The Horizon Gap: Planning, Memory, Execution, Training, and Evaluation for Long-Horizon LLM Agents](https://arxiv.org/abs/2608.06663)

**<font color=#1a73e8>作者：</font>** Mingguang Chen, Licheng Wang, Bo Qu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Frontier language models solve reasoning problems in a single forward pass that would have been research contributions years ago, yet fail at multi-hour tasks: losing track of earlier decisions, declaring half-finished work done, or drifting from goals. We call this the horizon gap and survey 1,547 arXiv papers (2024-2026) collected via systematic seed harvest with a disclosed 26.8% bleed filter, extended by targeted supplementation. We disambiguate three routinely conflated properties: long-horizon (task property: required steps), long-context (model property: token capacity), and long-term memory (system property: persistence across steps/sessions). We organize the corpus into six categories tracking a long-horizon task's lifecycle -- planning, memory, execution, training, evaluation, and foundations/safety -- crossed with an axis capturing where horizons are carried (within-context, within-task-beyond-context, or cross-task-persistent). Across all categories, we find the same pattern: outcome-only signals grow uninformative as horizons lengthen, and the field's response -- whether process reward models, credit assignment, or trajectory-level diagnostics -- manufactures denser step-level signals. We treat critical and diagnostic literature as first-class threads throughout, arguing that segregating critique from method would routinely split single papers across chapters. We close by naming open measurement problems: decomposing model versus harness capability, managing correlated bias in process-level signals used for both training and evaluation, and whether long-horizon reliability admits general predictive theory.

---


### 38. [TA-RAG: Tone Awareness as a Design Imperative for Retrieval-Augmented Generation](https://arxiv.org/abs/2608.06672)

**<font color=#1a73e8>作者：</font>** Yong-Bin Kang, Anthony McCosker  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-Augmented Generation (RAG) has become a robust architecture for grounding large language models (LLMs) in trusted knowledge. However, standard RAG systems exhibit a structural limitation: retrieved documents carry their own communication styles-professional jargon, formal tone, or academic writings-that shape the behavior of a RAG system before any tone instructions are processed, often causing the system to ignore user requests for a specific tone. We term this phenomenon contextual decoupling, in which a system optimises for factual accuracy while remaining decoupled from the social or operational context of the recipient. Building on prior research in public health peer-support communities, we identify three communicative misalignment-linguistic, cognitive, and relational-that can persist even when retrieval is relevant and the generated response is factually accurate. We conceptualise these as failures of communicative transformation, which remain largely invisible to accuracy-centred RAG evaluation metrics. To address this gap, we propose Tone-Aware RAG (TA-RAG), a conceptual architectural framework that positions communicative alignment alongside factual accuracy as a core design objective. TA-RAG operationalises four constraints-stigma-free language, readability alignment, recipient-sensitive adaptation, and empathetic framing-across the retrieval, context construction, generation, and constraint validation phases in the proposed RAG pipeline. We further highlight an evaluation agenda for jointly assessing factual fidelity and communicative alignment, and identify open challenges. We argue that tone awareness should be treated not as an optional refinement, but as a present design imperative for RAG systems operating in socially sensitive and high-stakes contexts.

---


### 39. [When Semantics Saturate or Emerge: Adaptation-Conditional Semantic Utility in Source-Free Cross-Domain Few-Shot Learning](https://arxiv.org/abs/2608.06673)

**<font color=#1a73e8>作者：</font>** Wei Liu, Xing Deng, Haijian Shao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Language descriptions in source-free cross-domain few-shot learning (SF-CDFSL) are often selected according to zero-shot accuracy obtained with a frozen vision--language model. This paper asks whether that ranking remains valid after target-domain visual adaptation. Under a strictly paired protocol, we compare a generic class-name template with fixed detailed class descriptions before and after visual Low-Rank Adaptation (LoRA) on EuroSAT, CropDisease, ISIC, and ChestX. Let $\deltazero$ and $\deltalora$ denote the Detailed-minus-Base accuracy before and after adaptation, respectively. Two recurring regimes emerge. In \emph{semantic saturation}, $\deltazero>0$ but $0<\deltalora\ll\deltazero$: on EuroSAT and CropDisease, initial gains of 8.13--21.54 percentage points contract to 0.69--2.96 points after LoRA. In \emph{semantic emergence}, $\deltazero\leq0$ but $\deltalora>0$: on ISIC and ChestX, detailed descriptions become more useful only after the visual representation is updated. Training trajectories and sample-level decomposition show that saturation is driven mainly by Base-LoRA recovering errors already solved by detailed semantics, whereas emergence is associated with prediction turnover and newly formed Detailed-only correct decisions. Fixed-point-free shuffled-semantic controls, a second CLIP backbone, and multiple random seeds support the broad pattern while identifying ChestX 1-shot as a weak boundary case. These findings establish that zero-shot prompt quality is an incomplete proxy for adaptation-anchor quality and motivate evaluating language on both sides of the adaptation boundary.

---


### 40. [Policy-Masked Private Experts: Auditable and Reversible Capability Access Control in Sparse MoE Models](https://arxiv.org/abs/2608.06690)

**<font color=#1a73e8>作者：</font>** Zhuoheng Huang, Mukesh Singh  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Most language-model access controls regulate behavior while leaving the same computation available to every request. We study a different systems question: can trusted authorization determine which newly trained parameters are reachable by the forward pass? Policy-Masked Private Experts freezes a pretrained sparse Mixture-of-Experts (MoE) model, trains a disjoint expert branch, and selects the public or private pool before top-k routing. The resulting claim is narrow but testable: under the declared trusted computing base (TCB), an unauthorized request executes no private expert. It does not imply that the public model lacks the same semantic capability.
We test this separation between execution control and task utility in Qwen3-30B-A3B and DeepSeek-V2-Lite. Three Qwen BF16 seeds update all 32 private experts while the public fingerprint remains unchanged. Across 64 adversarial scenarios and 96 deny/fail-closed events, unauthorized private execution is zero; independent hooks exactly match 11,616 routed private rows and allow-deny-allow recovery is exact. On two prospectively frozen Qwen benchmarks, the private branch improves exact tool use by 5.0 percentage points (pp) (five versus zero discordances; one-sided Holm p = 0.03125, corresponding two-sided exact p = 0.0625) and 21.3 pp (percentile-bootstrap 95% CI [13.3, 29.3], Holm p = 0.000031). Three arm-blinded model evaluators retain a positive external effect of 18.7 pp (95% CI [9.3, 28.0]). A parameter-matched Lora has similar external utility, but a post-hoc request gate leaves 1,225 adapter calls under deny; the disjoint expert branch leaves none. DeepSeek reproduces the route invariant and gains 27.0 pp. A valid sealed evaluation is near-neutral. These results support auditable, reversible control over a trained parameter path, while showing that useful transfer remains distribution dependent.

---


### 41. [A Multi-Agent Framework for Automated Coarse-Grained Molecular Dynamics of Polymers](https://arxiv.org/abs/2608.06694)

**<font color=#1a73e8>作者：</font>** Joohee Choi, Junhyeong Lee, Seunghwa Ryu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Coarse-grained (CG) molecular dynamics extends polymer simulation beyond the scales accessible to all-atom (AA) methods, but bottom-up CG modeling is laborious. The CG resolution is a design choice, so a transferable parameter set is generally not available and the potentials are derived anew for each polymer mapping. Here we present CGMas, a multi-agent framework that automates topology construction, equilibration, mapping, potential derivation, and validation from a natural-language specification of the polymer and target resolution. A large-language-model (LLM) reasoning agent infers the AA topology from polymer name, while layered self-correction resolves physical errors common to unsaturated, heteroatom-containing, and polar polymers. Downstream agents equilibrate the system, map it onto CG representation, derive potentials through Boltzmann inversion, and benchmark the model against its atomistic reference. CGMas completed all 27 homopolymer and copolymer tasks, matched the AA density to within 5% in 22, and reduced simulation from 38-88 min to 1 min, establishing agentic LLMs as a route to automated polymer coarse-graining.

---


### 42. [AgentPatch: Coarse-to-Fine Weak-Task Repair for Merging Agentic Multimodal Large Language Models](https://arxiv.org/abs/2608.06699)

**<font color=#1a73e8>作者：</font>** Zibo Shao, Baochen Xiong, Chengdong Xu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic multimodal large language models (MLLMs) extend multimodal perception and reasoning with planning, tool use, and interaction in dynamic environments. Yet current models are specialized for particular tools or environments, complicating consolidation into a single generalist. We formulate Agentic MLLM Merging and identify two challenges: asymmetric capability preservation, whereby capabilities with different interaction complexity are retained unevenly, producing weak tasks after merging, and behavior-critical forgetting, whereby losing decisive actions can derail long-horizon execution. We propose AgentPatch, a training-free coarse-to-fine repair framework. It selects a stable merged backbone, restores diluted weak-task-specific signals through Weak-Task Unique Residual Recovery, and applies an Agent-Guided Behavior-Critical Patch that recovers decisive behaviors under explicit capability protection. AgentPatch produces a single static checkpoint without routing or ensembles. Experiments across six agentic and multimodal benchmarks show that AgentPatch improves diverse merged backbones, alleviates weak-task degradation, and better balances weak-task recovery with the preservation of complementary search and agentic visual processing capabilities. Code is available at this https URL.

---


### 43. [WebRider: Persona-Conditioned Intent Controllers for Live-Web Assistance](https://arxiv.org/abs/2608.06704)

**<font color=#1a73e8>作者：</font>** Zhi Li, Tao Zhou, Yeqing Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Delegating a web task involves more than asking a question; it requires transferring a policy: what to verify, how to handle uncertainty, which preferences matter, and when to stop. Yet, current live-web agents are evaluated solely on the final answer, ignoring the policy constraints that define the delegation. A plausible final answer can conceal violations of that policy. Our full live audit reveals this critical gap: a strong controller completes 99.2% of tasks but honors all policy constraints in only 38.8% of cases. Finishing does not imply fidelity. WebRider bridges this gap by formalizing the delegated policy as an intent contract---an operational record of goals, constraints, evidence obligations, answer form, and task-local persona controls that must hold even as web pages change. WebRider employs a hierarchical architecture: a top-layer controller maintains the contract, a middle layer realizes intentions as guarded executable actions, and a tool layer executes these actions via browser, search, and maps tools. Our benchmark, RiderBench, evaluates this design on 4,096 live-web contracts across 42 public websites, auditing both the internal contract state and the visible user experience to determine if a rollout preserved its policy and if the steps were persona-consistent. The guarded middle interface also serves as a high-quality training signal; an 8B action-policy model trained through this interface outperforms executable-only baselines under a fixed controller. By making the browsing path a first-class object, WebRider enables a system that is auditable, human-judgeable, and learnable without conflating action realization with final-answer decisions. Dataset URL: this http URL.

---


### 44. [MolBioKG: Grounding Out-of-Graph Molecules in Biomedical Knowledge Graphs via Multi-Resolution Structural Anchoring](https://arxiv.org/abs/2608.06713)

**<font color=#1a73e8>作者：</font>** Yiming Zhang, Hikaru Shindo, Shuan Chen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Biomedical knowledge graphs (KGs) accelerate drug discovery, but standard pipelines assume query molecules already exist as graph entities, leaving unregistered molecules disconnected. We address this cold-start challenge, termed the out-of-graph molecule problem, by introducing MolBioKG. This two-layer system grounds unseen molecules in biomedical evidence via multi-resolution structural anchoring. It connects an index of 2.74 million molecules (represented by scaffolds, fragments, functional groups, and fingerprints) to a 9.6-million-edge KG. Given only a SMILES string, MolBioKG retrieves structurally related graph entities and traverses their biomedical neighborhoods without task-specific training. It features two inference mechanisms: static multi-anchor retrieval using Reciprocal Rank Fusion, and Adapt-KG, a tool-using LLM policy for adaptive traversal. Evaluated across in-graph link recovery, complex multi-hop reasoning, and out-of-graph generalization, MolBioKG outperforms strong baselines. Notably, it raises Hits@10 from 0.585 to 0.876 in multi-hop reasoning and out-of-graph target recall from 0.145 to 0.269, all while ensuring predictions retain traceable structural anchors and source-attributed KG evidence.

---


### 45. [The Optimizer Is the Agent: Reasoning-Driven Search across Prompts, Programs, and ML Workflows](https://arxiv.org/abs/2608.06714)

**<font color=#1a73e8>作者：</font>** Junbo Li, Boyi Liu, Canwen Xu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent systems for optimizing prompts, programs, and ML workflows typically rely on explicit outer-loop controllers such as evolutionary search, bandits, or textual-gradient methods. We ask a fundamentally different question: how much of this search policy can be internalized by a single tool-using agent? We present ReASearch, a unified framework for reasoning-driven optimization in which the agent autonomously decides what to evaluate, how to diagnose failures, which edits to make, and when to verify or restart. Rather than serving only as a proposal generator guided by hand-designed heuristics, the agent actively analyzes outcomes, allocates budget, and refines its strategy over long horizons through persistent memory. With a shared agent loop and domain-specific tools, ReASearch instantiates the exact same scaffold to optimize prompts, programs, and ML workflows. Across 14 diverse tasks, it is competitive with and mostly better than specialized optimization systems, achieving gains of 2% to 40% over strong domain-specific baselines, and in some cases discovering solutions that improve on prior human best-known results. Crucially, we observe that complex search behaviors, which are typically implemented by explicit controllers, emerge naturally from the agent's reasoning process.

---


### 46. [Do Audio Language Models Use Paralinguistic Evidence? Counterfactual Audits for Response Evaluation](https://arxiv.org/abs/2608.06718)

**<font color=#1a73e8>作者：</font>** Kevin Miller, Arjun Chandra, Venkatesh Saligrama  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Audio-language models (ALMs) are increasingly used as judges for speech-to-speech systems, but a judge that receives audio may not actually use paralinguistic evidence. We introduce counterfactual audits for paralinguistic response evaluation. Each audit item holds the transcript fixed while varying affect, prosody, or the timing of an affective shift, forcing a valid judge to track the audio cue rather than lexical content or response style. We evaluate ALM judges using a native one-context judgment protocol and a contrastive recoverability control, then further decompose each item into its constituent perception and response-mapping skills. This yields useful diagnostic states that identify different sources of judge failures. Across Gemini, GPT, and open audio models, we find that contrastive success often overstates native judge reliability, and that similar aggregate accuracies can hide different failure modes. These results suggest that ALM judges should not be evaluated by accuracy alone, instead requiring thorough behavioral audits before deployment.

---


### 47. [CustomDance: Customized 3D Dance Generation with Coarse-to-Fine Human-Centered Interactive Control](https://arxiv.org/abs/2608.06722)

**<font color=#1a73e8>作者：</font>** Xulong Tang, Kaixing Yang, Xiaohu Guo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> With the rise of AI-generated content (AIGC) and advanced techniques for 3D human representation, the task of generating 3D dance movements has become an exciting area of research. Despite significant advancements, current methods often fail to provide comprehensive and distinct control over various multimodal inputs from users, such as music or specific descriptions of desired movements. As a result, the generated motions may be statistically plausible and technically correct, but they often lack depth, expressiveness, and alignment with the user's creative vision. To address this issue, we present CustomDance, a coarse-to-fine interactive system designed for customized 3D dance generation. Inspired by the workflows of expert choreographers, CustomDance introduces a novel paradigm to AI-assisted choreography through three interconnected stages. First, a multimodal Large Language Model (MLLM) analyzes the music and a high-level text prompt to identify key temporal anchors and creative cues for the piece. Next, for each anchor, a multimodal retriever suggests high-quality motion clips from a dance library based on local music and text, empowering the user with concrete and predictable options. Finally, a custom music-conditioned diffusion in-painter seamlessly connects the selected phrases, allowing for iterative, user-guided refinement of the final composition, supported by visualizations of motion dynamics. Our evaluations demonstrate that CustomDance not only highlights the significant creative utility and empowering potential of our AI-assisted choreography paradigm, but also outperforms competitive baselines across quantitative and qualitative comparisons.

---


### 48. [Multi-Level Modeling of Large Language Model Inference Latency and Energy via Hybrid Analytical--Machine-Learning Predictors](https://arxiv.org/abs/2608.06723)

**<font color=#1a73e8>作者：</font>** Saeid Shokoufa, Mohammad Erfan Sadeghi, Mehdi Kamal 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The rapid scaling of Large Language Models (LLMs) has significantly increased computational cost, energy consumption, and inference latency, making accurate estimation essential for sustainable artificial intelligence deployment and hardware-aware design. In this work, we introduce Hybrid Modeling for Energy and Latency of LLMs (HYMELL), a hybrid three-level framework for estimating LLM inference latency and energy by combining analytical modeling with machine learning (ML). HYMELL models LLM execution through a three-level hierarchy: analytical estimation of primitive operations, ML prediction of higher-level components, and an end-to-end model that captures system-level overheads across both prefill and decode phases. The framework supports diverse architectures, including dense and mixture-of-experts (MoE) feed-forward networks (FFNs), as well as multi-head attention (MHA) and grouped-query attention (GQA) mechanisms. Evaluated on an NVIDIA H100 graphics processing unit (GPU), HYMELL achieves high predictive accuracy; notably, for LLaMA 3 8B, it attains less than 5% error for both prefill and decode phases. By predicting execution costs directly from architectural parameters, it enables fast, hardware-free design space exploration and energy-efficient optimization.

---


### 49. [IB-RL: Isolated Bilateral Reinforcement Learning for Strategic Dialogue Agents](https://arxiv.org/abs/2608.06735)

**<font color=#1a73e8>作者：</font>** Senhao Wang, Chenghao Cai, Haitao Hu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) has achieved strong results in improving large language models (LLMs) on tasks with stationary, verifiable rewards, such as mathematical reasoning and code execution. In these settings, the environment follows fixed rules and does not adapt strategically to the agent. Strategic dialogue differs in this respect: the environment is another agent that adapts to the policy, and success depends on the interaction between the two sides. Despite this interactive nature, current RL approaches typically train a target agent against a fixed counterpart or simulator. We find that this training paradigm encourages the policy to exploit counterpart-specific regularities rather than learn strategies that generalize across counterparts. We call this problem the static-counterpart mismatch, which we quantify directly in our experiments. To address it, we propose Isolated Bilateral Reinforcement Learning (IB-RL), in which the two roles coevolve through joint rollouts while each role optimizes its own reward through fully independent advantages, action masks, and update paths. We evaluate frozen policies against fully independent held-out counterparts in both domains. On Vehicle TeleSales, IB-RL achieves 89.6% Success@1, compared to 84.6% for the best unilateral RL baseline. On Deal-or-NoDeal, it reaches 98.4% agreement against DeepSeek V4 Pro, compared to 86.4% for the best unilateral baseline. These results indicate that jointly training both roles with strict peragent isolation produces policies that generalize more effectively to unseen counterparts.

---


### 50. [Solver-Guided Reasoning for Mixed-Equilibrium Strategies](https://arxiv.org/abs/2608.06741)

**<font color=#1a73e8>作者：</font>** Han Wang, Philippe Beardsell, Boning Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reasoning in large language models (LLMs) is often grounded in human text, human demonstrations, and human-generated rationales. For equilibrium reasoning in complex games, however, relying on human data can be suboptimal. In fact, human play is often guided by intuition and heuristics and can deviate substantially from game equilibrium. This discrepancy is amplified in games with mixed-strategy equilibria, where human data is heavily biased toward pure strategies. Consequently, conditioning LLMs on this data yields weak game strategies. To grant LLMs the reasoning capacity in games, in this work, we study how to elicit equilibrium play using solver output. We propose Mixed-Strategy Decision Tree (MDT), which articulates the silent optimality of the equilibrium into sparse strategic rules that both humans and LLMs could understand. Using solver output rather than human annotation allows us to extend the input to arbitrarily new states and continuations. We instantiate this study on No-Limit Texas Hold'em by querying a solver oracle for over \textbf{250 million mixed-strategy decisions}; MDT together with other techniques \textbf{reduces the $\ell_1$ distance to the equilibrium by $52.6\%$} across $8$ different LLM configurations. A Route-only ablation tests the incremental contribution of the shadow-based contrast, while complete River-endgame and Liar's Dice experiments evaluate strategic fidelity and portability beyond the original NLH communication setting.

---


> [!TIP]
> 当前位于：**1-50**（第 1/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-170](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
