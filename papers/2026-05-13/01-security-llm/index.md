# 🔐 大模型安全相关研究 | 2026年05月13日

> 本类共 **22** 篇论文

> 聚焦大模型安全、对齐、可信与防护方向。

> [!TIP]
> - [返回当日日报目录](../index.md)

---

### 1. [PASA: A Principled Embedding-Space Watermarking Approach for LLM-Generated Text under Semantic-Invariant Attacks](https://arxiv.org/abs/2605.10977)

**<font color=#1a73e8>作者：</font>** Zhenxin Ai, Haiyun He  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Watermarking for large language models (LLMs) is a promising approach for detecting LLM-generated text and enabling responsible deployment. However, existing watermarking methods are often vulnerable to semantic-invariant attacks, such as paraphrasing. We propose PASA, a principled, robust, and distortion-free watermarking algorithm that embeds and detects a watermark at the semantic level. PASA operates on semantic clusters in a latent embedding space and constructs a distributional dependency between token and auxiliary sequences via shared randomness synchronized by a secret key and semantic history. This design is grounded in our theoretical framework that characterizes a jointly optimal embedding-detection pair, achieving the fundamental trade-offs among detection accuracy, robustness, and distortion. Evaluations across multiple LLMs and semantic-invariant attacks demonstrate that PASA remains robust even under strong paraphrasing attacks while preserving high text quality, outperforming standard vocabulary-space baselines. Ablation studies further validate the effectiveness of our hyperparameter choices. Webpage: this https URL.

---


### 2. [Few-Shot Truly Benign DPO Attack for Jailbreaking LLMs](https://arxiv.org/abs/2605.10998)

**<font color=#1a73e8>作者：</font>** Sangyeon Yoon, Wonje Jeung, Yoonjun Cho 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Fine-tuning APIs make frontier LLMs easy to customize, but they can also weaken safety alignment during fine-tuning. While prior work shows that benign supervised fine-tuning (SFT) can reduce refusal behavior, deployed fine-tuning pipelines increasingly support preference-based objectives, whose safety risks remain less understood. We show that Direct Preference Optimization (DPO) introduces a stronger and harder-to-audit failure mode. We propose a truly benign DPO attack using only 10 harmless preference pairs, the minimum data scale accepted by OpenAI's fine-tuning service. Each pair contains a benign prompt, a normal helpful answer as the preferred response, and a refusal as the dispreferred response. Unlike prior benign fine-tuning attacks, our data exhibits no suspicious behavior: it is practically indistinguishable from the fine-tuning request of a legitimate user seeking to reduce over-refusal, making harmful intent almost impossible to infer from the request alone. Nevertheless, because DPO directly optimizes the model to prefer helpful answers over refusals, this seemingly benign objective broadly suppresses refusal behavior and transfers to harmful prompts outside the fine-tuning data. Across OpenAI models supporting DPO fine-tuning, our attack achieves attack success rates of 59.13% on GPT-4o, 70.20% on GPT-4.1, 54.80% on GPT-4.1-mini, and 81.73% on GPT-4.1-nano, at costs of only \$1.7, \$1.7, \$0.3, and \$0.1. Moreover, on open-weight models that do not impose minimum data requirements, we find that this effect can emerge from even a single benign preference pair.

---


### 3. [AgentShield: Deception-based Compromise Detection for Tool-using LLM Agents](https://arxiv.org/abs/2605.11026)

**<font color=#1a73e8>作者：</font>** Yassin H. Rassul, Tarik A. Rashid  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Defenses against indirect prompt injection (IPI) in tool-using LLM agents share two structural weaknesses. First, they all attempt to prevent attacks rather than detect the compromises that slip through. Second, they have only been evaluated in English, leaving users of low-resource languages such as Kurdish and Arabic without tested protection. This paper addresses both gaps with AgentShield, a deception-based detection framework that places three layers of traps inside the agent's tool interface: fake tools, fake credentials, and allowlisted parameters. The same trap triggers serve as high-precision labels for a self-supervised classifier. An LLM agent that follows an attacker's hidden instruction almost always touches one of these traps, which gives both a real-time compromise signal and a zero-FP label for training a downstream detector without manual annotation. Across 176 cross-lingual attack prompts and four LLMs from three providers, and because modern LLMs already refuse most IPI attempts on their own (attack success rate <= 10%), AgentShield's job is to catch the attacks that do slip through. On commercial models, it catches 90.7%-100% of such successful attacks, with zero false alarms on 485 normal-use tests. It survives a systematic adaptive-attack evaluation with zero evasion on commercial models, and the self-supervised classifier transfers across models and languages without retraining.

---


### 4. [FragBench: Cross-Session Attacks Hidden in Benign-Looking Fragments](https://arxiv.org/abs/2605.11029)

**<font color=#1a73e8>作者：</font>** Astha Mehta, Niruthiha Selvanayagam, Cedric Lam 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> An attacker can split a malicious goal into sub-prompts that each look benign on their own and only become harmful in combination. Existing LLM safety benchmarks evaluate prompts one at a time, or across turns of a single chat, and so do not look for a malicious signal spread across separate sessions with no shared context. We build FragBench, a benchmark drawn from 24 real-world cyber-incident campaigns, which keeps the full attack trail: the multi-fragment kill chain, the per-fragment safety-judge verdicts, sandboxed execution traces, and a matched set of benign cover sessions. FragBench splits this trail into two paired tasks: an adversarial rewriter that hardens fragments against a single-turn safety judge (FragBench Attack), and a graph-based user-level detector trained on the resulting interactions (FragBench Defense). The single-turn judge is near chance on the released corpus by construction, but four GNN variants and three classical-ML baselines all recover the cross-session feature, reaching aggregate event-level F1 = 0.88-0.96. Defending against fragmented LLM misuse therefore requires modeling the cross-session interaction graph, rather than isolated prompts. Our generator, rewriter, sandbox harness, and detector are released at this https URL.

---


### 5. [Portable Agent Memory: A Protocol for Cryptographically-Verified Memory Transfer Across Heterogeneous AI Agents](https://arxiv.org/abs/2605.11032)

**<font color=#1a73e8>作者：</font>** Santhosh Kumar Ravindran  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We present Portable Agent Memory, an open protocol and reference implementation for transferring persistent memory state across heterogeneous AI agents. Modern AI agents accumulate rich context -- episodic events,semantic knowledge, procedural skills, working state, and identity preferences -- but this context remains locked within vendor-specific runtimes. Portable Agent Memory addresses this through: (1) a five-component structured memory model with content-addressable entries linked by a Merkle-DAG provenance graph providing tamper-evidence; (2) capability-based access control enabling selective, scoped disclosure of memory segments; (3) an injection-resistant rehydration protocol that adapts recalled content to heterogeneous target models while mitigating indirect prompt injection; and (4) a JSON-first serialization format with optional CBOR compaction for efficient transport. We provide a Python SDK with 54 passing tests, agent skills for multiple platforms, and demonstrate cross-model memory transfer between GPT-4, Claude, Gemini, and Llama architectures. The protocol is open-source under Apache 2.0.

---


### 6. [Sequential Behavioral Watermarking for LLM Agents](https://arxiv.org/abs/2605.11036)

**<font color=#1a73e8>作者：</font>** Hyeseon An, Shinwoo Park, Dongsu Kim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLM-based agents act through sequences of executable decisions, but their trajectories provide little evidence of which agent or policy produced them, making provenance, ownership, and unauthorized reuse difficult to establish from observed behavior alone. This motivates watermarking signals embedded directly into agent behavior rather than only into generated text, since text watermarking cannot capture the action-level decisions that define agent execution. Recent agent watermarking methods address this gap by moving the watermark from generated text to behavioral choices. However, by treating each action step as an independent trial, they overlook trajectory structure and become fragile when trajectories are perturbed, truncated, or observed without reliable alignment. We propose SeqWM, a sequential behavioral watermarking framework that embeds signals into history-conditioned transition patterns and verifies trajectories position-agnostically against random-key baselines. Experiments across diverse agent benchmarks and LLM backbones show that SeqWM consistently achieves reliable detection while preserving agent utility, and remains robust under trajectory corruption where round-indexed behavioral watermarks collapse.

---


### 7. [The Granularity Mismatch in Agent Security: Argument-Level Provenance Solves Enforcement and Isolates the LLM Reasoning Bottleneck](https://arxiv.org/abs/2605.11039)

**<font color=#1a73e8>作者：</font>** Linfeng Fan, Ziwei Li, Yuan Tian 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Tool-using LLM agents must act on untrusted webpages, emails, files, and API outputs while issuing privileged tool calls. Existing defenses often mediate trust at the granularity of an entire tool invocation, forcing a brittle choice in mixed-trust workflows: allow external content to influence a call and risk hijacked destinations or commands, or quarantine the call and block benign retrieval-then-act behavior. The key observation behind this paper is that indirect prompt injection becomes dangerous not when untrusted content appears in context, but when it determines an authority-bearing argument. We present \textsc{PACT} (\emph{Provenance-Aware Capability Contracts}), a runtime monitor that assigns semantic roles to tool arguments, tracks value provenance across replanning steps, and checks whether each argument's origin satisfies its role-specific trust contract. Under oracle provenance, \textsc{PACT} achieves 100\% utility and 100\% security on mixed-trust diagnostic suites, while flat invocation-level monitors incur false positives or false negatives. In full AgentDojo deployments across five models, \textsc{PACT} reaches 100\% security on the three strongest models while recovering 38.1--46.4\% utility, 8--16 percentage points above CaMeL at the same security level. Ablations show that both semantic roles and cross-step provenance are necessary. \textsc{PACT} reframes agent security as authority binding, and isolates the remaining deployment bottleneck to provenance inference and contract synthesis.

---


### 8. [MCPShield: Content-Aware Attack Detection for LLM Agent Tool-Call Traffic](https://arxiv.org/abs/2605.11053)

**<font color=#1a73e8>作者：</font>** Sultan Zavrak  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The Model Context Protocol (MCP) has become a widely adopted interface for LLM agents to invoke external tools, yet learned monitoring of MCP tool-call traffic remains underexplored. In this article, MCPShield is presented as an attack detection framework for MCP tool-call traffic that encodes each agent session as a graph (tool calls as nodes, sequential and data-flow links as edges), enriches nodes with sentence-embedding features over arguments and responses, and classifies sessions as benign or attacked. Three GNN architectures (GAT, GCN, GraphSAGE), a no-graph MLP, and classical baselines (XGBoost, random forest, logistic regression, linear SVM) are evaluated, with the full architecture comparison conducted on RAS-Eval (task-stratified splits) and GraphSAGE retained as the GNN baseline on ATBench and a combined-source variant (both label-stratified). Three findings emerge. First, content-level features are essential: metadata-only detection plateaus around an AUROC of 0.64 regardless of architecture, while content embeddings push the AUROC above 0.89. Second, naive random-split evaluation inflates AUROC by up to 26 percentage points relative to task-disjoint splits, a memorization confound that prior agent-detection work has not addressed. Third, the detection signal resides primarily in the SBERT content embeddings: an AUROC of 0.975 was reached by tree ensembles on pooled embeddings, performing, for the most part, better than the neural architectures in the primary RAS-Eval setting including GNNs (0.917) and the MLP (0.896), and self-supervised pre-training does not deliver a label-efficiency advantage on this task.

---


### 9. [Benchmarking LLM-Based Static Analysis for Secure Smart Contract Development: Reliability, Limitations, and Potential Hybrid Solutions](https://arxiv.org/abs/2605.11163)

**<font color=#1a73e8>作者：</font>** Stefan-Claudiu Susan, Andrei Arusoaie, Dorel Lucanu  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The irreversible nature of blockchain transactions makes the identification of smart contract vulnerabilities an essential requirement for secure system development. While Large Language Models (LLMs) are increasingly integrated into developer workflows, their reliability as autonomous security auditors remains unproven. We assess whether current generative models are a viable replacement for, or only a complement to, traditional static-analysis tools.
Our findings indicate that LLM efficacy is undermined by both inherent lexical bias and a lack of rigorous validation of external data inputs. This reliance on non-semantic heuristics, such as identifier naming, leads to a high frequency of false positives. Furthermore, prompting techniques reveal a trade-off between precision and recall. These results were derived using our custom automated framework, which achieves 92% accuracy in classifying model outputs.

---


### 10. [Adversarial SQL Injection Generation with LLM-Based Architectures](https://arxiv.org/abs/2605.11188)

**<font color=#1a73e8>作者：</font>** Ali Karakoc, H. Birkan Yilmaz  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> SQL injection (SQLi) attacks are still one of the serious attacks ranked in the Open Worldwide Application Security Project (OWASP) Top 10 threats. Today, with advances in Artificial Intelligence (AI), especially in Large Language Models (LLMs), an opportunity has been created for automating adversarial attack tests to measure the defense mechanisms. In this paper, we aim to create a comprehensive evaluation of use cases that utilize LLMs for adversarial SQL injection generation. We introduce two novel LLM-based systems, Retrieval Augmented Generation for Adversarial SQLi (RADAGAS) and Reflective Chain-of-Thought SQLi (RefleXQLi), and compare them with existing baselines against 10 Web Application Firewalls (WAFs) and one execution-based MySQL validator. To perform a comprehensive test, we used six rule-based open-source WAFs (ModSecurity PL1--3, Coraza PL1--3), 2 AI/ML-based WAFs (WAF Brain, CNN-WAF), and 2 commercial WAFs (AWS WAF and Cloudflare WAF). For the LLM models, we used GPT-4o, Claude 3.7 Sonnet, and DeepSeek R1. Our tests consist of 240 experiments that generate 240,000 payloads and perform 2.2 million tests against WAFs. Our comprehensive evaluation reveals that RADAGAS-GPT4o outperforms other baseline models with a 22.73\% bypass rate. The proposed RADAGAS variants are highly successful on AI/ML-based WAFs (92.49\% on WAF-Brain by RADAGAS-DeepSeek, 80.48\% on CNN-WAF by RADAGAS-Claude), but struggle to bypass rule-based WAFs (0--5.70\% on ModSecurity and Coraza). In addition to these findings, another observation is that creating less diverse payloads achieves more bypasses, however they show poor results if the initially chosen payload is not successful. We observe that our findings provide a comprehensive view on using LLM-based approaches in security testing.

---


### 11. [Continuous Discovery of Vulnerabilities in LLM Serving Systems with Fuzzing](https://arxiv.org/abs/2605.11202)

**<font color=#1a73e8>作者：</font>** Yunze Zhao, Yibo Zhao, Yuchen Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLM inference and serving systems have become security-critical infrastructure; however, many of their most concerning failures arise from the serving layer rather than from model behavior alone. Modern inference engines combine KV cache, batching, prefix sharing, speculative decoding, adapters, and multi-tenant scheduling, creating shared-state behavior that only emerges under realistic concurrent workloads and is missed by standard model, safety, and API tests. We present GRIEF, a greybox fuzzer for LLM inference engines that treats timed multi-request traces as first-class inputs, uses lightweight oracles to detect crashes, hangs, performance pathologies, and silent output corruption, and applies controlled replay with log-probability checks to confirm reproducible serving-layer failures. Across early campaigns on vLLM and SGLang, GRIEF discovers 15 vulnerabilities, 10 confirmed by engine developers, including 2 CVEs, spanning KV-cache isolation failures, cross-request performance interference, and crash or liveness bugs. These results show that concurrency, caching, and state reuse can induce silent cross-request contamination, noisy-neighbor denial of service, and delayed crashes without malformed inputs or explicit server errors, making concurrent serving behavior a first-class security and reliability boundary for LLM infrastructure.

---


### 12. [Comment and Control: Hijacking Agentic Workflows via Context-Grounded Evolution](https://arxiv.org/abs/2605.11229)

**<font color=#1a73e8>作者：</font>** Neil Fendley, Zhengyu Liu, Aonan Guan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Automation platforms such as GitHub Actions and n8n are increasingly adopting so-called agentic workflows, which integrate Large Language Model (LLM) agents for tasks such as code review and data synchronization. While bringing convenience for developers, this integration exposes a new risk: An adversary may control and craft certain inputs, such as GitHub issue comments, to manipulate the LLM agent for unwanted actions, such as credential exfiltration and arbitrary command execution. To our knowledge, no prior academic work has studied such a risk in agentic workflows. In this paper, we design the first detection and exploitation framework, called JAW, to hijack agentic workflows hosted on automation platforms via a novel approach called Context-Grounded Evolution. Our key idea is to evolve agentic workflow inputs under the contexts derived from hybrid program analysis for hijacking purposes. Specifically, JAW generates agentic workflow contexts through three analyses: (i) static path-feasibility analysis to identify feasible agent-invocation paths and the input constraints required to trigger them, (ii) dynamic prompt-provenance analysis to determine how that input is transformed and embedded into the LLM context, and (iii) capability analysis to identify the actions and restrictions available to the agent at runtime. Our evaluation of JAW on GitHub workflows and n8n templates showed that 4714 GitHub workflows and eight n8n templates can be successfully hijacked, for example, to leak user credentials. Our findings span 15 widely-used GitHub Actions, including official GitHub Actions for Claude Code, Gemini CLI, Qwen CLI, and Cursor CLI, and two official n8n nodes. We responsibly disclosed all findings to the affected vendors and received many acknowledgements, fixes, and bug bounties, notably from GitHub, Google, and Anthropic.

---


### 13. [Can a Single Message Paralyze the AI Infrastructure? The Rise of AbO-DDoS Attacks through Targeted Mobius Injection](https://arxiv.org/abs/2605.11442)

**<font color=#1a73e8>作者：</font>** Zi Liang, Ronghua Li, Yanyun Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large Language Model (LLM) agents have emerged as key intermediaries, orchestrating complex interactions between human users and a wide range of digital services and LLM infrastructures. While prior research has extensively examined the security of LLMs and agents in isolation, the systemic risk of the agent acting as a disruptive hub within the user-agent-service chain remains largely overlooked. In this work, we expose a novel threat paradigm by introducing Mobius Injection, a sophisticated attack that weaponizes autonomous agents into zombie nodes to launch what we define as gent-based and -Oriented DDoS (AbO-DDoS) attacks. By exploiting a structural vulnerability in agentic logic named Semantic Closure, an adversary can induce sustained recursive execution of agent components through a single textual injection. We demonstrate that this attack is exceptionally lightweight, stealthy against both traditional DDoS monitors and contemporary AI safety filters, and highly configurable, allowing for surgical targeting of specific environments or model providers. To evaluate the real-world impact, we conduct extensive experiments across three representative claw-style agents and three mainstream coding agents, integrated with 12 frontier proprietary or open-weight LLMs. Our results demonstrate that Mobius Injection achieves substantial attack success across diverse tasks, driving single-node call amplification up to 51.0x and multi-node p95 latency inflation up to 229.1x. The attack performance exhibits a superlinear increase with the number of poisoning nodes. To mitigate Mobius Injection, we propose a proactive defense mechanism using Agent Component Energy (ACE) Analysis, which detects malicious recursive triggers by measuring anomalous energy in the agent's component graph.

---


### 14. [Digital Identity for Agentic Systems: Toward a Portable Authorization Standard for Autonomous Agents](https://arxiv.org/abs/2605.11487)

**<font color=#1a73e8>作者：</font>** Partha Madhira  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Enterprise AI is shifting from copilots to autonomous agents capable of executing workflows, negotiating outcomes, and making decisions with limited human oversight. As these systems extend across organizational boundaries, identity alone is insufficient: an agent's authority must also be explicit, constrained, auditable, revocable, and consistently interpretable by independent receivers. This paper analyzes representative enterprise use cases in insurance claims processing and supply chain integrity to surface structural gaps in existing identity and access models. It proposes a portable authorization model for autonomous agents based on issuer-authored authorization payloads, typed constraint algebra, decision-consistent evaluation semantics, delegation attenuation, governed semantic resolution, fail-closed processing, and pre-flight discovery. The model separates credential containers, authorization payload semantics, and enforcement engines, allowing profiles such as JWT/JWS, Verifiable Credentials, OAuth Rich Authorization Requests, or policy-engine bindings to preserve a common authorization meaning across trust boundaries.

---


### 15. [FlowSteer: Prompt-Only Workflow Steering Exposes Planning-Time Vulnerabilities in Multi-Agent LLM Systems](https://arxiv.org/abs/2605.11514)

**<font color=#1a73e8>作者：</font>** Fanxiao Li, Jiaying Wu, Tingchao Fu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Multi-agent systems (MAS) powered by large language models (LLMs) increasingly adopt planner--executor architectures, where planners convert prompts into subtasks, roles, dependencies, and routing paths. This flexibility enables adaptive coordination, but exposes an attack surface in workflow formation: prompts can shape agent organization without modifying MAS infrastructure. We study this risk through social influence probing workflows to identify high-impact subtasks and malicious-signal propagation. The analysis reveals two vulnerabilities: workflow position can amplify or suppress a malicious signal, and sycophantic framing makes downstream agents more likely to relay it. We translate these findings into FlowSteer, a prompt-only workflow steering attack that converts vulnerability priors into one crafted prompt. FlowSteer aligns a malicious signal with influential task components and guides replanning toward dependencies that preserve propagation. Experiments show that FlowSteer increases malicious success by up to 55% over naive prompting, transfers across MAS setups, and remains effective with black-box topology inference. As FlowSteer biases the planning signals that generate the workflow, MAS defenses that inspect only the generated workflow provide limited protection. As such, we introduce FlowGuard, an input-side defense that reduces malicious success by up to 34% while preserving prompt utility. Our results position workflow formation as a new safety frontier for multi-agent LLM systems, opening a planning-time security perspective on how agent coordination itself can be attacked and defended.

---


### 16. [Every Bit, Everywhere, All at Once: A Binomial Multibit LLM Watermark](https://arxiv.org/abs/2605.11653)

**<font color=#1a73e8>作者：</font>** Thibaud Gloaguen, Robin Staab, Mark Vero 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> With LLM watermarking already being deployed commercially, practical applications increasingly require multibit watermarks that encode more complex payloads, such as user IDs or timestamps, into the generated text. In this work, we propose a fundamentally new approach for multibit watermarking: introducing binomial encoding to directly encode every bit of the payload at every token position. We complement our approach with a stateful encoder that during generation dynamically redirects encoding pressure toward underencoded bits. Our evaluation against 8 baselines on up to 64-bit payloads shows that our scheme achieves superior message accuracy and robustness, with the gap to baseline methods widening in more relevant settings (i.e., large payloads and low-distortion regimes). At the same time, we challenge prior works' evaluation metrics, highlighting their lack of practical insights, and introduce per-bit confidence scoring as a practically relevant metric for evaluating multibit LLM watermarks.

---


### 17. [Safety Context Injection: Inference-Time Safety Alignment via Static Filtering and Agentic Analysis](https://arxiv.org/abs/2605.11664)

**<font color=#1a73e8>作者：</font>** Zhenhao Xu, Wenhan Chang, Yichuan Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large Reasoning Models (LRMs) improve performance on complex tasks, but they also make safety control harder at deployment time. In black-box settings, defenders cannot modify model weights and must instead intervene at inference time. This setting creates three practical challenges: harmful intent may be hidden by educational or role-play framing, deep safety analysis can introduce non-trivial latency, and long adversarial contexts can dilute the local cues that simpler filters rely on. These challenges can expose an apparent thinking--output gap, where the model appears cautious during reasoning but still produces an unsafe final answer. To address this problem, we propose Safety Context Injection (SCI), an inference-time framework that separates safety assessment from task generation and prepends a structured external risk report as injected safety context for the protected model. The framework is instantiated in two complementary variants: Static Model Filtering (SMF), a lightweight one-pass guard for fast deployment, and Dynamic Agents Filtering (DAF), an agentic-loop-based analyzer that iteratively gathers and synthesizes evidence for ambiguous or long-context attacks. Across AdvBench and GPTFuzz, spanning base and reasoning models under five jailbreak families, both variants reduce attack success rate and toxicity in the evaluated settings. SMF offers an efficient low-latency option, while DAF is more effective when harmful intent is semantically disguised or dispersed across long contexts.

---


### 18. [Five Attacks on x402 Agentic Payment Protocol](https://arxiv.org/abs/2605.11781)

**<font color=#1a73e8>作者：</font>** Zelin Li, Qin Wang, Zhipeng Wang  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The x402 protocol revives the HTTP 402 Payment Required status code to enable web-native micropayments across APIs, content, and agents. It combines synchronous HTTP authorization with asynchronous blockchain settlement and introduces a cross-layer attack surface absent from conventional web and on-chain payments. In this paper, we formally analyze x402 and empirically show that it is vulnerable in both design and implementation. We present five concrete attacks that reveal weaknesses in authorization, binding, replay protection, and web-layer handling, showing that x402 is vulnerable across multiple stages of the payment workflow. We validate these attacks through a reproducible testbed on local chains, Base Sepolia, and live endpoints and further audit three open-source SDKs and endpoints. Our results show that all five attacks are practical and can cause either unpaid service or paid-but-denied outcomes. We also propose practical mitigations.

---


### 19. [PrivacySIM: Evaluating LLM Simulation of User Privacy Behavior](https://arxiv.org/abs/2605.12147)

**<font color=#1a73e8>作者：</font>** James Flemings, Murali Annavaram  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used to simulate human behavior, but their ability to simulate $individual$ privacy decisions is not well understood. In this paper, we address the problem of evaluating whether a core set of user persona attributes can drive LLMs to simulate individual-level privacy behavior. We introduce PrivacySIM, an evaluation suite that benchmarks LLM simulation of user privacy behavior against the ground-truth responses of 1,000 users. These users are drawn from five published user studies on privacy spanning LLM healthcare consultations, conversational agents, and chatbots. Drawing on these user studies, we hypothesize three persona facets as plausible predictors of privacy decision-making: demographics, previous experiences, and stated privacy attitudes. We condition nine frontier LLMs on subsets of these three facets and measure how often each model's response to a data-sharing scenario matches the user's actual response. Our findings show that (1) privacy persona conditioning consistently improves simulation quality over no-persona conditioning, but even the strongest model (40.4\% accuracy) remains far from faithfully simulating individual privacy decisions. (2) A user's stated privacy attitudes alone may not be the best predictor because they often diverge from the user's actual privacy behavior. (3) Users with high AI/chatbot experience but low stated privacy attitudes are the most challenging to simulate. PrivacySIM is a first step toward understanding and improving the capabilities of LLMs to simulate user privacy decisions. We release PrivacySIM to enable further evaluation of LLM privacy simulation.

---


### 20. [Reconstruction of Personally Identifiable Information from Supervised Finetuned Models](https://arxiv.org/abs/2605.12264)

**<font color=#1a73e8>作者：</font>** Sae Furukawa, Alina Oprea  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Supervised Finetuning (SFT) has become one of the primary methods for adapting a large language model (LLM) with extensive pre-trained knowledge to domain-specific, instruction-following tasks. SFT datasets, composed of instruction-response pairs, often include user-provided information that may contain sensitive data such as personally identifiable information (PII), raising privacy concerns. This paper studies the problem of PII reconstruction from SFT models for the first time. We construct multi-turn, user-centric Q&A datasets in sensitive domains, specifically medical and legal settings, that incorporate PII to enable realistic evaluation of leakage. Using these datasets, we evaluate the extent to which an adversary, with varying levels of knowledge about the fine-tuning dataset, can infer sensitive information about individuals whose data was used during SFT. In the reconstruction setting, we propose COVA, a novel decoding algorithm to reconstruct PII under prefix-based attacks, consistently outperforming existing extraction methods. Our results show that even partial attacker knowledge can significantly improve reconstruction success, while leakage varies substantially across PII types.

---


### 21. [Attacks and Mitigations for Distributed Governance of Agentic AI under Byzantine Adversaries](https://arxiv.org/abs/2605.12364)

**<font color=#1a73e8>作者：</font>** Matthew D. Laws, Alina Oprea, Cristina Nita-Rotaru  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Agentic AI governance is a critical component of agentic AI infrastructure ensuring that agents follow their owner's communication and interaction policies, and providing protection against attacks from malicious agents. The state-of-the-art solution, SAGA, assumes a logically centralized point of trust, the Provider, which serves as a repository for user and agent information and actively enforces policies. While SAGA provides protection against malicious agents, it remains vulnerable to a malicious Provider that deviates from the protocol, undermining the security of the identity and access control infrastructure. Deployment on both private and public clouds, each susceptible to insider threats, further increases the risk of Provider compromise.
In this work, we analyze the attacks that can be mounted from a compromised Provider, taking into account the different system components and realistic deployments. We identify and execute several concrete attacks with devastating effects: undermining agent attributability, extracting private data, or bypassing access control. We then present three types of solutions for securing the Provider that offer different trade-offs between security and performance. We first present SAGA-BFT, a fully byzantine-resilient architecture that provides the strongest protection, but incurs significant performance degradation, due to the high-cost of byzantine resilient protocols. We then propose SAGA-MON and SAGA-AUD, two novel solutions that leverage lightweight server-side monitoring or client-side auditing to provide protection against most classes of attacks with minimal overhead. Finally, we propose SAGA-HYB, a hybrid architecture that combines byzantine-resilience with monitoring and auditing to trade-off security for performance. We evaluate all the architectures and compare them with SAGA. We discuss which solution is best and under what conditions.

---


### 22. [TextSeal: A Localized LLM Watermark for Provenance & Distillation Protection](https://arxiv.org/abs/2605.12456)

**<font color=#1a73e8>作者：</font>** Tom Sander, Hongyan Chang, Tomáš Souček 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We introduce TextSeal, a state-of-the-art watermark for large language models. Building on Gumbel-max sampling, TextSeal introduces dual-key generation to restore output diversity, along with entropy-weighted scoring and multi-region localization for improved detection. It supports serving optimizations such as speculative decoding and multi-token prediction, and does not add any inference overhead. TextSeal strictly dominates baselines like SynthID-text in detection strength and is robust to dilution, maintaining confident localized detection even in heavily mixed human/AI documents. The scheme is theoretically distortion-free, and evaluation across reasoning benchmarks confirms that it preserves downstream performance; while a multilingual human evaluation (6000 A/B comparisons, 5 languages) shows no perceptible quality difference. Beyond its use for provenance detection, TextSeal is also ``radioactive'': its watermark signal transfers through model distillation, enabling detection of unauthorized use.

---


> [!TIP]
> - [返回当日日报目录](../index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
